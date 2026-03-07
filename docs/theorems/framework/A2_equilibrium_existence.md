# A2 --- Equilibrium Existence

## Purpose

This theorem defines the notion of **equilibrium** for relational
potential systems and establishes conditions under which equilibria
exist.

The equilibrium concept is defined through the **equilibrium operator**

F(w, θ) = ∇\_w Φ(w, θ)

introduced in `docs/foundations/core_objects.md`.

This theorem connects the general framework to the equilibrium equation
used in the TDC model.

------------------------------------------------------------------------

# 1. Equilibrium Definition

Let

Φ(w, θ)

be a relational potential satisfying the regularity conditions
established in

A1 --- Admissible Relational Potential Well-Posedness.

Define the equilibrium operator

F(w, θ) = ∇\_w Φ(w, θ)

An **equilibrium state** for parameters θ is any state

w ∈ W

satisfying the stationarity condition

F(w, θ) = 0

Equivalently

∇\_w Φ(w, θ) = 0

------------------------------------------------------------------------

# 2. Stationarity Equation

Because the potential is differentiable in the state variables, the
equilibrium condition is well-defined on the admissible potential
domain.

The stationarity equation therefore defines the equilibrium system

F(w, θ) = 0

Solutions of this system are called **equilibrium points**.

------------------------------------------------------------------------

# 3. Coupling Operator Representation

Using the canonical object definitions from `core_objects.md`, the
Hessian is

H(w, θ) = ∇²_ww Φ(w, θ)

and the coupling operator is defined as

C(θ) = −H(w, θ)

When the equilibrium operator can be written in the form

F(w, θ) = θ − C(θ) w

the stationarity condition becomes

C(θ) w = θ

------------------------------------------------------------------------

# 4. Equilibrium Existence Under Invertibility

Assume the coupling operator

C(θ)

is invertible.

Then the equilibrium equation

C(θ) w = θ

has the unique solution

w\*(θ) = C(θ)⁻¹ θ

Thus an equilibrium exists for every parameter value θ for which the
coupling operator is invertible.

------------------------------------------------------------------------

# 5. Equilibrium Branch

Define the **equilibrium branch**

w\*(θ)

as the mapping assigning to each admissible parameter value the
corresponding equilibrium state.

Whenever the coupling operator is invertible, the equilibrium branch is
given by

w\*(θ) = C(θ)⁻¹ θ

------------------------------------------------------------------------

# 6. Verification of Stationarity

Substituting the equilibrium branch into the equilibrium operator gives

F(w\*(θ), θ) = 0

confirming that the branch indeed satisfies the equilibrium condition.

------------------------------------------------------------------------

# 7. TDC Model Instantiation

For the Theta-Dependent Curvature (TDC) model, the equilibrium operator
satisfies

F(w, θ) = θ − C(θ) w

where

C(θ) = −H(θ)

is the tridiagonal coupling operator derived from the TDC potential.

Therefore the equilibrium equation becomes

C(θ) w\*(θ) = θ

When the coupling matrix is nonsingular, the equilibrium branch is

w\*(θ) = C(θ)⁻¹ θ

This matches the equilibrium relation used in the TDC local ordering
theorem.

------------------------------------------------------------------------

# 8. Domain of Validity

The equilibrium existence result holds on the subset of the admissible
domain where

det C(θ) ≠ 0

This subset is denoted

Ω_eq

in the admissibility taxonomy.

------------------------------------------------------------------------

# 9. Conclusion

Under the regularity conditions of A1 and the invertibility of the
coupling operator, the relational potential framework admits an
equilibrium branch

w\*(θ)

defined by

C(θ) w\*(θ) = θ

This equilibrium branch forms the basis for the response analysis and
ordering results developed in later theorems.
