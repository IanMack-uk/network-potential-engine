# A2 --- Equilibrium Existence

## Purpose

This theorem defines the notion of **equilibrium** for relational
potential systems and records an explicit solvability/existence result
for a restricted model class in which the equilibrium operator admits an
affine coupling representation.

The equilibrium concept is defined through the **equilibrium operator**

F(w, θ) = ∇\_w Φ(w, θ)

introduced in `docs/foundations/core_objects.md`.

This theorem connects the framework equilibrium definition to the
explicit affine stationarity equation used in the TDC model.

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

C(w, θ) = −H(w, θ)

When the equilibrium operator can be written in the form

F(w, θ) = θ − C(θ) w

where C(θ) denotes either a model-specific coupling matrix independent of w, or the equilibrium-evaluated shorthand C(θ) := C(w*(θ), θ) when an equilibrium branch w*(θ) is licensed by later theorems,

the stationarity condition becomes

C(θ) w = θ

------------------------------------------------------------------------

# 4. Equilibrium Existence Under an Affine Coupling Representation

Assume the equilibrium operator admits an affine coupling representation

F(w, θ) = θ − C(θ) w

on the regime of interest, where C(θ) denotes either a model-specific coupling matrix independent of w, or the equilibrium-evaluated shorthand C(θ) := C(w*(θ), θ) when an equilibrium branch w*(θ) is licensed by later theorems.

Assume the coupling operator

C(θ)

is invertible.

Then the equilibrium equation

C(θ) w = θ

has the unique solution

w\*(θ) = C(θ)⁻¹ θ

Thus, under the affine coupling representation and invertibility, an equilibrium exists for every parameter value θ for which the coupling operator is invertible.

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

The explicit existence/solvability result in Sections 4–7 holds on any subset of the admissible
domain where the affine coupling representation is valid and where

det C(θ) ≠ 0

This subset is denoted

Ω_eq

in the admissibility taxonomy.

------------------------------------------------------------------------

# 9. Conclusion

Under the regularity conditions of A1, the affine coupling representation, and the invertibility of the
coupling operator, the framework admits an explicitly defined equilibrium branch

w\*(θ)

defined by

C(θ) w\*(θ) = θ

This equilibrium branch forms the basis for the response analysis and
ordering results developed in later theorems.

------------------------------------------------------------------------

# 10. Proof

## 10.1 Well-definedness of the equilibrium operator

By A1, the potential Φ(w, θ) is twice continuously differentiable in the
state variables on Ω_Φ. Therefore the gradient ∇\_w Φ(w, θ) exists and
is continuous on Ω_Φ. Hence the equilibrium operator

F(w, θ) = ∇\_w Φ(w, θ)

is well-defined on Ω_Φ.

## 10.2 Equilibrium definition and stationarity equation

By definition, an equilibrium state for parameters θ is any w ∈ W
satisfying F(w, θ) = 0. Since F is well-defined on Ω_Φ, the stationarity
equation is a well-defined system of n equations in n unknowns on Ω_Φ.

## 10.3 Existence under an affine coupling representation

Assume the equilibrium operator admits the representation

F(w, θ) = θ − C(θ) w.

Then the stationarity equation F(w, θ) = 0 is equivalent to

C(θ) w = θ.

If C(θ) is invertible, this linear system has the unique solution

w\*(θ) = C(θ)⁻¹ θ.

Thus an equilibrium exists for every θ such that det C(θ) ≠ 0, and the
equilibrium branch is uniquely defined on the corresponding subset Ω_eq.

## 10.4 Verification of stationarity

Substituting w\*(θ) into the coupling-form stationarity equation gives

C(θ) w\*(θ) = C(θ) C(θ)⁻¹ θ = θ,

which is equivalent to F(w\*(θ), θ) = 0.

## 10.5 TDC instantiation and computational verification

For the TDC model, the equilibrium operator satisfies

F(w, θ) = θ − C(θ) w

and the equilibrium branch is w\*(θ) = C(θ)⁻¹ θ whenever C(θ) is
nonsingular, matching the framework statement.

This identity chain is verified computationally in

`src/network_potential_engine/scripts/check_A2_tdc_equilibrium_existence.py`

and in the pytest file

`tests/test_A2_tdc_equilibrium_existence.py`.
