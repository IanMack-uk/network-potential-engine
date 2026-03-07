# Theorem Dependency Graph and TDC Alignment Guide

## Purpose

This note provides a clean architectural view of the theorem dependency graph for the Network Potential Framework and records the alignment rules needed to ensure that early framework theorems match the proved TDC local ordering theorem and the later theorem packages built on top of it.

The central design principle is:

> Theorems A1-D3 must be stated so that the TDC theorem is a direct instantiation of the general framework pipeline.

Equivalently, the TDC theorem should be treated as a certification target, or practical unit test, for the earlier layers of the framework.

---

## 1. Full Theorem Dependency Graph

The project architecture can be organised as the following dependency graph.

```text
FOUNDATIONS
A1  Well-Posedness of the Admissible Relational Potential
 |
A2  Equilibrium Existence
 |
A3  Interior Nondegeneracy / Strict Local Maximum
 |
 +----------------------+
 |                      |
 v                      |
OPERATOR                |
B1  Hessian-Coupling Theorem
 |
B2  Locality / Incident Structure Inheritance
 |
 v
RESPONSE
C1  Equilibrium Response Theorem
 |
 v
SIGN CONTROL
D1  Inverse Positivity Theorem
 |
D2  Mixed-Block Positivity Theorem
 |
D3  Response Positivity Theorem
 |
 v
ORDERING
E1  Explicit Admissible-Region Theorem
 |
E2  Segment / Path Certification Lemma
 |
E3  Local Weak Ordering Theorem
 |
E4  Strict Ordering Theorem
 |
 v
STRUCTURAL DIFFERENTIATION
F1  Structural Index Theorem
 |
F2  Differentiation Theorem
 |
F3  Role-Strata Theorem
 |
F4  Symmetry-Breaking Theorem
 |
 v
GENERICITY
G1  Generic Nondegeneracy Theorem
 |
G2  Generic Strict Differentiation Theorem
 |
 v
SCARCITY / CONSTRAINED GEOMETRY
H1  Constrained Equilibrium Theorem
 |
H2  Reduced Response Theorem
 |
H3  Face-Wise Ordering Theorem
 |
H4  Active-Set Stability Theorem
 |
 v
PROPAGATION / OPPORTUNITY / DYNAMICS / TOPOLOGY
I1  Propagation Geometry Theorem
 |
I2  Opportunity Kernel Theorem
 |
I3  Opportunity Monotonicity Theorem
 |
I4  Dynamical Formation Theorems
 |
I5  Endogenous Topology Theorems
```

---

## 2. Core Certification Spine

The logical spine of the programme is:

```text
potential
-> Hessian / coupling structure
-> equilibrium response identity
-> sign-controlled response
-> certified local ordering
-> structural differentiation
```

This is the core mechanism of the framework. Everything later in the programme depends on getting this chain right.

A useful compressed view is:

```text
A: foundations
-> B: operator generation
-> C: response identity
-> D: sign control
-> E: ordering
-> F onward: structural interpretation and extensions
```

---

## 3. Where the TDC Theorem Sits

The theorem in `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md` is not merely an isolated model-specific theorem. It is the first fully developed worked instance of the framework pipeline.

The TDC document contains the chain:

1. potential definition
2. gradient operator
3. Hessian / coupling relation
4. equilibrium equation
5. response identity
6. sign conditions
7. admissible region
8. ordering theorem

So, in framework language, the TDC theorem instantiates:

```text
A2 -> B1 -> C1 -> D1 -> D2 -> D3 -> E1 -> E2 -> E3
```

and implicitly relies on A1-type regularity as well.

Therefore the TDC theorem should be treated as the canonical reference implementation of the framework pipeline.

---

## 4. The TDC Consistency Principle

Every general theorem in A-E should satisfy the following test.

### TDC Consistency Test

If the general theorem is instantiated with the TDC potential, then it should reproduce the corresponding statement already proved in `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`.

