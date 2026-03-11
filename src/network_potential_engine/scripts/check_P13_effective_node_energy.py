from __future__ import annotations

import numpy as np

from network_potential_engine.energy.effective_energy import effective_energy_vector


def main() -> None:
    print("P13 effective node energy smoke-check")
    print("Definition: E_eff := beta0*s + beta1*(rho ⊙ v), where v := G s")
    print("(This check treats v as an input vector; it does not compute G.)")
    print()

    s = np.array([3.5, 3.0, 4.5], dtype=float)
    v = np.array([10.0, 20.0, 3.0], dtype=float)
    rho = np.array([2.0, 0.5, 0.0], dtype=float)

    beta0 = 2.0
    beta1 = 0.5

    E_eff = effective_energy_vector(s, v, rho, beta0=beta0, beta1=beta1)

    print("s   =", s)
    print("v   =", v)
    print("rho =", rho)
    print(f"beta0={beta0}, beta1={beta1}")
    print("E_eff =", E_eff)

    assert E_eff.shape == s.shape
    assert np.allclose(E_eff, beta0 * s + beta1 * (rho * v))

    print()
    print("P13 effective node energy smoke-check: PASS")


if __name__ == "__main__":
    main()
