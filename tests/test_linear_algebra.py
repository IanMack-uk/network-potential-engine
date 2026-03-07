import numpy as np

from network_potential_engine.numeric.linear_algebra import (
    diagonal_dominance_margins,
    has_nonnegative_off_diagonals,
    has_nonpositive_off_diagonals,
    is_strictly_diagonally_dominant,
    is_symmetric,
)


def test_is_symmetric_true_for_symmetric_matrix() -> None:
    matrix = np.array(
        [
            [2.0, -1.0, 0.5],
            [-1.0, 3.0, 0.0],
            [0.5, 0.0, 4.0],
        ]
    )

    assert is_symmetric(matrix) is True


def test_is_symmetric_false_for_nonsymmetric_matrix() -> None:
    matrix = np.array(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ]
    )

    assert is_symmetric(matrix) is False


def test_diagonal_dominance_margins_returns_expected_values() -> None:
    matrix = np.array(
        [
            [4.0, -1.0, -1.0],
            [-1.0, 5.0, -1.0],
            [-1.0, -1.0, 6.0],
        ]
    )

    margins = diagonal_dominance_margins(matrix)

    expected = np.array([2.0, 3.0, 4.0])
    assert np.allclose(margins, expected)


def test_is_strictly_diagonally_dominant_true_when_all_margins_positive() -> None:
    matrix = np.array(
        [
            [4.0, -1.0, -1.0],
            [-1.0, 5.0, -1.0],
            [-1.0, -1.0, 6.0],
        ]
    )

    assert is_strictly_diagonally_dominant(matrix) is True


def test_is_strictly_diagonally_dominant_false_when_margin_not_positive() -> None:
    matrix = np.array(
        [
            [1.0, -1.0],
            [-1.0, 1.0],
        ]
    )

    assert is_strictly_diagonally_dominant(matrix) is False


def test_has_nonpositive_off_diagonals_true_for_z_matrix_pattern() -> None:
    matrix = np.array(
        [
            [4.0, -1.0, 0.0],
            [-2.0, 3.0, -0.5],
            [0.0, -1.0, 2.0],
        ]
    )

    assert has_nonpositive_off_diagonals(matrix) is True


def test_has_nonpositive_off_diagonals_false_when_positive_offdiag_exists() -> None:
    matrix = np.array(
        [
            [4.0, 1.0],
            [-1.0, 3.0],
        ]
    )

    assert has_nonpositive_off_diagonals(matrix) is False


def test_has_nonnegative_off_diagonals_true_for_hessian_style_pattern() -> None:
    matrix = np.array(
        [
            [-4.0, 1.0, 0.0],
            [1.0, -3.0, 0.5],
            [0.0, 0.5, -2.0],
        ]
    )

    assert has_nonnegative_off_diagonals(matrix) is True


def test_has_nonnegative_off_diagonals_false_when_negative_offdiag_exists() -> None:
    matrix = np.array(
        [
            [-4.0, -1.0],
            [1.0, -3.0],
        ]
    )

    assert has_nonnegative_off_diagonals(matrix) is False
