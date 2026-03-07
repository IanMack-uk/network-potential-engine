import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.numeric.equilibrium import solve_equilibrium


def test_solve_equilibrium_finds_small_residual_solution() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    grad_fn = lambdify_matrix(grad, w, theta)

    theta_values = np.array([0.5, 0.25, -0.5], dtype=float)
    w0 = np.zeros(3, dtype=float)

    result = solve_equilibrium(grad_fn, theta_values, w0)

    assert result.w_star.shape == (3,)
    assert result.success is True
    assert result.residual_norm < 1e-8
