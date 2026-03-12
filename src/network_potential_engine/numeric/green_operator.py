from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from network_potential_engine.numeric.linear_algebra import (
    diagonal_dominance_margins,
    has_nonpositive_off_diagonals,
    is_symmetric,
    is_strictly_diagonally_dominant,
)
from network_potential_engine.numeric.optional_scipy import optional_scipy_lu_factor_solve
from network_potential_engine.theorem.exceptions import UnmetPredicateError, UnmetRegimeError


@dataclass(frozen=True)
class CouplingCertificate:
    is_symmetric: bool
    is_strictly_diagonally_dominant: bool
    has_nonpositive_off_diagonals: bool
    diagonal_dominance_margins: np.ndarray
    min_diagonal_dominance_margin: float
    tol: float
    regime_tag: str
    method: str

    def __post_init__(self) -> None:
        margins = np.asarray(self.diagonal_dominance_margins, dtype=float).reshape(-1).copy()
        margins.setflags(write=False)
        object.__setattr__(self, "diagonal_dominance_margins", margins)
        object.__setattr__(self, "min_diagonal_dominance_margin", float(self.min_diagonal_dominance_margin))

    @property
    def predicates(self) -> set[str]:
        present: set[str] = set()
        if self.is_symmetric:
            present.add("symmetric")
        if self.is_strictly_diagonally_dominant:
            present.add("strict_diag_dom")
        if self.has_nonpositive_off_diagonals:
            present.add("z_matrix")
        return present

    @property
    def is_nonsingular_m_matrix_regime(self) -> bool:
        return bool(self.is_strictly_diagonally_dominant and self.has_nonpositive_off_diagonals)

    def requires_regime(self, regime_tag: str) -> None:
        if self.regime_tag != regime_tag:
            raise UnmetRegimeError(
                required_regime_tag=regime_tag,
                actual_regime_tag=self.regime_tag,
                evidence={
                    "tol": self.tol,
                    "predicates": sorted(self.predicates),
                    "min_diagonal_dominance_margin": self.min_diagonal_dominance_margin,
                },
            )

    def requires_predicates(self, required: set[str]) -> None:
        missing = set(required) - self.predicates
        if missing:
            raise UnmetPredicateError(
                missing_predicates=missing,
                present_predicates=set(self.predicates),
                evidence={
                    "tol": self.tol,
                    "min_diagonal_dominance_margin": self.min_diagonal_dominance_margin,
                },
            )


@dataclass(frozen=True)
class GreenDiagnostics:
    backend_used: str
    condition_estimate: float | None
    near_singular: bool | None


@dataclass(frozen=True)
class GreenOperator:
    coupling_matrix: np.ndarray
    coupling_certificate: CouplingCertificate | None = None
    diagnostics: GreenDiagnostics | None = None
    _scipy_lu: tuple[object, object] | None = None
    _scipy_lu_solve: object | None = None

    def __post_init__(self) -> None:
        coupling = np.asarray(self.coupling_matrix, dtype=float).copy()
        if coupling.ndim != 2:
            raise ValueError("coupling_matrix must be a 2D array")
        if coupling.shape[0] != coupling.shape[1]:
            raise ValueError("coupling_matrix must be square")

        coupling.setflags(write=False)

        object.__setattr__(self, "coupling_matrix", coupling)

        backend_used = "numpy_solve"
        scipy_helpers = optional_scipy_lu_factor_solve()
        if scipy_helpers is not None:
            lu_factor, lu_solve = scipy_helpers
            lu, piv = lu_factor(coupling)
            object.__setattr__(self, "_scipy_lu", (lu, piv))
            object.__setattr__(self, "_scipy_lu_solve", lu_solve)
            backend_used = "scipy_lu"

        cond_est: float | None = None
        near_singular: bool | None = None
        if coupling.shape[0] <= 50:
            try:
                cond_est = float(np.linalg.cond(coupling))
                near_singular = bool(cond_est > 1e12)
            except Exception:
                cond_est = None
                near_singular = None

        object.__setattr__(
            self,
            "diagnostics",
            GreenDiagnostics(
                backend_used=backend_used,
                condition_estimate=cond_est,
                near_singular=near_singular,
            ),
        )

    @property
    def dimension(self) -> int:
        return int(self.coupling_matrix.shape[0])

    @property
    def certificate(self) -> CouplingCertificate | None:
        return self.coupling_certificate

    def apply(self, rhs: np.ndarray) -> np.ndarray:
        rhs_arr = np.asarray(rhs, dtype=float)
        if rhs_arr.ndim not in (1, 2):
            raise ValueError("rhs must be a 1D or 2D array")
        if rhs_arr.shape[0] != self.dimension:
            raise ValueError("rhs has incompatible dimension")

        if self._scipy_lu is not None and self._scipy_lu_solve is not None:
            lu, piv = self._scipy_lu
            lu_solve = self._scipy_lu_solve
            return np.asarray(lu_solve((lu, piv), rhs_arr), dtype=float)

        return np.linalg.solve(self.coupling_matrix, rhs_arr)

    def apply_to_matrix(self, rhs: np.ndarray) -> np.ndarray:
        rhs_arr = np.asarray(rhs, dtype=float)
        if rhs_arr.ndim != 2:
            raise ValueError("rhs must be a 2D array")
        return self.apply(rhs_arr)

    def matrix(self) -> np.ndarray:
        identity = np.eye(self.dimension, dtype=float)
        return self.apply(identity)


def certify_green_operator(
    coupling_matrix: np.ndarray | list[list[float]],
    *,
    tol: float = 1e-10,
) -> GreenOperator:
    coupling = np.asarray(coupling_matrix, dtype=float).copy()

    margins = diagonal_dominance_margins(coupling)

    certificate = CouplingCertificate(
        is_symmetric=is_symmetric(coupling, tol=tol),
        is_strictly_diagonally_dominant=is_strictly_diagonally_dominant(coupling, tol=tol),
        has_nonpositive_off_diagonals=has_nonpositive_off_diagonals(coupling, tol=tol),
        diagonal_dominance_margins=margins,
        min_diagonal_dominance_margin=float(np.min(margins)),
        tol=float(tol),
        regime_tag="strict_diag_dom_z_matrix",
        method="numeric",
    )

    return GreenOperator(coupling_matrix=coupling, coupling_certificate=certificate)