In schematic form:

```text
general theorem layer
        |
        v
instantiate with Phi_tdc
        |
        v
recover the TDC theorem statement already in the repo
```

If a framework theorem cannot be instantiated cleanly by the TDC model, then the framework theorem is likely mis-specified, too broad, or using the wrong objects.

---

## 5. Canonical Objects That Must Be Fixed Early

To prevent drift, the core mathematical objects must be defined once and then used unchanged throughout the theorem chain.

The canonical objects are:

```text
Phi(w, theta)            potential
F(w, theta) = grad_w Phi equilibrium operator
H = grad^2_ww Phi        Hessian
C = -H                   coupling operator
H_wtheta                 mixed derivative block
w*(theta)                equilibrium branch
D_theta w*(theta)        response operator
```

These are exactly the objects that appear throughout the TDC theorem.

The TDC theorem uses the forms:

```text
F(w, theta) = theta - C(theta) w
C(theta) = -H(theta)
D_theta w*(theta) = C(theta)^(-1) H_wtheta(w*(theta), theta)
```

Accordingly, the framework should standardise these objects at the A/B/C layers and forbid notational or structural divergence later.

---

## 6. Alignment Rules by Theorem Layer

### A1 - Well-Posedness

A1 must certify the existence and regularity of exactly the derivative objects used later.

Minimum regularity target:

```text
Phi is C^2 in w
Phi is C^1 in theta
```

This guarantees the existence of:

```text
grad_w Phi
grad^2_ww Phi
D_theta(grad_w Phi)
```

These are precisely the objects needed in the TDC theorem.

A1 should therefore be stated as a theorem about:

1. the admissible domain
2. continuity of the potential
3. regularity sufficient for later derivatives
4. exact availability of the derivative objects later invoked

If A1 is stated too weakly, later theorems will silently assume missing derivatives.
If A1 is stated using different objects, the chain will not match TDC.

---

### A2 - Equilibrium Existence

The TDC theorem defines equilibrium by the stationarity equation:

```text
F(w*(theta), theta) = 0
```

and, in model form, this becomes:

```text
C(theta) w*(theta) = theta
```

So A2 must define equilibrium through the equilibrium operator

```text
F(w, theta) = grad_w Phi(w, theta)
```

and not through any alternative construction unrelated to the gradient-based setup.

This preserves the TDC structure and ensures that later response theorems use the same notion of equilibrium.

---

### A3 - Interior Nondegeneracy / Strict Local Maximum

A3 must certify the invertibility and sign classification needed for the response theorem.

In practical terms, A3 is the gateway from mere stationarity to a usable local equilibrium branch.

It should provide the nondegeneracy conditions that make the later inverse-curvature machinery valid.

---

### B1 - Hessian-Coupling Theorem

The TDC theorem explicitly proves:

```text
C(theta) = -H(theta)
```

So B1 must export the coupling operator precisely as the negative equilibrium Hessian.

This is essential, because the response theorem and all later sign arguments use the same operator.
If B1 defines a different operator, the entire later architecture drifts away from the proved TDC mechanism.

---

### B2 - Locality / Incident Structure Inheritance

B2 should explain how locality in the potential induces locality in the Hessian and coupling operator.

This is not only a structural convenience. It is what turns the framework into a network theorem rather than generic optimisation.

B2 should therefore sit after B1 but before propagation and later structural packages.

---

### C1 - Equilibrium Response Theorem

The TDC theorem proves the factorised response identity:

```text
D_theta w*(theta) = C(theta)^(-1) H_wtheta(w*(theta), theta)
```

C1 must be formulated in exactly this factorised form.

This is a critical alignment requirement. If C1 is formulated differently, then D1-D3, E1-E3, and all later structural theorems will no longer be cleanly grounded in the same mechanism as the TDC theorem.

---

### D1-D3 - Sign-Controlled Response

The TDC ordering theorem depends on two sign facts:

