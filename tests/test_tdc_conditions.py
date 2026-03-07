import numpy as np

from network_potential_engine.symbolic.symbols import make_symbols
from network_potential_engine.symbolic.potential import (
    theta_dependent_curvature_potential,
)
from network_potential_engine.symbolic.gradient import gradient_of_potential
from network_potential_engine.numeric.lambdified import lambdify_matrix
from network_potential_engine.numeric.equilibrium import solve_equilibrium
from network_potential_engine.theorem.tdc_conditions import (
    check_tdc_conditions,
    tdc_curvature_margins,
    tdc_mixed_block_margins,
)


def test_tdc_curvature_margins_match_formula() -> None:
    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)
    margins = tdc_curvature_margins(
        theta_values,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    expected = np.array([1.04, 1.02, 1.00], dtype=float)
    assert np.allclose(margins, expected)


def test_tdc_mixed_block_margins_match_formula() -> None:
    w_star = np.array([0.16153807, 0.09753725, 0.03251242], dtype=float)
    margins = tdc_mixed_block_margins(
        w_star,
        theta_curvature_weight=0.2,
    )

    expected = 1.0 - 0.2 * w_star
    assert np.allclose(margins, expected)


def test_check_tdc_conditions_holds_for_current_second_model_example() -> None:
    w, theta = make_symbols(3, 3)

    phi = theta_dependent_curvature_potential(
        w,
        theta,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
        coupling_weight=0.5,
    )
    grad = gradient_of_potential(phi, w)
    grad_fn = lambdify_matrix(grad, w, theta)

    theta_values = np.array([0.2, 0.1, 0.0], dtype=float)
    w0 = np.zeros(3, dtype=float)

    eq_result = solve_equilibrium(grad_fn, theta_values, w0)

    check = check_tdc_conditions(
        theta_values=theta_values,
        w_star=eq_result.w_star,
        base_quadratic_weight=1.0,
        theta_curvature_weight=0.2,
    )

    assert check.curvature_margins.shape == (3,)
    assert check.mixed_block_margins.shape == (3,)
    assert check.curvature_condition_holds is True
    assert check.mixed_block_condition_holds is True
    assert check.all_conditions_hold is True
