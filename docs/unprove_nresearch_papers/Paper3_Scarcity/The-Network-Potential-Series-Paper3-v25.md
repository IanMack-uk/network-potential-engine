## 

## 

## 

## 

## Constrained Variational Optimisation and

## Scarcity Geometry in Network Potential Theory

#### 

#### 

#### 

#### **Author:** Ian Mack

#### **Date:** Feb. 2026

\
=

# Content

[Paper 3: Constrained Variational Optimisation and Scarcity Geometry in Network Potential Theory [4](#paper-3-constrained-variational-optimisation-and-scarcity-geometry-in-network-potential-theory)](#paper-3-constrained-variational-optimisation-and-scarcity-geometry-in-network-potential-theory)

[Abstract [4](#abstract)](#abstract)

[2.0 Foundational Operator Framework [5](#foundational-operator-framework)](#foundational-operator-framework)

[2.0.1 Configuration Space and Constraints [7](#configuration-space-and-constraints)](#configuration-space-and-constraints)

[2.0.2 Equilibrium Operators under Constraints [9](#equilibrium-operators-under-constraints)](#equilibrium-operators-under-constraints)

[2.0.3 Reduced Hessian Operators [12](#reduced-hessian-operators)](#reduced-hessian-operators)

[2.0.4 Structural Index under Constraints [14](#structural-index-under-constraints)](#structural-index-under-constraints)

[2.1 Introduction [17](#_Toc223028762)](#_Toc223028762)

[2.1.1 Background [17](#_Toc223028763)](#_Toc223028763)

[2.1.2 [19](#_Toc223028764)](#_Toc223028764)

[2.1.3 Main Contributions [21](#_Toc223028765)](#_Toc223028765)

[2.1.4 Conceptual Interpretation [24](#_Toc223028766)](#_Toc223028766)

[2.1.5 Position Within the Series [26](#_Toc223028767)](#_Toc223028767)

[2.2 Constrained Variational Framework [28](#constrained-variational-framework)](#constrained-variational-framework)

[2.2.1 Weighted Network Model [28](#weighted-network-model)](#weighted-network-model)

[2.2.2 Polyhedral Feasible Set [29](#polyhedral-feasible-set)](#polyhedral-feasible-set)

[2.2.3 Constrained Optimisation Problem [31](#constrained-optimisation-problem)](#constrained-optimisation-problem)

[2.3 First-Order Optimality and Normal Geometry [33](#first-order-optimality-and-normal-geometry)](#first-order-optimality-and-normal-geometry)

[2.3.1 Lagrangian and KKT Conditions [33](#lagrangian-and-kkt-conditions)](#lagrangian-and-kkt-conditions)

[2.4 Constrained Relational Rigidity [38](#constrained-relational-rigidity)](#constrained-relational-rigidity)

[2.4.1 Tangent Cone and Active Faces [38](#tangent-cone-and-active-faces)](#tangent-cone-and-active-faces)

[2.4.2 Reduced Hessian [40](#reduced-hessian)](#reduced-hessian)

[2.4.3 Constrained Hyperbolicity [44](#constrained-hyperbolicity)](#constrained-hyperbolicity)

[2.5 Polyhedral Architecture and Support Classification [47](#polyhedral-architecture-and-support-classification)](#polyhedral-architecture-and-support-classification)

[2.5.1 Face Selection [47](#face-selection)](#face-selection)

[2.5.2 Support Classification [49](#support-classification)](#support-classification)

[2.5.3 Coupling Morphology and Sparsity Geometry [52](#coupling-morphology-and-sparsity-geometry)](#coupling-morphology-and-sparsity-geometry)

[2.6 Active-Face Stability and Local Uniqueness [56](#active-face-stability-and-local-uniqueness)](#active-face-stability-and-local-uniqueness)

[2.6.1 Reduced-Hessian Characterisation [56](#reduced-hessian-characterisation)](#reduced-hessian-characterisation)

[2.6.2 Active-Face Stability Theorem [58](#active-face-stability-theorem)](#active-face-stability-theorem)

[2.6.3 Structural Lock-In under Scarcity [62](#structural-lock-in-under-scarcity)](#structural-lock-in-under-scarcity)

[2.6.4 Synthesis [64](#synthesis)](#synthesis)

[2.7 Budget Perturbations and Face Transitions [67](#budget-perturbations-and-face-transitions)](#budget-perturbations-and-face-transitions)

[2.7.1 Parameterised Constraint System [69](#parameterised-constraint-system)](#parameterised-constraint-system)

[2.7.2 Piecewise-Smooth Equilibrium Branches [72](#piecewise-smooth-equilibrium-branches)](#piecewise-smooth-equilibrium-branches)

[2.7.3 Normal-Cone Boundary Conditions [75](#normal-cone-boundary-conditions)](#normal-cone-boundary-conditions)

[2.7.4 Regime Boundaries and Phase Transitions [77](#regime-boundaries-and-phase-transitions)](#regime-boundaries-and-phase-transitions)

[2.8 Recovery of the Interior Regime and Structural Generality [81](#recovery-of-the-interior-regime-and-structural-generality)](#recovery-of-the-interior-regime-and-structural-generality)

[2.8.1 Collapse of the KKT System in the Absence of Coupling [81](#collapse-of-the-kkt-system-in-the-absence-of-coupling)](#collapse-of-the-kkt-system-in-the-absence-of-coupling)

[2.8.2 Tangent-Cone Reduction [82](#tangent-cone-reduction)](#tangent-cone-reduction)

[2.8.3 Normal-Cone Collapse [82](#normal-cone-collapse)](#normal-cone-collapse)

[2.8.4 Canonical Resource Structures [83](#canonical-resource-structures)](#canonical-resource-structures)

[2.8.5 Structural Generality [84](#structural-generality)](#structural-generality)

[2.9 Conclusion [85](#conclusion)](#conclusion)

[Bibliography [87](#bibliography)](#bibliography)

# Paper 3: Constrained Variational Optimisation and Scarcity Geometry in Network Potential Theory

## 

## Abstract

This paper has extended the Network Potential Functional from interior optimisation on the hypercube to constrained optimisation over general polyhedral feasible sets. The resulting framework embeds relational optimisation within a nonlinear programming and variational-inequality formulation in which equilibrium architecture emerges from the interaction between intrinsic marginal structure and polyhedral scarcity geometry.

The principal analytical results may be summarised as follows.

First, equilibrium is characterised by the normal-cone inclusion condition

``` math
\nabla\Phi(w^{\star}) \in N_{\Omega}(w^{\star}),
```

which replaces the interior stationarity condition of Paper 2. First-order optimality is therefore determined jointly by structural marginal returns and the geometry of the feasible polytope.

Second, local stability is governed by reduced-Hessian negativity on the tangent space:

``` math
v^{\top}D^{2}\Phi(w^{\star})v < 0\text{for all }v \in T_{\Omega}(w^{\star}) \smallsetminus \{ 0\}.
```

This extends the full-space curvature condition of the interior regime and yields a notion of **constrained relational rigidity**, in which stability is determined by curvature restricted to admissible directions within the active face.

Third, scarcity induces a face-dependent structural architecture. Each active face of the feasible polytope defines a structural regime within which equilibrium is locally unique and depends smoothly on resource parameters. Support classification — suppressed, interior-on-face, or saturated — is determined by shadow-price-adjusted marginal returns.

Fourth, regime transitions occur precisely when the structural marginal field reaches the boundary of a normal cone. Parameter space therefore admits a locally finite decomposition into regions of smooth equilibrium behaviour separated by lower-dimensional degeneracy sets. Architectural change under scarcity arises through discrete face transitions rather than infinitesimal deformation.

The interior theory developed in Paper 2 is recovered as the degenerate case in which no linear resource constraint binds and the normal cone collapses to the origin. The constrained formulation therefore strictly generalises the original Network Potential framework while preserving its variational structure.

Taken together, Papers I and II establish a dual structural principle governing relational optimisation:

- **Intrinsic curvature differentiates ties.**

- **Polyhedral scarcity selects ties.**

Equilibrium architecture emerges from the interaction between these two mechanisms.

This completes the static theory of constrained Network Potential optimisation. Subsequent papers will develop dynamical formulations, endogenous topology, and operator-theoretic extensions building on the variational and geometric foundations established here.

# 2.0 Foundational Operator Framework

Paper 3 extends the operator framework developed in Paper 2 to constrained optimisation problems in which equilibrium configurations lie on polyhedral feasible regions. While Paper 2 analysed interior equilibria on the hypercube $`W = \lbrack 0,1\rbrack^{\mid E \mid}`$ , the present work considers optimisation over constrained feasible sets in which equilibrium configurations may lie on lower-dimensional faces.

Within this framework, equilibrium structure is determined jointly by the curvature of the relational potential and the geometry of the feasible region. The operator-theoretic viewpoint of Paper 2 therefore extends naturally to constrained optimisation through reduced operators defined on active constraint faces.

Throughout this paper, the relational potential

``` math
\Phi:W \rightarrow \mathbb{R}
```

is assumed to satisfy the admissibility and regularity conditions established in Paper 2. In particular, equilibrium configurations are characterised by stationarity conditions, local curvature is determined by the Hessian operator, and perturbation responses are governed by inverse curvature operators on admissible tangent spaces.

The principal new feature introduced in Paper 2 is the presence of linear coupling constraints linking tie strengths. These constraints induce a polyhedral feasible region

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\},
```

where the matrix $`A`$encodes resource couplings among edges.

Optimisation under constraints therefore replaces interior stationarity conditions with constrained stationarity conditions expressed through the Karush–Kuhn–Tucker system

``` math
\nabla\Phi(w^{*}) \in N_{\mathcal{W}_{A}}(w^{*}),
```

where $`N_{\mathcal{W}_{A}}(w^{*})`$ denotes the normal cone of the feasible region at equilibrium.

Within a fixed active constraint face, equilibrium behaviour is governed by reduced operators obtained by restricting the Hessian operator to the tangent space of the feasible region. These reduced operators play the same role for constrained equilibria that the incident Hessian operator plays for interior equilibria in Paper 2.

Consequently, structural differentiation under constraints is determined by anisotropy of reduced equilibrium response operators, while transitions between architectural regimes correspond to changes in the active constraint set.

This section establishes the operator framework required for the constrained structural analysis developed in the remainder of the paper.

## 2.0.1 Configuration Space and Constraints

Let

``` math
G = (V,E)
```

be a fixed finite undirected graph with edge set $`E`$. Edge weights are represented by vectors

``` math
w \in \mathbb{R}^{\mid E \mid}
```

with components $`w_{e}`$indexed by edges $`e \in E`$.

In the unconstrained formulation analysed in Paper 2, the admissible weight domain is the hypercube

``` math
W = \lbrack 0,1\rbrack^{\mid E \mid},
```

with interior

``` math
W^{\circ} = (0,1)^{\mid E \mid}.
```

Paper 2 introduces explicit coupling constraints between edge weights. The admissible configuration space is therefore taken to be the polyhedral region

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\},
```

where

``` math
A \in \mathbb{R}^{m \times \mid E \mid}
```

is a constraint matrix and

``` math
b \in \mathbb{R}^{m}
```

is a constraint vector.

The inequalities

``` math
Aw \leq b
```

represent linear resource couplings among edge weights. These constraints may encode node-level allocation limits, global resource budgets, or overlapping group budgets.

The feasible region $`\mathcal{W}_{A}`$is a compact convex polytope contained in $`W`$. Its boundary consists of a finite collection of polyhedral faces corresponding to active subsets of the constraint system.

**Active Constraint Sets**

For a feasible configuration $`w \in \mathcal{W}_{A}`$, the **active constraint set** is defined by

``` math
\mathcal{A(}w) = \{ j:A_{j}w = b_{j}\} \cup \{ e:w_{e} = 0\text{ or }w_{e} = 1\},
```

where $`A_{j}`$ denotes the $`j`$-th row of $`A`$.

The active constraint set determines a polyhedral face

``` math
F(w) \subseteq \mathcal{W}_{A}
```

containing $`w`$.

Within a fixed face $`F`$, feasible perturbations are restricted to the tangent space

``` math
T_{F} = \{\delta w \in \mathbb{R}^{\mid E \mid}:A_{j}\delta w = 0\text{ for }j \in \mathcal{A(}w),\text{\:\,}\delta w_{e} = 0\text{ for active box constraints}\}.
```

The tangent space $`T_{F}`$ describes admissible infinitesimal variations of the weight vector that preserve the active constraint set.

**Interior and Boundary Regimes**

Configurations in the interior of the feasible region satisfy

``` math
Aw < b,0 < w_{e} < 1.
```

In this regime,

``` math
T_{F} = \mathbb{R}^{\mid E \mid},
```

and the optimisation problem reduces locally to the interior case analysed in Paper 2.

Boundary equilibria arise when one or more constraints are active. In such cases equilibrium behaviour is governed by operators restricted to the corresponding tangent space.

This distinction between interior and boundary regimes forms the geometric basis for the constrained structural analysis developed in the remainder of the paper.

## 

## 2.0.2 Equilibrium Operators under Constraints

Let

``` math
\Phi:W \rightarrow \mathbb{R}
```

be a relational potential satisfying the regularity conditions established in Paper 2, and let

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\}
```

be the polyhedral feasible region defined in Section 2.0.1.

An equilibrium configuration

``` math
w^{*} \in \mathcal{W}_{A}
```

is characterised by the constrained stationarity condition

``` math
\nabla\Phi(w^{*}) \in N_{\mathcal{W}_{A}}(w^{*}),
```

where

``` math
N_{\mathcal{W}_{A}}(w^{*})
```

denotes the normal cone of the feasible region at $`w^{*}`$.

Equivalently, equilibrium configurations satisfy the Karush–Kuhn–Tucker system

``` math
\nabla\Phi(w^{*}) + A^{\top}\lambda^{*} + \mu^{*} - \nu^{*} = 0,
```

subject to

``` math
{\lambda^{*} \geq 0,
}{\mu^{*} \geq 0,\nu^{*} \geq 0,
}
```

and complementary slackness conditions

``` math
{\lambda_{j}^{*}(A_{j}w^{*} - b_{j}) = 0,
}{\mu_{e}^{*}w_{e}^{*} = 0,\nu_{e}^{*}(1 - w_{e}^{*}) = 0.
}
```

Here

- $`\lambda^{*}`$denotes multipliers associated with linear constraints,

- $`\mu^{*}`$corresponds to lower box constraints,

- $`\nu^{*}`$corresponds to upper box constraints.

Thus, equilibrium weights are determined jointly by structural marginal incentives and constraint-induced shadow prices.

**Tangent-Space Operators**

Let

``` math
F \subseteq \mathcal{W}_{A}
```

be the polyhedral face determined by the active constraint set at $`w^{*}`$, and let

``` math
T_{F} \subseteq \mathbb{R}^{\mid E \mid}
```

denote the corresponding tangent space defined in Section 2.0.1.

Local equilibrium behaviour within the face $`F`$is governed by perturbations

``` math
\delta w \in T_{F}.
```

The second-order structure of the constrained optimisation problem is determined by the **restricted Hessian operator**

``` math
H_{F}(w^{*}) = D^{2}\Phi(w^{*}) \mid_{T_{F}},
```

obtained by restricting the Hessian operator to the tangent space.

Strict local maximality within the face requires that

``` math
H_{F}(w^{*})
```

be negative definite on $`T_{F}`$.

**Reduced Equilibrium Response Operators**

If the restricted Hessian operator

``` math
H_{F}(w^{*})
```

is nonsingular on $`T_{F}`$, then equilibrium weights vary differentiably with respect to perturbation parameters that preserve the active constraint set.

Under such perturbations the equilibrium response equation becomes

``` math
H_{F}(w^{*})\frac{dw^{*}}{d\lambda} = - P_{F}\frac{\partial}{\partial\lambda}\nabla\Phi_{\lambda}(w^{*}),
```

where

``` math
P_{F}
```

denotes projection onto the tangent space $`T_{F}`$.

Solving for the equilibrium response gives

``` math
\frac{dw^{*}}{d\lambda} = - H_{F}(w^{*})^{- 1}P_{F}\frac{\partial}{\partial\lambda}\nabla\Phi_{\lambda}(w^{*}).
```

Thus, the inverse restricted Hessian operator

``` math
H_{F}(w^{*})^{- 1}
```

acts as the equilibrium response operator within the active constraint face.

This reduced operator governs the first-order propagation of perturbations in constrained equilibrium configurations and plays the same role for boundary equilibria that the susceptibility kernel plays for interior equilibria in Paper 2.

## 

## 2.0.3 Reduced Hessian Operators

Structural differentiation under constraints is characterised by the sensitivity of equilibrium weights to perturbations that preserve the active constraint set.

Let

``` math
w^{*} \in \mathcal{W}_{A}
```

be an equilibrium configuration with active constraint face

``` math
F \subseteq \mathcal{W}_{A}
```

and tangent space

``` math
T_{F} \subseteq \mathbb{R}^{\mid E \mid}.
```

Let

``` math
H_{F}(w^{*}) = D^{2}\Phi(w^{*}) \mid_{T_{F}}
```

denote the restricted Hessian operator introduced in Section 2.0.2 and suppose that $`H_{F}(w^{*})`$ is nonsingular on $`T_{F}`$.

Let

``` math
g
```

denote a structural perturbation gradient projected onto the tangent space:

``` math
g_{F} = P_{F}g,
```

where $`P_{F}`$is the projection onto $`T_{F}`$.

Under perturbations that preserve the active constraint set, equilibrium weights vary according to the reduced equilibrium response equation

``` math
dw^{*} = - H_{F}(w^{*})^{- 1}g_{F}.
```

This vector describes the first-order equilibrium response within the constraint face.

**Definition 2.0.1 (Reduced Structural Index)**

The **reduced structural index vector** is defined by

``` math
\sigma_{F} = H_{F}(w^{*})^{- 1}g_{F}.
```

For an edge $`e \in E`$, the **reduced structural index** is

``` math
\left( \sigma_{F})_{e}. \right.\ 
```

The reduced structural index measures the first-order equilibrium responsiveness of edge weights under perturbations that preserve the active constraint set.

**Incident Reduced Differentiation**

For a node $`i \in V`$, structural differentiation within the constraint face occurs when

``` math
\left( \sigma_{F})_{e} \neq (\sigma_{F})_{f} \right.\ 
```

for distinct edges

``` math
e,f \in \delta(i).
```

This condition expresses differentiation of incident edges in terms of equilibrium response within the constrained tangent space.

**Relation to Interior Structural Indices**

When the equilibrium configuration lies in the interior of the feasible region,

``` math
Aw^{*} < b,0 < w_{e}^{*} < 1,
```

the tangent space satisfies

``` math
T_{F} = \mathbb{R}^{\mid E \mid},
```

and the restricted Hessian operator reduces to the full Hessian operator:

``` math
H_{F}(w^{*}) = H(w^{*}).
```

In this case the reduced structural index coincides with the structural index defined in Paper 2:

``` math
\sigma_{F} = \sigma.
```

Thus, the reduced structural index provides a natural extension of the interior structural index to constrained equilibrium configurations.

## 

## 2.0.4 Structural Index under Constraints

Throughout this paper, genericity statements are understood with respect to the class of admissible relational potentials introduced in Paper 2.

Let

``` math
\mathcal{F}
```

denote the class of relational potentials satisfying the regularity and admissibility conditions of Paper 2, equipped with the $`C^{2}`$topology on compact subsets of the configuration space.

A property is said to hold **generically** if it holds on an open dense subset of $`\mathcal{F}`$.

Generic properties therefore persist under sufficiently small perturbations of the relational potential and exclude only degenerate cases requiring exact algebraic coincidences among derivatives or constraint parameters.

**Generic Regularity Conditions**

Unless otherwise stated, all equilibria considered in this paper are assumed to satisfy the following generic regularity conditions:

**1. Nondegenerate Reduced Hessian**

The restricted Hessian operator

``` math
H_{F}(w^{*})
```

is nonsingular on the tangent space $`T_{F}`$.

**2. Strict Complementarity**

For each active inequality constraint,

``` math
\lambda_{j}^{*} > 0,
```

and for each active box constraint,

``` math
\mu_{e}^{*} > 0\text{or}\nu_{e}^{*} > 0.
```

**3. Stable Active Constraint Sets**

The active constraint set remains locally constant under sufficiently small perturbations of parameters.

**Structural Interpretation**

Failure of these conditions corresponds to boundary cases in which:

- the reduced operator loses invertibility,

- multiple constraint faces intersect,

- or equilibrium configurations transition between regimes.

Such degeneracies form a nowhere-dense subset of the admissible class and therefore do not affect generic structural behaviour.

The operator framework established in Sections 2.0.1–2.0.4 provides the foundation for the constrained structural analysis developed in the remainder of this paper.**\**

<span id="_Toc223028762" class="anchor"></span>**2.1 Introduction**

<span id="_Toc223028763" class="anchor"></span>**2.1.1 Background**\
The Network Potential Functional (NPF), introduced in the foundational dissertation of this series, defines a scalar functional on the space of weighted graphs. For a fixed simple graph $`G = (V,E)`$ with edge-weight vector $`w \in \lbrack 0,1\rbrack^{\mid E \mid}`$ , the functional

``` math
\Phi_{G}:\lbrack 0,1\rbrack^{\mid E \mid} \rightarrow \mathbb{R}
```

integrates three competing structural forces:

- cohesion (stability of direct ties),

- brokerage (exposure to nonredundant second-order neighbourhoods),

- redundancy (closure-induced overlap).

The optimisation problem

``` math
\underset{w \in \lbrack 0,1\rbrack^{\mid E \mid}}{\max}\Phi_{G}(w)
```

was shown to admit maximisers under compactness of the domain, with first-order conditions expressible as balance equations equating marginal cohesion and brokerage gains against redundancy costs.

Paper 2 developed the structural consequences of these balance equations under interior optimisation. Assuming strict local maximality and negative definiteness of the Hessian operator

``` math
H(w^{*}) = D^{2}\Phi_{G}(w^{*}),
```

optimal configurations were shown to generically exhibit structural differentiation: incident edges are strictly ordered according to their structural responsiveness, and symmetric configurations are unstable under perturbation. Structural differentiation was characterised through the structural index

``` math
\sigma_{e} = \mid (H(w^{*})^{- 1}g)_{e} \mid ,
```

which measures first-order equilibrium responsiveness to perturbation.

A key structural feature of the analysis in Paper 2 is that optimality was evaluated in the full ambient space $`\mathbb{R}^{\mid E \mid}`$. The feasible region was the hypercube $`\left\lbrack 0,1\rbrack^{\mid E \mid} \right.\`$ , and interior solutions were characterised by vanishing multipliers for box constraints. Curvature was therefore assessed relative to all directions in weight space, and differentiation emerged from anisotropy of the inverse Hessian operator.

However, the independence of edge weights implicit in the hypercube domain imposes a structural limitation. In many relational systems, tie strengths are not independently adjustable. Resource constraints—whether representing attention budgets, capacity limits, or overlapping allocation commitments—introduce linear coupling between weights.

Once such coupling is imposed, optimality is no longer determined solely by intrinsic curvature of $`\Phi_{G}`$ , but also by the geometry of the feasible region. Stationarity must then be interpreted relative to a tangent cone, and curvature must be evaluated on directions admissible under active constraints.

The present paper therefore extends the NPF framework from interior optimisation on a hypercube to constrained optimisation on a general polyhedral feasible set.

This shift is not merely technical; it alters the structural law governing equilibrium architecture.

Whereas Paper 2 demonstrated that intrinsic curvature induces differentiation among incident ties, the introduction of linear coupling reveals a second organising principle: scarcity geometry selects which ties survive. In the constrained regime, equilibrium architecture arises from the interaction between structural marginal incentives and the normal geometry of the feasible polytope.

The development that follows formalises this extension within the operator framework established in Section 2.0. The independent-weight domain is replaced by a polyhedral feasible set defined by arbitrary linear inequalities, and the resulting optimisation problem is analysed using Karush–Kuhn–Tucker conditions, normal-cone inclusion, and reduced-Hessian stability on tangent cones.

The interior regime studied in Paper 2 appears as the special case in which no coupling constraint binds and the reduced Hessian coincides with the full Hessian operator.

<span id="_Toc223028764" class="anchor"></span>**2.1.2 From Interior Architecture to Scarcity Geometry**\
The analysis of Paper 2 established that, in the absence of coupling constraints, equilibrium architecture is governed by intrinsic curvature of the Network Potential Functional.

When the maximiser lies in the interior of the hypercube, the first-order condition reduces to

``` math
\nabla\Phi_{G}(w^{*}) = 0,
```

and structural differentiation emerges from anisotropy of the inverse Hessian operator.

In this regime, architecture is an intrinsic property of the functional itself: differentiation is induced by imbalance in structural responsiveness across incident edges, and symmetry breaking follows from hyperbolicity of equilibrium.

The introduction of linear coupling constraints alters this geometry fundamentally. Consider a feasible region of the form

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{\mid E \mid} \mid Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\}.
```

The feasible set is a convex polytope embedded in $`\mathbb{R}^{\mid E \mid}`$. Interior stationarity is replaced by stationarity relative to a feasible cone, and curvature must be evaluated relative to directions admissible within the tangent cone of $`\mathcal{W}_{A}`$ at the candidate solution.

In the interior regime, optimality is determined by the vanishing of the gradient. Under coupling, optimality instead requires

``` math
\nabla\Phi_{G}(w^{*}) \in N_{\mathcal{W}_{A}}(w^{*}),
```

where $`N_{\mathcal{W}_{A}}(w^{*})`$ denotes the normal cone of the feasible polytope at $`w^{*}`$.

Thus, the structural marginal field must align with an outward normal of the active face.

This change has two immediate consequences.

**Face-Dependent Architecture**

Architecture becomes face-dependent. Rather than selecting a point in the interior of a smooth domain, the optimisation problem selects a face of the feasible polytope on which equilibrium lies.

Different active constraint sets correspond to different faces and therefore to distinct architectural regimes. Support patterns of edge weights are determined not solely by intrinsic curvature of $`\Phi_{G}`$, but by which inequalities bind.

**Scarcity-Induced Selection**

Scarcity induces endogenous sparsity.

In the interior regime, differentiation orders incident edges but does not eliminate them unless box constraints bind. Under linear coupling, however, the presence of positive Lagrange multipliers alters marginal balance conditions.

Edges whose structural marginal return falls below the effective shadow price imposed by active constraints are suppressed.

Thus, whereas Paper 2 established a law of differentiation, the constrained regime establishes a law of selection.

The structural problem therefore shifts from analysing smooth critical points in $`\mathbb{R}^{\mid E \mid}`$ to analysing equilibrium on polyhedral faces under non-concave curvature.

The appropriate mathematical framework is nonlinear programming with strong second-order sufficient conditions evaluated on tangent cones. Reduced-Hessian analysis replaces full-space definiteness, and regime transitions occur when the structural marginal field crosses the boundary of a normal cone associated with a given face.

In this sense, scarcity geometry acts as a projection operator on structural incentives. The intrinsic marginal forces generated by cohesion, brokerage, and redundancy are filtered through the linear coupling constraints, and the resulting projection determines both the support and stability of equilibrium configurations.

The interior regime analysed in Paper 2 appears as the special case in which no linear constraint binds and the normal cone reduce to $`\left\{ 0 \right\}`$.

The remainder of this paper formalises this shift. We show that under general linear coupling, equilibrium architecture is characterised by normal-cone inclusion, constrained relational rigidity, and face-dependent stability.

This extension reveals a second organising principle of relational optimisation: curvature differentiates ties, while polyhedral scarcity selects them.

<span id="_Toc223028765" class="anchor"></span>**2.1.3 Main Contributions**\
This paper extends the Network Potential Functional (NPF) framework from interior optimisation on the hypercube to constrained optimisation on general polyhedral domains. The principal contributions are the following.

**(i) Polyhedral Normal-Cone Characterisation**

We prove that a weight vector $`w^{*} \in \mathcal{W}_{A}`$satisfies the first-order necessary optimality conditions if and only if

``` math
\nabla\Phi_{G}(w^{*}) \in N_{\mathcal{W}_{A}}(w^{*}),
```

where $`N_{\mathcal{W}_{A}}(w^{*})`$denotes the normal cone of the feasible polytope at $`w^{*}`$.

This embeds the NPF optimisation problem within finite-dimensional variational inequality theory and establishes that equilibrium architecture is determined by the interaction between the structural marginal field and the outward normal geometry of the active face.

**(ii) Constrained Relational Rigidity**

We introduce a notion of constrained relational rigidity defined by negative definiteness of the reduced Hessian operator

``` math
H_{F}(w^{*}) = P_{F}^{T}H(w^{*})P_{F},
```

where $`P_{F}`$denotes the tangent-space projection operator associated with the active face $`F`$.

Under linear independence constraint qualification (LICQ) and strong second-order sufficiency on the tangent cone, we prove that constrained equilibria are locally unique and isolated within their active face.

This generalises the hyperbolic rigidity result of Paper 2 from full-space curvature to face-restricted reduced-Hessian geometry.

**(iii) Face Selection and Support Classification**

We establish a **Face Selection Theorem** showing that equilibrium configurations correspond to faces of the feasible polytope whose normal cones contain the structural marginal vector.

From this we derive a **Polyhedral Support Classification Theorem** characterising edge weights as:

- suppressed (inactive),

- saturated at upper bound,

- interior on the active face,

according to shadow-price-adjusted marginal incentives.

This yields a general sparsity law:

**Under linear resource coupling, ties survive precisely when their marginal structural return is not strictly dominated by the effective shadow price induced by the active constraint geometry.**

This result strictly generalises node-level and global budget pruning as special cases.

**(iv) Active-Face Stability and Architectural Lock-In**

We prove that under constrained rigidity and nondegeneracy, the active face is locally stable under small perturbations of constraint parameters or structural coefficients.

Thus scarcity-induced sparsity exhibits structural lock-in analogous to the differentiation lock-in established in Paper 2.

Local stability is governed by the reduced Hessian operator $`H_{F}(w^{*})`$, whose invertibility determines persistence of the active regime.

**(v) Regime Transitions under Budget Perturbation**

We analyse parameterised constraint systems

``` math
Aw \leq b(t)
```

and show that equilibrium branches are piecewise smooth within active regimes.

Face transitions occur precisely when the structural marginal vector crosses the boundary of a normal cone associated with the current face.

This yields a geometric characterisation of scarcity-induced phase transitions in terms of normal-cone bifurcation.

Collectively, these results establish that relational optimisation under the Network Potential Functional is governed by two interacting principles:

- **Intrinsic curvature induces differentiation (Paper 2).**

- **Polyhedral scarcity induces selection (Paper 2).**

The interior regime analysed previously is recovered as the special case in which no linear constraint binds and the normal cone reduce to $`\left\{ 0 \right\}`$.

<span id="_Toc223028766" class="anchor"></span>**2.1.4 Conceptual Interpretation**

The results developed in this paper reveal that equilibrium architecture under the Network Potential Functional is governed by two distinct geometric operators: intrinsic curvature and polyhedral scarcity.

In the interior regime analysed in Paper 2, architectural differentiation arises from anisotropy of the Hessian. Incident edges are ordered according to brokerage exposure and redundancy participation, and symmetry breaking follows from strict negative definiteness of the full curvature operator. Architecture in that regime is an intrinsic property of the functional: differentiation is induced by the internal geometry of $`\Phi_{G}`$.

The introduction of linear coupling constraints adds a second organising principle. The feasible region becomes a polytope whose faces encode resource allocation regimes. Optimality is no longer characterised by vanishing of the gradient, but by inclusion of the structural marginal field in the normal cone of the active face. Thus, equilibrium architecture is determined by a projection mechanism: intrinsic structural incentives are filtered through scarcity geometry.

Formally, equilibrium requires

``` math
\nabla\Phi_{G}\left( w^{*} \right) \in N_{\mathcal{W}_{A}}\left( w^{*} \right).
```

Geometrically, this condition states that the marginal incentive vector must lie within the outward normal cone of the face supporting the solution. Different faces correspond to different sparsity patterns and support configurations. The active face therefore acts as an architectural selector.

This yields a dual structural law:

- Curvature differentiates ties.

- Scarcity selects ties.

Differentiation arises from second-order structure of the functional; selection arises from first-order interaction between the gradient and constraint normals. When both mechanisms operate simultaneously, architecture becomes the outcome of a tension between marginal structural incentives and shadow-price geometry.

The constraint matrix $`A`$plays a central structural role. Its incidence structure determines which edges are coupled, and therefore which ties compete for shared resources. Sparse rows produce locally clustered suppression; dense rows induce global compression; hierarchical constraint families generate nested sparsity strata. In this sense, coupling geometry induces sparsity morphology.

The interior regime appears as the degenerate case in which no linear constraint binds. The normal cone then reduces to the zero vector, and equilibrium conditions collapse to the smooth stationarity analysed previously. Thus, the present framework strictly generalises the interior analysis rather than replacing it.

Taken together, the results show that relational optimisation under the NPF is not governed solely by smooth variational geometry. It is governed by the interaction between smooth curvature and polyhedral structure. Architecture is the equilibrium outcome of this interaction.

The subsequent sections formalise these claims, deriving first-order optimality conditions, defining constrained relational rigidity, and classifying support patterns via face selection and reduced-Hessian stability.

<span id="_Toc223028767" class="anchor"></span>**2.1.5 Position Within the Series**

This paper constitutes the second structural development in the Network Potential Series.

The foundational dissertation introduced the Network Potential Functional as a scalar variational object defined on weighted graphs, established existence of maximisers under compactness of the weight domain, and analysed curvature regimes governing local stability.

That work formalised relational optimisation as a potential-theoretic problem and provided the first-order and second-order tools necessary for equilibrium analysis.

Paper 2 advanced the theory by analysing strict interior maximisers. Under smooth stationarity and negative definiteness of the full Hessian operator, equilibrium configurations were shown to generically exhibit structural differentiation and symmetry breaking. Architecture in that regime arises from anisotropy of the inverse Hessian operator.

The present paper extends the framework to constrained optimisation under general linear resource coupling.

Whereas Paper 2 established a law of differentiation, Paper 2 establishes a law of selection.

By embedding the NPF within polyhedral nonlinear programming and reduced-Hessian operator theory, we show that equilibrium architecture is determined jointly by curvature and scarcity geometry.

The interior regime analysed previously is recovered as the special case in which no linear constraint binds.

The progression across the Series is therefore structural:

- The dissertation defined the variational object.

- Paper 2 analysed intrinsic architectural differentiation.

- Paper 2 analyses scarcity-induced support selection and face-dependent stability.

Subsequent developments will examine dynamical formulations and endogenous topological evolution under the NPF, but those lie beyond the scope of the present work.

Here the focus remains on static constrained equilibrium and its geometric structure.

With this positioning established, we now formalise the constrained optimisation problem and derive its necessary and sufficient optimality conditions.

# **2.2** Constrained Variational Framework

2.2.1 Weighted Network Model\
-----------------------------

Let $`G = (V,E)`$be a fixed finite simple graph with $`\mid E \mid = m`$.

A weighted configuration is represented by a vector

``` math
w = (w_{e})_{e \in E} \in \mathbb{R}^{m}.
```

The admissible weight domain without coupling constraints is the hypercube

``` math
\left\lbrack 0,1\rbrack^{m}. \right.\ 
```

We assume throughout that the Network Potential Functional

``` math
\Phi_{G}:\lbrack 0,1\rbrack^{m} \rightarrow \mathbb{R}
```

is twice continuously differentiable on an open neighbourhood of $`\left\lbrack 0,1\rbrack^{m} \right.\`$ ; that is,

``` math
\Phi_{G} \in C^{2}(U)\text{for some open set }U \supset \lbrack 0,1\rbrack^{m}.
```

This regularity ensures that:

- the gradient $`\nabla\Phi_{G}(w)`$is well defined and continuous,

- the Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w)
```

exists and is continuous,

- second-order optimality conditions can be formulated.

No global concavity is assumed. In particular, closure interactions in the redundancy component generically induce non-concave curvature regimes, so local analysis via first- and second-order conditions is required.

We emphasise that the graph $`G`$ is fixed throughout the present paper. The analysis concerns optimisation over edge weights rather than evolution of the underlying topology. Topological dynamics are deferred to later work in the Series.

With this smooth weighted model in place, we now introduce linear coupling constraints defining the polyhedral feasible region.

### 2.2.2 Polyhedral Feasible Set

To model resource coupling between edge weights, we introduce a finite system of linear inequalities.

Let

``` math
A \in \mathbb{R}^{k \times m},b \in \mathbb{R}^{k},
```

where $`m = \mid E \mid`$.

We define the polyhedral feasible region

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{m}:Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\}.
```

Here inequalities are understood componentwise.

The system $`Aw \leq b`$encodes arbitrary linear coupling constraints among edge weights.

This formulation subsumes, as special cases:

- node-level budget constraints,

- global budget constraints,

- overlapping allocation pools,

- hierarchical capacity systems,

- and other structured linear resource limits.

**Assumptions**

We impose the following standing assumptions.

**(A1) Non-emptiness**

The feasible region $`\mathcal{W}_{A}`$ is nonempty.

**(A2) Compactness**

Since $`0 \leq w \leq 1`$, the feasible set is bounded; together with closedness of linear inequality systems, this implies $`\mathcal{W}_{A}`$ is compact.

**(A3) Constraint Regularity**

At candidate optimal points, the Linear Independence Constraint Qualification (LICQ) holds; that is, the gradients of active constraints are linearly independent.

No convexity of $`\Phi_{G}`$ is assumed. The feasible set $`\mathcal{W}_{A}`$ is convex, but the objective is generically non-concave.

**Geometric Interpretation**

The set $`\mathcal{W}_{A}`$ is a convex polytope embedded in $`\mathbb{R}^{m}`$.

Each subset of binding constraints determines a face of this polytope.

Constrained equilibria therefore lie on faces determined by active linear inequalities and possibly active box constraints.

For a candidate equilibrium $`w^{*} \in \mathcal{W}_{A}`$ , admissible perturbations are restricted to the tangent cone

``` math
T_{\mathcal{W}_{A}}(w^{*}),
```

while equilibrium forces are represented by vectors in the normal cone

``` math
N_{\mathcal{W}_{A}}(w^{*}).
```

In contrast to the interior regime analysed in Paper 2, curvature must now be evaluated relative to directions contained in the tangent cone.

### 2.2.3 Constrained Optimisation Problem

We consider the nonlinear programming problem

``` math
\underset{w \in \mathcal{W}_{A}}{\max}\Phi_{G}(w),
```

where

``` math
\mathcal{W}_{A} = \left\{ w \in \mathbb{R}^{m}:Aw \leq b,\text{\:\,}0 \leq w \leq 1 \right\}.
```

The feasible set $`\mathcal{W}_{A}`$ is convex and compact by Assumptions (A1)–(A2), while the objective $`\Phi_{G}`$ is continuous and twice continuously differentiable on a neighbourhood of this set.

**Existence of Maximiser**

**Proposition 2.1 (Existence)**

There exists at least one maximiser

``` math
w^{*} \in \mathcal{W}_{A}
```

such that

``` math
\Phi_{G}(w^{*}) = \underset{w \in \mathcal{W}_{A}}{\max}\Phi_{G}(w).
```

**Proof**

The feasible set $`\mathcal{W}_{A}`$ is nonempty and compact. The function $`\Phi_{G}`$ is continuous on $`\mathcal{W}_{A}`$. The result follows from the Weierstrass extreme value theorem.

**Local Versus Global Optimality**

Because $`\Phi_{G}`$is not assumed concave, the maximiser need not be unique, and local maximisers may differ from global maximisers.

The analysis that follows therefore concerns:

- first-order necessary conditions,

- second-order sufficient conditions for strict local maximality,

- stability of equilibria within active faces.

We emphasise that convexity of the feasible set does not imply convexity of the optimisation problem. Structural multiplicity remains possible under scarcity.

**Notational Convention**

For the remainder of this paper, a vector

``` math
w^{*} \in \mathcal{W}_{A}
```

denotes a candidate local maximiser unless explicitly stated otherwise.

# 2.3 First-Order Optimality and Normal Geometry

### 2.3.1 Lagrangian and KKT Conditions

We derive first-order necessary conditions for constrained optimality of the Network Potential Functional over the polyhedral feasible region $`\mathcal{W}_{A}`$. Throughout, let

``` math
w^{\star} \in \mathcal{W}_{A}
```

denote a local maximiser and assume LICQ holds at $`w^{\star}`$.

**Lagrangian**

Let

``` math
A \in \mathbb{R}^{k \times m},b \in \mathbb{R}^{k},
```

with $`m = \mid E \mid`$.

Introduce Lagrange multipliers:

- $`\lambda \in \mathbb{R}_{\geq 0}^{k}`$for linear constraints $`Aw \leq b`$,

- $`\mu^{-} \in \mathbb{R}_{\geq 0}^{m}`$for lower bounds $`w \geq 0`$,

- $`\mu^{+} \in \mathbb{R}_{\geq 0}^{m}`$for upper bounds $`w \leq 1`$.

Define the Lagrangian

``` math
\mathcal{L(}w,\lambda,\mu^{-},\mu^{+}) = \Phi_{G}(w) + \lambda^{\top}(b - Aw) + (\mu^{-})^{\top}w + (\mu^{+})^{\top}(1 - w).
```

**Active Sets**

Define the active constraint index sets at $`w^{\star}`$:

``` math
{\mathcal{I(}w^{\star}) = \{ i \in \{ 1,\ldots,k\}:(Aw^{\star})_{i} = b_{i}\},
}{\mathcal{Z(}w^{\star}) = \{ j \in \{ 1,\ldots,m\}:w_{j}^{\star} = 0\},
}{\mathcal{U(}w^{\star}) = \{ j \in \{ 1,\ldots,m\}:w_{j}^{\star} = 1\}.
}
```

**Theorem 2.2 (KKT Necessary Conditions)**

If $`w^{\star}`$is a local maximiser and LICQ holds at $`w^{\star}`$, then there exist multipliers

``` math
\lambda^{\star} \in \mathbb{R}_{\geq 0}^{k},\mu^{- \star} \in \mathbb{R}_{\geq 0}^{m},\mu^{+ \star} \in \mathbb{R}_{\geq 0}^{m}
```

such that:

**(i) Stationarity**

``` math
\nabla\Phi_{G}(w^{\star}) - A^{\top}\lambda^{\star} + \mu^{- \star} - \mu^{+ \star} = 0.
```

**(ii) Primal feasibility**

``` math
Aw^{\star} \leq b,0 \leq w^{\star} \leq 1.
```

**(iii) Dual feasibility**

``` math
\lambda^{\star} \geq 0,\mu^{- \star} \geq 0,\mu^{+ \star} \geq 0.
```

**(iv) Complementarity**

``` math
{\lambda_{i}^{\star}((Aw^{\star})_{i} - b_{i}) = 0\forall i,
}{\mu_{j}^{- \star}w_{j}^{\star} = 0\forall j,
}{\mu_{j}^{+ \star}(1 - w_{j}^{\star}) = 0\forall j.
}
```

**Operator Interpretation**

Relative to the interior regime of Paper 2, stationarity no longer requires

``` math
\nabla\Phi_{G}(w^{\star}) = 0.
```

Instead, equilibrium is determined by balance between intrinsic structural marginals and constraint shadow prices:

``` math
\nabla\Phi_{G}(w^{\star}) = A^{\top}\lambda^{\star} - \mu^{- \star} + \mu^{+ \star}.
```

Thus, constrained equilibrium is determined jointly by:

- intrinsic structural incentives generated by $`\Phi_{G}`$,

- scarcity pressures encoded by $`A^{\top}\lambda^{\star}`$,

- and boundary activation represented by $`\mu^{- \star},\mu^{+ \star}`$.

The vector

``` math
\nabla\Phi_{G}(w^{\star})
```

therefore, acts as a structural marginal field whose equilibrium orientation is determined by polyhedral constraint geometry.

**2.3.2 Variational Inequality Formulation**

The Karush–Kuhn–Tucker conditions admit an equivalent geometric formulation in terms of variational inequalities and normal cones. This formulation makes explicit that constrained optimality is governed by the interaction between the structural marginal field $`\nabla\Phi_{G}`$ and the face geometry of the feasible polytope.

**Variational Inequality Formulation**

Let

``` math
\mathcal{W}_{A} \subset \mathbb{R}^{m}
```

be the feasible region.

Define the variational inequality problem:

``` math
\text{Find }w^{\star} \in \mathcal{W}_{A}\text{ such that }\langle\nabla\Phi_{G}(w^{\star}),w - w^{\star}\rangle \leq 0\forall w \in \mathcal{W}_{A}.
```

**Proposition 2.3 (First-Order Optimality as a Variational Inequality)**

If $`w^{\star}`$ is a local maximiser of $`\Phi_{G}`$ over $`\mathcal{W}_{A}`$, then $`w^{\star}`$satisfies the variational inequality above.

**Proof (sketch)**

For any feasible direction

``` math
d = w - w^{\star},
```

local maximality implies

``` math
D\Phi_{G}(w^{\star})\lbrack d\rbrack \leq 0.
```

Since $`\Phi_{G} \in C^{1}`$,

``` math
D\Phi_{G}(w^{\star})\lbrack d\rbrack = \langle\nabla\Phi_{G}(w^{\star}),d\rangle,
```

yielding the claim.

**Normal Cone**

For a closed convex set $`C \subset \mathbb{R}^{m}`$, define

``` math
N_{C}(x) = \{ y \in \mathbb{R}^{m}:\langle y,z - x\rangle \leq 0\ \forall z \in C\}.
```

For $`C = \mathcal{W}_{A}`$we write

``` math
N_{\mathcal{W}_{A}}(w^{\star}).
```

**Proposition 2.4 (Normal Cone Characterisation)**

A point $`w^{\star} \in \mathcal{W}_{A}`$ satisfies

``` math
\langle\nabla\Phi_{G}(w^{\star}),w - w^{\star}\rangle \leq 0\forall w \in \mathcal{W}_{A}
```

if and only if

``` math
\nabla\Phi_{G}(w^{\star}) \in N_{\mathcal{W}_{A}}(w^{\star}).
```

**Connection to KKT Multipliers**

Under LICQ,

``` math
N_{\mathcal{W}_{A}}(w^{\star}) = \{ A^{\top}\lambda - \mu^{-} + \mu^{+} \mid \lambda,\mu^{-},\mu^{+} \geq 0\text{ and complementarity holds}\}.
```

Consequently,

``` math
\nabla\Phi_{G}(w^{\star}) = A^{\top}\lambda^{\star} - \mu^{- \star} + \mu^{+ \star},
```

which states that $`\nabla\Phi_{G}(w^{\star})`$ is an outward normal vector to the feasible polytope at $`w^{\star}`$.

**Geometric Interpretation**

The inclusion

``` math
\nabla\Phi_{G}(w^{\star}) \in N_{\mathcal{W}_{A}}(w^{\star})
```

implies that $`w^{\star}`$lies on a face $`F`$of the polytope whose normal cone contains the structural marginal vector.

Thus, constrained optimisation selects:

- a weight configuration,

- an active face,

- and, therefore, a support regime.

This face dependence is the origin of the endogenous sparsity phenomena developed in later sections.

# 2.4 Constrained Relational Rigidity

## 2.4.1 Tangent Cone and Active Faces

The normal-cone characterisation of §2.3.2 shows that first-order optimality is governed by the outward geometry of the feasible polytope. To formulate second-order conditions, we must instead describe the admissible *directions* along which the objective may vary. These directions are encoded by the tangent cone of the feasible region at a candidate solution.

Throughout this section, let

``` math
\Omega = \{\text{ }w \in \mathbb{R}^{\mid E \mid}\text{\:\,}:\text{\:\,}Aw \leq b,\text{\:\,}0 \leq w \leq 1\text{ }\}
```

and let $`w^{\star} \in \Omega`$ satisfy the KKT conditions of Theorem 2.2 under LICQ.

**Active Constraint Structure**

Recall the active index sets at $`w^{\star}`$:

``` math
{\mathcal{I}_{A}(w^{\star}) = \{\text{ }i \in \{ 1,\ldots,m\}:(Aw^{\star} - b)_{i} = 0\text{ }\},
}{\mathcal{I}_{0}(w^{\star}) = \{\text{ }e \in E:w_{e}^{\star} = 0\text{ }\},\mathcal{I}_{1}(w^{\star}) = \{\text{ }e \in E:w_{e}^{\star} = 1\text{ }\}.
}
```

These indices determine a unique face of the polytope $`\Omega`$.

Define the active face:

``` math
F(w^{\star}) = \{\text{ }w \in \Omega:(Aw - b)_{i} = 0\text{ for }i \in \mathcal{I}_{A}(w^{\star}),\text{\:\,}w_{e} = 0\text{ for }e \in \mathcal{I}_{0}(w^{\star}),\text{\:\,}w_{e} = 1\text{ for }e \in \mathcal{I}_{1}(w^{\star})\}.
```

Thus, $`w^{\star}`$ lies in the relative interior of $`F(w^{\star})`$.

Architecturally, the active face encodes the *support regime* of the equilibrium:\
which resource constraints bind, which edges are suppressed, and which are saturated.

**Tangent Cone**

To analyse curvature under constraints, we must restrict attention to feasible directions.

**Definition 2.5 (Tangent Cone)**

The tangent cone of $`\Omega`$at $`w^{\star}`$ is defined by

``` math
T_{\Omega}(w^{\star}) = \{\text{ }v \in \mathbb{R}^{\mid E \mid}:\exists\text{ }t_{k} \downarrow 0,\text{\:\,}v_{k} \rightarrow v,\text{\:\,}w^{\star} + t_{k}v_{k} \in \Omega\}.
```

For polyhedral sets, this admits an explicit characterisation.

**Proposition 2.5 (Explicit Tangent Cone Formula)**

If LICQ holds at $`w^{\star}`$, then

``` math
T_{\Omega}(w^{\star}) = \{ v \in \mathbb{R}^{\mid E \mid}:\begin{matrix}
 & A_{i}v \leq 0 & & \text{for }i \in \mathcal{I}_{A}(w^{\star}), \\
 & v_{e} \geq 0 & & \text{for }e \in \mathcal{I}_{0}(w^{\star}), \\
 & v_{e} \leq 0 & & \text{for }e \in \mathcal{I}_{1}(w^{\star})
\end{matrix}\}.
```

Here $`A_{i}`$ denotes the $`i`$-th row of $`A`$.

**Proof (sketch).**\
A direction is feasible to first order if it does not violate any active inequality constraint. For inactive constraints strict slackness holds, so small perturbations preserve feasibility automatically. Box constraints contribute sign conditions on coordinates at the boundary. The result follows from standard polyhedral cone calculus.

**Tangent Space of the Active Face**

Within the active face, the admissible directions are those satisfying the active linear equalities exactly.

Define the linearised face space

``` math
\mathcal{L(}w^{\star}) = \left\{ v \in \mathbb{R}^{\mid E \mid}:\begin{matrix}
A_{i}v & = 0 & & \text{for }i \in \mathcal{I}_{A}(w^{\star}), \\
v_{e} & = 0 & & \text{for }e \in \mathcal{I}_{0}(w^{\star}) \cup \mathcal{I}_{1}(w^{\star})
\end{matrix} \right\}.
```

Under LICQ this is a linear subspace with dimension

``` math
\dim\mathcal{L(}w^{\star}) = \mid E \mid - \mid \mathcal{I}_{A}(w^{\star}) \mid - \mid \mathcal{I}_{0}(w^{\star}) \mid - \mid \mathcal{I}_{1}(w^{\star}) \mid .
```

This space is precisely the tangent space of the face $`F(w^{\star})`$.

**Geometric Interpretation**

The tangent cone $`T_{\Omega}(w^{\star})`$ describes all feasible first-order perturbations.\
The linear space $`\mathcal{L(}w^{\star})`$ describes directions *within* the active face.

Second-order sufficient conditions for strict local optimality must therefore be evaluated on:

``` math
v \in T_{\Omega}(w^{\star}) \smallsetminus \{ 0\},
```

and, under complementarity and strict positivity of multipliers, reduce to evaluation on

``` math
v\mathcal{\in L(}w^{\star}).
```

This marks the fundamental shift from the interior regime analysed in Paper 2.

- In Paper 2, curvature was assessed on all of $`\mathbb{R}^{\mid E \mid}`$.

- Under scarcity, curvature is assessed only on directions admissible within the active face.

Intrinsic differentiation is therefore filtered through polyhedral geometry.\
Rigidity is no longer full-space hyperbolicity; it becomes **face-restricted hyperbolicity**.

## 2.4.2 Reduced Hessian

Section 2.4.1 established that second-order analysis under linear coupling must be restricted to directions contained in the tangent cone of the feasible region and, in particular, to the linear space of the active face. We now formalise the curvature operator governing such constrained variations.

Throughout, let $`w^{\star} \in \mathcal{W}_{A}`$ satisfy the KKT conditions of Theorem 2.2 under LICQ, and let

``` math
H(w^{\star}): = \nabla^{2}\Phi_{G}(w^{\star})
```

denote the Hessian of the Network Potential Functional at $`w^{\star}`$.

**2.4.2.1 Face-Restricted Directions**

Recall the linearised active-face space

``` math
\mathcal{L(}w^{\star}) = \left\{ v \in \mathbb{R}^{\mid E \mid}:\begin{matrix}
A_{i}v & = 0 & & \text{for }i \in \mathcal{I}_{A}(w^{\star}), \\
v_{e} & = 0 & & \text{for }e \in \mathcal{I}_{0}(w^{\star}) \cup \mathcal{I}_{1}(w^{\star})
\end{matrix} \right\}.
```

Under LICQ, this is a linear subspace of $`\mathbb{R}^{\mid E \mid}`$. Variations in $`\mathcal{L(}w^{\star})`$ preserve all active constraints to first order and therefore move within the active face.

Let

``` math
Z \in \mathbb{R}^{\mid E \mid \times r}
```

be a matrix whose columns form an orthonormal basis of $`\mathcal{L(}w^{\star})`$, where

``` math
r = \dim\mathcal{L(}w^{\star}).
```

Any face-preserving perturbation can then be written as

``` math
v = Zy,y \in \mathbb{R}^{r}.
```

**Definition 2.6 (Reduced Hessian Operator)**

The reduced Hessian of $`\Phi_{G}`$at $`w^{\star}`$relative to the active face is defined by

``` math
H_{red}(w^{\star}) = Z^{\top}H(w^{\star})Z \in \mathbb{R}^{r \times r}.
```

This matrix represents the quadratic form of $`\Phi_{G}`$ restricted to variations within the active face. Indeed, for any $`v\mathcal{\in L(}w^{\star})`$with $`v = Zy`$,

``` math
v^{\top}H(w^{\star})v = y^{\top}H_{red}(w^{\star})y.
```

Thus, curvature along face-preserving directions is completely determined by the reduced Hessian.

**Second-Order Expansion on the Active Face**

Let $`v\mathcal{\in L(}w^{\star})`$ . Since $`w^{\star}`$ satisfies the KKT conditions, first-order variation vanishes along face-preserving directions:

``` math
\nabla\Phi_{G}(w^{\star})^{\top}v = 0.
```

Therefore, a second-order Taylor expansion yields

``` math
\Phi_{G}(w^{\star} + tv) = \Phi_{G}(w^{\star}) + \frac{t^{2}}{2}\text{ }v^{\top}H(w^{\star})v + o(t^{2}).
```

Consequently, strict local maximality relative to the active face requires

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v\mathcal{\in L(}w^{\star}) \smallsetminus \{ 0\}.
```

Equivalently,

``` math
H_{red}(w^{\star})\text{ is negative definite}.
```

This is the constrained analogue of full-space negative definiteness in Paper 2.

**Relation to the Interior Regime**

In the interior case analysed previously,

``` math
\mathcal{I}_{A}(w^{\star}) = \varnothing,\mathcal{I}_{0}(w^{\star}) = \varnothing,\mathcal{I}_{1}(w^{\star}) = \varnothing,
```

so that

``` math
\mathcal{L(}w^{\star}) = \mathbb{R}^{\mid E \mid},H_{red}(w^{\star}) = H(w^{\star}).
```

Thus, the reduced Hessian framework strictly generalises the interior curvature condition of Paper 2. Under scarcity, curvature is evaluated only along directions compatible with active resource coupling; directions that would violate binding constraints are excluded from second-order testing.

**Tangent-Cone Form and Complementarity**

When inequality multipliers corresponding to active constraints are strictly positive, feasible perturbations can be sign-restricted, and second-order sufficient conditions are naturally stated on the full tangent cone:

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v \in T_{\mathcal{W}_{A}}(w^{\star}) \smallsetminus \{ 0\}.
```

Under strict complementarity and LICQ, this condition reduces to negative definiteness of the reduced Hessian on $`\mathcal{L(}w^{\star})`$.

Thus:

- Tangent cone $`\text{\:\,}T_{\mathcal{W}_{A}}(w^{\star})`$ : first-order feasible directions

- Active-face linear space $`\text{\:\,}\mathcal{L(}w^{\star})`$ : face-preserving directions

- Reduced Hessian $`\text{\:\,}H_{red}(w^{\star})`$ : curvature operator governing constrained rigidity

**Architectural Interpretation**

In Paper 2, rigidity was encoded by full-space curvature: negative definiteness of $`H(w^{\star})`$ensured isolation and local stability.

Under scarcity, rigidity becomes face-restricted:

- the active face determines which edges remain adjustable,

- the reduced Hessian determines whether those adjustable directions exhibit negative curvature,

- suppressed or saturated edges do not contribute to curvature testing.

Thus, equilibrium architecture is determined jointly by:

- **which face is selected** (first-order normal geometry), and

- **whether curvature is negative along that face** (second-order reduced geometry).

We now formalise this principle in the Constrained Hyperbolicity Theorem.

## 2.4.3 Constrained Hyperbolicity

We now formalise the second-order sufficient condition governing strict local maximality under linear coupling.

Let $`w^{\star} \in \mathcal{W}_{A}`$satisfy the KKT conditions of Theorem 2.2 under LICQ, and let

``` math
H(w^{\star}) = \nabla^{2}\Phi_{G}(w^{\star})
```

denote the Hessian of the Network Potential Functional at $`w^{\star}`$.

**Definition 2.7 (Constrained Relational Rigidity)**

We say that $`w^{\star}`$satisfies constrained relational rigidity if

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v \in T_{\mathcal{W}_{A}}(w^{\star}) \smallsetminus \{ 0\}.
```

That is, the Hessian is negative definite on the admissible variation cone.

Under LICQ and strict complementarity, this condition is equivalent to

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v\mathcal{\in L(}w^{\star}) \smallsetminus \{ 0\},
```

equivalently, to negative definiteness of the reduced Hessian

``` math
H_{red}(w^{\star}).
```

**Theorem 2.4 (Constrained Hyperbolicity Theorem)**

Suppose:

- $`w^{\star} \in \mathcal{W}_{A}`$ satisfies the KKT conditions,

- LICQ holds at $`w^{\star}`$,

- $`w^{\star}`$ satisfies constrained relational rigidity.

Then:

- $`w^{\star}`$ is a strict local maximiser of $`\Phi_{G}`$ over $`\mathcal{W}_{A}`$,

- $`w^{\star}`$ is isolated within its active face $`F(w^{\star})`$,

- the active face $`F(w^{\star})`$ is locally invariant under sufficiently small perturbations of $`\Phi_{G}`$.

**Proof**

Since $`w^{\star}`$satisfies the KKT conditions, first-order feasible variations satisfy

``` math
\nabla\Phi_{G}(w^{\star})^{\top}v \leq 0\text{for all }v \in T_{\mathcal{W}_{A}}(w^{\star}).
```

For face-preserving directions $`v\mathcal{\in L(}w^{\star})`$, complementarity implies

``` math
\nabla\Phi_{G}(w^{\star})^{\top}v = 0.
```

Let $`v \in T_{\mathcal{W}_{A}}(w^{\star}) \smallsetminus \{ 0\}`$.\
A second-order Taylor expansion yields

``` math
\Phi_{G}(w^{\star} + tv) = \Phi_{G}(w^{\star}) + t\text{ }\nabla\Phi_{G}(w^{\star})^{\top}v + \frac{t^{2}}{2}\text{ }v^{\top}H(w^{\star})v + o(t^{2}).
```

The first-order term is non-positive by first-order optimality.\
The second-order term is strictly negative by constrained relational rigidity.

Therefore, for sufficiently small $`t \neq 0`$,

``` math
\Phi_{G}(w^{\star} + tv) < \Phi_{G}(w^{\star}),
```

establishing strict local maximality.

Isolation within the active face follows because negative definiteness of the reduced Hessian implies nondegenerate quadratic curvature on $`\mathcal{L(}w^{\star})`$. Standard implicit-function arguments then yield local uniqueness within the active regime.

Local invariance of the active face follows because sufficiently small perturbations of $`\Phi_{G}`$ produce equilibria whose structural marginal vectors remain in the same normal cone, preserving the active constraint set.

**Structural Interpretation**

In the interior regime analysed in Paper 2,

``` math
T_{\mathcal{W}_{A}}(w^{\star}) = \mathbb{R}^{\mid E \mid},
```

So, rigidity required full-space negative definiteness.

Under scarcity:

- some directions are excluded by binding constraints,

- curvature is tested only on admissible directions,

- rigidity becomes face-restricted hyperbolicity.

Thus:

- the normal cone determines which face is selected,

- the reduced Hessian determines whether that face is stable.

Scarcity therefore modifies both:

- first-order structure (selection), and

- second-order structure (rigidity).

# 2.5 Polyhedral Architecture and Support Classification

## 2.5.1 Face Selection

The first-order condition derived in §2.3.2,

``` math
\nabla\Phi_{G}(w^{\star}) \in N_{\mathcal{W}_{A}}(w^{\star}),
```

establishes that equilibrium is determined by alignment of the structural marginal vector with the normal cone of the feasible polytope. We now show that, under nondegeneracy, this condition selects a unique face and therefore determines the architectural support regime of the equilibrium.

**Face Structure of the Polytope**

Let

``` math
\mathcal{W}_{A} = \{ w \in \mathbb{R}^{\mid E \mid} \mid Aw \leq b,\text{\:\,}0 \leq w \leq 1\}.
```

Each face of $`\mathcal{W}_{A}`$corresponds to a collection of active constraints.

For an index set $`\mathcal{J} \subset \{ 1,\ldots,k\}`$ and boundary index sets\
$`\mathcal{I}_{0},\mathcal{I}_{1} \subset E`$, define the face

``` math
F(\mathcal{J,}\mathcal{I}_{0},\mathcal{I}_{1}) = \{ w \in \mathcal{W}_{A}:(Aw - b)_{i} = 0\text{ for }i \in \mathcal{J,}\text{\:\,}w_{e} = 0\text{ for }e \in \mathcal{I}_{0},\text{\:\,}w_{e} = 1\text{ for }e \in \mathcal{I}_{1}\}.
```

The associated normal cone is

``` math
N_{F} = \{ A^{\top}\lambda - \mu^{-} + \mu^{+}:\lambda_{i} \geq 0(i \in \mathcal{J),}\text{\:\,}\mu_{e}^{-} \geq 0(e \in \mathcal{I}_{0}),\text{\:\,}\mu_{e}^{+} \geq 0(e \in \mathcal{I}_{1})\}.
```

Multipliers are supported only on active constraints.

**Theorem 2.5 (Face Selection Theorem)**

Let $`w^{\star} \in \mathcal{W}_{A}`$ satisfy the KKT conditions under LICQ.

Assume strict complementarity:

``` math
\lambda_{i}^{\star} > 0(i \in \mathcal{I}_{A}(w^{\star})),\mu_{e}^{- \star} > 0(e \in \mathcal{I}_{0}(w^{\star})),\mu_{e}^{+ \star} > 0(e \in \mathcal{I}_{1}(w^{\star})).
```

Then:

- $`w^{\star}`$ lies in the relative interior of a unique face $`F(w^{\star})`$,

- the active index sets are locally constant under sufficiently small perturbations of $`\Phi_{G}`$,

- the equilibrium support pattern is uniquely determined by

``` math
\nabla\Phi_{G}(w^{\star}) \in riN_{F(w^{\star})}.
```

**Proof**

By the normal-cone characterisation,

``` math
\nabla\Phi_{G}(w^{\star}) = A^{\top}\lambda^{\star} - \mu^{- \star} + \mu^{+ \star},
```

with multipliers satisfying complementarity conditions.

Strict complementarity implies that all active multipliers are strictly positive. Therefore,

``` math
\nabla\Phi_{G}(w^{\star}) \in riN_{F(w^{\star})}.
```

Relative interiors of normal cones associated with distinct faces of a polyhedral set are disjoint. Consequently, the gradient cannot lie in the relative interiors of two distinct normal cones, and the active face is uniquely determined.

Local constancy of the active sets follows from continuity of $`\nabla\Phi_{G}`$ together with persistence of strict complementarity: sufficiently small perturbations cannot move the gradient across a normal-cone boundary while multipliers remain positive.

**Architectural Interpretation**

The Face Selection Theorem establishes the first structural law of constrained Network Potential optimisation:

> The equilibrium support pattern is determined by the face of the feasible polytope whose normal cone contains the structural marginal vector.

This contrasts with the interior regime analysed in Paper 2, where stationarity required

``` math
\nabla\Phi_{G}(w^{\star}) = 0
```

and no face geometry intervened.

Under scarcity, equilibrium is determined by membership of the gradient in a normal cone rather than by vanishing of the gradient.

Different faces correspond to distinct architectural regimes:

- faces with many active box constraints correspond to sparse support,

- faces with dense linear coupling correspond to compressed allocations,

- higher-dimensional faces permit redistribution among edges.

Thus, polyhedral scarcity acts as a selector of relational architecture.

## 2.5.2 Support Classification

The Face Selection Theorem establishes that equilibrium lies in the relative interior of a unique face of the feasible polytope. We now characterise the structural role of individual edges within that face.

Let $`w^{\star} \in \mathcal{W}_{A}`$ satisfy the KKT conditions under LICQ and strict complementarity. Recall the multiplier decomposition

``` math
\nabla\Phi_{G}(w^{\star}) = A^{\top}\lambda^{\star} - \mu^{- \star} + \mu^{+ \star},
```

with

``` math
\lambda^{\star} \geq 0,\mu^{- \star} \geq 0,\mu^{+ \star} \geq 0,
```

and complementarity relations

``` math
\lambda_{i}^{\star}(Aw^{\star} - b)_{i} = 0,\mu_{e}^{- \star}w_{e}^{\star} = 0,\mu_{e}^{+ \star}(1 - w_{e}^{\star}) = 0.
```

**Edge-Level Stationarity**

For each edge $`e \in E`$, the stationarity condition reads

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) = \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie} - \mu_{e}^{- \star} + \mu_{e}^{+ \star}.
```

This identity expresses marginal structural incentives as the balance between intrinsic marginal returns and shadow-price adjustments induced by active constraints.

**Theorem 2.6 (Support Classification Theorem)**

Suppose LICQ and strict complementarity hold at $`w^{\star}`$.

Then each edge $`e \in E`$ belongs uniquely to one of the following classes.

**(i) Suppressed edges**

``` math
w_{e}^{\star} = 0,\mu_{e}^{- \star} > 0,\mu_{e}^{+ \star} = 0,
```

and

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) < \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

**(ii) Saturated edges**

``` math
w_{e}^{\star} = 1,\mu_{e}^{+ \star} > 0,\mu_{e}^{- \star} = 0,
```

and

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) > \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

**(iii) Interior-on-face edges**

``` math
0 < w_{e}^{\star} < 1,\mu_{e}^{- \star} = \mu_{e}^{+ \star} = 0,
```

and

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) = \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

These three cases are mutually exclusive and collectively exhaustive.

**Proof**

Complementarity implies:

- If $`w_{e}^{\star} = 0`$then $`\mu_{e}^{- \star} \geq 0`$and $`\mu_{e}^{+ \star} = 0`$.

- If $`w_{e}^{\star} = 1`$then $`\mu_{e}^{+ \star} \geq 0`$and $`\mu_{e}^{- \star} = 0`$.

- If $`0 < w_{e}^{\star} < 1`$then

``` math
\mu_{e}^{- \star} = \mu_{e}^{+ \star} = 0.
```

Substituting these cases into the stationarity condition yields the stated inequalities and equality conditions.

Strict complementarity implies that boundary multipliers are strictly positive, ensuring uniqueness of classification.

**Structural Law of Scarcity**

For interior-on-face edges the equilibrium condition reduces to

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) = \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

Thus, an edge remains adjustable within the active face precisely when its marginal structural return equals the effective shadow price induced by active constraints.

Edges whose marginal return lies below this shadow price are suppressed, while edges whose marginal return exceeds it saturate at the upper boundary.

This yields the central sparsity principle of constrained Network Potential optimisation:

> Under linear resource coupling, ties survive precisely when their marginal structural return matches the effective shadow price induced by active constraints.

**Architectural Consequences**

Support is determined jointly by

- the structural marginal field $`\nabla\Phi_{G}(w^{\star})`$,

- the constraint geometry encoded in $`A`$,

- the shadow-price vector $`\lambda^{\star}`$.

Different coupling structures therefore induce distinct sparsity morphologies:

- Row-sparse $`A`$produces localised suppression,

- Dense rows produce global compression,

- Overlapping constraint families produce stratified support regimes.

Thus, polyhedral scarcity determines relational roles through the geometry of the feasible polytope.

## 2.5.3 Coupling Morphology and Sparsity Geometry

The Support Classification Theorem shows that equilibrium support is determined by comparison between marginal structural returns and the shadow prices generated by active constraints. We now analyse how the structure of the constraint matrix $`A`$determines the resulting sparsity geometry.

Throughout this section let

``` math
\mathcal{W}_{A} = \{\text{ }w \in \mathbb{R}^{\mid E \mid} \mid Aw \leq b,\text{\:\,}0 \leq w \leq 1\}.
```

**Coupling Geometry**

Each row of the constraint matrix $`A`$defines a linear coupling relation among edge weights. The support pattern of $`A`$therefore induces a coupling hypergraph on the edge set $`E`$:

``` math
e \sim f \Longleftrightarrow \exists i\text{ such that }A_{ie} \neq 0\text{ and }A_{if} \neq 0.
```

Edges that appear in the same constraint row compete for a shared resource allocation.

At equilibrium the stationarity condition implies

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w^{\star}) = \sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

Thus, the effective shadow price acting on edge $`e`$is determined by the weighted participation of that edge in active constraints. Sparsity therefore reflects not only boundary activation but also the combinatorial support structure of $`A`$.

**Sparsity Regimes**

Different coupling morphologies induce qualitatively distinct support patterns.

**(i) Local Node-Level Budgets**

Suppose each constraint row corresponds to a single vertex $`i`$, with

``` math
\sum_{j \in N(i)}^{}w_{ij} \leq B_{i}.
```

Competition is then localised to incident edges of vertex $`i`$. Suppression occurs within star neighbourhoods, producing node-wise pruning of incident ties.

**(ii) Global Budget Constraints**

Suppose a single dense constraint enforces

``` math
\sum_{e \in E}^{}w_{e} \leq B.
```

All edges then compete globally for a single resource pool. The shadow price is uniform across edges, and sparsity arises through global thresholding of marginal structural returns.

**(iii) Overlapping Coupling Families**

Suppose rows of $`A`$overlap partially in support. Then edges may participate in multiple binding constraints, producing cumulative shadow prices

``` math
\sum_{i \in \mathcal{I}_{A}(w^{\star})}^{}\lambda_{i}^{\star}A_{ie}.
```

Edges that participate in several active constraints experience higher effective shadow prices and are therefore more likely to be suppressed unless their marginal structural return is sufficiently large.

Overlapping constraint families therefore generate hierarchical sparsity regimes.

**Normal-Cone Geometry**

The face selected by equilibrium corresponds to a set of active inequalities. The normal cone at that face is generated by the corresponding constraint normals together with box normals:

``` math
N_{\mathcal{W}_{A}}(w^{\star}) = cone(\{ A_{i}^{\top}:i \in \mathcal{I}_{A}(w^{\star})\} \cup \{ - e_{e}:e \in \mathcal{I}_{0}(w^{\star})\} \cup \{ e_{e}:e \in \mathcal{I}_{1}(w^{\star})\}),
```

where $`e_{e}`$denotes the coordinate basis vector associated with edge $`e`$.

The equilibrium condition

``` math
\nabla\Phi_{G}(w^{\star}) \in N_{\mathcal{W}_{A}}(w^{\star})
```

therefore, determines both the active constraint set and the support configuration.

Suppressed edges correspond to directions aligned with outward box normals, while interior edges correspond to directions orthogonal to active face constraints.

Thus, sparsity patterns correspond to faces whose normal cones contain the structural marginal vector.

**Structural Law of Coupling Morphology**

The sparsity pattern induced by constrained Network Potential optimisation depends jointly on:

- the combinatorial support of the constraint matrix $`A`$,

- the distribution of shadow prices $`\lambda^{\star}`$,

- the interaction between coupling geometry and intrinsic structural marginal returns.

Scarcity therefore induces geometrically structured suppression governed by the normal-cone architecture of the feasible polytope.

In particular:

- Sparse rows of $`A`$produce localised sparsity,

- Dense rows produce global compression,

- Hierarchically nested rows produce layered architectural regimes.

**Relation to Paper 2**

In the interior regime analysed in Paper 2, no linear coupling constraint binds and

``` math
\nabla\Phi_{G}(w^{\star}) = 0.
```

All edges remain adjustable and architecture is governed solely by intrinsic curvature of the Network Potential Functional.

Under linear coupling, however, the feasible region imposes directional asymmetry even when intrinsic curvature is isotropic. Scarcity therefore acts as an external symmetry-breaking mechanism.

Thus, while Paper 2 established a law of differentiation, the present section establishes a law of geometry-induced selection.

# 2.6 Active-Face Stability and Local Uniqueness

### 

Sections 2.5.1–2.5.3 established that equilibrium architecture is determined by face selection and shadow-price-adjusted marginal conditions. We now show that, under constrained relational rigidity, the selected face is locally stable, and the equilibrium is locally unique within that regime.

Throughout, let $`w^{\star} \in \Omega`$ satisfy:

- The KKT conditions,

- LICQ,

- Strict complementarity,

- Constrained relational rigidity (Definition 2.7).

## 2.6.1 Reduced-Hessian Characterisation

Let $`w^{\star} \in \Omega`$ satisfy the KKT conditions under LICQ, and let the active index sets be fixed. Recall the linearised active-face space

``` math
\mathcal{L(}w^{\star}) = \{\text{ }v \in \mathbb{R}^{\mid E \mid}:A_{i}v = 0\text{ for }i \in \mathcal{I}_{A}(w^{\star}),\text{\:\,}v_{e} = 0\text{ for }e \in \mathcal{I}_{0}(w^{\star}) \cup \mathcal{I}_{1}(w^{\star})\}.
```

Under strict complementarity, admissible second-order perturbations lie in\
$`\mathcal{L(}w^{\star})`$ , the tangent space of the active face.

Let

``` math
H(w^{\star}) = \nabla^{2}\Phi(w^{\star})
```

denote the Hessian of the Network Potential Functional at $`w^{\star}`$.

**Definition 2.8 (Reduced-Hessian Negativity)**

We say that $`w^{\star}`$satisfies the reduced-Hessian condition if

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v\mathcal{\in L(}w^{\star}) \smallsetminus \{ 0\}.
```

Equivalently, if $`Z`$ is a matrix whose columns form an orthonormal basis of $`\mathcal{L(}w^{\star})`$ , then

``` math
H_{red}(w^{\star}) = Z^{\top}H(w^{\star})Z
```

is negative definite.

This condition is equivalent to constrained relational rigidity (Definition 2.7).

**Proposition 2.7 (Face-Restricted Second-Order Condition)**

Suppose:

- $`w^{\star}`$ satisfies the KKT conditions,

- LICQ holds at $`w^{\star}`$,

- strict complementarity holds.

Then the reduced-Hessian condition is equivalent to the strong second-order sufficient condition

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v \in T_{\Omega}(w^{\star}) \smallsetminus \{ 0\}.
```

**Proof**

Under LICQ and strict complementarity, feasible perturbations in the tangent cone decompose locally into:

- directions preserving all active constraints to first order,

- directions violating complementarity sign restrictions.

Face-preserving perturbations lie in the linear space $`\mathcal{L(}w^{\star})`$. Along such directions,

``` math
\nabla\Phi(w^{\star})^{\top}v = 0.
```

A second-order Taylor expansion gives

``` math
\Phi(w^{\star} + v) = \Phi(w^{\star}) + \frac{1}{2}v^{\top}H(w^{\star})v + o( \parallel v \parallel^{2}).
```

Negative definiteness on $`\mathcal{L(}w^{\star})`$ therefore implies strict decrease in all admissible directions.

Conversely, if the strong second-order sufficient condition holds on the tangent cone, it holds in particular on its linear subspace $`\mathcal{L(}w^{\star})`$ .

**Structural Significance**

The reduced-Hessian condition is the constrained analogue of full-space negative definiteness in the interior regime analysed in Paper 2.

In the absence of binding constraints,

``` math
\mathcal{L(}w^{\star}) = \mathbb{R}^{\mid E \mid}
```

and the reduced Hessian coincides with the full Hessian.

Under scarcity, curvature is tested only along directions compatible with the active face. Thus:

- **Face selection** is governed by first-order normal-cone geometry,

- **Rigidity** is governed by second-order curvature restricted to the face.

This reduced-Hessian characterisation provides the curvature foundation for the stability results that follow.

## 2.6.2 Active-Face Stability Theorem

We now show that, under reduced-Hessian negativity and strict complementarity, the active face selected by equilibrium is locally stable under small perturbations of structural parameters.

Let $`\Phi( \cdot ;\theta)`$ denote a $`C^{2}`$- smooth family of Network Potential functionals depending on a parameter vector\
$`\theta \in \Theta \subset \mathbb{R}^{p}`$.

For fixed $`\theta_{0}`$, suppose that

``` math
w^{\star} = w^{\star}(\theta_{0}) \in \Omega
```

satisfies:

- the KKT conditions,

- LICQ,

- strict complementarity,

- the reduced-Hessian condition of §2.6.1.

Let $`F(w^{\star})`$ denote the active face determined by the index sets

``` math
\mathcal{I}_{A}(w^{\star}),\mathcal{I}_{0}(w^{\star}),\mathcal{I}_{1}(w^{\star}).
```

**Theorem 2.8 (Active-Face Stability)**

Under the above assumptions, there exist $`\varepsilon > 0`$ and a neighbourhood\
$`U \subset \Theta`$of $`\theta_{0}`$ such that for all $`\theta \in U`$ with

``` math
\parallel \theta - \theta_{0} \parallel < \varepsilon,
```

there exists a unique equilibrium $`w^{\star}(\theta)`$ satisfying

``` math
{\mathcal{I}_{A}(w^{\star}(\theta)) = \mathcal{I}_{A}(w^{\star}),
}{\mathcal{I}_{0}(w^{\star}(\theta)) = \mathcal{I}_{0}(w^{\star}),
}{\mathcal{I}_{1}(w^{\star}(\theta)) = \mathcal{I}_{1}(w^{\star}).
}
```

In particular,

``` math
w^{\star}(\theta) \in riF(w^{\star})
```

for all such $`\theta`$.

**Proof**

The KKT conditions for $`\Phi( \cdot ;\theta)`$may be written as

``` math
\nabla\Phi(w;\theta) - A^{\top}\lambda + \mu - \nu = 0,
```

together with

``` math
{Aw - b \leq 0,0 \leq w \leq 1,
}{\lambda \geq 0,\mu \geq 0,\nu \geq 0,
}
```

and complementarity relations

``` math
{\lambda_{i}(Aw - b)_{i} = 0,
}{\mu_{e}w_{e} = 0,
}{\nu_{e}(1 - w_{e}) = 0.
}
```

**Reduction to the Active Face**

Under strict complementarity,

``` math
{\lambda_{i}^{\star} > 0i \in \mathcal{I}_{A}(w^{\star}),
}{\mu_{e}^{\star} > 0e \in \mathcal{I}_{0}(w^{\star}),
}{\nu_{e}^{\star} > 0e \in \mathcal{I}_{1}(w^{\star}),
}
```

So, the complementarity conditions reduce locally to equality constraints:

``` math
{(Aw - b)_{i} = 0i \in \mathcal{I}_{A}(w^{\star}),
}{w_{e} = 0e \in \mathcal{I}_{0}(w^{\star}),
}{w_{e} = 1e \in \mathcal{I}_{1}(w^{\star}).
}
```

Thus, equilibrium must lie in the affine manifold defining the active face.

**Reduced KKT System**

On the active face, the KKT conditions reduce to the smooth system

``` math
\nabla\Phi(w;\theta) = A^{\top}\lambda - \mu + \nu,
```

with multipliers restricted to the active sets.

The linearisation of this system with respect to $`w`$along the active face is

``` math
v \mapsto H(w^{\star})v
```

restricted to

``` math
v\mathcal{\in L(}w^{\star}).
```

Reduced-Hessian negativity implies that

``` math
H_{red}(w^{\star}) = Z^{\top}H(w^{\star})Z
```

is nonsingular.

Therefore, the Jacobian of the reduced KKT system is invertible.

Application of the Implicit Function Theorem

By the implicit function theorem, there exists a unique $`C^{1}`$solution branch

``` math
w^{\star}(\theta)
```

for $`\theta`$ sufficiently close to $`\theta_{0}`$.

Continuity of the multipliers and strict positivity at $`\theta_{0}`$imply that multiplier signs persist under sufficiently small perturbations.

Therefore, no new constraints become active and no active constraints deactivate.

Hence

``` math
w^{\star}(\theta) \in riF(w^{\star}).
```

This proves local invariance of the active face.

**Geometric Interpretation**

The equilibrium lies in the relative interior of a face whose normal cone contains the structural marginal vector.

Under reduced-Hessian negativity:

- the objective is locally concave along the face,

- the KKT system is nondegenerate,

- multiplier signs persist.

Thus, the selected face is locally invariant under parameter perturbations.

In contrast with the interior regime of Paper 2, where hyperbolicity ensures isolation in full space, stability here is restricted to the selected face.

Scarcity geometry therefore induces regime-level stability: architectural structure is preserved so long as the gradient remains within the same normal cone.

## 2.6.3 Structural Lock-In under Scarcity

Sections 2.5 and 2.6.2 established that equilibrium architecture is determined by face selection and that, under reduced-Hessian negativity and strict complementarity, the selected face persists under small perturbations. We now formalise the resulting lock-in principle.

Let

``` math
w^{\star}(\theta_{0}) \in \Omega
```

satisfy the hypotheses of Theorem 2.8, and let

``` math
F(w^{\star})
```

denote the corresponding active face.

**Theorem 2.9 (Structural Lock-In under Scarcity)**

Under the assumptions of Theorem 2.8, there exists a neighbourhood\
$`U \subset \Theta`$of $`\theta_{0}`$such that for all $`\theta \in U`$,

- The equilibrium $`w^{\star}(\theta)`$lies in the same active face $`F(w^{\star})`$,

- The support classification of edges remains unchanged,

- Variations in $`w^{\star}(\theta)`$occur smoothly within the affine manifold of that face.

In particular, the sparsity pattern and saturation structure are locally invariant.

**Proof**

By Theorem 2.8, the active index sets remain locally constant:

``` math
{\mathcal{I}_{A}(w^{\star}(\theta)) = \mathcal{I}_{A}(w^{\star}),
}{\mathcal{I}_{0}(w^{\star}(\theta)) = \mathcal{I}_{0}(w^{\star}),
}{\mathcal{I}_{1}(w^{\star}(\theta)) = \mathcal{I}_{1}(w^{\star}).
}
```

Therefore, the active face

``` math
F(w^{\star}) = \left\{ w \in \Omega:(Aw - b)_{i} = 0\text{\:\,}i \in \mathcal{I}_{A}(w^{\star}),\text{\:\,}w_{e} = 0\text{\:\,}e \in \mathcal{I}_{0}(w^{\star}),\text{\:\,}w_{e} = 1\text{\:\,}e \in \mathcal{I}_{1}(w^{\star}) \right\}
```

remains unchanged.

Within this face, the reduced KKT system is smooth and nondegenerate by reduced-Hessian negativity. The implicit function theorem therefore yields a smooth equilibrium branch

``` math
w^{\star}(\theta)
```

confined to $`F(w^{\star})`$.

Since boundary status of each edge is encoded in the active index sets, the classification into suppressed, saturated, and interior-on-face edges remains unchanged.

Therefore, architectural structure persists under sufficiently small perturbations.

**Structural Consequence**

Structural lock-in under scarcity differs fundamentally from hyperbolic lock-in in the interior regime of Paper 2.

In the interior regime:

- rigidity arises from full-space curvature,

- equilibria are isolated in $`\mathbb{R}^{\mid E \mid}`$.

Under scarcity:

- rigidity is face-restricted,

- equilibria may move smoothly within the selected face,

- escape from the face requires violation of multiplier positivity.

Transitions to a different sparsity regime occur only when the structural marginal vector crosses the boundary of the normal cone associated with $`F(w^{\star})`$ . At such points strict complementarity fails and face persistence is no longer guaranteed.

Thus, architectural change under scarcity occurs only through face transitions, not through infinitesimal deformation within a fixed regime.

## 2.6.4 Synthesis

Sections 2.3–2.6 establish a complete local theory of constrained equilibria for the Network Potential Functional under linear resource coupling. The results show that equilibrium architecture is determined jointly by first-order normal geometry, second-order curvature restricted to the active face, and stability of the resulting regime under perturbation.

The structural logic of constrained Network Potential optimisation may be summarised as follows.

**First-Order Geometry — Face Selection**

Equilibrium weights $`w^{\star}`$satisfy the variational inequality

``` math
\nabla\Phi(w^{\star}) \in N_{\Omega}(w^{\star}),
```

so that the structural marginal vector lies in the normal cone of the feasible polytope at $`w^{\star}`$.

Under LICQ and strict complementarity, this condition uniquely determines an active face $`F(w^{\star}) \subset \Omega`$. The selected face specifies the equilibrium support architecture, including suppressed edges, saturated edges, and interior-on-face edges.

Thus, equilibrium is determined not by vanishing of the gradient, as in the interior regime of Paper 2, but by alignment between the structural marginal field and the polyhedral normal geometry.

**Second-Order Geometry — Face-Restricted Rigidity**

Local maximality requires negative curvature along admissible directions:

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v\mathcal{\in L(}w^{\star}) \smallsetminus \{ 0\}.
```

Equivalently, the reduced Hessian

``` math
H_{red}(w^{\star})
```

is negative definite.

This condition ensures strict local maximality within the selected face and provides the constrained analogue of full-space hyperbolicity in Paper 2.

Under scarcity, curvature is evaluated only along directions compatible with active constraints. Directions violating binding constraints do not contribute to stability.

Thus, rigidity becomes face-restricted hyperbolicity rather than full-space hyperbolicity.

**Stability — Structural Lock-In**

Under reduced-Hessian negativity and strict complementarity, the KKT system is locally nondegenerate. The implicit function theorem therefore yields a unique smooth equilibrium branch

``` math
w^{\star}(\theta)
```

confined to the active face.

Consequently:

- the active constraint sets remain locally constant,

- the support classification remains unchanged,

- equilibrium weights vary smoothly within the selected face.

Architectural structure is therefore locally invariant under small perturbations.

**Regime Transitions**

Architectural change occurs only when the structural marginal vector exits the relative interior of the normal cone associated with $`F(w^{\star})`$.

At such points:

- strict complementarity fails,

- the active face changes,

- the reduced-Hessian characterisation ceases to guarantee persistence.

Transitions between sparsity regimes therefore occur through face-switching events corresponding to crossings of normal-cone boundaries.

**Structural Principle of Scarcity-Constrained Optimisation**

The results of this section establish the fundamental structural principle of constrained Network Potential optimisation:

> Equilibrium architecture is determined by polyhedral normal geometry, stabilised by face-restricted curvature, and persists under perturbations until the structural marginal vector crosses a normal-cone boundary.

This principle provides the geometric foundation for the regime-transition analysis developed in the following section.

# 2.7 Budget Perturbations and Face Transitions

Sections 2.5–2.6 established that equilibrium architecture is determined by face selection and that, under LICQ, strict complementarity, and reduced-Hessian negativity, the equilibrium is locally unique and varies smoothly within a fixed active face. We now analyse how equilibrium structure changes when the resource parameters vary sufficiently to alter the active constraint structure.

We consider a parametric family of feasible sets obtained by varying the right-hand side of the linear resource constraints. Let

``` math
\Omega(\beta) = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq \beta,\text{\:\,}0 \leq w \leq 1 \right\},
```

where

``` math
\beta \in \mathbb{R}^{m}
```

represents resource levels (budgets, capacities, or allocation bounds), and the constraint matrix $`A`$is fixed.

For each admissible parameter value $`\beta`$, consider the constrained optimisation problem

``` math
\underset{w \in \Omega(\beta)}{\max}\Phi(w).
```

Let $`w^{\star}(\beta)`$ denote an equilibrium satisfying the KKT conditions.

Under the regularity assumptions of §2.6, equilibrium varies smoothly with $`\beta`$within regions where the active constraint sets remain constant. Outside such regions, the active face of the feasible polytope may change, producing transitions between distinct architectural regimes.

The purpose of this section is to characterise these regime transitions.

**Structural Regimes**

Let

``` math
F(\beta) = F(w^{\star}(\beta))
```

denote the active face determined by the index sets

``` math
{I}_{A}(\beta),{I}_{0}(\beta),{I}_{1}(\beta).
```

Each face $`F`$has an associated normal cone

``` math
N_{F} = cone\left( \{ A_{i}^{\top}:i \in {I}_{A}\} \cup \{ - e_{e}:e \in {I}_{0}\} \cup \{ e_{e}:e \in {I}_{1}\} \right).
```

By the Face Selection Theorem (Theorem 2.5),

``` math
\nabla\Phi(w^{\star}(\beta)) \in N_{F}.
```

Under strict complementarity,

``` math
\nabla\Phi(w^{\star}(\beta)) \in riN_{F}.
```

Thus, each equilibrium regime corresponds to a region of parameter space for which the structural marginal vector lies in the relative interior of a fixed normal cone.

Within such a region:

- the active constraint sets remain constant,

- the support classification is fixed,

- the equilibrium varies smoothly with $`\beta`$.

Transitions between regimes occur precisely when

``` math
\nabla\Phi(w^{\star}(\beta)) \in \partial N_{F},
```

that is, when the structural marginal vector reaches the boundary of a normal cone.

At such parameter values strict complementarity fails and the active face may change.

**Relation to Stability Theory**

Section 2.6 established that equilibrium is locally confined to a fixed face under small perturbations of parameters. The present section describes how this confinement breaks down when perturbations become sufficiently large to move the gradient across boundaries of normal cones.

The structural theory therefore decomposes into two complementary components:

**Local theory (§2.6)**

- fixed active face

- smooth equilibrium branch

- structural lock-in

**Global theory (§2.7)**

- regime transitions

- face switching

- polyhedral regime decomposition

## 2.7.1 Parameterised Constraint System

We consider a parametric family of feasible sets obtained by varying the right-hand side of the linear resource constraints. Let

``` math
\Omega(\beta) = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq \beta,\text{\:\,}0 \leq w \leq 1 \right\},
```

where

``` math
\beta \in \mathbb{R}^{k}
```

represents resource levels and the constraint matrix

``` math
A \in \mathbb{R}^{k \times \mid E \mid}
```

is fixed.

For each admissible parameter value $`\beta`$, consider the constrained optimisation problem

``` math
\underset{w \in \Omega(\beta)}{\max}\Phi(w).
```

Let $`w^{\star}(\beta)`$ denote a solution satisfying the Karush–Kuhn–Tucker conditions.

**Parametric KKT System**

For each $`\beta`$, first-order optimality requires existence of multipliers

``` math
\lambda \in \mathbb{R}^{k},\mu \in \mathbb{R}^{\mid E \mid},\nu \in \mathbb{R}^{\mid E \mid}
```

such that

``` math
\nabla\Phi(w) = A^{\top}\lambda - \mu + \nu,
```

subject to the feasibility conditions

``` math
Aw - \beta \leq 0,0 \leq w \leq 1,
```

the multiplier conditions

``` math
\lambda \geq 0,\mu \geq 0,\nu \geq 0,
```

and complementarity relations

``` math
{\lambda_{i}(Aw - \beta)_{i} = 0,
}{\mu_{e}w_{e} = 0,
}{\nu_{e}(1 - w_{e}) = 0.
}
```

**Reference Equilibrium**

Let $`\beta_{0}`$be a reference parameter value and suppose that the corresponding equilibrium

``` math
w^{\star}(\beta_{0})
```

satisfies:

- LICQ,

- strict complementarity,

- reduced-Hessian negativity (Definition 2.8).

Let the associated active index sets be

``` math
{I}_{A},{I}_{0},{I}_{1}.
```

**Reduced Equality System**

Under strict complementarity, the active constraints hold as equalities in a neighbourhood of $`\beta_{0}`$:

``` math
{\left( Aw - \beta)_{i} = 0\text{for }i \in {I}_{A} \right.,
}{w_{e} = 0\text{for }e \in {I}_{0},
}{w_{e} = 1\text{for }e \in {I}_{1}.
}
```

The KKT system therefore reduces locally to the smooth equality system

``` math
\nabla\Phi(w) = A^{\top}\lambda - \mu + \nu,
```

together with the above active equalities and multiplier restrictions

``` math
{\lambda_{i} > 0(i \in {I}_{A}),
}{\mu_{e} > 0(e \in {I}_{0}),
}{\nu_{e} > 0(e \in {I}_{1}).
}
```

This defines a smooth nonlinear system in the endogenous variables

``` math
\left( w,\lambda,\mu,\nu \right)
```

and parameter $`\beta`$.

**Local Solvability**

Under LICQ and reduced-Hessian negativity, the Jacobian of the reduced KKT system with respect to the endogenous variables is nonsingular at

``` math
(w^{\star}(\beta_{0}),\lambda^{\star}(\beta_{0}),\mu^{\star}(\beta_{0}),\nu^{\star}(\beta_{0})).
```

Consequently, by the implicit function theorem, there exists a neighbourhood $`U`$of $`\beta_{0}`$ and a unique continuously differentiable mapping

``` math
\beta \mapsto w^{\star}(\beta)
```

defined for $`\beta \in U`$, provided the active index sets remain unchanged.

Thus, equilibrium varies smoothly with the budget parameters within a fixed active regime.

## 2.7.2 Piecewise-Smooth Equilibrium Branches

We now analyse the dependence of equilibria on the parameter $`\beta`$within a fixed active regime.

Let $`\beta_{0} \in \mathbb{R}^{k}`$and suppose that the equilibrium

``` math
w^{\star}(\beta_{0})
```

satisfies:

- the KKT conditions,

- LICQ,

- strict complementarity,

- reduced-Hessian negativity (Definition 2.8).

Let the active index sets at $`\beta_{0}`$ be

``` math
{I}_{A} = {I}_{A}(w^{\star}(\beta_{0})),{I}_{0} = {I}_{0}(w^{\star}(\beta_{0})),{I}_{1} = {I}_{1}(w^{\star}(\beta_{0})).
```

**Reduced KKT System on a Fixed Face**

Within this active regime, the KKT conditions reduce locally to the smooth equality system

``` math
\nabla\Phi(w) = A^{\top}\lambda - \mu + \nu,
```

together with the active equalities

``` math
{\left( Aw - \beta)_{i} = 0\text{for }i \in {I}_{A} \right.,
}{w_{e} = 0\text{for }e \in {I}_{0},
}{w_{e} = 1\text{for }e \in {I}_{1},
}
```

and multiplier positivity conditions

``` math
\lambda_{i} > 0(i \in {I}_{A}),\mu_{e} > 0(e \in {I}_{0}),\nu_{e} > 0(e \in {I}_{1}).
```

This defines a smooth nonlinear system

``` math
F(w,\lambda,\mu,\nu,\beta) = 0
```

in the endogenous variables

``` math
\left( w,\lambda,\mu,\nu \right)
```

and parameter $`\beta`$.

**Local Smooth Dependence**

Under LICQ and reduced-Hessian negativity, the Jacobian of the reduced KKT system with respect to the endogenous variables is nonsingular at $`\beta_{0}`$.

Therefore, by the implicit function theorem, there exists a neighbourhood

``` math
U \subset \mathbb{R}^{k}
```

of $`\beta_{0}`$ and a unique $`C^{1}`$mapping

``` math
\beta \mapsto (w^{\star}(\beta),\lambda^{\star}(\beta),\mu^{\star}(\beta),\nu^{\star}(\beta))
```

such that:

- the KKT system is satisfied for all $`\beta \in U`$,

- the active index sets remain unchanged,

- strict complementarity persists.

**Theorem 2.11 (Piecewise-Smooth Equilibrium Branches)**

Let $`w^{\star}(\beta_{0})`$ satisfy LICQ, strict complementarity, and reduced-Hessian negativity. Then there exists a neighbourhood $`U`$of $`\beta_{0}`$such that:

1.  The equilibrium $`w^{\star}(\beta)`$ is uniquely defined for all $`\beta \in U`$,

2.  The mapping

``` math
\beta \mapsto w^{\star}(\beta)
```

is $`C^{1}`$on $`U`$,

3.  The active index sets

``` math
{I}_{A},{I}_{0},{I}_{1}
```

remain constant on $`U`$.

**Piecewise-Smooth Structure**

As $`\beta`$varies globally, the parameter space decomposes into regions on which the active index sets remain constant. On each such region:

- the equilibrium mapping is smooth,

- the active face is fixed,

- the support classification is unchanged.

Non-smooth behaviour can occur only at parameter values where strict complementarity fails and the equilibrium reaches the boundary of a normal cone. At such points the active index sets may change, producing a transition to a different equilibrium branch.

Thus, the equilibrium mapping

``` math
\beta \mapsto w^{\star}(\beta)
```

is piecewise $`C^{1}`$, with regime boundaries determined by normal-cone degeneracy.

## 

## 

## 

## 2.7.3 Normal-Cone Boundary Conditions

We now characterise the precise condition under which an active regime ceases to persist.

Let

``` math
\beta_{0} \in \mathbb{R}^{k}
```

and suppose that $`w^{\star}(\beta_{0})`$ satisfies the hypotheses of Theorem 2.11. Let

``` math
F: = F(w^{\star}(\beta_{0}))
```

denote the active face determined by the index sets

``` math
\left( {I}_{A},{I}_{0},{I}_{1} \right).
```

**Normal-Cone Characterisation**

From §2.3, first-order optimality may be written as

``` math
\nabla\Phi(w^{\star}(\beta)) \in N_{\Omega(\beta)}(w^{\star}(\beta)).
```

Within a fixed active face $`F`$, this condition is equivalent to

``` math
\nabla\Phi(w^{\star}(\beta)) \in riN_{F},
```

where $`{ri}N_{F}`$denotes the relative interior of the normal cone of $`F`$.

Thus, persistence of the active regime is equivalent to the condition that the structural marginal vector remains in the relative interior of the same normal cone.

**Degeneracy and Multiplier Vanishing**

Strict complementarity at $`\beta_{0}`$ implies

``` math
{\lambda_{i}^{\star}(\beta_{0}) > 0(i \in {I}_{A}),
}{\mu_{e}^{\star}(\beta_{0}) > 0(e \in {I}_{0}),
}{\nu_{e}^{\star}(\beta_{0}) > 0(e \in {I}_{1}).
}
```

Equivalently,

``` math
\nabla\Phi(w^{\star}(\beta_{0})) \in riN_{F}.
```

A necessary condition for a change of active set is therefore that for some parameter value $`\beta_{c}`$,

``` math
\nabla\Phi(w^{\star}(\beta_{c})) \in \partial N_{F},
```

that is, the structural marginal vector reaches the boundary of the normal cone.

At such a point at least one multiplier vanishes:

``` math
\lambda_{i}^{\star}(\beta_{c}) = 0,\text{or}\mu_{e}^{\star}(\beta_{c}) = 0,\text{or}\nu_{e}^{\star}(\beta_{c}) = 0.
```

Such multiplier degeneracy corresponds to loss of strict complementarity and signals the possibility of a transition to a neighbouring active face.

**Theorem 2.12 (Normal-Cone Boundary Criterion)**

Let $`\beta_{0}`$ satisfy the assumptions of Theorem 2.11 and let $`F`$denote the associated active face.

If

``` math
\nabla\Phi(w^{\star}(\beta_{0})) \in riN_{F},
```

then the active index sets remain locally constant in a neighbourhood of $`\beta_{0}`$.

Conversely, if there exists a parameter value $`\beta_{c}`$ such that

``` math
\nabla\Phi(w^{\star}(\beta_{c})) \in \partial N_{F},
```

then $`\beta_{c}`$ is a candidate transition point at which the active face may change.

**Proof**

Local constancy of the active sets follows from strict complementarity together with Theorem 2.11. While the structural marginal vector remains in $`{ri}N_{F}`$, all associated multipliers remain strictly positive and the implicit-function construction of §2.7.2 persists.

If

``` math
\nabla\Phi(w^{\star}(\beta_{c})) \in \partial N_{F},
```

then at least one multiplier vanishes. Arbitrarily small perturbations of $`\beta`$may therefore cause the corresponding constraint to become inactive or to be replaced by an adjacent active constraint.

Since relative interiors of normal cones corresponding to distinct faces are disjoint in a polyhedral set, the equilibrium cannot remain in the face $`F`$once the structural marginal vector exits $`{ri}N_{F}`$.

Thus active-set change can occur only at normal-cone boundary points.

## 2.7.4 Regime Boundaries and Phase Transitions

We now synthesise the local analysis of §§2.7.1–2.7.3 into a global description of the parameter space.

Let

``` math
\Omega(\beta) = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq \beta,\text{\:\,}0 \leq w \leq 1 \right\},
```

where

``` math
\beta \in \mathbb{R}^{k},
```

and suppose that for each admissible parameter value $`\beta`$, equilibrium $`w^{\star}(\beta)`$ satisfies the KKT conditions.

**Regime Regions**

For each admissible active index triple

``` math
({I}_{A},{I}_{0},{I}_{1}),
```

define the associated **regime region**

``` math
\mathcal{R(}{I}_{A},{I}_{0},{I}_{1}) = \left\{ \beta \in \mathbb{R}^{k}:\begin{matrix}
 & \text{there exists }w^{\star}(\beta)\text{ satisfying the KKT system,} \\
 & \text{with active sets }({I}_{A},{I}_{0},{I}_{1}), \\
 & \text{and satisfying LICQ, strict complementarity,} \\
 & \text{and reduced-Hessian negativity}
\end{matrix} \right\}.
```

By Theorem 2.11, each regime region is locally open, and the equilibrium mapping

``` math
\beta \mapsto w^{\star}(\beta)
```

is $`C^{1}`$ on that region.

Within a regime region:

- The active face is fixed,

- The support classification is constant,

- The equilibrium varies smoothly with $`\beta`$.

**Regime Boundaries**

Let $`F`$ denote the face associated with a given active index triple.

From §2.7.3, regime persistence is equivalent to

``` math
\nabla\Phi(w^{\star}(\beta)) \in riN_{F}.
```

Define the associated **regime boundary**

``` math
\partial\mathcal{R}_{F} = \left\{ \beta:\nabla\Phi(w^{\star}(\beta)) \in \partial N_{F} \right\}.
```

At such parameter values:

- At least one multiplier vanishes,

- Strict complementarity fails,

- The reduced KKT Jacobian becomes singular in a boundary direction.

Thus, regime boundaries correspond precisely to **normal-cone degeneracy**.

**Face Transitions**

When $`\beta`$ crosses a regime boundary $`\partial\mathcal{R}_{F}`$ , one or more of the following events must occur:

- A previously inactive linear constraint becomes active,

- An active linear constraint becomes inactive,

- A suppressed edge becomes interior,

- An interior edge becomes saturated,

- A saturated edge becomes interior.

Each such event changes the active index sets and therefore selects a new face of the feasible polytope.

Since relative interiors of distinct normal cones are disjoint, the equilibrium cannot remain in the same regime once

``` math
\nabla\Phi(w^{\star}(\beta)) \notin riN_{F}.
```

The solution must therefore reorganise in a neighbouring face.

**Theorem 2.15 (Polyhedral Regime Decomposition)**

Assume LICQ and reduced-Hessian negativity hold within active regimes.

Then the parameter space admits a locally finite partition

``` math
\mathbb{R}^{k} = \bigcup_{\alpha}^{}\mathcal{R}_{\alpha},
```

where:

- Each region $`\mathcal{R}_{\alpha}`$corresponds to a unique active face,

- On each region the equilibrium mapping is $`C^{1}`$,

- Active index sets remain constant on each region,

- Transitions between regimes occur only across normal-cone boundaries,

- Boundary sets are lower-dimensional subsets of parameter space.

**Geometric Interpretation**

The parameter space is partitioned into regions corresponding to distinct active faces of the feasible polytope.

Within each region:

- The equilibrium lies in a fixed face,

- The normal cone containing the structural marginal vector is constant,

- The reduced-Hessian operator governs local curvature.

Regime transitions occur precisely when the structural marginal vector crosses a boundary between adjacent normal cones.

Thus, the dependence of equilibrium architecture on resource parameters is **piecewise-smooth and polyhedrally organised**.

# 2.8 Recovery of the Interior Regime and Structural Generality

This section shows that the constrained variational framework developed in Paper 2 strictly generalises the interior optimisation regime analysed in Paper 2. The interior case appears as the degenerate regime in which no linear resource constraint binds and the feasible region locally coincide with the hypercube interior.

We also show that the polyhedral formulation accommodates a wide class of resource-coupling structures within a single geometric framework.

### **2.8.1 Collapse of the KKT System in the Absence of Coupling**

Consider the feasible set

``` math
\Omega(\beta) = \left\{ w \in \mathbb{R}^{\mid E \mid}:Aw \leq \beta,\text{\:\,}0 \leq w \leq 1 \right\}.
```

Suppose that at an equilibrium $`w^{\star}`$,

``` math
\left( Aw^{\star} - \beta)_{i} < 0\text{for all }i \right.,
```

so that no linear resource constraint is active. Then

``` math
{I}_{A}(w^{\star}) = \varnothing,\lambda^{\star} = 0.
```

The KKT stationarity condition therefore reduces to

``` math
\nabla\Phi(w^{\star}) = - \mu^{\star} + \nu^{\star}.
```

If, in addition, all box constraints are inactive,

``` math
0 < w_{e}^{\star} < 1\text{for all }e \in E,
```

then

``` math
\mu^{\star} = 0,\nu^{\star} = 0,
```

and hence

``` math
\nabla\Phi(w^{\star}) = 0.
```

Thus, the constrained first-order system reduces exactly to the interior stationarity condition analysed in Paper 2.

### **2.8.2 Tangent-Cone Reduction**

If no constraint binds at $`w^{\star}`$, then

``` math
T_{\Omega}(w^{\star}) = \mathbb{R}^{\mid E \mid}.
```

The reduced-Hessian condition therefore reduces to full-space negative definiteness:

``` math
v^{\top}D^{2}\Phi(w^{\star})v < 0\text{for all }v \neq 0.
```

This coincides with the strict local maximality condition used in Paper 2 to establish structural differentiation and relational rigidity.

Thus full-space hyperbolicity appears as the unconstrained limit of constrained relational rigidity.

### **2.8.3 Normal-Cone Collapse**

In the interior regime the normal cone satisfies

``` math
N_{\Omega}(w^{\star}) = \{ 0\}.
```

Consequently the constrained optimality condition

``` math
\nabla\Phi(w^{\star}) \in N_{\Omega}(w^{\star})
```

reduces to

``` math
\nabla\Phi(w^{\star}) = 0.
```

Thus, the variational inequality formulation collapses to smooth critical-point analysis.

Equivalently, the active face is full-dimensional and scarcity geometry is inactive. The interior regime of Paper 2 therefore corresponds to the degenerate case in which the feasible polytope contributes no directional asymmetry.

### **2.8.4 Canonical Resource Structures**

The polyhedral formulation accommodates a broad class of resource-coupling structures within a unified geometric framework.

**Node Budgets**

Vertex-specific constraints of the form

``` math
\sum_{j \in N(i)}^{}w_{ij} \leq B_{i},i \in V,
```

correspond to choosing $`A`$as the node–edge incidence matrix.

In this case scarcity geometry induces competition among edges incident to the same vertex, producing locally structured suppression.

**Global Budget**

A single global constraint

``` math
\sum_{e \in E}^{}w_{e} \leq B
```

produces uniform resource coupling across all edges.

All ties compete for a shared resource, and equilibrium architecture reflects global compression governed by a single shadow price.

**Overlapping Group Budgets**

For subsets $`G_{\mathcal{l}} \subseteq E`$,

``` math
\sum_{e \in G_{\mathcal{l}}}^{}w_{e} \leq B_{\mathcal{l}},\mathcal{l} = 1,\ldots,k,
```

rows of $`A`$ encode group membership.

Overlapping constraint families produce multi-scale coupling structures and stratified sparsity regimes determined by the interaction of multiple shadow prices.

All such cases are handled uniformly by the normal-cone and reduced-Hessian framework developed in this paper.

### **2.8.5 Structural Generality**

The constrained Network Potential optimisation problem therefore provides a unified geometric characterisation of relational allocation.

For admissible equilibria:

- **First-order optimality** is expressed as normal-cone inclusion

``` math
\nabla\Phi(w^{\star}) \in N_{\Omega}(w^{\star}).
```

- **Second-order stability** is determined by reduced-Hessian negativity on the tangent cone.

- **Architectural regimes** correspond to faces of the feasible polytope.

- **Regime transitions** occur when the structural marginal vector crosses a normal-cone boundary.

When no linear constraint binds, the framework reduces exactly to the interior theory of Paper 2. When constraints bind, scarcity geometry selects the active face and determines the support structure.

Thus, Paper 2 does not replace the interior analysis; rather, it embeds it within a strictly more general polyhedral variational framework.

# 2.9 Conclusion

This paper has extended the Network Potential Functional from interior optimisation on the hypercube to constrained optimisation over general polyhedral feasible sets. The resulting framework embeds relational optimisation within a nonlinear programming and variational-inequality formulation in which equilibrium architecture emerges from the interaction between intrinsic marginal structure and polyhedral scarcity geometry.

The principal analytical results may be summarised as follows.

First, equilibrium is characterised by the normal-cone inclusion condition

``` math
\nabla\Phi(w^{\star}) \in N_{\Omega}(w^{\star}),
```

which replaces the interior stationarity condition of Paper 2. First-order optimality is therefore determined jointly by structural marginal returns and the geometry of the feasible polytope.

Second, local stability is governed by reduced-Hessian negativity on the tangent space:

``` math
v^{\top}D^{2}\Phi(w^{\star})v < 0\text{for all }v \in T_{\Omega}(w^{\star}) \smallsetminus \{ 0\}.
```

This extends the full-space curvature condition of the interior regime and yields a notion of **constrained relational rigidity**, in which stability is determined by curvature restricted to admissible directions within the active face.

Third, scarcity induces a face-dependent structural architecture. Each active face of the feasible polytope defines a structural regime within which equilibrium is locally unique and depends smoothly on resource parameters. Support classification — suppressed, interior-on-face, or saturated — is determined by shadow-price-adjusted marginal returns.

Fourth, regime transitions occur precisely when the structural marginal field reaches the boundary of a normal cone. Parameter space therefore admits a locally finite decomposition into regions of smooth equilibrium behaviour separated by lower-dimensional degeneracy sets. Architectural change under scarcity arises through discrete face transitions rather than infinitesimal deformation.

The interior theory developed in Paper 2 is recovered as the degenerate case in which no linear resource constraint binds and the normal cone collapses to the origin. The constrained formulation therefore strictly generalises the original Network Potential framework while preserving its variational structure.

Taken together, Papers I and II establish a dual structural principle governing relational optimisation:

- **Intrinsic curvature differentiates ties.**

- **Polyhedral scarcity selects ties.**

Equilibrium architecture emerges from the interaction between these two mechanisms.

This completes the static theory of constrained Network Potential optimisation. Subsequent papers will develop dynamical formulations, endogenous topology, and operator-theoretic extensions building on the variational and geometric foundations established here.

# Bibliography

Boyd, S. and Vandenberghe, L. (2004) *Convex Optimization*. Cambridge: Cambridge University Press.

Mack, I. (2026) Network Potential and Relational Optimisation: Balancing Cohesion, Brokerage, and Redundancy in Weighted Networks. Dissertation.

Monderer, D. and Shapley, L.S. (1996) ‘Potential games’, *Games and Economic Behavior*, 14(1), pp. 124–143.

Nash, J. (1951) ‘Non-cooperative games’, *Annals of Mathematics*, 54(2), pp. 286–295.

Rockafellar, R.T. (1970) *Convex Analysis*. Princeton: Princeton University Press.