```text
C(theta)^(-1) >= 0
H_wtheta >= 0
```

and combines them to conclude:

```text
D_theta w*(theta) >= 0
```

Therefore the D-layer should always be structured as:

- D1: inverse positivity conditions
- D2: mixed-block positivity conditions
- D3: response positivity

The TDC theorem should then appear as a specific instance of these general sign-control theorems.

---

### E1-E3 - Ordering Package

The TDC theorem uses two final ingredients:

1. positivity of the response operator on an admissible region
2. path integration along a segment joining parameters

The key identity is:

```text
w*(theta') - w*(theta)
    = integral from 0 to 1 of D_theta w*(gamma(t)) (theta' - theta) dt
```

So the framework ordering package should be standardised as:

- E1: admissible region
- E2: path or segment certification
- E3: local weak ordering theorem

This guarantees that the general ordering theorem reduces exactly to the TDC ordering proof when specialised.

---

## 7. Why the TDC Theorem Is the Unit Test

The simplest way to think about the framework is:

```text
framework theorems
      |
      v
instantiate with Phi_tdc
      |
      v
must reproduce tdc_local_ordering_theorem
```

In this sense, the TDC theorem is the unit test for the full architecture.

It is not merely evidence that one model works.
It is the object that forces the general theorem chain to stay mathematically coherent.

---

## 8. Recommended Repository Structure for Alignment

To minimise drift, the repository should define the core objects in one place, for example:

```text
docs/foundations/core_objects.md
```

This file should define:

- potential
- gradient
- Hessian
- coupling operator
- mixed derivative block
- equilibrium
- response operator

Then every theorem document should reference those definitions rather than silently redefining objects.

This will make it much easier to:

1. audit theorem dependencies
2. check consistency across documents
3. verify TDC instantiation
4. prevent notation drift across the A-I packages

---

## 9. Practical Development Rule

When drafting any theorem from A1 through E3, apply the following checklist.

### Framework-to-TDC Checklist

1. Does the theorem use the canonical objects `Phi`, `F`, `H`, `C`, `H_wtheta`, `w*`, and `D_theta w*`?
2. Does the theorem require exactly the regularity needed for those objects?
3. Does equilibrium arise from `F = grad_w Phi`?
4. Does the theorem preserve `C = -H`?
5. Does the response theorem preserve the factorisation `D_theta w* = C^{-1} H_wtheta`?
6. Are sign theorems split into inverse positivity, mixed-block positivity, and response positivity?
7. Does the ordering theorem use admissible-region control plus path integration?
8. If `Phi_tdc` is substituted, do we recover the TDC theorem already in the repository?

A no-answer to any of these questions indicates a likely specification error.

---

## 10. Immediate Consequence for A1 Development

If development starts from A1, then A1 should not be written as an isolated regularity note with no relation to the later chain.

Instead A1 should be written so that it certifies the exact objects needed by:

- A2 equilibrium existence
- B1 Hessian-coupling
- C1 response identity
- D1-D3 sign control
- E1-E3 ordering

In particular, A1 should explicitly certify the existence of:

- `grad_w Phi`
- `grad^2_ww Phi`
- `D_theta(grad_w Phi)`

because these are exactly the derivative objects later used in the TDC theorem and in the general framework pipeline.

---

## 11. Summary

The architecture of the project is best understood as a single certified chain:

```text
A1-A3  foundations
-> B1-B2  operator generation
-> C1  response identity
-> D1-D3  sign-controlled response
-> E1-E4  ordering
-> F-I  structural, generic, constrained, and dynamic extensions
```

To keep this architecture coherent, the TDC theorem should be treated as the reference instantiation of the framework.

The governing alignment rule is:

> A1-E3 must be formulated so that substituting the TDC potential reproduces the TDC theorem already proved in the repository.

That principle gives a concrete method for keeping the framework mathematically consistent as the theorem stack is built upward from the foundations.
