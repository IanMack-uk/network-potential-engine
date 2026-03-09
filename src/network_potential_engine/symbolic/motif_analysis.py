from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal

import sympy as sp

from network_potential_engine.symbolic.hessian import hessian_of_potential
from network_potential_engine.symbolic.operators import coupling_operator_from_hessian
from network_potential_engine.symbolic.potential import theta_dependent_curvature_potential


SignLabel = Literal["positive", "negative", "zero", "unknown"]


@dataclass(frozen=True)
class PotentialGroup:
    """Pilot semantic grouping for theorem S1 development.

    This grouping is intended to produce proof-oriented units for an S1 cross-partial
    sign inventory. It is not (yet) an authoritative or certified motif ontology.
    """

    group_id: str
    group_name: str
    group_class: str
    expr: sp.Expr


@dataclass(frozen=True)
class OffDiagonalEntry:
    i: int
    j: int
    hessian_entry: str
    coupling_entry: str
    hessian_sign: SignLabel
    coupling_sign: SignLabel


@dataclass(frozen=True)
class GroupReport:
    group_id: str
    group_class: str
    taxonomy_class: str
    expr: str
    variables: list[str]
    off_diagonal_entries: list[OffDiagonalEntry]


@dataclass(frozen=True)
class CrossPartialReport:
    model: str
    groups: list[GroupReport]
    aggregated_is_zmatrix: bool
    aggregated_off_diagonal_entries: list[OffDiagonalEntry]


def _classify_sign(expr: sp.Expr) -> SignLabel:
    simplified = sp.simplify(expr)

    if simplified == 0:
        return "zero"

    if simplified.is_positive is True:
        return "positive"

    if simplified.is_negative is True:
        return "negative"

    return "unknown"


def _variables_in_expr(expr: sp.Expr, w: sp.Matrix, theta: sp.Matrix) -> list[str]:
    names: list[str] = []

    for i in range(w.rows):
        sym = w[i, 0]
        if expr.has(sym):
            names.append(str(sym))

    for i in range(theta.rows):
        sym = theta[i, 0]
        if expr.has(sym):
            names.append(str(sym))

    return names


def _taxonomy_class_for_group_class(group_class: str) -> str:
    mapping = {
        "edge_local": "A",
        "linear": "A",
        "diagonal": "A",
        "interaction": "B",
        "closure": "C",
    }

    return mapping.get(group_class, "unknown")


def decompose_tdc_into_pilot_groups(
    w: sp.Matrix,
    theta: sp.Matrix,
    *,
    base_quadratic_weight: sp.Expr | float = 1,
    theta_curvature_weight: sp.Expr | float = sp.Rational(1, 5),
    coupling_weight: sp.Expr | float = sp.Rational(1, 2),
) -> list[PotentialGroup]:
    """Return pilot semantic groups for the TDC potential.

    This is a Phase-1 decomposition suitable for S1 tooling and tests.
    """

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        coupling_weight=coupling_weight,
    )

    q = sp.sympify(base_quadratic_weight)
    alpha = sp.sympify(theta_curvature_weight)
    c = sp.sympify(coupling_weight)
    n = w.rows

    linear = sp.simplify(sum(theta[i, 0] * w[i, 0] for i in range(n)))

    diagonal_curvature = sp.simplify(
        -sp.Rational(1, 2)
        * sum((q + alpha * theta[i, 0]) * w[i, 0] ** 2 for i in range(n))
    )

    coupling = sp.simplify(
        -sp.Rational(1, 2)
        * c
        * sum((w[i, 0] - w[i + 1, 0]) ** 2 for i in range(n - 1))
    )

    residual = sp.simplify(phi - (linear + diagonal_curvature + coupling))
    if residual != 0:
        raise ValueError(
            "TDC pilot group decomposition does not sum to Phi; residual is nonzero."
        )

    return [
        PotentialGroup(
            group_id="linear",
            group_name="linear term",
            group_class="linear",
            expr=linear,
        ),
        PotentialGroup(
            group_id="diagonal_curvature",
            group_name="diagonal curvature",
            group_class="diagonal",
            expr=diagonal_curvature,
        ),
        PotentialGroup(
            group_id="coupling",
            group_name="nearest-neighbour coupling",
            group_class="interaction",
            expr=coupling,
        ),
    ]


