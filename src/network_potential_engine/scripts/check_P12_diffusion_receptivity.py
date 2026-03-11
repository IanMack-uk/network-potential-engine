from __future__ import annotations

import numpy as np

from network_potential_engine.diffusion.receptivity import receptivity_modulate


def main() -> None:
    print("P12 diffusion / receptivity smoke-check")
    print("Definition: v_tilde := rho ⊙ v")
    print()

    rho = np.array([2.0, 0.5, 0.0], dtype=float)
    v = np.array([10.0, 20.0, 3.0], dtype=float)

    v_tilde = receptivity_modulate(rho, v)

    print("rho =", rho)
    print("v   =", v)
    print("v~  =", v_tilde)

    assert v_tilde.shape == v.shape
    assert np.allclose(v_tilde, rho * v)

    print()
    print("P12 diffusion / receptivity smoke-check: PASS")


if __name__ == "__main__":
    main()
