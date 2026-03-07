## Balancing Cohesion, Brokerage, and

## Redundancy in Weighted Networks

#### **Author:** Ian Mack

#### **Date:** Feb. 2026

## Abstract

This thesis develops a functional framework for optimisation on weighted networks. Let $`G`$ be a finite undirected graph with fixed topology and variable edge weights. A scalar functional, termed the **Network Potential Functional**, is defined on the compact space of admissible tie-strength configurations and provides a quantitative measure of structural quality.

The functional is constructed as a combination of stability, mobility, and redundancy components defined on the weighted network. These components capture local cohesive structure, nonredundant connectivity, and weighted closure respectively, and together determine a global potential defined over the weight space.

The Network Potential Functional is shown to be bounded and continuous on the admissible domain and therefore to admit maximising configurations. Explicit gradient expressions are derived, yielding necessary conditions for interior optima and characterising optimal configurations as balance points between stability, mobility, and redundancy contributions.

Curvature properties of the functional are analysed. Under triangle-free conditions the functional is concave and therefore admits globally optimal configurations. In general networks closure interactions produce nonconcavity, leading to locally optimal configurations interpreted as structurally stable equilibria.

Reachability properties are established linking node potential to structural exposure. Node potential is shown to bound brokerage-weighted reach, and a two-hop reach theorem establishes monotonic growth of expected nonredundant second-neighbour exposure with enriched mobility.

The Network Potential Functional defines an energy-like quantity on weighted graphs and provides a mathematical framework for optimisation and equilibrium analysis on weighted network structures.

# Content

