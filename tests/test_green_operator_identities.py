import numpy as np

from network_potential_engine.numeric.green_operator import certify_green_operator


def test_green_operator_is_two_sided_inverse_on_identity_rhs() -> None:
    C = np.array(
        [
            [2.0, -1.0, 0.0],
            [-1.0, 2.0, -1.0],
            [0.0, -1.0, 2.0],
        ],
        dtype=float,
    )
    G = certify_green_operator(C)
    I = np.eye(C.shape[0], dtype=float)

    G_matrix = G.apply_to_matrix(I)

    assert np.allclose(C @ G_matrix, I)
    assert np.allclose(G_matrix @ C, I)


def test_green_operator_matrix_is_symmetric_in_symmetric_spd_regime() -> None:
    C = np.array(
        [
            [2.0, -1.0, 0.0],
            [-1.0, 2.0, -1.0],
            [0.0, -1.0, 2.0],
        ],
        dtype=float,
    )
    G = certify_green_operator(C)
    G_matrix = G.matrix()

    assert np.allclose(G_matrix, G_matrix.T)


def test_green_quadratic_form_is_positive_in_spd_regime() -> None:
    C = np.array(
        [
            [2.0, -1.0, 0.0],
            [-1.0, 2.0, -1.0],
            [0.0, -1.0, 2.0],
        ],
        dtype=float,
    )
    G = certify_green_operator(C)

    x = np.array([1.0, -2.0, 0.5], dtype=float)
    val = float(x.T @ G.apply(x))
    assert val > 0.0


def test_green_matrix_is_entrywise_nonnegative_in_m_matrix_regime() -> None:
    C = np.array(
        [
            [3.0, -1.0, 0.0],
            [-1.0, 3.0, -1.0],
            [0.0, -1.0, 2.0],
        ],
        dtype=float,
    )
    G = certify_green_operator(C)
    assert G.certificate is not None
    assert G.certificate.is_nonsingular_m_matrix_regime

    G_matrix = G.matrix()
    assert bool(np.all(G_matrix >= -1e-12))
