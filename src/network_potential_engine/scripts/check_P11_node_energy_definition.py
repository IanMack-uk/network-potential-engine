from __future__ import annotations

import numpy as np

from network_potential_engine.energy.node_energy import energy_vector


def main() -> None:
    print("P11 node energy definition smoke-check")
    print("Definition: E := β0 s + β1 v where v := G s")
    print("(This check treats v as an input vector; it does not compute G.)")
    print()

    s = np.array([3.5, 3.0, 4.5], dtype=float)
    v = np.array([1.0, 2.0, 3.0], dtype=float)

    beta0 = 2.0
    beta1 = 0.5

    E = energy_vector(s, v, beta0=beta0, beta1=beta1)

    print("s =", s)
    print("v =", v)
    print(f"β0={beta0}, β1={beta1}")
    print("E =", E)

    assert E.shape == s.shape
    assert np.allclose(E, beta0 * s + beta1 * v)

    print()
    print("P11 node energy definition smoke-check: PASS")


if __name__ == "__main__":
    main()