[1. Introduction [10](#introduction)](#introduction)

[1.1 Motivation [11](#motivation)](#motivation)

[1.2 Contribution [11](#contribution)](#contribution)

[1.2.1 A Functional Formulation of Relational Structure [11](#a-functional-formulation-of-relational-structure)](#a-functional-formulation-of-relational-structure)

[1.2.2 Definition of the Network Potential Functional [12](#definition-of-the-network-potential-functional)](#definition-of-the-network-potential-functional)

[1.2.3 Structural Optimality Conditions [12](#structural-optimality-conditions)](#structural-optimality-conditions)

[1.2.4 Curvature Regimes [12](#curvature-regimes)](#curvature-regimes)

[1.2.5 Reachability Guarantees [12](#reachability-guarantees)](#reachability-guarantees)

[1.3 Structure of the Thesis [13](#structure-of-the-thesis)](#structure-of-the-thesis)

[1.4 Conceptual Position [13](#conceptual-position)](#conceptual-position)

[2. Weighted Network Model [14](#weighted-network-model)](#weighted-network-model)

[2.1 Networks and Tie Strength [14](#networks-and-tie-strength)](#networks-and-tie-strength)

[2.2 Neighbourhood Structure [14](#neighbourhood-structure)](#neighbourhood-structure)

[2.3 Weight Transformations [15](#weight-transformations)](#weight-transformations)

[2.4 Neighbourhood Overlap [16](#neighbourhood-overlap)](#neighbourhood-overlap)

[2.5 Brokerage Proxy [16](#brokerage-proxy)](#brokerage-proxy)

[2.6 Stability Functional [17](#stability-functional)](#stability-functional)

[2.7 Mobility Functional [18](#mobility-functional)](#mobility-functional)

[2.8 Closure Redundancy [19](#closure-redundancy)](#closure-redundancy)

[2.9 Structural Interpretation [20](#structural-interpretation)](#structural-interpretation)

[2.10 Structural Decomposition [20](#structural-decomposition)](#structural-decomposition)

[2.11 Discussion [21](#discussion)](#discussion)

[3. Network Potential as a Functional on Weighted Graphs [22](#network-potential-as-a-functional-on-weighted-graphs)](#network-potential-as-a-functional-on-weighted-graphs)

[3.1 Network Potential [22](#network-potential)](#network-potential)

[3.2 Node-Level Network Potential [22](#node-level-network-potential)](#node-level-network-potential)

[3.3 Global Network Potential [23](#global-network-potential)](#global-network-potential)

[3.4 Well-Definedness and Bounds [23](#well-definedness-and-bounds)](#well-definedness-and-bounds)

[3.5 Continuity [25](#continuity)](#continuity)

[3.6 Existence of Optimal Configurations [25](#existence-of-optimal-configurations)](#existence-of-optimal-configurations)

[3.7 Gradient Structure [26](#gradient-structure)](#gradient-structure)

[3.8 Node-Level Gradient [27](#node-level-gradient)](#node-level-gradient)

[3.9 Structural Interpretation [27](#structural-interpretation-1)](#structural-interpretation-1)

[3.10 Balanced Tie-Mix Condition [28](#balanced-tie-mix-condition)](#balanced-tie-mix-condition)

[3.11 Discussion [28](#discussion-1)](#discussion-1)

[4. Curvature Regimes and Optimisation Implications [30](#curvature-regimes-and-optimisation-implications)](#curvature-regimes-and-optimisation-implications)

[4.1 Overview [30](#overview)](#overview)

[4.2 Concave Regime [30](#concave-regime)](#concave-regime)

[4.3 General Regime [33](#general-regime)](#general-regime)

[4.4 Optimisation Consequences [34](#optimisation-consequences)](#optimisation-consequences)

[4.5 Coordinate Ascent Interpretation [34](#coordinate-ascent-interpretation)](#coordinate-ascent-interpretation)

[4.6 Balanced Tie-Mix Equilibria [35](#balanced-tie-mix-equilibria)](#balanced-tie-mix-equilibria)

[4.7 Structural Stability [36](#structural-stability)](#structural-stability)

[4.8 Interpretation [36](#interpretation)](#interpretation)

[4.9 Discussion [36](#discussion-2)](#discussion-2)

[5. Reachability Guarantees [38](#reachability-guarantees-1)](#reachability-guarantees-1)

[5.1 Overview [38](#overview-1)](#overview-1)

[5.2 Reachable Structural Diversity [38](#reachable-structural-diversity)](#reachable-structural-diversity)

[5.3 Basic Properties [39](#basic-properties)](#basic-properties)

[5.4 Network Potential Bounds Reachability [39](#network-potential-bounds-reachability)](#network-potential-bounds-reachability)

[5.5 Invertible Bound [40](#invertible-bound)](#invertible-bound)

[5.6 Structural Interpretation [41](#structural-interpretation-2)](#structural-interpretation-2)

[5.7 Two-Hop Structural Reach [41](#two-hop-structural-reach)](#two-hop-structural-reach)

[5.8 Bounds on Two-Hop Reach [41](#bounds-on-two-hop-reach)](#bounds-on-two-hop-reach)

[5.9 Enriched Mobility Functional [42](#enriched-mobility-functional)](#enriched-mobility-functional)

[5.10 Two-Hop Reach Theorem [42](#two-hop-reach-theorem)](#two-hop-reach-theorem)

[5.11 Two-Hop Reach Corollary [43](#two-hop-reach-corollary)](#two-hop-reach-corollary)

[5.12 Relationship to Network Potential [44](#relationship-to-network-potential)](#relationship-to-network-potential)

[5.13 Discussion [44](#discussion-3)](#discussion-3)

[6. Relational Optimisation and Equilibrium Structure [45](#relational-optimisation-and-equilibrium-structure)](#relational-optimisation-and-equilibrium-structure)

[6.1 Overview [45](#overview-2)](#overview-2)

[6.2 Relational Optimisation Problem [45](#relational-optimisation-problem)](#relational-optimisation-problem)

[6.3 Local Optimality [46](#local-optimality)](#local-optimality)

[6.4 Tie-Level Optimality Conditions [46](#tie-level-optimality-conditions)](#tie-level-optimality-conditions)

[6.5 Tie-Level Equilibrium Interpretation [46](#tie-level-equilibrium-interpretation)](#tie-level-equilibrium-interpretation)

[6.6 Pairwise Stability [47](#pairwise-stability)](#pairwise-stability)

[6.7 Structural Equilibria [48](#structural-equilibria)](#structural-equilibria)

[6.8 Structural Properties of Equilibria [48](#structural-properties-of-equilibria)](#structural-properties-of-equilibria)

[6.9 Equilibrium Interpretation [49](#equilibrium-interpretation)](#equilibrium-interpretation)

[6.10 Network Potential as an Energy Functional [50](#network-potential-as-an-energy-functional)](#network-potential-as-an-energy-functional)

[6.11 Interpretation [50](#interpretation-1)](#interpretation-1)

[6.12 Discussion [51](#discussion-4)](#discussion-4)

[7. Conclusion and Future Directions [52](#conclusion-and-future-directions)](#conclusion-and-future-directions)

[7.1 Overview [52](#overview-3)](#overview-3)

[7.2 Summary of Results [52](#summary-of-results)](#summary-of-results)

[7.3 Theoretical Significance [54](#theoretical-significance)](#theoretical-significance)

[7.4 Limitations [55](#limitations)](#limitations)

[7.5 Extensions to Dynamic Networks [55](#extensions-to-dynamic-networks)](#extensions-to-dynamic-networks)

[7.6 Algorithmic Optimisation [56](#algorithmic-optimisation)](#algorithmic-optimisation)

[7.7 Alternative Structural Measures [56](#alternative-structural-measures)](#alternative-structural-measures)

[7.8 Higher-Order Reachability [56](#higher-order-reachability)](#higher-order-reachability)

[7.9 Game-Theoretic Extensions [57](#game-theoretic-extensions)](#game-theoretic-extensions)

[7.10 Final Remarks [57](#final-remarks)](#final-remarks)

[References [59](#references)](#references)

[8. Limitations and Future Mathematical Development [60](#limitations-and-future-mathematical-development)](#limitations-and-future-mathematical-development)

[8.1 Overview [60](#overview-4)](#overview-4)

[8.2 Scope of the Base Formulation [60](#scope-of-the-base-formulation)](#scope-of-the-base-formulation)

[8.2.1 Fixed Topology [60](#fixed-topology)](#fixed-topology)

[8.2.2 Continuous Tie Strength Representation [61](#continuous-tie-strength-representation)](#continuous-tie-strength-representation)

[8.2.3 Structural Regularisation within the Functional [62](#structural-regularisation-within-the-functional)](#structural-regularisation-within-the-functional)

[8.3 Structural Limitations [63](#structural-limitations)](#structural-limitations)

[8.3.1 Fixed Topology Assumption [63](#fixed-topology-assumption)](#fixed-topology-assumption)

[8.3.2 Absence of Explicit Allocation Constraints [64](#absence-of-explicit-allocation-constraints)](#absence-of-explicit-allocation-constraints)

[8.3.3 Motif-Based Redundancy Model [64](#motif-based-redundancy-model)](#motif-based-redundancy-model)

[8.3.4 Static Optimisation Framework [65](#static-optimisation-framework)](#static-optimisation-framework)

[8.4 Constrained Optimisation Extensions [65](#constrained-optimisation-extensions)](#constrained-optimisation-extensions)

[8.5 Dynamic and Topological Extensions [66](#dynamic-and-topological-extensions)](#dynamic-and-topological-extensions)

[8.6 Dynamical Formulations [67](#dynamical-formulations)](#dynamical-formulations)

[8.7 Optimisation Landscape and Structural Regimes [68](#optimisation-landscape-and-structural-regimes)](#optimisation-landscape-and-structural-regimes)

[8.8 Relationship to Existing Network Measures [68](#relationship-to-existing-network-measures)](#relationship-to-existing-network-measures)

[8.9 Concluding Remarks [68](#concluding-remarks)](#concluding-remarks)

# Chapter 1

# Introduction

Networks provide the structural context within which information, resources, and opportunities propagate. The structure of a node’s connections influences both its cohesive capacity and access to nonredundant information (Burt, 1992). Strong ties support trust and coordination, while weak ties often provide bridges between otherwise disconnected regions of a network (Granovetter, 1973). At the same time, excessive closure among neighbours produces redundancy and reduces (Coleman, 1988).

This thesis develops a formal theory of relational optimisation in weighted networks. The central problem is to characterise how tie strengths should be distributed across a fixed network topology in order to balance cohesion, brokerage, and redundancy. Rather than treating network structure as static, tie strength is modelled as a continuous variable, allowing relational structure to be analysed as an optimisation problem.

The primary contribution of this work is the introduction of the Network Potential Functional, a scalar functional defined on weighted graphs. The Network Potential Functional measures structural quality by combining three components:

- a cohesion component reflecting strong-tie capacity,

- a brokerage component reflecting nonredundant weak-tie reach,

- a redundancy component penalising excessive closure.

Relational optimisation is formulated as the maximisation of network potential over the space of admissible tie strengths. This formulation allows network structure to be analysed using tools from optimisation theory and functional analysis.

The resulting framework establishes several foundational properties:

- Network potential is well-defined on compact weight domains.

- Optimal tie configurations exist.

- Local optima satisfy explicit balance conditions.

- Network potential bounds reachable structural diversity.

- Two-hop structural reach increases with brokerage-weighted weak ties.

These results provide a mathematical formalisation of the balance between cohesive and bridging ties.

## 

## 1.1 Motivation

A central observation in network theory is that networks must simultaneously support stability and exploration (Newman, 2010). Highly cohesive structures provide reliability and coordination but tend to concentrate interactions within redundant clusters. Conversely, networks dominated by weak bridging ties provide access to diverse opportunities but lack structural support.

The tension between cohesion and reach suggests that network structure should be understood as a balance rather than as an extreme. However, most existing work describes this balance qualitatively or empirically rather than through a formal optimisation framework.

The approach taken here is to treat relational structure as an optimisation problem defined over weighted networks (Jackson, 2008). Tie strength is interpreted as a continuous resource allocated across edges. The optimal distribution of tie strengths emerges from the interaction between cohesion benefits, brokerage benefits, and redundancy costs.

This formulation allows relational structure to be studied using precise mathematical tools.

## 

## 1.2 Contribution

This thesis makes the following contributions:

### 

### 1.2.1 A Functional Formulation of Relational Structure

Relational structure is represented as a weighted network with fixed topology, and network quality is expressed through a scalar functional defined over the weight space.

This formulation allows relational structure to be analysed as a continuous optimisation problem.

### 

### 1.2.2 Definition of the Network Potential Functional

The Network Potential Functional is introduced as a measure of structural quality that balances cohesion, brokerage, and redundancy.

The functional is defined on a compact domain and admits optimal configurations.

### 

### 1.2.3 Structural Optimality Conditions

Explicit gradient expressions are derived for the Network Potential Functional, yielding balance conditions governing optimal tie strengths.

These conditions formalise the trade-off between strong and weak ties.

### 

### 1.2.4 Curvature Regimes

Conditions are identified under which the Network Potential Functional is concave and therefore globally optimisable. The role of closure redundancy in producing nonconcavity is characterised.

### 

### 1.2.5 Reachability Guarantees

Node potential is shown to bound brokerage-weighted reach. In particular, higher node potential implies greater reachable structural diversity.

A two-hop reach theorem establishes monotonic growth of nonredundant second-neighbour exposure with enriched mobility.

## 

## 1.3 Structure of the Thesis

The remainder of this thesis is organised as follows:

- Chapter 2 introduces the weighted network model and structural functionals.

- Chapter 3 defines the Network Potential Functional and establishes its fundamental properties.

- Chapter 4 characterises curvature regimes and optimisation implications.

- Chapter 5 develops reachability guarantees and two-hop reach theorems.

- Chapter 6 discusses implications for relational optimisation and network structure.

- Chapter 7 concludes.

## 

## 1.4 Conceptual Position

This thesis develops a theory of relational optimisation in the spirit of formal network and game-theoretic analysis. The objective is to define a mathematical object — the Network Potential Functional — and to characterise its structural properties.

The theory does not assume a particular application domain. Instead, it treats relational structure abstractly as a weighted network and studies how tie strengths influence structural opportunity.

The Network Potential Functional provides a mathematical representation of the balance between cohesion and brokerage that arises naturally in networked systems.

# Chapter 2

# Weighted Network Model

## 

## 2.1 Networks and Tie Strength

Let

``` math
\mathcal{G = (}V,E,w)
```

be a finite weighted undirected network (Diestel, 2017) where:

- $`V\`$is a finite set of nodes with $`\mid V \mid = n < \infty`$,

- $`E \subseteq \left\{ \left\{ i,j \right\} \subseteq V:i \neq j \right\}`$ is a set of undirected edges,

- $`w:E \rightarrow \lbrack 0,1\rbrack`$ assigns a weight $`w_{ij}`$ to each edge.

The quantity $`w_{ij}`$ represents tie strength between nodes $`i`$ and $`j`$. The topology $`E`$ is assumed fixed throughout the base theory, while tie strengths vary continuously.

The weight space is therefore the hypercube

``` math
\mathcal{W} = \lbrack 0,1\rbrack^{\mid E \mid}.
```

A weight assignment is denoted

``` math
w = (w_{ij})_{\{ i,j\} \in E}.
```

The weighted network model treats relational structure as a continuous configuration within $`\mathcal{W}`$.

## 2.2 Neighbourhood Structure

For each node $`i \in V`$, define the neighbourhood:

``` math
\Gamma(i) = \{ j \in V:\{ i,j\} \in E\}.
```

Define the degree:

``` math
d_{i} = \mid \Gamma(i) \mid .
```

The maximum degree is denoted:

``` math
\Delta = \underset{i \in V}{\max}d_{i}.
```

Since $`V`$is finite,

``` math
\Delta < \infty.
```

Neighbourhood structure is determined entirely by topology $`E`$ and remains fixed under weight variation.

## 

## 2.3 Weight Transformations

Fix exponent

``` math
p \geq 1.
```

Define the strong-tie transformation:

``` math
S_{ij} = w_{ij}^{p}.
```

Define the weak-tie transformation:

``` math
W_{ij} = (1 - w_{ij})^{p}.
```

These satisfy:

``` math
0 \leq S_{ij} \leq 1,0 \leq W_{ij} \leq 1.
```

The exponent $`p`$controls the sensitivity of the transformations to extreme weights.

For $`p = 1`$, transformations are linear.

For $`p > 1`$, extreme values are amplified:

- Strong ties contribute disproportionately to cohesion.

- Weak ties contribute disproportionately to brokerage.

These transformations allow strong and weak ties to be treated symmetrically within a single formal framework.

## 

## 2.4 Neighbourhood Overlap

For edges $`\{ i,j\} \in E`$, define neighbourhood overlap:

``` math
O_{ij} = \frac{\mid \Gamma(i) \cap \Gamma(j) \mid}{\mid \Gamma(i) \cup \Gamma(j) \mid}.
```

This is a Jaccard similarity measure between neighbourhood sets (Jaccard, 1901).

The overlap satisfies:

``` math
0 \leq O_{ij} \leq 1.
```

Interpretation:

- $`O_{ij} = 1`$ corresponds to identical neighbourhoods.

- $`O_{ij} = 0`$ corresponds to disjoint neighbourhoods.

## 

## 2.5 Brokerage Proxy

Define brokerage:

``` math
B_{ij} = 1 - O_{ij}.
```

This quantity measures structural nonredundancy.

The brokerage proxy satisfies:

``` math
0 \leq B_{ij} \leq 1.
```

High brokerage corresponds to edges connecting structurally distinct neighbourhoods.

Low brokerage corresponds to edges embedded within closed clusters.

Since brokerage depends only on topology:

``` math
B_{ij}
```

is constant under weight variation.

### 

### 2.6 Stability Functional

Define the stability functional:

``` math
A_{i}(w) = \sum_{j \in \Gamma(i)}^{}S_{ij}.
```

Explicitly:

``` math
A_{i}(w) = \sum_{j \in \Gamma(i)}^{}w_{ij}^{p}.
```

The stability functional measures cohesive capacity around node $`i`$.

##### Proposition 2.1 (Bounds on Stability)

For all nodes $`i`$:

``` math
0 \leq A_{i}(w) \leq d_{i}.
```

Proof

Each term satisfies:

``` math
0 \leq w_{ij}^{p} \leq 1.
```

Summing over $`d_{i}`$terms yield the bounds. ∎

## 2.7 Mobility Functional

Define the mobility functional:

``` math
M_{i}(w) = \sum_{j \in \Gamma(i)}^{}W_{ij}B_{ij}.
```

Explicitly:

``` math
M_{i}(w) = \sum_{j \in \Gamma(i)}^{}{(1 -}w_{ij})^{p}B_{ij}.
```

This functional measures brokerage-weighted weak-tie mass.

##### Proposition 2.2 (Bounds on Mobility)

For all nodes $`i`$:

``` math
0 \leq M_{i}(w) \leq d_{i}.
```

Proof

Since:

``` math
0 \leq (1 - w_{ij})^{p} \leq 1
```

and

``` math
0 \leq B_{ij} \leq 1,
```

each summand lies in $`\left\lbrack 0,1 \right\rbrack`$. Summing over $`d_{i}`$terms give the result. ∎

## 

## 2.8 Closure Redundancy

Define adjacency indicator:

``` math
1_{E}(j,k) = \left\{ \begin{matrix}
1 & \text{if }\{ j,k\} \in E \\
0 & \text{otherwise}.
\end{matrix} \right.\ 
```

Define redundancy:

``` math
R_{i}(w) = \sum_{\{ j,k\} \subseteq \Gamma(i)}^{}S_{ij}S_{ik}1_{E}(j,k).
```

Explicitly:

``` math
R_{i}(w) = \sum_{\{ j,k\} \subseteq \Gamma(i)}^{}w_{ij}^{p}w_{ik}^{p}1_{E}(j,k).
```

This functional measures weighted triadic closure around node $`i`$.

##### Proposition 2.3 (Bounds on Redundancy)

For all nodes $`i`$:

``` math
0 \leq R_{i}(w) \leq \binom{d_{i}}{2}.
```

Proof

Each summand satisfies:

``` math
0 \leq w_{ij}^{p}w_{ik}^{p} \leq 1.
```

The number of unordered neighbour pairs equals:

``` math
\binom{d_{i}}{2}.
```

Summation yields the result. ∎

### 

### 

### 2.9 Structural Interpretation

The weighted network model decomposes relational structure into three components:

**Cohesion**

Measured by:

``` math
A_{i}(w).
```

This represents the aggregate strength of ties around node $`i`$.

**Brokerage**

Measured by:

``` math
M_{i}(w).
```

This represents access to structurally distinct regions of the network through weak ties.

**Redundancy**

Measured by:

``` math
R_{i}(w).
```

This represents structural closure among neighbours.

## 

## 2.10 Structural Decomposition

For each node $`i`$, the triple

``` math
\left( A_{i}(w),M_{i}(w),R_{i}(w) \right)
```

provides a structural decomposition of the node's relational configuration.

The quantities satisfy degree-controlled bounds:

``` math
{A_{i}(w) \leq d_{i}
}{M_{i}(w) \leq d_{i}
}{R_{i}(w) \leq \binom{d_{i}}{2}.
}
```

These bounds depend only on topology.

## 

## 2.11 Discussion

The weighted network model represents relational structure as a continuous configuration within a compact domain.

This formulation permits:

- differential analysis,

- optimisation analysis,

- equilibrium characterisation.

The structural functionals $`A_{i}(w)`$, $`M_{i}(w)`$, and $`R_{i}(w)`$ provide a decomposition of relational structure into cohesion, brokerage, and redundancy components.

The next chapter introduces the Network Potential Functional and studies its properties as a scalar functional defined on the weight space.

# Chapter 3

# Network Potential as a Functional on Weighted Graphs

## 

## 3.1 Network Potential

Chapter 2 introduced the weighted network model and the structural functionals

``` math
A_{i}(w),M_{i}(w),R_{i}(w),
```

which measure cohesion, brokerage-weighted reach, and closure redundancy, respectively.

This chapter introduces the central object of the theory: the **Network Potential Function**, which combines these structural quantities into a scalar measure of relational structure.

The Network Potential Function is defined at the node level and extended to the network as a whole.

## 

## 3.2 Node-Level Network Potential

### 

##### Definition 3.1 (Network Potential Function)

Let

``` math
\theta_{A},\theta_{M},\theta_{R} \geq 0
```

be fixed parameters.

For node $`i \in V`$, define the **Network Potential Function**

``` math
NPF_{i}(w) = \theta_{A}log(1 + A_{i}(w)) + \theta_{M}log(1 + M_{i}(w)) - \theta_{R}log(1 + R_{i}(w)).
```

The Network Potential Function measures the structural quality of node $`i`$'s relational configuration.

The three terms represent:

- cohesion through strong ties,

- nonredundant reach through brokerage-weighted weak ties,

- redundancy penalties through closure.

The logarithmic form ensures diminishing marginal returns in each component.

## 

## 3.3 Global Network Potential

### 

##### Definition 3.2 (Network Potential Functional)

Define the Network Potential Functional

``` math
\Phi(w) = \sum_{i \in V}^{}{NP}F_{i}(w).
```

For fixed $`V`$and $`E`$, the functional

``` math
\Phi:\lbrack 0,1\rbrack^{\mid E \mid}\mathbb{\rightarrow R}
```

maps tie-strength configurations to scalar potential values.

The functional $`\Phi(w)`$measures global structural quality.

Relational optimisation is formulated as:

``` math
\underset{w \in \lbrack 0,1\rbrack^{\mid E \mid}}{max}\Phi(w).
```

### 3.4 Well-Definedness and Bounds

The following theorem establishes that network potential is well-defined and degree-controlled.

**Theorem 3.1 (Bounds on Node Potential)**

For all nodes $`i`$:

``` math
- \theta_{R}log\left( 1+\binom{d_{i}}{2} \right) \leq NPF_{i}(w) \leq (\theta_{A} + \theta_{M})log(1 + d_{i}).
```

Proof

From Chapter 2:

``` math
{0 \leq A_{i} \leq d_{i}
}{0 \leq M_{i} \leq d_{i}
}{0 \leq R_{i} \leq \binom{d_{i}}{2}.
}
```

Since:

``` math
{\theta_{A}log(1 + A_{i}) \geq 0
}{\theta_{M}log(1 + M_{i}) \geq 0
}
```

and

``` math
- \theta_{R}log(1 + R_{i}) \geq - \theta_{R}log\left( 1+\binom{d_{i}}{2} \right),
```

the lower bound follows.

For the upper bound:

``` math
{log(1 + A_{i}) \leq log(1 + d_{i}),
}{log(1 + M_{i}) \leq log(1 + d_{i}),
}
```

and

``` math
- \theta_{R}log(1 + R_{i}) \leq 0.
```

Substitution yields the result. ∎

##### Corollary 3.1

For all weight assignments $`w`$, the functional $`\Phi(w)`$is finite.

### 

### 3.5 Continuity

##### 

##### Theorem 3.2 (Continuity)

The functional

``` math
\Phi(w)
```

is continuous on $`\left\lbrack 0,1\rbrack^{\mid E \mid} \right.\`$.

Proof

Each structural functional is continuous:

``` math
{A_{i}(w) = \sum w_{ij}^{p}
}{M_{i}(w) = \sum(1 - w_{ij})^{p}B_{ij}
}{R_{i}(w) = \sum w_{ij}^{p}w_{ik}^{p}1_{E}(j,k).
}
```

The logarithm

``` math
log(1 + x)
```

is continuous for $`x \geq 0`$.

Composition preserves continuity.

Finite summation preserves continuity. ∎

### 

### 3.6 Existence of Optimal Configurations

### 

##### Theorem 3.3 (Existence of Maximizers)

There exists

``` math
w^{\star} \in \lbrack 0,1\rbrack^{\mid E \mid}
```

such that

``` math
\Phi(w^{\star}) = \underset{w \in \lbrack 0,1\rbrack^{\mid E \mid}}{max}\Phi(w).
```

Proof

The domain $`\left\lbrack 0,1\rbrack^{\mid E \mid} \right.\`$is compact.

The functional $`\Phi`$is continuous.

Apply the Weierstrass extreme value theorem (Rudin, 1976). ∎

### 

### 3.7 Gradient Structure

Optimisation of network potential depends on how potential changes with tie strength.

For edge $`\{ i,j\} \in E`$:

``` math
\frac{\partial\Phi}{\partial w_{ij}} = \frac{\partial NPF_{i}}{\partial w_{ij}} + \frac{\partial NPF_{j}}{\partial w_{ij}}.
```

##### Lemma 3.1 (Derivatives of Structural Functionals)

For $`p > 1`$:

``` math
{\frac{\partial A_{i}}{\partial w_{ij}} = pw_{ij}^{p - 1}
}{\frac{\partial M_{i}}{\partial w_{ij}} = - p(1 - w_{ij})^{p - 1}B_{ij}
}{\frac{\partial R_{i}}{\partial w_{ij}} = pw_{ij}^{p - 1}\sum_{k \in \Gamma(i) \smallsetminus \{ j\}}^{}w_{ik}^{p}1_{E}(j,k).
}
```

Proof

Differentiate sums and products directly. ∎

### 

### 3.8 Node-Level Gradient

### 

##### Theorem 3.4 (Node Potential Gradient)

For $`p > 1`$:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}} = pw_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{i}}-\frac{\theta_{R}}{1 + R_{i}}C_{ij} \right) - p(1 - w_{ij})^{p - 1}B_{ij}\frac{\theta_{M}}{1 + M_{i}},
```

where

``` math
C_{ij} = \sum_{k \in \Gamma(i) \smallsetminus \{ j\}}^{}w_{ik}^{p}1_{E}(j,k).
```

Proof

Apply the chain rule to Definition 3.1 and substitute Lemma 3.1. ∎

### 

### 3.9 Structural Interpretation

The gradient expression decomposes into three competing forces:

**Cohesion Incentive**

``` math
\frac{\theta_{A}}{1 + A_{i}}
```

encourages stronger ties.

**Redundancy Pressure**

``` math
\frac{\theta_{R}}{1 + R_{i}}C_{ij}
```

penalises ties that increase closure redundancy.

**Brokerage Incentive**

``` math
B_{ij}\frac{\theta_{M}}{1 + M_{i}}
```

encourages weak ties connecting distinct neighbourhoods.

### 

### 3.10 Balanced Tie-Mix Condition

Interior optima must satisfy:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}} = 0.
```

Thus:

``` math
w_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{i}}-\frac{\theta_{R}}{1 + R_{i}}C_{ij} \right) = (1 - w_{ij})^{p - 1}B_{ij}\frac{\theta_{M}}{1 + M_{i}}.
```

This equation characterises optimal tie strengths.

The left-hand side represents cohesion adjusted for redundancy.

The right-hand side represents brokerage-weighted mobility.

Optimal relational structure occurs when these forces balance.

### 

### 3.11 Discussion

The Network Potential Functional provides a scalar representation of relational structure over weighted networks.

The functional is:

- well-defined,

- continuous,

- bounded,

- optimisable.

The gradient reveals that optimal tie configurations arise from a balance between cohesion, brokerage, and redundancy.

This establishes network potential as a natural objective for relational optimisation.

The next chapter characterises curvature regimes and the implications for optimisation.

# Chapter 4

# Curvature Regimes and Optimisation Implications

## 

## 4.1 Overview

Chapter 3 introduced the Network Potential Functional

``` math
\Phi(w) = \sum_{i \in V}^{}{NP}F_{i}(w),
```

defined on the compact domain

``` math
\mathcal{W} = \lbrack 0,1\rbrack^{\mid E \mid}.
```

This chapter characterises the curvature properties of the functional and the implications for relational optimisation.

Understanding curvature is essential for determining:

- existence and uniqueness of optima,

- optimisation methods,

- stability of tie configurations.

The Network Potential Functional exhibits two distinct regimes:

1.  A concave regime corresponding to sparse closure.

2.  A general regime in which closure redundancy produces nonconcavity.

## 4.2 Concave Regime

The concave regime corresponds to networks with minimal closure.

##### Definition 4.1 (Triangle-Free Neighbourhoods)

A network satisfies the **triangle-free neighbourhood condition** if for every node $`i`$,

``` math
\{ j,k\} \notin E\text{for all }j,k \in \Gamma(i),\text{ }j \neq k.
```

Equivalently:

``` math
R_{i}(w) \equiv 0\text{for all }w.
```

##### Theorem 4.1 (Concavity Under Sparse Closure)

Suppose:

- $`\left. \ p \in (0,1 \right\rbrack`$,

- triangle-free neighbourhoods hold.

Then:

``` math
\Phi(w)
```

is concave on $`\left\lbrack 0,1\rbrack^{\mid E \mid} \right.\`$.

Proof

Under triangle-free neighbourhoods:

``` math
R_{i}(w) = 0,
```

so

``` math
NPF_{i}(w) = \theta_{A}log(1 + A_{i}(w)) + \theta_{M}log(1 + M_{i}(w)).
```

For $`p \leq 1`$:

``` math
w^{p}
```

is concave.

Thus:

``` math
A_{i}(w) = \sum w_{ij}^{p}
```

is concave.

Similarly:

``` math
\left( 1-w_{ij})^{p} \right.\ 
```

is concave.

Therefore:

``` math
M_{i}(w)
```

is concave.

Since $`\log(1 + x)`$is concave increasing:

``` math
NPF_{i}(w)
```

is concave.

Summation preserves concavity. ∎

##### Corollary 4.1 (Global Optimality)

Under Theorem 4.1 conditions, any local maximum of

``` math
\Phi(w)
```

is a global maximum.

##### Corollary 4.2 (Uniqueness Under Strict Concavity)

If:

- triangle-free neighbourhoods hold,

- $`p < 1`$,

- $`\theta_{A},\theta_{M} > 0`$,

then

``` math
\Phi(w)
```

is strictly concave and admits a unique maximiser.

### 

### 4.3 General Regime

In most networks, closure redundancy is present.

##### Proposition 4.1 (Nonconcavity Under Closure)

Suppose:

``` math
\exists i,\text{ }j,k \in \Gamma(i)\text{such that }\{ j,k\} \in E.
```

Then the functional $`\Phi(w)`$is generally nonconcave.

Proof

For such nodes:

``` math
R_{i}(w) \supseteq w_{ij}^{p}w_{ik}^{p}.
```

This term is convex for $`p \geq 1`$.

The term:

``` math
- \theta_{R}log(1 + R_{i}(w))
```

is not concave in general.

Therefore:

``` math
NPF_{i}(w)
```

and thus $`\Phi(w)`$are not concave. ∎

### 

### 4.4 Optimisation Consequences

Because the functional is continuous on a compact domain:

##### Theorem 4.2 (Existence of Local Optima)

The functional

``` math
\Phi(w)
```

admits at least one global maximum and possibly multiple local maxima.

Proof

Global maxima exist by Theorem 3.3.

Nonconcavity permits multiple local maxima. ∎

### 

### 4.5 Coordinate Ascent Interpretation

Optimisation can be interpreted through local tie adjustments.

Consider a weight update:

``` math
w_{ij}^{\left( t+1 \right)} = w_{ij}^{(t)} + \eta g_{ij},
```

where:

``` math
g_{ij} = \frac{\partial\Phi}{\partial w_{ij}}.
```

Theorem 4.3 (Local Ascent Property)

If

``` math
\frac{\partial\Phi}{\partial w_{ij}} > 0,
```

then sufficiently small increases in $`w_{ij}`$increase $`\Phi(w)`$ (Boyd and Vandenberghe, 2004).

Proof

Immediate from differentiability. ∎

### 

### 4.6 Balanced Tie-Mix Equilibria

Interior optima satisfy:

``` math
\frac{\partial\Phi}{\partial w_{ij}} = 0.
```

From Chapter 3:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}} = pw_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{i}}-\frac{\theta_{R}}{1 + R_{i}}C_{ij} \right) - p(1 - w_{ij})^{p - 1}B_{ij}\frac{\theta_{M}}{1 + M_{i}}.
```

Thus, interior equilibria satisfy:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}} + \frac{\partial NPF_{j}}{\partial w_{ij}} = 0.
```

##### Theorem 4.4 (Tie-Balance Characterisation)

At an interior optimum, tie strengths satisfy:

``` math
\text{cohesion gain} - \text{redundancy cost} = \text{brokerage gain}.
```

Explicitly:

``` math
w_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{i}}-\frac{\theta_{R}}{1 + R_{i}}C_{ij} \right) + w_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{j}}-\frac{\theta_{R}}{1 + R_{j}}C_{ji} \right) = (1 - w_{ij})^{p - 1}\left( B_{ij}\frac{\theta_{M}}{1 + M_{i}}+B_{ij}\frac{\theta_{M}}{1 + M_{j}} \right).
```

### 

### 4.7 Structural Stability

Curvature properties determine stability of tie configurations.

##### Theorem 4.5 (Local Stability)

Let $`w^{\star}`$be a strict local maximiser.

Then there exists

``` math
\epsilon > 0
```

such that:

``` math
\parallel w - w^{\star} \parallel < \epsilon \Rightarrow \Phi(w) \leq \Phi(w^{\star}).
```

Proof

Standard result for strict local maxima of continuous functions. ∎

### 

### 4.8 Interpretation

Curvature analysis shows that:

- Sparse networks permit global optimisation.

- Closed networks produce local optima.

- Optimal tie configurations satisfy explicit balance conditions.

The Network Potential Functional therefore defines a structural objective whose maximisers correspond to balanced relational configurations.

### 

### 4.9 Discussion

The Network Potential Functional exhibits both convex and nonconvex regimes depending on network closure.

The concave regime provides theoretical guarantees of global optimality.

The general regime corresponds more closely to empirical networks and leads naturally to equilibrium tie configurations.

This dual structure allows relational optimisation to be analysed both as a global optimisation problem and as a local equilibrium problem.

The next chapter develops reachability guarantees and establishes formal connections between network potential and structural opportunity.

# Chapter 5

# Reachability Guarantees

## 

## 5.1 Overview

Chapters 2–4 introduced the weighted network model, the Network Potential Functional, and its optimisation properties. The present chapter establishes formal connections between network potential and structural reach.

Relational structure determines the extent to which a node can access nonredundant regions of a network. Weak ties connecting structurally distinct neighbourhoods expand reachable opportunity, while redundant closure restricts effective reach.

This chapter defines measures of reachable structural diversity and establishes bounds relating these measures to node potential.

These results provide a theoretical connection between network potential and relational opportunity.

## 

## 5.2 Reachable Structural Diversity

Reachable structural diversity measures the extent to which a node can access structurally distinct neighbourhoods through weak ties.

##### Definition 5.1 (Reachable Structural Diversity)

For node $`i`$, define reachable structural diversity:

``` math
RSD_{i}(w) = \sum_{j \in \Gamma(i)}^{}{(1 -}w_{ij})^{p}B_{ij}.
```

Equivalently:

``` math
RSD_{i}(w) = M_{i}(w).
```

Thus, reachable structural diversity coincides with the mobility functional defined in Chapter 2.

This measure reflects the total brokerage-weighted weak-tie mass available to node $`i`$.

## 

## 5.3 Basic Properties

##### 

##### Proposition 5.1 (Bounds)

For all nodes $`i`$:

``` math
0 \leq RSD_{i}(w) \leq d_{i}.
```

Proof

Each term satisfies:

``` math
0 \leq (1 - w_{ij})^{p}B_{ij} \leq 1.
```

Summation over $`d_{i}`$terms gives the bounds. ∎

## 

## 5.4 Network Potential Bounds Reachability

The Network Potential Function provides a lower bound on reachable structural diversity.

##### Theorem 5.1 (NPF Lower Bound)

Let $`d_{i} = \mid \Gamma(i) \mid`$.

Then for all weight assignments $`w`$:

``` math
NPF_{i}(w) \geq \theta_{M}log(1 + RSD_{i}(w)) - \theta_{R}log\left( 1+\binom{d_{i}}{2} \right).
```

Proof

From Chapter 3:

``` math
NPF_{i} = \theta_{A}log(1 + A_{i}) + \theta_{M}log(1 + M_{i}) - \theta_{R}log(1 + R_{i}).
```

Since:

``` math
{A_{i} \geq 0,
}{R_{i} \leq \binom{d_{i}}{2},
}
```

the inequality follows directly. ∎

##### Corollary 5.1 (Reachability Implication)

For fixed degree $`d_{i}`$:

``` math
NPF_{i}(w_{1}) > NPF_{i}(w_{2})
```

implies that the minimum reachable structural diversity consistent with $`NPF_{i}(w_{1})`$exceeds that consistent with $`NPF_{i}(w_{2})`$.

## 

## 5.5 Invertible Bound

##### 

##### Theorem 5.2 (Reachability Lower Bound)

For $`\theta_{M} > 0`$:

``` math
RSD_{i}(w) \geq exp\left( \frac{NPF_{i}(w) + \theta_{R}log\left( 1+\binom{d_{i}}{2} \right)}{\theta_{M}} \right) - 1.
```

Proof

Rearrange Theorem 5.1 and exponentiate. ∎

### 

## 5.6 Structural Interpretation

Theorems 5.1–5.2 show that node potential controls reachable structural diversity.

Higher potential configurations require:

- greater brokerage-weighted weak-tie mass,

- or reduced redundancy,

- or increased cohesion.

Thus, network potential serves as a structural indicator of relational opportunity.

### 

## 5.7 Two-Hop Structural Reach

The one-hop reachability measure $`RSD_{i}(w)`$captures direct access to structurally distinct neighbours. Many relational opportunities arise through indirect contacts beyond the immediate neighbourhood.

This section introduces a measure of nonredundant two-hop reach.

##### Definition 5.2 (Two-Hop Nonredundant Reach)

Define:

``` math
RSD_{i}^{(2)}(w) = \sum_{j \in \Gamma(i)}^{}{(1 -}w_{ij})^{p}B_{ij}\sum_{k \in \Gamma(j) \smallsetminus \Gamma(i)}^{}{(1 -}w_{jk})^{p}.
```

The inner summation measures weak-tie mass from neighbour $`j`$to nodes not already adjacent to $`i`$.

The outer summation weights this quantity by brokerage-weighted weak ties from $`i`$to $`j`$.

This functional measures expected exposure to nonredundant second neighbours.

## 

## 5.8 Bounds on Two-Hop Reach

##### 

##### Proposition 5.2

For all nodes $`i`$:

``` math
0 \leq RSD_{i}^{(2)}(w) \leq d_{i}\Delta.
```

Proof

Each factor satisfies:

``` math
0 \leq (1 - w_{ij})^{p}B_{ij} \leq 1
```

and

``` math
0 \leq (1 - w_{jk})^{p} \leq 1.
```

The outer summation contains $`d_{i}`$terms.

The inner summation contains at most $`\Delta`$terms.

Multiplication yields the bound. ∎

## 

## 5.9 Enriched Mobility Functional

Define enriched mobility:

##### Definition 5.3

For parameter $`\alpha \geq 0`$:

``` math
{\widetilde{M}}_{i}(w) = M_{i}(w) + \alpha RSD_{i}^{(2)}(w).
```

The enriched mobility functional incorporates both direct and indirect reach.

## 

## 5.10 Two-Hop Reach Theorem

##### 

##### Theorem 5.3 (Monotonicity of Two-Hop Reach)

For fixed topology and $`p \geq 1`$:

``` math
{\widetilde{M}}_{i}(w)
```

is nonincreasing in each weight $`w_{ij}`$.

Equivalently, weakening ties increases enriched mobility.

Proof

Each term in $`M_{i}`$and $`RSD_{i}^{(2)}`$contains factors of the form:

``` math
\left( 1-w_{ij})^{p}. \right.\ 
```

Since:

``` math
\frac{d}{dw}(1 - w)^{p} < 0,
```

increasing weights reduces each factor.

All terms are nonnegative.

Thus:

``` math
\frac{\partial{\widetilde{M}}_{i}}{\partial w_{ij}} \leq 0.
```
∎

## 

## 5.11 Two-Hop Reach Corollary

##### 

##### Corollary 5.2

Decreasing tie strengths increases expected exposure to nonredundant second neighbours.

## 5.12 Relationship to Network Potential

##### 

##### Proposition 5.3

For fixed $`A_{i}`$and $`R_{i}`$:

``` math
NPF_{i}(w)
```

is strictly increasing in enriched mobility.

Proof

Immediate from Definition 3.1. ∎

## 

## 5.13 Discussion

This chapter establishes a formal connection between network potential and structural opportunity.

Key results include:

- Network potential bounds reachable structural diversity.

- Higher potential implies greater minimum reach.

- Two-hop reach increases with brokerage-weighted weak ties.

These results provide a theoretical interpretation of network potential as a measure of relational opportunity.

Together with the optimisation results of Chapter 4, the theory establishes network potential as a structural objective governing relational configuration.

# Chapter 6

# Relational Optimisation and Equilibrium Structure

## 

## 6.1 Overview

Chapters 2–5 introduced the weighted network model, the Network Potential Functional, and its reachability implications. The present chapter develops the interpretation of network potential as an objective governing relational configurations.

Relational optimisation is formulated as the selection of tie strengths that maximise the Network Potential Functional. The resulting configurations may be interpreted either as global optima or as locally stable equilibria.

This chapter establishes equilibrium concepts for weighted networks (Nash, 1951) and characterises the structural properties of equilibrium tie configurations.

## 

## 6.2 Relational Optimisation Problem

Let

``` math
\mathcal{W} = \lbrack 0,1\rbrack^{\mid E \mid}
```

be the weight space defined in Chapter 2.

Relational optimisation is defined as:

**Definition 6.1 (Relational Optimisation Problem)**

``` math
\underset{w\mathcal{\in W}}{max}\Phi(w).
```

A maximiser

``` math
w^{\star}
```

is called an optimal tie configuration.

Existence of such configurations follows from Theorem 3.3.

## 

## 6.3 Local Optimality

Because the Network Potential Functional is generally nonconcave (Chapter 4), optimisation typically produces local optima.

##### Definition 6.2 (Local Optimal Configuration)

A weight assignment $`w^{\star}`$is a local optimum if there exists $`\epsilon > 0`$such that

``` math
\parallel w - w^{\star} \parallel < \epsilon \Rightarrow \Phi(w) \leq \Phi(w^{\star}).
```

Local optima correspond to structurally stable tie configurations.

## 

## 6.4 Tie-Level Optimality Conditions

Interior optima satisfy first-order conditions.

##### Theorem 6.1 (First-Order Optimality Conditions)

If $`w^{\star}`$is an interior optimum, then for all edges $`\{ i,j\} \in E`$:

``` math
\frac{\partial\Phi}{\partial w_{ij}}(w^{\star}) = 0.
```

Proof

Necessary condition for interior maxima of differentiable functions. ∎

## 

## 6.5 Tie-Level Equilibrium Interpretation

The gradient expression from Chapter 3 yields:

``` math
\frac{\partial\Phi}{\partial w_{ij}} = \frac{\partial NPF_{i}}{\partial w_{ij}} + \frac{\partial NPF_{j}}{\partial w_{ij}}.
```

Thus, equilibrium requires:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}} = - \frac{\partial NPF_{j}}{\partial w_{ij}}.
```

This condition represents a balance between the marginal structural incentives of the two endpoints of an edge.

## 

## 6.6 Pairwise Stability

Tie adjustments involve two nodes simultaneously. This motivates a pairwise stability concept (Jackson, 2008).

##### Definition 6.3 (Pairwise Stability)

A weight assignment $`w^{\star}`$is pairwise stable if for every edge $`\{ i,j\} \in E`$there exists no feasible perturbation $`\delta`$such that:

``` math
\Phi(w^{\star} + \delta e_{ij}) > \Phi(w^{\star}),
```

where $`e_{ij}`$is the coordinate direction corresponding to edge $`\left\{ i,j \right\}`$.

Pairwise stability corresponds to the absence of mutually beneficial tie adjustments.

##### Theorem 6.2 (Local Optima Are Pairwise Stable)

Every local optimum is pairwise stable.

Proof

If a local optimum admitted a beneficial perturbation along any coordinate direction, it would not be locally maximal. ∎

## 

## 6.7 Structural Equilibria

Optimal configurations reflect the structural decomposition introduced in Chapter 2.

##### Definition 6.4 (Balanced Structural Configuration)

A configuration is balanced if interior ties satisfy:

``` math
w_{ij}^{p - 1}\left( \frac{\theta_{A}}{1 + A_{i}}-\frac{\theta_{R}}{1 + R_{i}}C_{ij} \right) = (1 - w_{ij})^{p - 1}B_{ij}\frac{\theta_{M}}{1 + M_{i}}
```

and the analogous condition for node $`j`$.

Balanced configurations equalise marginal cohesion and brokerage incentives.

## 

## 6.8 Structural Properties of Equilibria

Equilibrium tie configurations exhibit systematic structural properties.

##### Theorem 6.3 (Brokerage Differentiation)

At equilibrium, edges with higher brokerage values $`B_{ij}`$have lower equilibrium weights than edges with lower brokerage values, all else equal.

Proof Sketch

From Chapter 3:

``` math
\frac{\partial NPF_{i}}{\partial w_{ij}}
```

contains a term proportional to:

``` math
B_{ij}(1 - w_{ij})^{p - 1}.
```

Higher brokerage increases the incentive for lower weights, shifting equilibrium solutions downward.

##### Theorem 6.4 (Closure Suppression)

Edges embedded in highly closed neighbourhoods have lower equilibrium weights than edges in open neighbourhoods, all else equal.

Proof Sketch

Closure terms increase $`C_{ij}`$, increasing the redundancy penalty and reducing equilibrium weights.

##### Theorem 6.5 (Degree Normalisation)

Nodes with larger degree $`d_{i}`$exhibit smaller marginal cohesion gains:

``` math
\frac{\theta_{A}}{1 + A_{i}}
```

decreases with $`d_{i}`$.

Proof

Since $`A_{i}`$increases with degree:

``` math
1 + A_{i}
```

increases.

The reciprocal decreases.

## 

## 6.9 Equilibrium Interpretation

Equilibrium tie configurations balance three structural forces:

**Cohesion**

Encourages stronger ties.

**Brokerage**

Encourages weaker ties connecting distinct neighbourhoods.

**Closure Control**

Discourages redundant strong ties.

## 

## 6.10 Network Potential as an Energy Functional

The Network Potential Functional can be interpreted as an energy function for relational structure.

Tie adjustments correspond to energy changes:

``` math
\Delta\Phi.
```

Equilibria correspond to local maxima of network potential.

##### Theorem 6.6 (Potential Structure)

Tie adjustments increase network potential if and only if they increase the sum of node potentials.

Proof

Immediate from Definition 3.2.

## 

## 6.11 Interpretation

Relational optimisation produces tie configurations that balance stability and reach.

Equilibria correspond to structurally balanced networks in which:

- cohesive ties provide support,

- brokerage ties provide reach,

- redundancy is controlled.

The Network Potential Functional therefore defines a structural objective governing relational organisation.

## 

## 6.12 Discussion

This chapter establishes the equilibrium interpretation of relational optimisation.

The Network Potential Functional provides:

- an optimisation objective,

- equilibrium characterisation,

- structural predictions.

Together with the reachability results of Chapter 5, this establishes a unified framework linking relational structure, optimisation, and opportunity.

# Chapter 7

# Conclusion and Future Directions

## 

## 7.1 Overview

This thesis introduced a formal framework for relational optimisation in weighted networks based on the **Network Potential Functional**, a scalar functional defined over tie strengths and structural configuration. The theory formulates relational structure as a continuous optimisation problem on weighted graphs with fixed topology.

The Network Potential Functional combines three structural components:

- cohesion, measured through strong-tie capacity,

- brokerage, measured through nonredundant weak-tie reach,

- redundancy, measured through closure among neighbours.

These components are integrated into a single functional defined on the compact domain

``` math
\left\lbrack 0,1\rbrack^{\mid E \mid}. \right.\ 
```

The resulting framework provides a mathematical formulation of relational structure as an optimisation problem and establishes formal connections between tie configuration and structural reach.

## 

## 7.2 Summary of Results

The main results of this thesis may be summarised as follows.

**Functional Formulation**

Relational structure was represented as a weighted network with fixed topology, allowing tie strengths to vary continuously. The Network Potential Functional

``` math
\Phi(w) = \sum_{i \in V}^{}{NP}F_{i}(w)
```

was defined as a scalar functional on the weight space.

The functional was shown to be:

- bounded,

- continuous,

- well-defined on compact domains.

Existence of optimal configurations followed directly from compactness.

**Structural Optimality**

Gradient expressions were derived for the Network Potential Functional, yielding explicit conditions governing optimal tie strengths.

Interior optima satisfy balance equations equating marginal cohesion gains, redundancy costs, and brokerage benefits.

These conditions formalise the trade-off between strong and weak ties as an equilibrium relationship.

**Curvature Regimes**

Curvature analysis identified two regimes:

- a concave regime corresponding to sparse closure,

- a general regime in which closure produces nonconcavity.

In the concave regime, global optimisation is guaranteed. In the general regime, optimal configurations correspond to locally stable equilibria.

**Reachability Guarantees**

Formal reachability measures were introduced and linked to network potential.

Node potential was shown to bound reachable structural diversity, establishing a quantitative relationship between tie configuration and structural reach.

Two-hop reach measures were introduced to capture indirect structural exposure.

Enriched mobility was shown to increase with brokerage-weighted weak ties.

These results establish network potential as a structural measure of relational opportunity.

**Equilibrium Structure**

Local optima of the Network Potential Functional were interpreted as equilibrium tie configurations.

Equilibria satisfy balance conditions between cohesion, brokerage, and redundancy.

Structural properties of equilibria were characterised, including:

- brokerage differentiation,

- closure suppression,

- degree normalisation.

The Network Potential Functional was shown to act as an energy-like function governing relational configurations.

## 

## 7.3 Theoretical Significance

The Network Potential Functional provides a unified mathematical framework for analysing relational structure as an optimisation problem.

The framework formalises the balance between cohesion and brokerage that arises naturally in networked systems. While these concepts have been widely discussed in network theory, they have rarely been expressed as a continuous optimisation problem defined on weighted graphs.

The present work introduces a functional representation of relational structure that permits analysis using tools from optimisation theory and functional analysis.

The theory establishes:

- a continuous representation of tie strength,

- a scalar objective for relational configuration,

- equilibrium conditions for tie distributions,

- guarantees linking structure to reachability.

These elements provide a foundation for a mathematical theory of relational optimisation.

## 

## 7.4 Limitations

The theory developed in this thesis is intentionally restricted to a base model with fixed network topology.

Edge formation and dissolution are not explicitly modelled. Instead, the analysis assumes that relational structure evolves through continuous variation in tie strengths.

This restriction simplifies the mathematical analysis and allows the Network Potential Functional to be treated as a continuous functional on a compact domain.

However, many real networks evolve through discrete structural changes. Extending the theory to evolving graphs remains an important direction for future work.

## 

## 7.5 Extensions to Dynamic Networks

One natural extension of the theory is to allow edges to appear or disappear as tie strengths cross thresholds.

For example, a topology may be defined by:

``` math
E(w) = \{\{ i,j\}:w_{ij} > \tau\}.
```

Such a model would produce a piecewise-continuous Network Potential Functional and would allow network evolution to be studied as a dynamical process.

Dynamic models of this type would connect relational optimisation to network formation theory.

## 

## 7.6 Algorithmic Optimisation

The Network Potential Functional provides a natural objective for computational optimisation.

Gradient expressions derived in Chapter 3 allow the use of continuous optimisation methods such as projected gradient ascent:

``` math
w^{\left( t+1 \right)} = \Pi_{\left\lbrack 0,1\rbrack^{\mid E \mid} \right.\ }\left( w^{(t)} + \eta\nabla\Phi(w^{(t)}) \right).
```

Analysis of convergence properties for such algorithms represents a promising area for future research.

## 

## 7.7 Alternative Structural Measures

The structural functionals introduced in Chapter 2 represent one possible decomposition of relational structure.

Alternative formulations could include:

- centrality-weighted brokerage,

- path-based reach measures,

- spectral measures of redundancy,

- entropy-based diversity measures.

Such extensions would produce alternative forms of the Network Potential Functional and may reveal additional structural properties.

## 

## 7.8 Higher-Order Reachability

Chapter 5 introduced a two-hop reach measure as a first extension beyond direct neighbourhoods.

Further extensions could consider:

- multi-hop reachability,

- diffusion-based reach measures,

- probabilistic reach models.

These extensions would allow network potential to be linked more directly to dynamic processes such as information propagation.

## 

## 7.9 Game-Theoretic Extensions

The equilibrium interpretation developed in Chapter 6 suggests a connection with game-theoretic models.

One possible direction is to treat nodes as agents selecting tie strengths to maximise individual potential functions:

``` math
\underset{w_{i}}{max}NPF_{i}(w).
```

Such a formulation would produce strategic interaction over tie strengths and could yield equilibrium concepts analogous to Nash equilibrium.

This approach would connect relational optimisation with network games and congestion models.

## 

## 7.10 Final Remarks

This thesis introduced the Network Potential Functional as a mathematical object defined on weighted networks and demonstrated its usefulness for analysing relational structure.

The theory shows that relational configurations can be studied as solutions to optimisation problems defined over tie strengths.

By integrating cohesion, brokerage, and redundancy into a single functional framework, the Network Potential Functional provides a formal representation of the structural balance underlying effective networks.

The results presented here establish a foundation for the study of relational optimisation and suggest a range of directions for further theoretical development.

# References

Boyd, S. and Vandenberghe, L. (2004) Convex Optimization. Cambridge: Cambridge University Press.

Burt, R.S. (1992) Structural Holes: The Social Structure of Competition. Cambridge, MA: Harvard University Press.

Coleman, J.S. (1988) 'Social capital in the creation of human capital', American Journal of Sociology, 94, pp. S95–S120.

Diestel, R. (2017) Graph Theory. 5th edn. Berlin: Springer.

Granovetter, M.S. (1973) 'The strength of weak ties', American Journal of Sociology, 78(6), pp. 1360–1380.

Jaccard, P. (1901) Étude comparative de la distribution florale. Bulletin de la Société Vaudoise des Sciences Naturelles, 37, pp. 547–579.

Jackson, M.O. (2008) Social and Economic Networks. Princeton: Princeton University Press.

Nash, J. (1951) 'Non-cooperative games', Annals of Mathematics, 54(2), pp. 286–295.

Newman, M.E.J. (2010) Networks: An Introduction. Oxford: Oxford University Press.

Rudin, W. (1976) Principles of Mathematical Analysis. 3rd edn. New York: McGraw-Hill.

# Chapter 8

# Limitations and Future Mathematical Development

### 

## 8.1 Overview

The preceding chapters introduced the Network Potential Functional as a scalar functional defined on the space of weighted graphs with fixed topology and established its fundamental analytical and optimisation properties. The framework provides a mathematically well-posed formulation of relational optimisation in which tie strengths vary continuously over a compact domain.

The purpose of the present chapter is to clarify the scope of the base theory and to identify directions for further mathematical development. The limitations discussed here are primarily structural rather than technical: they arise from deliberate modelling choices made in order to obtain a tractable and analytically transparent theory.

The framework developed in this thesis should therefore be understood as a base formulation of relational optimisation on weighted networks rather than as a complete theory of network evolution.

### 

## 8.2 Scope of the Base Formulation

### 

### 8.2.1 Fixed Topology

The theory developed in Chapters 2–6 assumes a finite undirected graph

``` math
G = (V,E)
```

with fixed topology. Tie strengths vary continuously over the admissible domain

``` math
\Omega = \lbrack 0,1\rbrack^{E},
```

and the Network Potential Functional

``` math
\Phi:\Omega \rightarrow \mathbb{R}
```

is optimised over this domain.

This formulation isolates the problem of **relational allocation**, namely the distribution of tie strengths across a given structural scaffold. The assumption of fixed topology allows the admissible domain to be compact and enables the use of standard tools from optimisation theory and functional analysis.

In many empirical networks, however, relational structure evolves not only through variation in tie strengths but also through the formation and dissolution of edges. The present theory therefore describes optimisation on a fixed network rather than network formation itself.

The extension of the Network Potential Functional to evolving graph topologies represents a natural direction for further development and is discussed in Section 8.5.

#### 

### 8.2.2 Continuous Tie Strength Representation

Tie strengths are represented by continuous weights

``` math
w_{e} \in \lbrack 0,1\rbrack,e \in E,
```

which are interpreted as relative intensities of interaction or relational investment.

This representation allows relational structure to be treated as a continuous configuration within a finite-dimensional space and permits differential analysis of structural incentives. The resulting framework provides explicit gradient expressions and balance conditions governing optimal tie strengths.

The continuous representation is primarily analytical in purpose and does not prescribe a unique empirical interpretation of tie strength. In empirical applications, tie strengths may represent heterogeneous quantities such as interaction frequency, communication intensity, or collaborative investment. The mapping between empirical measures and the abstract weight space therefore remains application-dependent.

### 

### 8.2.3 Structural Regularisation within the Functional

Although the admissible domain is unconstrained apart from the bounds

``` math
0 \leq w_{e} \leq 1,
```

the Network Potential Functional contains intrinsic structural regularisation mechanisms that prevent trivial maximisation by uniform weight increase.

The node-level Network Potential Function has the form

``` math
\Phi_{i}(w) = \log(1 + S_{i}(w)) + \beta\log(1 + M_{i}(w)) - \gamma\log(1 + R_{i}(w)),
```

where the stability functional $`S_{i}`$, the mobility functional $`M_{i}`$, and the redundancy functional $`R_{i}`$were defined in Chapter 2.

The logarithmic form ensures diminishing marginal returns for both cohesion and brokerage components. In addition, the redundancy functional introduces a closure penalty that increases with weighted triadic density. Since the redundancy functional involves products of edge weights, it grows polynomially in local tie strengths, while the cohesion and mobility contributions grow logarithmically.

Consequently, increases in tie strength within highly closed neighbourhoods produce rapidly increasing redundancy penalties relative to cohesion gains. These mechanisms act as intrinsic stabilising forces and permit the existence of interior optimal configurations without explicit resource constraints.

Nevertheless, these mechanisms depend on parameter values and local network structure. The introduction of explicit allocation constraints provides a stronger structural guarantee and is discussed in Section 8.4.

## 

## 8.3 Structural Limitations

### 

### 8.3.1 Fixed Topology Assumption

The restriction to fixed topology is the principal structural limitation of the present theory. In many networks, structural adaptation occurs through the creation and removal of edges rather than solely through variation in tie strengths.

The present framework studies optimisation on a fixed edge set

``` math
E,
```

and therefore, represents only a subset of the full configuration space of relational structures.

Allowing topology to vary would transform the optimisation problem into a mixed discrete–continuous problem involving both edge selection and tie-strength allocation. Such formulations would connect the Network Potential Functional to network formation models and combinatorial optimisation problems.

#### 

### 8.3.2 Absence of Explicit Allocation Constraints

The admissible domain

``` math
\Omega = \lbrack 0,1\rbrack^{E}
```

places independent bounds on each edge weight but does not impose resource constraints coupling weights incident to a common node.

In many relational settings, tie strengths represent allocations of limited resources such as time or attention. This motivates constraints of the form

``` math
\sum_{j \in N(i)}^{}w_{ij} \leq B_{i},i \in V,
```

or global constraints such as

``` math
\sum_{e \in E}^{}w_{e} \leq B.
```

Such constraints would transform the admissible domain into a compact convex polytope and would produce optimisation problems with Karush–Kuhn–Tucker structure.

The unconstrained formulation adopted here allows analytical transparency and yields explicit structural balance conditions. However, constrained formulations may provide stronger guarantees of structural robustness and represent an important direction for further work.

### 

### 8.3.3 Motif-Based Redundancy Model

Redundancy in the present framework is defined through weighted triadic closure among neighbours. The redundancy functional measures the extent to which neighbours of a node are connected to one another and therefore captures local structural overlap.

Triadic closure provides a natural first-order model of redundancy and allows the Network Potential Functional to be expressed in terms of local network structure. However, redundancy may also arise through longer paths or community-level overlap that is not captured by triangles alone.

Alternative redundancy measures could incorporate higher-order motifs, path-based overlap, or spectral measures of structural dependence. Such extensions would produce alternative forms of the Network Potential Functional and may reveal additional structural regimes.

### 

### 8.3.4 Static Optimisation Framework

The present theory is formulated as a static optimisation problem. Optimal configurations and local maxima of the Network Potential Functional are interpreted as structurally stable states.

While this interpretation is consistent with local improvement dynamics, the thesis does not specify a dynamical model describing the evolution of tie strengths. In particular, convergence properties and basins of attraction are not analysed.

The development of explicit dynamical models would provide a deeper understanding of equilibrium selection and structural stability.

### 

## 8.4 Constrained Optimisation Extensions

A natural extension of the present framework is the introduction of allocation constraints coupling incident tie strengths.

Under node-level budget constraints

``` math
\sum_{j \in N(i)}^{}w_{ij} \leq B_{i},
```

the admissible domain becomes a compact convex polytope

``` math
\Omega_{B} \subseteq \lbrack 0,1\rbrack^{E}.
```

Optimisation of the Network Potential Functional over $`\Omega_{B}`$leads to constrained optimisation problems characterised by Karush–Kuhn–Tucker conditions.

Such formulations preserve compactness while introducing explicit trade-offs between competing ties. Constrained models therefore provide a natural mathematical representation of limited relational capacity.

Projected gradient methods and related optimisation techniques provide natural computational approaches for such problems.

### 

## 8.5 Dynamic and Topological Extensions

A major extension of the theory is the endogenisation of network topology. Instead of fixing the edge set $`E`$, one may consider configuration spaces of the form

``` math
\Omega^{*} = \bigcup_{E' \subseteq V \times V}^{}{\lbrack 0,1}\rbrack^{E'}.
```

Optimisation over $`\Omega^{*}`$ would allow both tie strengths and edge sets to vary simultaneously.

One possible formulation introduces threshold-dependent topology:

``` math
E(w) = \{ e \in V \times V:w_{e} \geq \tau\},
```

leading to piecewise-continuous potential functions.

More general formulations may be interpreted as dynamical systems on evolving graphs or as variational problems on combinatorial structures.

Such extensions would connect relational optimisation to network formation theory and represent a substantial expansion of the present framework.

### 

## 8.6 Dynamical Formulations

The Network Potential Functional provides a natural objective for continuous-time or discrete-time tie adjustment processes.

One possible formulation is gradient flow:

``` math
\dot{w} = \nabla\Phi(w),
```

with projection onto the admissible domain where necessary.

Under constrained domains, projected dynamics of the form

``` math
\dot{w} = \Pi_{T(w)}\nabla\Phi(w)
```

may be considered, where $`T(w)`$ denotes the tangent cone of the admissible domain.

Analysis of convergence properties and stability of such dynamics represents a natural extension of the equilibrium interpretation developed in Chapter 6.

In concave regimes, convergence to global optima may be expected. In nonconcave regimes, multiple stable configurations may arise.

## 8.7 Optimisation Landscape and Structural Regimes

Chapter 4 established that curvature properties of the Network Potential Functional depend strongly on local closure structure. Triangle-free neighbourhoods produce concave regimes with globally optimal configurations, while closure produces nonconcavity and multiple local optima.

Further development of this landscape perspective represents an important direction for future work. In particular, one may seek to characterise critical points and their stability properties as functions of structural parameters such as triangle density and degree distribution.

Such analyses would clarify the relationship between network topology and the multiplicity of structurally stable configurations.

### 

## 8.8 Relationship to Existing Network Measures

The Network Potential Functional integrates cohesion, brokerage, and redundancy within a single optimisation framework. While these components are closely related to classical network concepts, the functional formulation differs from standard network indices.

Further work may establish formal relationships between the Network Potential Functional and existing structural measures such as clustering coefficients, constraint indices, and expansion properties.

Such comparisons would clarify the structural meaning of network potential and strengthen connections with existing network science literature.

### 

## 8.9 Concluding Remarks

The Network Potential Functional provides a mathematically well-defined objective for relational optimisation on weighted networks. The framework establishes a continuous formulation of tie-strength allocation that permits analysis using tools from optimisation theory and functional analysis.

The present theory should be viewed as a base formulation describing optimisation on weighted graphs with fixed topology. Extensions incorporating allocation constraints, dynamical processes, and evolving topology represent natural directions for further development.

Together, these directions suggest a broader mathematical programme in which relational structure is studied as a variational problem on evolving networks.
