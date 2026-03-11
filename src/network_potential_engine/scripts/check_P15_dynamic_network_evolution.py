from __future__ import annotations

import numpy as np

from network_potential_engine.dynamics.gradient_flow import euler_step


def phi_quadratic(w: np.ndarray, theta: np.ndarray) -> float:
    d = w - theta
    return float(-0.5 * np.dot(d, d))


def grad_phi_quadratic(w: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return theta - w


def main() -> None:
    print("P15 dynamic network evolution smoke-check")
    print("Dynamics template (Euler discretisation of ascent): w_{t+1} = w_t + η ∇_w Φ(w_t, θ)")
    print("Toy potential: Φ(w,θ) = -1/2 ||w-θ||^2 (maximiser at w=θ)")
    print()

    theta = np.array([2.0, -1.0, 3.0], dtype=float)
    w = np.array([0.0, 0.0, 0.0], dtype=float)
    eta = 0.5

    print("Initial state:")
    print("  theta =", theta)
    print("  w0    =", w)
    print("  Φ(w0) =", phi_quadratic(w, theta))
    print()

    for t in range(25):
        w = euler_step(w, theta, grad_phi_quadratic, eta)
        print(f"Step {t+1}: w = {w},  Φ(w) = {phi_quadratic(w, theta)}")

    # Converges geometrically to theta for eta in (0, 2).
    assert np.allclose(w, theta, atol=1e-6)
    print()
    print("P15 dynamic network evolution smoke-check: PASS")


if __name__ == "__main__":
    main()
