
# Core Mathematical Objects

This document defines the **canonical mathematical objects** used throughout the Network Potential Framework.

All theorems, lemmas, and code components must reference these definitions.
No later theorem may redefine these objects or introduce alternate notation for them.

The purpose of this document is to:
1. Freeze the canonical objects used in the framework.
2. Specify the dependency structure between them.
3. Provide the **TDC model instantiation** that serves as a reference implementation.

---

# 1. Ambient Variables

## State variables
w ∈ ℝⁿ

These represent **network weights / state variables**.

## Parameter variables
θ ∈ ℝⁿ

These represent **external parameters or inputs** controlling the system.

---

# 2. Potential

The framework is built around a **relational potential function**

Φ(w, θ) : ℝⁿ × ℝⁿ → ℝ

Later theorems impose regularity conditions such as

Φ ∈ C² in w  
Φ ∈ C¹ in θ

These conditions guarantee that the derivative objects defined below exist.

---

# 3. Equilibrium Operator

F(w, θ) := ∇w Φ(w, θ)

Equilibria satisfy

F(w, θ) = 0

---

# 4. Hessian

H(w, θ) := ∇²ww Φ(w, θ)

This operator captures curvature of the potential with respect to the state variables.

---

# 5. Coupling Operator

C(w, θ) := −H(w, θ)

In many models (including TDC) the Hessian does not depend on w, so the coupling operator may be written as C(θ) without ambiguity.

---

# 6. Mixed Derivative Block

H_wθ(w, θ) := Dθ(∇w Φ(w, θ))

Equivalently

H_wθ(w, θ) = ∂²Φ / (∂w ∂θ)

---

# 7. Equilibrium Branch

w*(θ)

satisfies

F(w*(θ), θ) = 0

---

# 8. Response Operator

R(θ) = Dθ w*(θ)

Under appropriate invertibility conditions

R(θ) = C(θ)⁻¹ H_wθ(w*(θ), θ)

---

# 9. Object Dependency Structure

| Object | Depends on |
|------|------|
| Φ | primitive definition |
| F | Φ |
| H | Φ |
| H_wθ | Φ |
| C | H |
| w*(θ) | F, C |
| R(θ) | C, H_wθ, w* |

Dependency graph:

Φ
│
├── F = ∇wΦ
│
├── H = ∇²wwΦ
│     │
│     └── C = −H
│
└── H_wθ = Dθ(∇wΦ)

F , C → equilibrium branch w*(θ)

C , H_wθ → response operator R

---

# 10. TDC Model Instantiation

The **Theta‑Dependent Curvature (TDC) model** provides a reference implementation.

Φ_tdc(w, θ) =
Σ_i θ_i w_i
− ½ Σ_i (q + α θ_i) w_i²
− (c/2) Σ_{i=1}^{n−1} (w_i − w_{i+1})²

## Equilibrium operator

F(w, θ) = θ − C(θ) w

## Coupling operator

C(θ) is tridiagonal with

diagonal: q + αθ_i + (c or 2c)  
off‑diagonal: −c

## Equilibrium

C(θ) w*(θ) = θ

If invertible:

w*(θ) = C(θ)⁻¹ θ

## Mixed derivative block

H_wθ(w, θ) = diag(1 − α w₁, … , 1 − α w_n)

## Response operator

R(θ) = C(θ)⁻¹ H_wθ(w*(θ), θ)

---

# 11. Consistency Requirement

All later theorems in the framework must use **exactly the objects defined here**.

---

# Summary

Canonical objects:

Φ, F, H, C, H_wθ, w*(θ), R(θ)

All theoretical results and code implementations must remain consistent with these definitions.
