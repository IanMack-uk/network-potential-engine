import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import bootstrap_potential
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.symbolic.equilibrium import bootstrap_symbolic_equilibrium
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.numeric.equilibrium import solve_equilibrium


def test_symbolic_and_numeric_equilibrium_agree_for_bootstrap_model() -> None:
    w, theta = make_symbols(3, 3)
    phi = bootstrap_potential(w, theta)
    grad = gradient_of_potential(phi, w)

    symbolic_eq = bootstrap_symbolic_equilibrium(phi, w, theta)
    symbolic_eq_fn = lambdify_matrix(symbolic_eq, w, theta)

    grad_fn = lambdify_matrix(grad, w, theta)

    theta_values = np.array([0.5, 0.25, -0.5], dtype=float)
    w0 = np.zeros(3, dtype=float)

    numeric_result = solve_equilibrium(grad_fn, theta_values, w0)
    symbolic_value = symbolic_eq_fn(np.zeros(3, dtype=float), theta_values)

    assert numeric_result.success is True
    assert symbolic_value.shape == (3,)
    assert np.allclose(symbolic_value, numeric_result.w_star)
