from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential


@dataclass(frozen=True)
class MMatrixRowEntry:
    row_index: int
    diagonal_entry: str
    offdiag_row_sum: str
    dominance_margin: str
    is_strictly_dominant: bool


@dataclass(frozen=True)
class MMatrixReport:
    model: str
    n: int
    parameters: dict[str, str]
    rows: list[MMatrixRowEntry]
    minimum_dominance_margin: str
    all_rows_strictly_dominant: bool
    all_offdiagonals_nonpositive: bool
    s3_mmatrix_preconditions_met: bool
    expected_margin_formula_recovered: bool
    inverse_nonnegative_small_n: bool | None


def _make_symbols(*, n: int) -> tuple[sp.Matrix, sp.Matrix]:
    w = sp.Matrix([sp.Symbol(f"w{i}", real=True) for i in range(n)])
    theta = sp.Matrix([sp.Symbol(f"theta{i}", positive=True) for i in range(n)])
    return w, theta


def _row_offdiag_abs_sum(C: sp.Matrix, i: int) -> sp.Expr:
    n = C.rows
    if C.cols != n:
        raise ValueError("C must be square")

    return sp.simplify(sum(sp.Abs(C[i, j]) for j in range(n) if j != i))


def _all_offdiagonals_nonpositive(C: sp.Matrix) -> bool:
    n = C.rows
    if C.cols != n:
        raise ValueError("C must be square")

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            entry = sp.simplify(C[i, j])
            if entry.is_nonpositive is not True:
                return False
    return True


def _write_report_json(report: MMatrixReport, artifact_path: str | Path) -> None:
    p = Path(artifact_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(asdict(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _print_matrix(name: str, M: sp.Matrix) -> None:
    print(f"{name} =")
    for i in range(M.rows):
        row = ", ".join(str(sp.simplify(M[i, j])) for j in range(M.cols))
        print(f"  [{row}]")


def _optional_inverse_nonnegativity_check() -> bool | None:
    try:
        n = 3
        w, theta = _make_symbols(n=n)

        q = sp.Integer(1)
        alpha = sp.Rational(1, 5)
        c = sp.Rational(1, 2)

        phi = theta_dependent_curvature_potential(
            w,
            theta,
            base_quadratic_weight=q,
            theta_curvature_weight=alpha,
            coupling_weight=c,
        )

        hess = hessian_of_potential(phi, w)
        C = coupling_operator_from_hessian(hess)
        C_inv = sp.simplify(C.inv())

        for entry in list(C_inv):
            if sp.simplify(entry).is_nonnegative is not True:
                return False

        return True
    except Exception:
        return None


def check_s3_tdc_mmatrix(
    *,
    verbose: bool = False,
    artifact_path: str | Path | None = None,
) -> MMatrixReport:
    n = 5
    w, theta = _make_symbols(n=n)

    q = sp.Integer(1)
    alpha = sp.Rational(1, 5)
    c = sp.Rational(1, 2)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=q,
        theta_curvature_weight=alpha,
        coupling_weight=c,
    )

    hess = hessian_of_potential(phi, w)
    C = coupling_operator_from_hessian(hess)

    if verbose:
        print("Symbolic objects:")
        print(f"- Phi(w, theta) = {sp.simplify(phi)}")
        _print_matrix("- H(w, theta)", hess)
        _print_matrix("- C(w, theta) = -H", C)

    rows: list[MMatrixRowEntry] = []
    margins: list[sp.Expr] = []

    expected_formula_recovered = True

    for i in range(n):
        if verbose:
            print(f"\nrow {i} computation:")
        diag = sp.simplify(C[i, i])
        if verbose:
            print(f"  diagonal d_i = C[{i},{i}] = {diag}")
        offdiag_sum = _row_offdiag_abs_sum(C, i)
        if verbose:
            terms = [
                f"|C[{i},{j}]|={sp.simplify(sp.Abs(C[i, j]))}"
                for j in range(n)
                if j != i
            ]
            print(f"  offdiag abs terms: {', '.join(terms)}")
            print(f"  offdiag sum r_i = {offdiag_sum}")
        margin = sp.simplify(diag - offdiag_sum)

        if verbose:
            print(f"  margin m_i = d_i - r_i = {margin}")

        expected = sp.simplify(q + alpha * theta[i, 0])
        if sp.simplify(margin - expected) != 0:
            expected_formula_recovered = False

        is_strictly_dominant = margin.is_positive is True

        rows.append(
            MMatrixRowEntry(
                row_index=i,
                diagonal_entry=str(diag),
                offdiag_row_sum=str(offdiag_sum),
                dominance_margin=str(margin),
                is_strictly_dominant=is_strictly_dominant,
            )
        )
        margins.append(margin)

    minimum_margin = sp.simplify(sp.Min(*margins))
    all_rows_strict = all(r.is_strictly_dominant for r in rows)
    all_offdiag_nonpositive = _all_offdiagonals_nonpositive(C)
    s3_preconditions_met = all_rows_strict and all_offdiag_nonpositive

    inverse_nonnegative_small_n = _optional_inverse_nonnegativity_check()

    report = MMatrixReport(
        model="tdc",
        n=n,
        parameters={"q": str(q), "alpha": str(alpha), "c": str(c)},
        rows=rows,
        minimum_dominance_margin=str(minimum_margin),
        all_rows_strictly_dominant=all_rows_strict,
        all_offdiagonals_nonpositive=all_offdiag_nonpositive,
        s3_mmatrix_preconditions_met=s3_preconditions_met,
        expected_margin_formula_recovered=expected_formula_recovered,
        inverse_nonnegative_small_n=inverse_nonnegative_small_n,
    )

    if artifact_path is not None:
        _write_report_json(report, artifact_path)

    return report


def run_all_checks() -> None:
    artifact_path = Path("docs/artifacts/S3/tdc_mmatrix_report.json")
    report = check_s3_tdc_mmatrix()

    print("TDC S3 M-Matrix Preconditions Check")
    print("===================================")
    print("")
    print(f"All off-diagonals nonpositive (Z-matrix): {report.all_offdiagonals_nonpositive}")
    print(f"All rows strictly diagonally dominant: {report.all_rows_strictly_dominant}")
    print(f"Minimum dominance margin: {report.minimum_dominance_margin}")
    print(f"Expected TDC margin formula recovered: {report.expected_margin_formula_recovered}")
    print(f"S3 preconditions met: {report.s3_mmatrix_preconditions_met}")
    print(
        f"Optional small-n sanity check (inverse entrywise nonnegative): {report.inverse_nonnegative_small_n}"
    )
    print("")
    print("Per-row summary:")
    for row in report.rows:
        print(
            f"row {row.row_index}: diagonal = {row.diagonal_entry}, "
            f"offdiag_sum = {row.offdiag_row_sum}, margin = {row.dominance_margin}"
        )

    _write_report_json(report, artifact_path)
    print("")
    print(f"wrote artifact: {artifact_path}")


if __name__ == "__main__":
    run_all_checks()
