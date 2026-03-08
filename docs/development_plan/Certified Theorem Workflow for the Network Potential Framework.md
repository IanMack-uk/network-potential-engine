# Certified Theorem Workflow for the Network Potential Framework — Version 2

## Status (repo as of now)

-   A1: complete (theorem doc + proof integration + TDC check scripts/tests)
-   A2: complete (theorem doc + proof integration + TDC check scripts/tests)
-   A3: complete (interior nondegeneracy / strict local maximum theorem doc + proof integration + TDC check scripts/tests)
-   C1: draft exists as `docs/theorems/framework/DRAFT_C1_equilibrium_regularity.md` (equilibrium response identity); not yet finalized
-   Next formal theorem target in this workflow: B1

Naming alignment:

-   A3 is reserved for interior nondegeneracy / strict local maximum.
-   The equilibrium response identity belongs to C1 (not A3).

## Overview

The TDC local ordering theorem shows that the mathematically correct certification chain is not:

**potential → differentiation**

but rather:

**potential → coupling/Hessian structure → equilibrium response identity → sign-controlled response → certified local ordering → structural differentiation.**

In the TDC model, this chain is explicit: the scalar potential generates the equilibrium operator $`F(w,\theta) = \theta - C(\theta)w`$, the Hessian satisfies $`C(\theta) = - H(\theta)`$, the equilibrium is $`w^{*}(\theta) = C(\theta)^{- 1}\theta`$, and the response identity is

``` math
D_{\theta}w^{*}(\theta) = C(\theta)^{- 1}H_{w\theta}(w^{*}(\theta),\theta).
```

The ordering theorem then follows only after certifying inverse positivity, mixed-block positivity, and persistence on an admissible region $`\mathcal{R}`$.

Accordingly, the Network Potential Framework should be certified in the following logical order.

## A. Framework Foundations

### Theorem A1 — Admissible Relational Potential Well-Posedness

Prove that the Network Potential functional is well-defined on its admissible domain, with the exact regularity claimed.

This should certify:

- the admissible domain is mathematically well-defined,

- the potential is continuous on that domain,

- all derivative objects used later are well-defined where invoked.

This is the base layer of the entire framework.

### Theorem A2 — Equilibrium Existence

Prove that the framework admits equilibria under the declared regime.

This should certify:

- existence of interior equilibria in the unconstrained case,

- existence of constrained equilibria in the scarcity case,

- precise distinction between stationarity and constrained optimality.

### Theorem A3 — Interior Nondegeneracy / Strict Local Maximum Theorem

Prove that, in the relevant regime, equilibria are nondegenerate strict local maximisers.

This should certify:

- Hessian sign classification,

- local stability,

- local uniqueness where available.

This is the foundational gateway for any later response theorem.

## B. Operator Generation

### Theorem B1 — Hessian–Coupling Theorem

Prove that the equilibrium Hessian generates the coupling operator.

In the TDC model this appears as

``` math
C(\theta) = - H(\theta),
```

which is exactly the prototype for the general framework.

This theorem should export:

- the coupling operator as the negative equilibrium Hessian,

- symmetry/self-adjointness when the hypotheses justify it,

- the operator object on which all later response theory depends.

### Theorem B2 — Locality / Incident Structure Inheritance Theorem

Prove that the structural locality assumptions of the Network Potential functional induce corresponding locality in the Hessian/coupling operator.

This should certify:

- incident decomposition,

- neighbourhood-limited interaction structure,

- sparsity/locality of the operator.

This is what makes the framework specifically a network theory rather than generic optimisation theory.

## C. Equilibrium Response

### Theorem C1 — Equilibrium Response Theorem

Prove that in the certified interior nondegenerate regime, equilibrium depends differentiably on parameters and admits a response identity of the form

``` math
D_{\theta}w^{*} = (\text{inverse curvature})(\text{mixed perturbation block}).
```

In the TDC model, this is

``` math
D_{\theta}w^{*}(\theta) = C(\theta)^{- 1}H_{w\theta}(w^{*}(\theta),\theta).
```

This is the core comparative-statics theorem of the framework.

It replaces the need for separate “susceptibility theorem” and “response decomposition theorem” blocks, because the factorisation is already built into the response identity itself.

## D. Sign-Controlled Response

### Theorem D1 — Inverse Positivity Theorem

Prove sufficient conditions under which the inverse curvature / response operator has the required sign structure.

In the TDC model, this is obtained by showing that $`q + \alpha\theta_{i} > 0`$makes $`C(\theta)`$a strictly diagonally dominant Z-matrix and hence a nonsingular M-matrix, so

``` math
C(\theta)^{- 1} \geq 0.
```

### Theorem D2 — Mixed-Block Positivity Theorem

Prove sufficient conditions under which the perturbation-entry block has the required sign.

In the TDC model,

``` math
H_{w\theta}(w,\theta) = diag(1 - \alpha w_{1},\ldots,1 - \alpha w_{n}),
```

so sign control reduces to proving

