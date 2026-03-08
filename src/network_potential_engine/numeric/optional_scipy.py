from __future__ import annotations

from collections.abc import Callable


def require_scipy_root() -> Callable:
    try:
        from scipy.optimize import root  # type: ignore
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "SciPy is required for this operation (scipy.optimize.root). "
            "Install scipy or use a NumPy-only certification check when available."
        ) from e

    return root
