from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class CertificationError(Exception):
    """Base class for certification-layer errors."""


class MathematicalRegimeError(CertificationError):
    """Base class for mathematical (theorem-regime) failures."""


class NumericalOperatorError(CertificationError):
    """Base class for numerical/operator execution failures."""


@dataclass
class MissingCertificateError(MathematicalRegimeError):
    message: str
    evidence: dict[str, Any] | None = None

    def __str__(self) -> str:
        return self.message


@dataclass
class UnmetRegimeError(MathematicalRegimeError):
    required_regime_tag: str
    actual_regime_tag: str
    evidence: dict[str, Any] | None = None

    def __str__(self) -> str:
        return (
            f"Required regime_tag='{self.required_regime_tag}', "
            f"but actual regime_tag='{self.actual_regime_tag}'."
        )


@dataclass
class UnmetPredicateError(MathematicalRegimeError):
    missing_predicates: set[str]
    present_predicates: set[str]
    evidence: dict[str, Any] | None = None

    def __str__(self) -> str:
        missing = sorted(self.missing_predicates)
        return f"Missing required predicates: {missing}"


@dataclass
class NonInvertibleCouplingError(NumericalOperatorError):
    message: str
    evidence: dict[str, Any] | None = None

    def __str__(self) -> str:
        return self.message