``` math
1 - \alpha w_{i}^{*}(\theta) \geq 0\text{for all }i.
```

### Theorem D3 — Response Positivity Theorem

Combine the previous two results to certify sign of the full equilibrium response map.

In the TDC prototype, the conclusion is

``` math
D_{\theta}w^{*}(\theta) \geq 0
```

entrywise when both inverse positivity and mixed-block positivity hold.

This is the immediate theorem that turns operator structure into monotone comparative statics.

## E. Interior Ordering Package

This is where the TDC local ordering theorem sits most directly.

### Theorem E1 — Explicit Admissible-Region Theorem

Construct an explicit region on which the hypotheses of the response positivity theorem hold.

In the TDC model, the admissible region is

``` math
\mathcal{R =}\left\{ \theta:m(\theta) > 0,\text{\:\,}\alpha\frac{\parallel \theta \parallel_{\infty}}{m(\theta)} \leq 1 \right\},m(\theta): = \underset{i}{\min}(q + \alpha\theta_{i}).
```

This theorem should not be treated as a universal standalone foundation theorem. It belongs specifically to the ordering package, because its role is to certify where sign-controlled response is valid.

### Lemma E2 — Segment / Path Certification Lemma

Prove usable sufficient conditions ensuring that an entire path between two parameter points remains in the admissible region.

In the TDC model, this is done by endpoint data via the segment certificate.

This is essential because pointwise response positivity alone is not enough to yield an ordering theorem.

### Theorem E3 — Local Weak Ordering Theorem

Prove that ordered parameter changes imply ordered equilibrium changes whenever the connecting path stays inside the certified region.

In the TDC model:

``` math
\theta' \succeq \theta \Longrightarrow w^{*}(\theta') \succeq w^{*}(\theta)
```

provided the segment lies in $`\mathcal{R}`$.

This is the first genuine structural-ordering theorem.

### Theorem E4 — Strict Ordering Theorem

Strengthen weak ordering to strict ordering under stronger irreducibility / strict positivity conditions.

This is the natural next theorem after local weak ordering and should be treated as part of the same package.

## F. Structural Differentiation Package

Only once the ordering package is certified should the framework move to broader architectural claims.

### Theorem F1 — Structural Index Theorem

Define structural indices from the now-certified response operator and prove their mathematical well-posedness and interpretability.

This comes after response/order certification, not before it. Paper 2 explicitly treats structural differentiation as arising from equilibrium responses governed by the inverse incident Hessian operator and then defines a structural index as a measure of responsiveness.

### Theorem F2 — Differentiation Theorem

Prove that non-equal structural indices imply differentiated equilibrium tie strengths under the certified local regime.

### Theorem F3 — Role-Strata Theorem

Prove that incident ties partition into structural role classes under certified asymmetry conditions.

### Theorem F4 — Symmetry-Breaking Theorem

Prove that symmetry is lost under admissible perturbations when the relevant nondegeneracy conditions hold.

These are the true architectural theorems of the framework, but they are downstream of ordering, not upstream.

## G. Genericity Package

These theorems should remain later-stage results.

### Theorem G1 — Generic Nondegeneracy Theorem

Show that degenerate or exactly symmetric cases form an exceptional set.

### Theorem G2 — Generic Strict Differentiation Theorem

Show that strict differentiation and role separation hold generically once the relevant asymmetry and nondegeneracy conditions are imposed.

This is where the broad “generic structural differentiation” language of the programme properly belongs. It should not be treated as part of the immediate core chain already certified by the TDC mechanism. Paper 2’s broader claims about generic strict dispersion and symmetry exceptions are at this higher layer.

## H. Scarcity / Constrained Geometry

Only after the interior response-ordering chain is secure.

### Theorem H1 — Constrained Equilibrium Theorem

Characterise constrained equilibria by normal-cone / variational inequality conditions.

### Theorem H2 — Reduced Response Theorem

Derive the constrained analogue of the response identity using tangent-space or reduced-Hessian geometry.

### Theorem H3 — Face-Wise Ordering Theorem

Establish ordering within fixed active-set regions.

### Theorem H4 — Active-Set Stability Theorem

Control when the constrained ordering result persists without face switching.

This is the correct scarcity generalisation of the interior TDC mechanism.

## I. Propagation, Opportunity, Dynamics, and Topology

These should remain later packages, built on the certified response-and-ordering layers.

### Theorem I1 — Propagation Geometry Theorem

Prove quantitative propagation properties from the locality and response operators.

### Theorem I2 — Opportunity Kernel Theorem

Define and certify structural opportunity measures from the propagation/response operators.

### Theorem I3 — Opportunity Monotonicity Theorem

Show how certified local relational improvements affect opportunity measures.

### Theorem I4 — Dynamical Formation Theorems

Establish gradient-flow or related dynamical results.

### Theorem I5 — Endogenous Topology Theorems

Extend the theory to edge creation/removal and topological adaptation.

These are important for applications, but they are not part of the minimal core theorem chain.
