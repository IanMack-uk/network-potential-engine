import numpy as np


def main() -> None:
    print("P6 equilibrium network smoke-check")
    print("Equilibrium definition (P6): w* ∈ argmax_{w ∈ W_feas(r)} Φ(w, \\tilde{θ})")
    print("Interface lemma (conditional): if w* is an interior maximiser and Φ is differentiable, then ∇_w Φ(w*, \\tilde{θ})=0")
    print()

    # Simple 1D quadratic example: Φ(w) = -(w-a)^2.
    # Unconstrained maximiser is w*=a, and ∂Φ/∂w = -2(w-a) which vanishes at w=a.
    a = 0.7
    w_star = a

    def phi(w: float) -> float:
        return -((w - a) ** 2)

    def dphi(w: float) -> float:
        return -2.0 * (w - a)

    print("Example (1D, interior/unconstrained):")
    print("  Φ(w) = -(w-a)^2")
    print(f"  a = {a}")
    print(f"  Unconstrained argmax is w* = a = {w_star}")
    print(f"  ∂Φ/∂w (w) = -2(w-a)")
    print(f"  ∂Φ/∂w (w*) = {dphi(w_star)}")
    assert abs(dphi(w_star)) == 0.0
    print()

    # Demonstrate a feasibility domain that contains the maximiser in its interior.
    # Here we use a simple interval [0,1] as a stand-in for W_feas(r).
    w_min, w_max = 0.0, 1.0
    print("Feasibility stand-in:")
    print(f"  W_feas(r) ≈ [ {w_min}, {w_max} ]")
    assert w_min < w_star < w_max
    print(f"  w* = {w_star} lies in the interior of W_feas(r)")
    print()

    # Show that w* yields greater or equal objective value than nearby points.
    eps = 1e-3
    left = w_star - eps
    right = w_star + eps
    print("Local optimality check:")
    print(f"  Φ(w*) = {phi(w_star)}")
    print(f"  Φ(w* - ε) = {phi(left)}")
    print(f"  Φ(w* + ε) = {phi(right)}")
    assert phi(w_star) >= phi(left)
    assert phi(w_star) >= phi(right)
    print()

    print("P6 equilibrium network smoke-check: PASS")


if __name__ == "__main__":
    main()