def decompose_tdc_into_admissible_grammar_terms(
    w: sp.Matrix,
    theta: sp.Matrix,
    *,
    base_quadratic_weight: sp.Expr | float = 1,
    theta_curvature_weight: sp.Expr | float = sp.Rational(1, 5),
    coupling_weight: sp.Expr | float = sp.Rational(1, 2),
) -> list[PotentialGroup]:
    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=base_quadratic_weight,
        theta_curvature_weight=theta_curvature_weight,
        coupling_weight=coupling_weight,
    )

    q = sp.sympify(base_quadratic_weight)
    alpha = sp.sympify(theta_curvature_weight)
    c = sp.sympify(coupling_weight)
    n = w.rows

    groups: list[PotentialGroup] = []

    for i in range(n):
        expr = sp.simplify(theta[i, 0] * w[i, 0])
        groups.append(
            PotentialGroup(
                group_id=f"edge_linear_{i}",
                group_name=f"edge-local linear term i={i}",
                group_class="edge_local",
                expr=expr,
            )
        )

    for i in range(n):
        expr = sp.simplify(-sp.Rational(1, 2) * (q + alpha * theta[i, 0]) * w[i, 0] ** 2)
        groups.append(
            PotentialGroup(
                group_id=f"edge_diag_curvature_{i}",
                group_name=f"edge-local diagonal curvature i={i}",
                group_class="edge_local",
                expr=expr,
            )
        )

    for i in range(n):
        coeff = sp.Rational(1, 2) if (i == 0 or i == n - 1) else 1
        expr = sp.simplify(-c * coeff * w[i, 0] ** 2)
        groups.append(
            PotentialGroup(
                group_id=f"edge_coupling_diag_{i}",
                group_name=f"edge-local coupling diagonal contribution i={i}",
                group_class="edge_local",
                expr=expr,
            )
        )

    for i in range(n - 1):
        expr = sp.simplify(c * w[i, 0] * w[i + 1, 0])
        groups.append(
            PotentialGroup(
                group_id=f"pair_coupling_{i}_{i+1}",
                group_name=f"pairwise coupling interaction ({i},{i+1})",
                group_class="interaction",
                expr=expr,
            )
        )

    residual = sp.simplify(phi - sum((g.expr for g in groups), sp.Integer(0)))
    if residual != 0:
        raise ValueError(
            "TDC admissible-grammar decomposition does not sum to Phi; residual is nonzero."
        )

    return groups


def _off_diagonal_entries_for_hessian(hess: sp.Matrix) -> list[tuple[int, int]]:
    n = hess.rows
    if hess.cols != n:
        raise ValueError("hessian must be square")

    return [(i, j) for i in range(n) for j in range(n) if i != j]


def build_cross_partial_report_for_groups(
    *,
    model: str,
    groups: list[PotentialGroup],
    w: sp.Matrix,
    theta: sp.Matrix,
) -> CrossPartialReport:
    group_reports: list[GroupReport] = []

    aggregated_hess = sp.zeros(w.rows, w.rows)
    for g in groups:
        aggregated_hess += hessian_of_potential(g.expr, w)

    aggregated_hess = sp.simplify(aggregated_hess)
    aggregated_coupling = coupling_operator_from_hessian(aggregated_hess)

    aggregated_entries: list[OffDiagonalEntry] = []
    for i, j in _off_diagonal_entries_for_hessian(aggregated_hess):
        hij = sp.simplify(aggregated_hess[i, j])
        cij = sp.simplify(aggregated_coupling[i, j])

        aggregated_entries.append(
            OffDiagonalEntry(
                i=i,
                j=j,
                hessian_entry=str(hij),
                coupling_entry=str(cij),
                hessian_sign=_classify_sign(hij),
                coupling_sign=_classify_sign(cij),
            )
        )

    aggregated_is_zmatrix = all(e.coupling_sign in ("negative", "zero") for e in aggregated_entries)

    for g in groups:
        hess_g = hessian_of_potential(g.expr, w)
        coupling_g = coupling_operator_from_hessian(hess_g)

        entries_g: list[OffDiagonalEntry] = []
        for i, j in _off_diagonal_entries_for_hessian(hess_g):
            hij = sp.simplify(hess_g[i, j])
            cij = sp.simplify(coupling_g[i, j])

            entries_g.append(
                OffDiagonalEntry(
                    i=i,
                    j=j,
                    hessian_entry=str(hij),
                    coupling_entry=str(cij),
                    hessian_sign=_classify_sign(hij),
                    coupling_sign=_classify_sign(cij),
                )
            )

        group_reports.append(
            GroupReport(
                group_id=g.group_id,
                group_class=g.group_class,
                taxonomy_class=_taxonomy_class_for_group_class(g.group_class),
                expr=str(sp.simplify(g.expr)),
                variables=_variables_in_expr(g.expr, w, theta),
                off_diagonal_entries=entries_g,
            )
        )

    return CrossPartialReport(
        model=model,
        groups=group_reports,
        aggregated_is_zmatrix=aggregated_is_zmatrix,
        aggregated_off_diagonal_entries=aggregated_entries,
    )


def report_to_json_dict(report: CrossPartialReport) -> dict[str, Any]:
    raw = asdict(report)

    raw["schema"] = {
        "pilot_semantic_grouping": True,
        "note": "Pilot semantic grouping for theorem S1; not an authoritative motif ontology.",
    }

    return raw


def write_report_json(report: CrossPartialReport, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    payload = report_to_json_dict(report)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
