
# Admissibility Taxonomy

This document defines the **admissibility structure** used throughout the Network Potential Framework.

The purpose of this taxonomy is to clearly separate:

- the **domain on which objects are defined**
- the **domains on which theorems are certified**
- the **special regions used for positivity, response, or ordering theorems**

Without this separation, later theorems may accidentally introduce hidden assumptions about where results hold.

This document ensures that all admissibility concepts are defined **once and only once**.

---

# 1. Ambient Domain

The **ambient domain** is the full space in which the variables of the framework live.

We consider pairs

(w, θ)

with

w ∈ ℝⁿ  
θ ∈ ℝⁿ

Thus the ambient domain is

Ω := ℝⁿ × ℝⁿ

All objects in the framework are initially defined on subsets of Ω.

---

# 2. Domain of Definition of the Potential

The **potential function**

Φ(w, θ)

is defined on a subset

Ω_Φ ⊆ Ω.

This domain specifies where the potential is finite and well-defined.

Typical requirements:

- Φ(w, θ) is finite-valued
- Φ(w, θ) is continuous

Later theorems may require stronger regularity conditions.

---

# 3. Admissible State Domain

The **state domain** defines the allowable region for the state variables.

W ⊆ ℝⁿ

w ∈ W

The admissible state domain may impose constraints such as:

- boundedness
- positivity
- interior feasibility conditions
- network constraints

The potential is evaluated only for

(w, θ) ∈ W × Θ

for some parameter domain Θ.

---

# 4. Admissible Parameter Domain

The **parameter domain** defines the allowable parameter values.

Θ ⊆ ℝⁿ

θ ∈ Θ

The parameter domain is chosen so that:

- the potential is well-defined
- equilibrium equations are meaningful
- derivative objects exist

---

# 5. Interior Admissible Region

Some theorems require **interior conditions**, such as:

- differentiability
- nondegeneracy
- invertibility of operators

We therefore define the **interior admissible region**

Ω_int ⊆ W × Θ

This region is typically characterized by conditions such as:

- Hessian invertibility
- smooth dependence on parameters

Later results such as the response identity are usually proven on Ω_int.

---

# 6. Boundary or Constrained Region

In some models, the admissible domain may include **boundary regions** or constraints.

Examples:

- inequality constraints
- parameter limits
- feasibility conditions

These regions are denoted

Ω_boundary

and may require separate analysis.

Many framework theorems are stated only on the **interior admissible region** to avoid degeneracies.

---

# 7. Equilibrium Admissibility Region

Equilibrium results require the existence of solutions

F(w, θ) = 0

with

F(w, θ) = ∇w Φ(w, θ).

We therefore define the **equilibrium admissibility region**

Ω_eq ⊆ Ω

on which equilibria exist.

Within this region, an equilibrium branch

w*(θ)

may be defined.

---

# 8. Response Admissibility Region

The response identity

R(θ) = Dθ w*(θ)

typically requires additional conditions such as:

- invertibility of the coupling operator
- differentiability of the equilibrium branch

The **response admissibility region** is therefore

Ω_resp ⊆ Ω_eq

where the response operator is well-defined.

---

# 9. Ordering / Positivity Regions

Later theorems (such as ordering or monotonicity results) require additional **sign conditions**.

These typically involve:

- inverse positivity of the coupling operator
- positivity of the mixed derivative block
- positivity of the response operator

We therefore define an **ordering admissible region**

R ⊆ Ω_resp

within which these sign conditions hold.

Importantly:

The ordering region **R is not the same as the domain of the potential**.

It is a **theorem-specific admissible region** defined by additional structural conditions.

---

# 10. Domain Hierarchy

The admissibility domains form a nested structure:

Ω (ambient domain)

⊇ Ω_Φ (domain where potential is defined)

⊇ W × Θ (state/parameter admissible domains)

⊇ Ω_int (interior region)

⊇ Ω_eq (equilibrium existence region)

⊇ Ω_resp (response admissible region)

⊇ R (ordering / positivity region)

Each theorem specifies the **smallest domain on which its conclusions are guaranteed**.

---

# 11. Theorem Usage of Domains

Different theorems operate on different admissible domains.

Typical structure:

| Theorem | Domain Used |
|-------|-------------|
| A1 – Well-posedness | Ω_Φ |
| A2 – Equilibrium existence | Ω_eq |
| A3 – Equilibrium regularity | Ω_int |
| C1 – Response identity | Ω_resp |
| D-layer positivity results | Ω_resp |
| E-layer ordering theorems | R |

This separation prevents later results from introducing hidden assumptions.

---

# 12. Consistency Requirement

No theorem in the framework may introduce a new notion of admissibility without defining it in terms of the domains above.

All results must explicitly state **which admissible region they require**.

This guarantees that:

- assumptions remain transparent
- theorem dependencies are explicit
- the framework remains internally consistent.

---

# Summary

The admissibility taxonomy distinguishes between:

- ambient domain Ω
- potential domain Ω_Φ
- admissible state domain W
- admissible parameter domain Θ
- interior region Ω_int
- equilibrium region Ω_eq
- response region Ω_resp
- ordering region R

Later theorems specify the domain on which their conclusions are valid.
