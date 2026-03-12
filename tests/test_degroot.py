import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from network_potential_engine.diffusion.degroot import (
    degroot_simulate,
    degroot_simulate_with_receptivity,
    degroot_step,
    degroot_step_with_receptivity,
    transition_matrix_from_adjacency,
)


def test_transition_matrix_from_adjacency_row_stochastic() -> None:
    A = np.array(
        [
            [0.0, 1.0, 1.0],
            [2.0, 0.0, 0.0],
            [0.0, 3.0, 0.0],
        ],
        dtype=float,
    )

    P = transition_matrix_from_adjacency(A)
    assert np.allclose(np.sum(P, axis=1), np.ones((3,), dtype=float))


def test_transition_matrix_from_adjacency_adds_self_loop_for_dangling_row() -> None:
    A = np.array(
        [
            [0.0, 1.0],
            [0.0, 0.0],
        ],
        dtype=float,
    )

    P = transition_matrix_from_adjacency(A, add_self_loops_for_dangling=True)
    assert np.allclose(P[0], np.array([0.0, 1.0]))
    assert np.allclose(P[1], np.array([0.0, 1.0]))
    assert np.allclose(np.sum(P, axis=1), np.ones((2,), dtype=float))


def test_transition_matrix_from_adjacency_rejects_negative_weights() -> None:
    A = np.array([[0.0, -1.0], [0.0, 0.0]], dtype=float)
    with pytest.raises(ValueError, match="entrywise nonnegative"):
        transition_matrix_from_adjacency(A)


def test_degroot_step_and_simulate_shapes() -> None:
    A = np.array(
        [
            [0.0, 1.0],
            [1.0, 0.0],
        ],
        dtype=float,
    )
    P = transition_matrix_from_adjacency(A)

    x0 = np.array([1.0, 0.0], dtype=float)
    x1 = degroot_step(P, x0)
    assert np.allclose(x1, np.array([0.0, 1.0]))

    xs = degroot_simulate(P, x0, n_steps=3)
    assert xs.shape == (4, 2)
    assert np.allclose(xs[0], x0)
    assert np.allclose(xs[1], np.array([0.0, 1.0]))
    assert np.allclose(xs[2], np.array([1.0, 0.0]))
    assert np.allclose(xs[3], np.array([0.0, 1.0]))


def test_degroot_simulate_rejects_negative_n_steps() -> None:
    P = np.eye(2, dtype=float)
    x0 = np.zeros((2,), dtype=float)
    with pytest.raises(ValueError, match="n_steps"):
        degroot_simulate(P, x0, n_steps=-1)


def test_degroot_step_with_receptivity_is_elementwise_modulation_of_step() -> None:
    A = np.array(
        [
            [0.0, 1.0],
            [1.0, 0.0],
        ],
        dtype=float,
    )
    P = transition_matrix_from_adjacency(A)
    x0 = np.array([1.0, 0.0], dtype=float)
    rho = np.array([2.0, 0.5], dtype=float)

    x1 = degroot_step(P, x0)
    x1r = degroot_step_with_receptivity(P, x0, rho)
    assert np.allclose(x1r, rho * x1)


def test_degroot_simulate_with_receptivity_applies_each_step() -> None:
    A = np.array(
        [
            [0.0, 1.0],
            [1.0, 0.0],
        ],
        dtype=float,
    )
    P = transition_matrix_from_adjacency(A)
    x0 = np.array([1.0, 0.0], dtype=float)
    rho = np.array([2.0, 0.5], dtype=float)

    xs = degroot_simulate_with_receptivity(P, x0, rho, n_steps=3)
    assert xs.shape == (4, 2)
    assert np.allclose(xs[0], x0)
    assert np.allclose(xs[1], rho * (P @ x0))
    assert np.allclose(xs[2], rho * (P @ xs[1]))
