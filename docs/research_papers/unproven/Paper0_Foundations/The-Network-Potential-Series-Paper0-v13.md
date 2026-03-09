## 

## 

## 

## Representation and Axiomatic Foundations

## of Relational Potentials on Weighted Graphs

#### 

#### 

#### 

#### **Author:** Ian Mack

#### **Date:** Feb. 2026

# 

# Contents

[Paper 0 Representation and Axiomatic Foundations of Relational Potentials on Weighted Graphs [4](#paper-0-representation-and-axiomatic-foundations-of-relational-potentials-on-weighted-graphs)](#paper-0-representation-and-axiomatic-foundations-of-relational-potentials-on-weighted-graphs)

[Abstract [4](#abstract)](#abstract)

[0. Introduction [5](#introduction)](#introduction)

[0.1 Variational Formulation of Relational Architecture [5](#variational-formulation-of-relational-architecture)](#variational-formulation-of-relational-architecture)

[0.2 The Network Potential Functional [9](#the-network-potential-functional)](#the-network-potential-functional)

[0.3 Need for an Axiomatic Framework [11](#need-for-an-axiomatic-framework)](#need-for-an-axiomatic-framework)

[0.4 Objectives of Paper 0 [13](#objectives-of-paper-0)](#objectives-of-paper-0)

[0.5 Weighted Graph Framework [14](#weighted-graph-framework)](#weighted-graph-framework)

[0.5.1 Graph Structure [14](#graph-structure)](#graph-structure)

[0.5.2 Weight Domain [15](#weight-domain)](#weight-domain)

[0.5.3 Edge Coordinates [17](#edge-coordinates)](#edge-coordinates)

[0.5.4 Incident Sets [17](#incident-sets)](#incident-sets)

[0.5.5 Local Structural Variables [17](#local-structural-variables)](#local-structural-variables)

[0.6 Relational Potentials [18](#relational-potentials)](#relational-potentials)

[0.6.1 Definition [18](#definition)](#definition)

[0.6.2 Regularity Class [19](#regularity-class)](#regularity-class)

[0.6.3 Equilibrium Configurations [20](#equilibrium-configurations)](#equilibrium-configurations)

[0.6.4 Variational Inequality Formulation [21](#variational-inequality-formulation)](#variational-inequality-formulation)

[0.6.5 Structural Contributions [22](#structural-contributions)](#structural-contributions)

[0.6.6 Structural Marginals [23](#structural-marginals)](#structural-marginals)

[0.6.7 Relational Rigidity and Structural Stability [24](#relational-rigidity-and-structural-stability)](#relational-rigidity-and-structural-stability)

[0.7 Axioms for Admissible Relational Potentials [27](#axioms-for-admissible-relational-potentials)](#axioms-for-admissible-relational-potentials)

[0.7.1 Locality [34](#locality)](#locality)

[0.7.2 Symmetry [35](#symmetry)](#symmetry)

[0.7.3 Monotonicity [36](#monotonicity)](#monotonicity)

[0.7.4 Diminishing Returns [36](#diminishing-returns)](#diminishing-returns)

[0.7.5 Structural Interaction [37](#structural-interaction)](#structural-interaction)

[0.7.6 Regularity [39](#regularity)](#regularity)

[0.7.7 Structural Sufficiency [40](#structural-sufficiency)](#structural-sufficiency)

[0.8 Structural Marginal Theory [43](#structural-marginal-theory)](#structural-marginal-theory)

[0.8.1 Edgewise Marginals [43](#edgewise-marginals)](#edgewise-marginals)

[0.8.2 Structural Coordinates [45](#structural-coordinates)](#structural-coordinates)

[0.8.3 Structural Coordinate Representation [48](#structural-coordinate-representation)](#structural-coordinate-representation)

[0.8.4 Structural Marginal Decomposition [50](#structural-marginal-decomposition)](#structural-marginal-decomposition)

[0.9 Representation Theory [53](#representation-theory)](#representation-theory)

[0.9.0 Structural Equivalence [54](#structural-equivalence)](#structural-equivalence)

[Definition 0.9.0 (Structural Equivalence) [55](#definition-0.9.0-structural-equivalence)](#definition-0.9.0-structural-equivalence)

[0.9.1 Integrability Conditions [58](#integrability-conditions)](#integrability-conditions)

[0.9.2 Representation Theorem [62](#representation-theorem)](#representation-theorem)

[0.9.3 Canonical Form [65](#canonical-form)](#canonical-form)

[0.10 The Network Potential Functional [70](#the-network-potential-functional-1)](#the-network-potential-functional-1)

[0.10.1 Definition [71](#definition-1)](#definition-1)

[0.10.2 Verification of Axioms [72](#verification-of-axioms)](#verification-of-axioms)

[0.10.3 Canonical Status [74](#canonical-status)](#canonical-status)

[0.11 Operator-Theoretic Structure [75](#operator-theoretic-structure)](#operator-theoretic-structure)

[0.11.1 Hessian Operator [75](#hessian-operator)](#hessian-operator)

[0.11.2 Incident Hessian [78](#incident-hessian)](#incident-hessian)

[0.11.3 Susceptibility Kernel [79](#susceptibility-kernel)](#susceptibility-kernel)

[0.12 Implications for the Network Potential Series [81](#implications-for-the-network-potential-series)](#implications-for-the-network-potential-series)

[0.12.1 Structural Differentiation [81](#structural-differentiation)](#structural-differentiation)

[0.12.2 Scarcity Geometry [82](#scarcity-geometry)](#scarcity-geometry)

[0.12.3 Dynamics [83](#dynamics)](#dynamics)

[0.12.4 Topological Endogeneity [84](#topological-endogeneity)](#topological-endogeneity)

[0.12.5 Functional Generalisation [84](#functional-generalisation)](#functional-generalisation)

[0.13 Conclusion [85](#conclusion)](#conclusion)

[Bibliography [88](#bibliography)](#bibliography)

# Paper 0 Representation and Axiomatic Foundations of Relational Potentials on Weighted Graphs

### Abstract

This paper establishes the axiomatic foundations of relational potentials on weighted graphs. Relational potentials are scalar functionals defined on the space of admissible edge-weight configurations and interpreted variationally as measures of global structural value. An admissible class of relational potentials is characterised by locality, symmetry, monotonicity, and diminishing-return conditions governing marginal structural contributions of tie strengths.

Under mild regularity assumptions, relational potentials satisfying these axioms admit canonical marginal representations in terms of cohesion, mobility, and redundancy components. These components arise as structurally distinct contributions to marginal structural value and define a canonical decomposition of admissible relational potentials.

The Network Potential Functional provides a canonical example within this admissible class. The admissible class defined here establishes the functional setting for the Network Potential Series and provides the foundation for the structural differentiation, scarcity geometry, and dynamical analyses developed in subsequent papers.

## 0. Introduction

### 0.1 Variational Formulation of Relational Architecture

Relational structure in weighted networks may be formulated variationally through scalar functionals defined on the space of admissible edge-weight configurations. Such functionals assign a global structural value to each configuration of tie strengths and thereby induce equilibrium architecture through optimisation.

Let

``` math
G = (V,E)
```

be a finite undirected graph and let

``` math
\Omega_{G} \subset \mathbb{R}^{\mid E \mid}
```

be a compact domain of admissible edge weights. A weight configuration is represented by a vector

``` math
w = (w_{e})_{e \in E} \in \Omega_{G},
```

where $`w_{e}`$denotes the strength of edge $`e`$.

**Definition 0.1 (Relational Potential)**

A **relational potential** on $`G`$is a continuously differentiable functional

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R.}
```

Equilibrium configurations $`w^{*} \in \Omega_{G}`$ are characterised by standard variational conditions. Interior equilibria satisfy

``` math
\nabla\Phi_{G}(w^{*}) = 0,
```

while boundary equilibria are characterised by the associated variational inequality conditions determined by the feasible domain $`\Omega_{G}`$.

Within this formulation, relational architecture is interpreted as an equilibrium property of a finite-dimensional variational system. The distribution of tie strengths is determined endogenously through optimisation under a global structural objective rather than through exogenously imposed structural rules.

Structural properties of weighted networks may therefore be analysed through the geometry of relational potentials and the stability properties of their stationary points.

This variational formulation places relational optimisation within the general framework of finite-dimensional nonlinear optimisation and potential-based equilibrium theory. Weighted networks are thereby interpreted as equilibrium configurations of smooth scalar functionals defined on compact subsets of Euclidean space, permitting structural questions to be studied using the analytical and geometric tools of variational analysis.

**Variational Regime**

The analysis developed in this paper concerns relational systems whose marginal structural incentives admit a scalar potential representation. Within this **variational regime**, weighted networks are interpreted as equilibrium configurations of a smooth relational potential.

Let

``` math
F(w) = (F_{e}(w))_{e \in E}
```

denote marginal structural incentives. The variational regime assumes that these incentives arise as the gradient of a scalar functional:

``` math
F(w) = \nabla\Phi_{G}(w).
```

This representation implies the integrability condition

``` math
\frac{\partial F_{e}}{\partial w_{f}}(w) = \frac{\partial F_{f}}{\partial w_{e}}(w)\text{for all }e,f \in E.
```

This assumption restricts attention to conservative structural incentive systems for which marginal structural values are mutually compatible and admit integration into a global structural objective.

Not all relational systems admit such a representation. Non-conservative structural incentives may produce cyclic adjustment processes or path-dependent evolution that cannot be captured by a scalar potential. The present work therefore identifies and studies the admissible class of relational systems for which relational architecture can be analysed through variational methods.

Within this regime, relational architecture arises as the equilibrium geometry of a smooth optimisation landscape.

**0.1.1 The Variational Assumption**

The central premise of the Network Potential framework is that a class of weighted networks may be represented as equilibrium configurations of a scalar relational potential.

Within this framework, relational architecture is determined by a functional

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

defined on the space of admissible edge-weight configurations, and equilibrium structures arise as stationary points of this functional subject to the constraints defining $`\Omega_{G}`$.

Marginal structural incentives

``` math
F(w) = (F_{e}(w))_{e \in E}
```

are assumed to be conservative in the sense that

``` math
F(w) = \nabla\Phi_{G}(w).
```

Equivalently, marginal incentives satisfy the integrability condition

``` math
\frac{\partial F_{e}}{\partial w_{f}}(w) = \frac{\partial F_{f}}{\partial w_{e}}(w).
```

The existence of a scalar relational potential expresses the assumption that structural incentives are globally consistent and can be integrated into a shared structural objective. In this setting, the structural value of a tie is not an intrinsic property of an isolated edge but a contribution to a global architectural state.

The variational assumption provides the analytical foundation for the Network Potential Series. The existence of a scalar potential ensures that relational dynamics admit a Lyapunov structure and that equilibrium configurations may be analysed using variational principles.

In particular, the operator-theoretic analysis developed in subsequent papers relies on the existence of the Hessian operator

``` math
D^{2}\Phi_{G}(w),
```

whose spectral and structural properties determine local stability, structural rigidity, and equilibrium response.

Without a potential representation, relational adjustment processes may exhibit non-conservative or cyclic behaviour and would not admit a unified variational description. The present framework therefore restricts attention to relational systems for which architecture arises as an equilibrium property of a scalar potential.

This assumption defines the mathematical domain of applicability of the Network Potential framework.

## 

## 0.2 The Network Potential Functional

The Network Potential Functional introduced in Mack (2026) provides a concrete example of a relational potential defined on weighted graphs. The functional assigns a scalar value to each configuration of tie strengths and thereby induces equilibrium structure through variational optimisation. It is defined on a compact domain of admissible edge weights and may be interpreted as an energy-like quantity on weighted networks.

The Network Potential Functional combines three structural components governing the contribution of tie strengths to global structural value.

**Cohesion (Stability)**\
The cohesion component measures the stabilising contribution of direct ties. Cohesion is determined by the aggregate strength of ties incident to each node, transformed to emphasise strong connections. Increasing tie strengths raises structural value through the accumulation of cohesive capacity, subject to diminishing marginal returns. The cohesion component therefore captures the contribution of sustained or intensive relationships to structural stability.

**Brokerage (Mobility)**\
The brokerage component measures access to structurally distinct regions of the network through nonredundant weak ties. Brokerage is determined by brokerage-weighted weak-tie mass and reflects the extent to which a node is connected to separated neighbourhoods. Ties connecting structurally distinct neighbourhoods contribute more strongly to brokerage value than ties embedded within closed clusters. The brokerage component therefore represents structural reach beyond the immediate neighbourhood.

**Redundancy (Closure)**\
The redundancy component measures the extent of closure among neighbouring nodes and represents diminishing structural value associated with overlapping neighbourhood structure. Redundancy increases with weighted triadic closure and penalises configurations in which structural access is duplicated through multiple overlapping ties. The redundancy component therefore captures the structural costs associated with excessive neighbourhood overlap.

Together these components define a relational potential

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

that measures structural quality of weighted networks through a balance between cohesion, brokerage, and redundancy. Equilibrium configurations correspond to stationary points of the functional on the admissible weight domain.

The foundational analytical properties of the Network Potential Functional were established in Mack (2026). The functional is bounded and continuous on compact weight domains and therefore admits maximising configurations.

Interior optima satisfy explicit gradient conditions that characterise equilibrium tie strengths as balance points between cohesion, brokerage, and redundancy contributions.

Curvature analysis identifies distinct structural regimes. Under sparse closure conditions the functional is concave and therefore admits globally optimal configurations, while closure interactions in general networks produce nonconcavity and permit multiple locally optimal configurations interpreted as structurally stable equilibria.

Local stability properties of equilibrium configurations are determined by the definiteness properties of the associated Hessian operator.

These results establish the Network Potential Functional as a well-defined variational object on weighted graphs and demonstrate that optimisation under the functional produces structured equilibrium configurations.

The present paper does not depend on the specific analytic form of the Network Potential Functional. Instead, the functional serves as a motivating example for a broader class of relational potentials defined through structural conditions on marginal contributions of tie strengths. The axiomatic framework developed in the following sections identifies natural conditions under which relational potentials admit systematic structural analysis and places the Network Potential Functional within this admissible class.

## 0.3 Need for an Axiomatic Framework

While the Network Potential Functional provides a concrete and analytically tractable formulation of relational optimisation, the structural investigations developed in the subsequent papers of this series require a broader functional setting. In particular, the curvature-based structural differentiation results established in Paper I and the constrained optimisation framework developed in Paper II rely on regularity and structural properties that are not specific to the Network Potential Functional itself. These results depend primarily on general features of relational potentials defined on weighted graphs, and their validity should not depend on the particular analytic form of a single functional.

More fundamentally, the Network Potential Functional represents one member of a potentially large class of scalar functionals defined on the space of edge-weight configurations. Without a general characterisation of such functionals, structural results derived for a specific functional remain model-dependent and their scope remains unclear. In particular, it is natural to ask under what structural conditions relational potentials admit systematic analysis through variational methods and which properties of equilibrium configurations depend only on general structural principles rather than on specific modelling choices.

These considerations motivate the development of an axiomatic formulation of relational potentials. The objective is to identify natural structural conditions under which relational potentials define well-behaved variational systems on weighted graphs. Such conditions include locality of structural contributions, invariance under relabelling of nodes, and regularity properties governing marginal structural responses to changes in tie strengths. Together these conditions define an admissible class of relational potentials suitable for structural analysis.

An axiomatic framework serves two complementary purposes. First, it provides a precise mathematical definition of relational potentials independent of any particular analytic specification. Second, it establishes the functional setting within which the structural results of the Network Potential Series may be formulated. In particular, the admissible class introduced here provides the domain for the curvature-based structural differentiation analysis of Paper I and the polyhedral scarcity geometry developed in Paper II. The same functional setting also underlies the dynamical formulations, topological extensions, and generalised structural measures developed in subsequent papers.

A central objective of the axiomatic framework is to identify structural properties of relational potentials that are invariant under admissible transformations of the functional representation. Structural features of interest include equilibrium stationary configurations, local stability properties, and perturbation responses determined by curvature operators. These quantities depend only on marginal structural incentives and their local variation and therefore should be regarded as intrinsic characteristics of relational potentials rather than properties of a particular analytic specification.

This observation leads naturally to the introduction of an equivalence relation on admissible relational potentials. Two relational potentials that generate identical marginal structural incentives and identical local curvature geometry represent the same underlying relational architecture and should therefore be regarded as structurally equivalent. The representation results developed in Section 0.9 formalise this idea by defining structural equivalence and identifying canonical representatives of the resulting equivalence classes.

Within this framework, the Network Potential Functional is interpreted not as a defining model but as a canonical coordinate realisation of admissible relational potentials. The axioms introduced below formalise the structural principles implicit in the Network Potential Functional and identify the general conditions under which relational optimisation generates structured equilibrium architectures. Subsequent papers analyse the geometric and variational consequences of these structural principles in a coordinate-independent manner, relying only on properties that are invariant under structural equivalence.

## 0.4 Objectives of Paper 0

The purpose of this paper is to establish the axiomatic and representational foundations of relational potentials on weighted graphs. The results developed here define an admissible class of scalar functionals suitable for variational analysis and provide the mathematical framework within which the structural investigations of the Network Potential Series are formulated.

First, relational potentials are defined as smooth scalar functionals on compact domains of admissible edge weights. This formulation places relational optimisation within the setting of finite-dimensional variational analysis and provides a precise mathematical description of weighted networks as equilibrium configurations of a scalar potential.

Second, an admissible class of relational potentials is introduced through structural conditions governing marginal contributions of tie strengths. These conditions include locality of structural interactions, invariance under relabelling of nodes, monotonicity of marginal structural value, and diminishing-return properties of individual ties. Together these axioms define a class of relational potentials for which equilibrium configurations admit systematic structural analysis.

Third, representation results are established showing that relational potentials satisfying the admissibility conditions admit canonical marginal decompositions into cohesion, mobility, and redundancy components under mild regularity assumptions. These results demonstrate that the cohesion–mobility–redundancy structure arises naturally from general structural principles rather than from a specific analytic construction.

Fourth, the Network Potential Functional is shown to arise as a canonical representative of the admissible class. In this sense the functional provides a concrete realisation of the abstract framework developed in this paper while remaining one instance among a broader family of relational potentials.

Taken together, these results establish the mathematical foundations of relational potentials on weighted graphs and provide the functional setting within which the structural and dynamical investigations developed in subsequent papers are carried out.

## 0.5 Weighted Graph Framework

This section establishes the basic notation and structural setting used throughout the paper. Relational potentials are defined on weighted graphs with fixed topology and continuously varying edge weights. The definitions introduced here provide the configuration space on which relational potentials act.

### 0.5.1 Graph Structure

Let

``` math
G = (V,E)
```

be a finite undirected graph, where $`V`$is a finite set of nodes and

``` math
E \subseteq \{\{ i,j\}:i,j \in V,\text{ }i \neq j\}
```

is a set of unordered node pairs representing edges. The number of edges is denoted by $`\mid E \mid`$.

Throughout this paper the graph topology is assumed to be fixed. Relational optimisation is therefore studied on a fixed graph with continuously adjustable tie strengths. Extensions in which the edge set varies endogenously are considered in Paper IV.

### 0.5.2 Weight Domain

A weight configuration on $`G`$ is represented by a vector

``` math
w \in \Omega_{G} \subset \mathbb{R}^{\mid E \mid}.
```

Unless otherwise specified, the admissible weight domain is taken to be the hypercube

``` math
\Omega_{G} = \lbrack 0,1\rbrack^{\mid E \mid}.
```

Throughout the paper the admissible domain is denoted

``` math
\Omega = \lbrack 0,1\rbrack^{m} \subset \mathbb{R}^{m},
```

where $`m = \mid E \mid`$ is the number of edges of $`G`$. The domain $`\Omega\`$therefore represents the feasible set of admissible edge-weight configurations.

The interval $`\left\lbrack 0,1 \right\rbrack`$ represents normalised tie strengths, where $`0`$corresponds to the absence of a tie and $`1`$corresponds to maximal tie strength.

The compactness of $`\Omega`$plays an important role in the analysis of relational potentials, ensuring the existence of maximising configurations and the boundedness of admissible weight sequences.

More general compact domains may be considered without altering the structural results developed in this paper, but the hypercube provides a convenient canonical representation.

The interior of the admissible domain is given by

``` math
\Omega^{\circ} = (0,1)^{m}.
```

The interior domain $`\Omega^{\circ}`$is open, connected, and simply connected as a subset of $`\mathbb{R}^{m}`$, while the full domain $`\Omega`$is compact and convex. These geometric properties play an important role in the representation theory developed in Section 0.9, where integrability conditions are established on open simply connected subsets of the weight space.

Throughout the paper relational potentials are assumed to admit a twice continuously differentiable extension to an open neighbourhood

``` math
U \subset \mathbb{R}^{\mid E \mid}
```

satisfying

``` math
\Omega_{G} \subset U,
```

where $`U`$is open and simply connected.

All differential operators are defined on $`U`$and restricted to $`\Omega_{G}`$when required. In particular,

``` math
\Phi_{G} \in C^{2}(U),
```

ensuring that gradients and Hessian operators are well-defined throughout the admissible domain.

### 0.5.3 Edge Coordinates

For each edge $`e \in E`$, the scalar variable

``` math
w_{e}
```

denotes the weight of edge $`e`$. A weight configuration may therefore be written as

``` math
w = (w_{e})_{e \in E}.
```

Edge weights are interpreted as continuously adjustable tie strengths. The coordinate representation allows relational potentials to be treated as functions of finitely many real variables and permits the use of standard tools from finite-dimensional analysis.

### 0.5.4 Incident Sets

For each node $`i \in V`$, the incident edge set is defined by

``` math
\delta(i) = \{ e \in E:e\ is\ incident\ to\ i\}
```

The set $`\delta(i)`$ therefore contains all edges having $`i`$as an endpoint. Incident sets determine the local coordinate structure associated with each node and play a central role in the locality conditions imposed on relational potentials.

### 0.5.5 Local Structural Variables

Relational potentials generally depend not only on individual edge weights but also on structural characteristics of the local neighbourhood surrounding each edge. To describe such dependencies abstractly, it is convenient to introduce local structural variables associated with each edge.

For each edge $`e \in E`$, let

``` math
S_{e}(w)
```

denote a separation variable measuring structural distinction between the neighbourhoods connected by edge $`e`$, and let

``` math
R_{e}(w)
```

denote a redundancy variable measuring the extent of neighbourhood overlap associated with edge $`e`$.

These variables are assumed to depend only on edge weights in a finite neighbourhood of $`e`$. Their precise analytic form is not specified at this stage. Instead, they serve as abstract structural coordinates through which relational potentials may depend on local network structure.

These structural variables correspond to the structural coordinate maps introduced formally in Axiom A6 (Section 0.7.7)**.**

The separation variables capture structural reach beyond the immediate neighbourhood of an edge, while the redundancy variables capture structural overlap among neighbouring nodes. Concrete constructions of such variables appear in the Network Potential Functional and in the generalised structural measures considered in later papers.

## 0.6 Relational Potentials

This section introduces the basic mathematical object studied throughout the paper. Relational potentials are scalar functionals defined on the space of admissible edge-weight configurations and interpreted variationally as measures of global structural value. The definitions introduced here provide the functional framework within which admissible relational potentials are characterised in subsequent sections.

### 0.6.1 Definition

Let $`G = (V,E)`$ be a finite undirected graph and let $`\Omega_{G} \subset \mathbb{R}^{\mid E \mid}`$ denote the admissible domain of edge weights defined in Section 0.5.

A relational potential on $`G`$ is a scalar functional

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

that assigns a real-valued structural potential to each weight configuration $`w \in \Omega_{G}`$.

Relational potentials are interpreted variationally: configurations of tie strengths are regarded as equilibrium states of a system governed by optimisation of the functional $`\Phi_{G}`$. Structural properties of weighted networks may therefore be analysed through the analytical and geometric properties of relational potentials and their equilibrium configurations.

### 0.6.2 Regularity Class

Throughout this paper relational potentials are assumed to admit a twice continuously differentiable extension to an open neighbourhood of the admissible weight domain.

Let

``` math
\Omega = \lbrack 0,1\rbrack^{m} \subset \mathbb{R}^{m}
```

denote the admissible weight domain defined in Section 0.5.2, where $`m = \mid E \mid`$. We assume that there exists an open set

``` math
U \subset \mathbb{R}^{m}
```

satisfying

``` math
\Omega \subset U,
```

such that the relational potential satisfies

``` math
\Phi_{G} \in C^{2}(U).
```

Consequently, the gradient field

``` math
F(w) = \nabla\Phi_{G}(w)
```

and the Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w)
```

exist and are continuous on $`U`$ and in particular on the admissible domain $`\Omega`$. The Hessian operator $`H(w)`$ is symmetric for all $`w \in U`$, since it is the second derivative of a scalar potential.

Admissible relational potentials therefore belong to the functional class

``` math
\Phi_{G} \in C^{2}(U),
```

where $`U \subset \mathbb{R}^{m}`$ is an open neighbourhood of the admissible domain.

**Domain Geometry**

The admissible domain $`\Omega`$ is a compact convex hyperrectangle in $`\mathbb{R}^{m}`$. In particular:

- $`\Omega`$ is convex,

- $`\Omega`$ is path-connected,

- $`\Omega`$ is compact.

The interior domain

``` math
\Omega^{\circ} = (0,1)^{m}
```

is open, connected, and simply connected as a subset of $`\mathbb{R}^{m}`$.

These geometric properties ensure that the integrability results established in Section 0.9.1 apply on open simply connected neighbourhoods of the admissible domain.

### 0.6.3 Equilibrium Configurations

Equilibrium configurations of relational potentials are characterised by first-order optimality conditions on the admissible domain.

A configuration $`w^{\text{\textbackslash*}} \in \Omega`$ is an equilibrium configuration if it maximises the relational potential over the admissible domain:

``` math
\Phi_{G}(w^{\text{\textbackslash*}}) \geq \Phi_{G}(w)\ for\ all\ w\  \in \Omega.\ 
```

Interior equilibria satisfy the stationarity condition

``` math
\nabla\Phi_{G}(w^{\text{\textbackslash*}}) = 0.
```

However, equilibrium configurations may occur on the boundary of $`\Omega`$, where one or more edge weights satisfy

``` math
w_{e}^{\text{\textbackslash*}} = 0orw_{e}^{\text{\textbackslash*}} = 1.
```

In such cases the appropriate first-order optimality condition is expressed as a variational inequality.

Higher-order structural properties of equilibrium configurations are determined by curvature properties of the relational potential. In particular, the notions of relational rigidity and structural stability introduced below characterise the behaviour of equilibria under perturbations.

### 0.6.4 Variational Inequality Formulation

A configuration $`w^{\text{\textbackslash*}} \in \Omega`$ is an equilibrium configuration if

``` math
\langle\nabla\Phi_{G}(w^{\text{\textbackslash*}}),\text{\:\,}v - w^{\text{\textbackslash*}}\rangle\  \leq 0\ for\ all\ v\  \in \Omega.\ 
```

Equivalently,

``` math
\nabla\Phi_{G}(w^{\text{\textbackslash*}}) \in N_{\Omega}(w^{\text{\textbackslash*}}),
```

where $`N_{\Omega}(w^{\text{\textbackslash*}})`$ denotes the normal cone to $`\Omega`$ at $`w^{\text{\textbackslash*}}`$.

For the hypercube domain

``` math
\Omega = \lbrack 0,1\rbrack^{m},
```

the normal-cone condition is equivalent to the componentwise conditions

``` math
\left\{ \begin{matrix}
\partial_{e}\Phi_{G}(w^{\text{\textbackslash*}}) = 0, & 0 < w_{e}^{\text{\textbackslash*}} < 1, \\
\partial_{e}\Phi_{G}(w^{\text{\textbackslash*}}) \leq 0, & w_{e}^{\text{\textbackslash*}} = 1, \\
\partial_{e}\Phi_{G}(w^{\text{\textbackslash*}}) \geq 0, & w_{e}^{\text{\textbackslash*}} = 0.
\end{matrix} \right.\ 
```

Thus, interior edges satisfy marginal balance conditions, while boundary edges satisfy sign-restricted marginal conditions.

If $`w^{\text{\textbackslash*}} \in \Omega^{\circ}`$, the normal cone reduces to

``` math
N_{\Omega}(w^{\text{\textbackslash*}}) = \{ 0\},
```

and the variational inequality reduces to the stationarity condition

``` math
\nabla\Phi_{G}(w^{\text{\textbackslash*}}) = 0.
```

The variational inequality formulation provides a unified characterisation of equilibrium configurations valid for both interior and boundary regimes. This formulation forms the foundation for the constrained optimisation theory developed in Paper II.

### 0.6.5 Structural Contributions

Relational potentials are interpreted as aggregations of local structural contributions associated with nodes and edges of the graph. The structural value assigned to a weight configuration reflects the combined effect of individual ties together with the structural relationships among neighbouring ties.

In admissible relational potentials, marginal structural contributions depend primarily on edge weights incident to individual nodes together with structural variables determined by the local neighbourhoods of those edges. These structural variables will include measures of structural separation and structural redundancy defined on neighbourhood subgraphs.

The precise form of local structural contributions will be characterised later as a consequence of the admissibility axioms and the representation results established in subsequent sections.

### 0.6.6 Structural Marginals

The marginal structural contribution of an edge $`e \in E`$ is defined by the partial derivative

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w).
```

The function $`F_{e}(w)`$ represents the marginal change in structural potential produced by an infinitesimal increase in the strength of edge $`e`$.

Equilibrium configurations satisfy the variational inequality conditions of Section 0.6.4. In particular, interior equilibria satisfy

``` math
F_{e}(w^{*})\  = \ 0\ for\ all\ e \in E.
```

Structural properties of equilibrium configurations are determined by the behaviour of the marginal functions $`F_{e}(w)`$ together with the curvature properties of the Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w).
```

In particular, negative definiteness of the Hessian operator characterises relational rigidity and determines stability properties of equilibrium configurations. The operator-theoretic interpretation of these curvature conditions is developed in Section 0.11.

### 

**Marginal Structural Field**

The marginal structural field is defined by

``` math
F(w) = \nabla\Phi_{G}(w),
```

where

``` math
F(w) = (F_{e}(w))_{e \in E}.
```

The marginal structural field will be treated as the primary object of axiomatic and representation-theoretic analysis in the subsequent sections.

Axioms A1–A6 impose structural conditions directly on the marginal field $`F(w)`$, while Section 0.9 establishes the integrability conditions under which admissible marginal fields correspond to admissible relational potentials.

The marginal representation therefore provides the central link between the axiomatic formulation and the variational structure of relational potentials.

### 0.6.7 Relational Rigidity and Structural Stability

The variational formulation allows equilibrium configurations to be characterised not only by first-order optimality conditions but also by curvature properties of the relational potential. These curvature properties determine the stability of equilibrium tie strengths under perturbations of structural parameters.

The following definitions formalise the notions of relational rigidity and structural stability used throughout the Network Potential Series.

**Definition 0.6.7.1 (Strict Equilibrium)**

A configuration $`w^{\star} \in \Omega`$ is a **strict equilibrium** of a relational potential $`\Phi_{G}`$ if there exists a neighbourhood $`U`$of $`w^{\star}`$ such that

``` math
\Phi_{G}(w^{\star}) > \Phi_{G}(w)\text{for all }w \in U \smallsetminus \{ w^{\star}\}.
```

A strict equilibrium is therefore an isolated local maximiser of the relational potential.

**Definition 0.6.7.2 (Relational Rigidity)**

Let $`w^{\star} \in \Omega^{\circ}`$ be an interior equilibrium satisfying

``` math
\nabla\Phi_{G}(w^{\star}) = 0.
```

The equilibrium $`w^{\star}`$ is said to be **relationally rigid** if the Hessian operator

``` math
H(w^{\star}) = D^{2}\Phi_{G}(w^{\star})
```

is **strictly negative definite**, i.e.

``` math
v^{\top}H(w^{\star})v < 0\text{for all }v \in \mathbb{R}^{m} \smallsetminus \{ 0\}.
```

Relational rigidity therefore requires strict negative definiteness of the curvature operator at equilibrium.

**Proposition 0.6.7.3 (Rigidity Implies Strict Equilibrium)**

If $`w^{\star} \in \Omega^{\circ}`$ is relationally rigid, then $`w^{\star}`$ is a strict equilibrium.

**Proof**

By Taylor expansion,

``` math
\Phi_{G}(w^{\star} + v) = \Phi_{G}(w^{\star}) + \frac{1}{2}v^{\top}H(w^{\star})v + o( \parallel v \parallel^{2}).
```

Since $`H(w^{\star}) \prec 0`$,

``` math
v^{\top}H(w^{\star})v\  < 0\ for\ all\ v\  \neq 0,\ 
```

so $`\Phi_{G}(w^{\star} + v) < \Phi_{G}(w^{\star})`$ for sufficiently small $`v \neq 0`$. Thus $`w^{\star}`$ is a strict local maximiser.

**Definition 0.6.7.4 (Structural Stability)**

Let $`\Phi_{G}(w,\theta)`$ be a family of admissible relational potentials depending smoothly on a parameter vector $`\theta \in \mathbb{R}^{k}`$.

An equilibrium $`w^{\star}`$ at parameter value $`\theta^{\star}`$ is **structurally stable** if there exist neighbourhoods $`U \subset \Omega`$ and $`V \subset \mathbb{R}^{k}`$ such that for every $`\theta \in V`$ there exists a unique equilibrium

``` math
w(\theta) \in U
```

depending continuously on $`\theta`$, with

``` math
w(\theta^{\star}) = w^{\star}.
```

**Proposition 0.6.7.5 (Rigidity Implies Structural Stability)**

Let $`w^{\star} \in \Omega^{\circ}`$ satisfy

``` math
\nabla\Phi_{G}(w^{\star},\theta^{\star}) = 0
```

and suppose

``` math
D^{2}\Phi_{G}(w^{\star},\theta^{\star})
```

is strictly negative definite.

Then $`w^{\star}`$ is structurally stable.

**Proof**

Define

``` math
F(w,\theta) = \nabla\Phi_{G}(w,\theta).
```

Then

``` math
F(w^{\star},\theta^{\star}) = 0,
```

and

``` math
D_{w}F(w^{\star},\theta^{\star}) = D^{2}\Phi_{G}(w^{\star},\theta^{\star}).
```

Since $`D^{2}\Phi_{G}(w^{\star},\theta^{\star})`$ is strictly negative definite, it is invertible.

The Implicit Function Theorem therefore yields neighbourhoods

``` math
U \subset \Omega^{\circ},V \subset \mathbb{R}^{k}
```

of $`w^{\star}`$ and $`\theta^{\star}`$ respectively, and a unique continuously differentiable function

``` math
w:V \rightarrow U
```

such that

``` math
F(w(\theta),\theta) = 0
```

for all $`\theta \in V`$, with

``` math
w(\theta^{\star}) = w^{\star}.
```

Thus, there exists a unique continuously differentiable equilibrium branch $`w(\theta)`$ defined for $`\theta`$ in a neighbourhood of $`\theta^{\star}`$, and therefore $`w^{\star}`$is structurally stable.

## 0.7 Axioms for Admissible Relational Potentials

Let $`G = (V,E)`$ be a finite undirected graph with $`\mid E \mid = m`$ , and let

``` math
\Omega_{G} = \lbrack 0,1\rbrack^{m}
```

denote the admissible weight domain. A weight configuration is denoted

``` math
w = (w_{e})_{e \in E}.
```

Let

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

be a twice continuously differentiable scalar functional.

The admissible class of relational potentials consists of functionals satisfying the axioms stated below. These axioms define the functional setting within which the structural and dynamical results of the Network Potential Series are formulated.

The axioms serve distinct roles within the theory. Axioms A1 and A6 determine the structural representation of marginal functions developed in Section 0.8. Axioms A3 and A4 determine qualitative behaviour of marginal structural components. Axiom A5 provides operator-theoretic control used in subsequent papers of the series. Axiom A2 imposes structural invariance but is not required for the representation theorems of Sections 0.8–0.9.

**Definition 0.7.1 (Admissible Relational Potential)**

A relational potential on $`G`$ is admissible if

``` math
\Phi_{G} \in C^{2}(U)
```

for some open set $`U \subset \mathbb{R}^{m}`$ satisfying

``` math
\Omega_{G} \subset U
```

and if $`\Phi_{G}`$ satisfies Axioms A1–A6 below.

**Axiom A1 — Locality**

Marginal structural contributions depend only on a finite neighbourhood of each edge.

For each edge $`e \in E`$ there exists a finite set

``` math
N(e) \subseteq E
```

with $`e \in N(e)`$ such that

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w) = F_{e}(w_{N(e)})
```

for some function

``` math
F_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R.}
```

The set $`N(e)`$ is called a **structural neighbourhood** of $`e`$.

Thus, marginal structural incentives depend only on edge weights in a bounded neighbourhood of $`e`$.

**Uniform Locality**

There exists an integer $`k \geq 1`$ such that

``` math
N(e) \subseteq \{ f \in E:d_{E}(e,f) \leq k\}
```

for all $`e \in E`$, where $`d_{E}`$ denotes edge-distance in the line graph of $`G`$.

Thus, structural dependence is uniformly local across the graph.

**Axiom A2 — Symmetry**

Relational potentials are invariant under graph automorphisms.

Let

``` math
\pi:V \rightarrow V
```

be a graph automorphism and let the induced permutation of edges be denoted

``` math
e \mapsto \pi(e).
```

For any weight configuration $`w \in \Omega_{G}`$ , define

``` math
w_{e}^{\pi} = w_{\pi(e)}.
```

Then

``` math
\Phi_{G}(w^{\pi}) = \Phi_{G}(w)
```

for all automorphisms $`\pi`$and all $`w \in \Omega_{G}`$.

This invariance condition ensures that structural value depends only on network topology and not on arbitrary labelling.

This condition is not required for the representation theory developed in Sections 0.8–0.9 but ensures structural invariance of admissible relational potentials.

**Consequence**

For structurally equivalent edges $`e`$and $`f`$,

``` math
F_{e} = F_{f}
```

after identification of coordinates under the automorphism.

Thus, marginal structural behaviour depends only on local structural type.

**Axiom A3 — Monotonicity**

Increasing tie strength does not decrease structural potential.

For every edge $`e \in E`$,

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w) \geq 0
```

for all

``` math
w \in \Omega_{G}.
```

Thus, tie strengthening never decreases structural value when other weights are fixed.

This condition determines the sign structure of structural components but is not required for the representation results of Sections 0.8–0.9.

**Axiom A4 — Diminishing Returns**

Marginal structural contributions decrease with tie strength.

For every edge $`e \in E`$,

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}^{2}}(w) < 0
```

for all

``` math
w \in \Omega_{G}^{\circ}.
```

Thus, marginal structural value is strictly decreasing in own-edge weight.

This condition ensures interior equilibria arise through marginal balance rather than boundary saturation and provides the curvature structure used in subsequent papers of the Network Potential Series.

**Axiom A5 — Controlled Structural Interaction**

Structural interactions between ties are local and uniformly bounded.

For all edges $`e,f \in E`$,

``` math
\mid \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \mid \leq C_{ef}
```

for all

``` math
w \in \Omega_{G},
```

where constants $`C_{ef} \geq 0`$ satisfy the following conditions.

**Local Support**

There exists an integer $`k \geq 1`$ such that

``` math
C_{ef} = 0\text{whenever}d_{E}(e,f) > k.
```

Thus, edges separated by more than $`k`$steps in the line graph of $`G`$ have no second-order interaction.

**Uniform Boundedness**

There exists a constant $`C > 0`$ such that

``` math
C_{ef} \leq C
```

for all edges $`e,f \in E`$.

Thus cross-partial interactions remain uniformly bounded throughout the admissible domain.

**Incident Diagonal Dominance**

In regimes where operator-theoretic stability is required, the Hessian operator is assumed to satisfy **incident diagonal dominance** on the interior domain.

For all $`w \in \Omega_{G}^{\circ}`$ and all edges $`e \in E`$,

``` math
- \frac{\partial^{2}\Phi_{G}}{\partial w_{e}^{2}}(w)\text{\:\,} \geq \text{\:\,}\sum_{\begin{array}{r}
f \in E \\
f \neq e
\end{array}}^{}{\mid \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \mid}.
```

This condition ensures that own-edge curvature dominates cross-partial interactions.

When strict inequality holds uniformly — i.e. there exists $`\alpha > 0`$ such that

``` math
- \frac{\partial^{2}\Phi_{G}}{\partial w_{e}^{2}}(w)\text{\:\,} \geq \text{\:\,}\alpha + \sum_{f \neq e}^{}{\mid \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \mid}
```

for all $`e \in E`$ and $`w \in \Omega_{G}^{\circ}`$ — the Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w)
```

is uniformly negative definite on the interior domain and therefore invertible.

**Structural Role**

The bounded interaction conditions above define the admissible class of relational potentials used throughout the Network Potential Series.

Local boundedness ensures that marginal structural incentives depend only on a finite structural neighbourhood, while incident diagonal dominance guarantees that structural curvature is governed primarily by own-edge effects rather than cross-partial interactions.

These properties ensure stability and well-posedness of the operator-theoretic framework developed in subsequent sections.

In particular, under strict incident diagonal dominance the susceptibility operator

``` math
H(w)^{- 1}
```

is well-defined at interior equilibria.

**Axiom A6 — Structural Sufficiency**

Marginal structural functions depend only on a finite system of structural coordinates.

For each edge $`e \in E`$, there exists a continuous mapping

``` math
T_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R}^{k}
```

such that the marginal structural function satisfies

``` math
F_{e}(w) = f_{e}(T_{e}(w))
```

for some continuous function

``` math
f_{e}:\mathbb{R}^{k} \rightarrow \mathbb{R.}
```

The structural coordinate map is assumed to take the form

``` math
T_{e}(w) = (w_{e},S_{e}(w),R_{e}(w)),
```

where:

- $`w_{e}`$is the intrinsic coordinate,

- $`S_{e}(w)`$is a separation coordinate,

- $`R_{e}(w)`$is a redundancy coordinate.

The structural coordinates depend only on weights in the structural neighbourhood $`N(e)`$.

This axiom provides the structural coordinate representation used in Section 0.8 and is essential for the representation results developed in Sections 0.8–0.9.

### 0.7.1 Locality

Marginal structural contributions are determined by local structural information.

For each edge $`e = (i,j) \in E`$ , the marginal structural function

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w)
```

depends only on the weights of edges in a neighbourhood of $`e`$. In particular, there exists a finite set

``` math
N(e) \subseteq E
```

with $`e \in N(e)`$ , consisting of edges incident to $`i`$ or $`j`$ together with edges participating in local structural configurations involving $`e`$, such that

``` math
F_{e}(w) = F_{e}(w_{N(e)})
```

for all $`w \in \Omega`$.

Thus, marginal structural incentives are determined by local neighbourhood structure rather than by distant parts of the graph.

The locality condition ensures that relational potentials describe structural interactions arising from bounded relational configurations and permits equilibrium architecture to be analysed through neighbourhood-based structural variables. In particular, the locality neighbourhood $`N(e)`$provides the domain on which the structural coordinate maps introduced in Axiom A6 are defined.

### 0.7.2 Symmetry

Relational potentials are invariant under relabelling of nodes.

Let

``` math
\pi:V \rightarrow V
```

be an automorphism of the graph $`G`$, inducing a permutation of edges $`e \mapsto \pi(e)`$. For any weight configuration $`w \in \Omega_{G}`$, define the permuted configuration $`w^{\pi}`$ by

``` math
w_{e}^{\pi} = w_{\pi(e)}.
```

An admissible relational potential satisfies

``` math
\Phi_{G}(w^{\pi}) = \Phi_{G}(w)
```

for all automorphisms $`\pi`$and all $`w \in \Omega_{G}.`$

This invariance condition ensures that structural value depends only on the topology of the weighted graph and not on arbitrary labelling of nodes or edges.

In particular, structurally equivalent edges have identical marginal structural functions after identification of neighbourhood coordinates under the automorphism.

### 0.7.3 Monotonicity

Increasing tie strengths does not decrease structural value.

For each edge $`e \in E`$,

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w) \geq 0
```

for all $`w \in \Omega_{G}.`$

Thus, increasing the strength of a tie never decreases structural potential when all other tie strengths are held fixed.

Monotonicity expresses the principle that additional relational investment cannot reduce structural value in isolation. Structural trade-offs arise through interaction effects among ties rather than through negative intrinsic contributions of individual ties.

### 0.7.4 Diminishing Returns

Individual ties exhibit diminishing marginal structural returns.

For each edge $`e \in E`$,

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}^{2}}(w) < 0
```

for all

``` math
w \in \Omega_{G}^{\circ}.
```

Thus, the marginal structural value of increasing a tie strength decreases as the tie becomes stronger.

The diminishing-return condition ensures that equilibrium tie strengths arise from balance between marginal structural incentives rather than from unbounded increases in individual tie strengths. This condition plays a central role in establishing interior equilibrium behaviour and stability properties.

### 0.7.5 Structural Interaction

Structural interactions between ties are controlled by bounded cross-partial effects.

For edges $`e,f \in E`$ with $`e \neq f`$, define the cross-partial derivatives

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w).
```

Admissible relational potentials satisfy bounded cross-partial interaction conditions of the form

``` math
\mid \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \mid \leq C_{ef}
```

for all $`w \in \Omega_{G}`$ , where the constants $`C_{ef} \geq 0`$ depend only on structural relationships between edges $`e`$and $`f`$.

Moreover, there exists an integer $`k \geq 1`$ such that

``` math
C_{ef} = 0wheneverd_{E}(e,f) > k,
```

where $`d_{E}`$ denotes edge-distance in the line graph of $`G`$.

Thus, structural interactions remain localised and arbitrarily strong long-range coupling between unrelated ties is excluded.

Controlled structural interaction guarantees that marginal structural signals arising from local structure are not dominated by distant structural effects and permits equilibrium architecture to be analysed through local curvature operators.

**Spectral Interpretation of Structural Interaction**

The cross-partial structure induced by admissible relational potentials defines an **interaction graph on edges**, in which two edges $`e`$and $`f`$are adjacent whenever

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \neq 0
```

for some $`w \in \Omega_{G}`$.

Under the locality assumptions above, this interaction graph coincides with a bounded-radius neighbourhood structure in the line graph of $`G`$. In particular, each edge interacts structurally with only finitely many neighbouring edges.

This locality structure provides a natural operator-theoretic interpretation of curvature. The Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w)
```

may be viewed as a weighted adjacency operator on the interaction graph, with diagonal entries representing own-edge curvature and off-diagonal entries representing structural interactions between neighbouring ties.

Under the incident diagonal dominance conditions introduced in Axiom A5, own-edge curvature dominates cross-edge interactions in the sense that

``` math
\mid H_{ee}(w) \mid > \sum_{f \neq e}^{} \mid H_{ef}(w) \mid 
```

for all edges $`e`$.

As shown in Section 0.11, this dominance condition provides a sufficient spectral criterion for negative definiteness of the Hessian operator,

``` math
H(w) \prec 0,
```

ensuring that interior equilibria are strict local maximisers and that the susceptibility operator $`H(w)^{- 1}`$ is well-defined.

Thus, the locality assumptions of admissible relational potentials induce a controlled interaction topology that supports rigorous operator-theoretic stability analysis.

### 0.7.6 Regularity

Admissible relational potentials satisfy the regularity conditions stated in Section 0.6.

In particular, relational potentials admit a twice continuously differentiable extension to an open neighbourhood $`U \subset \mathbb{R}^{m}`$ with

``` math
\Omega \subset U,
```

so that the gradient and Hessian operators

``` math
\nabla\Phi_{G}(w),D^{2}\Phi_{G}(w)
```

are well defined and continuous on the admissible weight domain $`\Omega`$.

These regularity conditions ensure that equilibrium configurations depend smoothly on structural parameters and permit analysis of stability, perturbation response, and dynamical behaviour through differential methods.

The regularity assumptions also provide the differentiability structure required for the representation theory developed in Section 0.9 and for the operator-theoretic analysis developed in subsequent papers of the Network Potential Series.

### 0.7.7 Structural Sufficiency

**Axiom A6 — Structural Sufficiency**

For each edge $`e \in E`$, the marginal structural function

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w)
```

depends only on a finite collection of local structural invariants determined by the structural neighbourhood $`N(e)`$.

More precisely, there exists a continuous structural coordinate map

``` math
T_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R}^{k}
```

such that

``` math
F_{e}(w) = f_{e}(T_{e}(w_{N(e)}))
```

for some continuous function $`f_{e}`$.

Thus, marginal structural functions admit a finite-dimensional coordinatisation in terms of local structural invariants determined by the structural neighbourhood $`N(e)`$.

This axiom formalises the principle that marginal structural incentives depend only on finitely many locally determined structural variables rather than on the full global weight configuration.

**Axiom A6′ — Additive Structural Separability**

Marginal structural functions are additively separable in structural coordinates.

For each edge $`e \in E`$ , there exist continuously differentiable functions

``` math
{C_{e}':\lbrack 0,1\rbrack \rightarrow \mathbb{R},
}{B_{e}':\mathbb{R} \rightarrow \mathbb{R},
}{D_{e}':\mathbb{R} \rightarrow \mathbb{R}
}
```

such that the marginal structural function admits the decomposition

``` math
F_{e}(w) = C_{e}'(w_{e}) + B_{e}'(S_{e}(w)) - D_{e}'(R_{e}(w)).
```

This assumption ensures that marginal structural incentives decompose into intrinsic, separation, and redundancy components independently.

Axiom A6′ provides the structural separability condition required for the marginal decomposition theorem of Section 0.8 and the canonical representation results of Section 0.9.

**Canonical Structural Coordinates**

In this paper a canonical three-coordinate normal form is used in which the structural coordinate map takes the form

``` math
T_{e}(w) = \left( w_{e},S_{e}(w),R_{e}(w) \right),
```

where the structural coordinate functions

``` math
S_{e}(w),R_{e}(w)
```

depend only on weights in the structural neighbourhood $`N(e)`$.

The coordinate $`w_{e}`$represents intrinsic tie strength, while the coordinates $`S_{e}(w)`$ and $`R_{e}(w)`$ represent structural characteristics associated with edge $`e`$, such as separation and redundancy exposure.

This three-coordinate representation serves as a canonical structural coordinate system for admissible marginal structural functions. Alternative finite coordinate systems compatible with Axiom A1 produce structurally equivalent relational potentials.

The specific forms of the functions $`S_{e}(w)`$and $`R_{e}(w)`$are not fixed by the axioms. Different constructions satisfying locality and symmetry conditions yield equivalent structural descriptions.

**Interpretation**

Axiom A6 formalises the requirement that marginal structural incentives depend on a finite collection of local structural invariants. This condition ensures that admissible marginal functions admit finite-dimensional coordinate representations compatible with the locality axiom.

Axiom A6′ strengthens this requirement by imposing additive separability of marginal structural incentives in structural coordinates. This separability condition permits marginal structural contributions to be decomposed into intrinsic, separation, and redundancy components and therefore enables the canonical structural representation established in Section 0.9.

The structural coordinate maps provide a reduced representation of marginal structural incentives that forms the basis for the marginal decomposition results of Section 0.8 and the representation theory developed in Section 0.9.

Section 0.8 establishes structural coordinate representations for admissible marginal functions, while Section 0.9 shows that admissible relational potentials admit canonical structural normal forms uniquely determined up to additive constants.

## 0.8 Structural Marginal Theory

This section develops a marginal representation theory for admissible relational potentials. The axioms introduced in Section 0.7 impose structural restrictions on marginal functions that allow marginal structural contributions to be expressed in terms of a finite system of local structural variables.

The central idea is that the marginal structural contribution of an edge depends on three distinct structural components:

- the intrinsic contribution of the tie itself,

- structural separation between its endpoints,

- structural redundancy in its neighbourhood.

<!-- -->

- 

These components arise naturally from the locality and symmetry axioms and provide a canonical coordinate system for marginal structural incentives.

### 0.8.1 Edgewise Marginals

Let $`G = (V,E)`$be a finite undirected graph and let

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

be an admissible relational potential satisfying the axioms of Section 0.7.

For each edge $`e \in E`$, define the marginal structural function

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w).
```

The value $`F_{e}(w)`$represents the marginal change in structural potential produced by an infinitesimal increase in the strength of edge $`e`$.

Local Dependence

By Axiom A1 (Locality), there exists a finite neighbourhood

``` math
N(e) \subseteq E
```

such that

``` math
F_{e}(w) = F_{e}(w_{N(e)})
```

for all $`w \in \Omega_{G}.`$

Thus, marginal structural contributions are determined entirely by the local structural environment of the edge.

**Symmetry**

By Axiom A2 (Symmetry), if edges $`e`$and $`f`$are equivalent under a graph automorphism, then their marginal functions coincide after identification of neighbourhood coordinates.

Thus, marginal functions depend only on the structural type of the local configuration.

Monotonicity and Curvature

By Axioms A3–A4,

``` math
F_{e}(w) \geq 0
```

and

``` math
\frac{\partial F_{e}}{\partial w_{e}}(w) < 0
```

for all $`w \in \Omega_{G}^{\circ}.`$

Thus, marginal structural contributions are nonnegative and strictly decreasing in own-edge weight.

**Role of Marginals**

The family of marginal functions

``` math
\left\{ F_{e}\}_{e \in E} \right.\ 
```

completely determines the relational potential up to an additive constant and therefore provides the natural objects for representation analysis.

### 0.8.2 Structural Coordinates

The locality condition established in Axiom A1 implies that marginal structural functions depend only on weights in a finite neighbourhood of each edge. In particular, for each edge $`e \in E`$,

``` math
F_{e}(w) = F_{e}(w_{N(e)}),
```

where $`N(e)`$is the structural neighbourhood of $`e`$.

Axiom A6 implies that marginal structural functions depend only on a finite set of structural invariants determined by the neighbourhood $`N(e)`$. Consequently, for each edge $`e \in E`$there exists a finite-dimensional coordinate map

``` math
T_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R}^{k}
```

and a continuous function $`f_{e}`$such that

``` math
F_{e}(w) = f_{e}(T_{e}(w)).
```

Specifically, for each edge $`e = (i,j)`$ , there exists a structural coordinate map

``` math
T_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R}^{k}
```

such that

``` math
F_{e}(w) = f_{e}(T_{e}(w))
```

for some continuous function $`f_{e}`$.

A convenient structural coordinate system may be chosen of the form

``` math
T_{e}(w) = (w_{e},S_{e}(w),R_{e}(w)),
```

consisting of intrinsic, separation, and redundancy variables.

These coordinates provide a local structural description of the neighbourhood environment of edge $`e`$.

**Intrinsic Coordinate**

The intrinsic coordinate is simply the edge weight

``` math
w_{e}.
```

This variable measures the direct strength of the tie and determines the intrinsic marginal structural contribution governed by the diminishing-return axiom.

**Separation Coordinate**

The separation coordinate

``` math
S_{e}(w)
```

measures the structural separation between endpoints $`i`$and $`j`$through alternative paths in the network.

Formally, $`S_{e}(w)`$ is any continuous function satisfying:

**Local dependence**

``` math
S_{e}(w) = S_{e}(w_{N(e)})
```

**Automorphism invariance**

``` math
S_{\pi(e)}(w^{\pi}) = S_{e}(w)
```

**Monotonicity under alternative connectivity**

Increasing weights of alternative paths between $`i`$and $`j`$does not increase $`S_{e}(w)`$.

Thus, larger values of $`S_{e}(w)`$correspond to greater structural separation and therefore greater brokerage exposure.

Typical constructions of $`S_{e}(w)`$ include functions of weighted alternative paths between $`i`$and $`j`$within the neighbourhood $`N(e)`$. For example, $`S_{e}(w)`$ may be defined in terms of weighted path lengths or effective resistance-type quantities computed on bounded neighbourhood subgraphs.

**Redundancy Coordinate**

The redundancy coordinate

``` math
R_{e}(w)
```

measures the extent to which endpoints $`i`$and $`j`$are connected through alternative short paths.

Formally, $`R_{e}(w)`$is any continuous function satisfying:

**Local dependence**

``` math
R_{e}(w) = R_{e}(w_{N(e)})
```

**Automorphism invariance**

``` math
R_{\pi(e)}(w^{\pi}) = R_{e}(w)
```

**Monotonicity under closure**

Increasing weights of alternative short paths between $`i`$and $`j`$does not decrease $`R_{e}(w)`$.

Thus, larger values of $`R_{e}(w)`$ correspond to greater structural redundancy.

Typical constructions of $`R_{e}(w)`$ include weighted counts of triangles and short cycles containing edge $`e`$, or other measures of local closure computed on neighbourhood subgraphs.

**Structural Coordinate Representation**

The variables

``` math
\left( w_{e},S_{e}(w),R_{e}(w) \right)
```

provide a system of local structural coordinates describing the neighbourhood environment of edge $`e`$.

Different choices of separation and redundancy coordinates satisfying the conditions above produce structurally equivalent relational potentials. The canonical coordinate system therefore represents a normal form rather than a unique structural parametrisation.

By Axiom A6, marginal structural incentives admit a representation in terms of these structural coordinates. These coordinates therefore provide a reduced structural description of marginal structural behaviour that serves as the basis for the representation results developed in Section 0.9.

### 0.8.3 Structural Coordinate Representation

The admissibility axioms imply that marginal structural functions admit a representation in terms of structural coordinates. In particular, marginal structural incentives depend only on intrinsic tie strength together with structural separation and redundancy variables defined on local neighbourhoods.

**Theorem 0.8.1 (Structural Coordinate Representation)**

Let $`\Phi_{G}`$ be an admissible relational potential satisfying the axioms of Section 0.7. Then for each edge $`e \in E`$ there exists a continuous function

``` math
H_{e}:\lbrack 0,1\rbrack \times \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}
```

such that

``` math
F_{e}(w) = H_{e}(w_{e},S_{e}(w),R_{e}(w))
```

for all $`w \in \Omega`$.

**Proof**

By Axiom A1 (Locality), for each edge $`e \in E`$there exists a finite structural neighbourhood $`N(e) \subseteq E`$ such that

``` math
F_{e}(w) = F_{e}(w_{N(e)})
```

for all $`w \in \Omega`$. Thus, the marginal structural function depends only on the finite-dimensional vector

``` math
w_{N(e)} \in \lbrack 0,1\rbrack^{\mid N(e) \mid}.
```

By Axiom A6 (Structural Sufficiency), there exists a continuous structural coordinate map

``` math
T_{e}:\lbrack 0,1\rbrack^{\mid N(e) \mid} \rightarrow \mathbb{R}^{k}
```

and a continuous function

``` math
f_{e}:T_{e}(\lbrack 0,1\rbrack^{\mid N(e) \mid}) \rightarrow \mathbb{R}
```

such that

``` math
F_{e}(w) = f_{e}(T_{e}(w_{N(e)})).
```

Choosing admissible structural invariants

``` math
T_{e}(w_{N(e)}) = (w_{e},S_{e}(w),R_{e}(w))
```

yields a coordinate representation of the marginal function. Defining

``` math
H_{e}(x,s,r) = f_{e}(x,s,r),
```

we obtain

``` math
F_{e}(w) = H_{e}(w_{e},S_{e}(w),R_{e}(w)).
```

where the structural variables $`S_{e}(w)`$ and $`R_{e}(w)`$ depend only on weights in the structural neighbourhood $`N(e)`$.

Defining

``` math
H_{e}(x,s,r) = f_{e}(x,s,r),
```

we obtain

``` math
F_{e}(w) = H_{e}(w_{e},S_{e}(w),R_{e}(w)),
```

establishing the structural coordinate representation.

### 0.8.4 Structural Marginal Decomposition

The structural coordinate representation yields a canonical decomposition of marginal structural contributions into intrinsic, separation, and redundancy components.

**Theorem 0.8.2 (Structural Marginal Decomposition)**

Let $`\Phi_{G}`$ be an admissible relational potential satisfying the axioms of Section 0.7.

Then for each edge $`e \in E`$, the marginal structural function admits a decomposition

``` math
F_{e}(w) = C_{e}'(w_{e}) + B_{e}'(S_{e}(w)) - D_{e}'(R_{e}(w)),
```

where

``` math
C_{e}:\lbrack 0,1\rbrack \rightarrow \mathbb{R},B_{e}:\mathbb{R} \rightarrow \mathbb{R},D_{e}:\mathbb{R} \rightarrow \mathbb{R}
```

are continuously differentiable functions satisfying

``` math
{C_{e}'(w_{e}) > 0,C_{e}^{''}(w_{e}) < 0,
}{B_{e}'(S) \geq 0,D_{e}'(R) \geq 0.
}
```

**Proof**

By Theorem 0.8.1, the marginal structural function admits a structural coordinate representation

``` math
F_{e}(w) = H_{e}(w_{e},S_{e}(w),R_{e}(w)),
```

for a continuously differentiable function $`H_{e}`$.

Let

``` math
x = w_{e},s = S_{e}(w),r = R_{e}(w).
```

By Axiom A6′ (Additive Structural Separability), the coordinate form satisfies

``` math
\frac{\partial^{2}H_{e}}{\partial x\partial s} = \frac{\partial^{2}H_{e}}{\partial x\partial r} = \frac{\partial^{2}H_{e}}{\partial s\partial r} = 0
```

on the interior domain.

Therefore:

``` math
\frac{\partial H_{e}}{\partial x}
```

depends only on $`x`$,

``` math
\frac{\partial H_{e}}{\partial s}
```

depends only on $`s`$,

and

``` math
\frac{\partial H_{e}}{\partial r}
```

depends only on $`r`$.

Integrating along coordinate directions yields functions

``` math
C_{e}'(x),B_{e}'(s),D_{e}'(r)
```

such that

``` math
H_{e}(x,s,r) = C_{e}'(x) + B_{e}'(s) - D_{e}'(r).
```

Thus

``` math
F_{e}(w) = C_{e}'\left( w_{e} \right) + B_{e}'\left( S_{e}(w) \right) - D_{e}'\left( R_{e}(w) \right).
```

``` math
```

**Interpretation**

The three components correspond to the fundamental structural mechanisms governing marginal structural value.

**Cohesion Component**

``` math
C_{e}'(w_{e})
```

represents the intrinsic structural contribution of the tie.

The diminishing-return axiom implies that

``` math
C_{e}^{''}(w_{e}) < 0.
```

This component governs stabilisation of strong ties.

**Brokerage Component**

``` math
B_{e}'(S_{e}(w))
```

represents the structural contribution arising from separation between endpoints.

Edges connecting otherwise weakly connected regions have larger separation values and therefore larger brokerage contributions.

**Redundancy Component**

``` math
D_{e}'(R_{e}(w))
```

represents structural redundancy.

Redundant alternative paths reduce marginal structural value.

**Significance**

The structural marginal decomposition provides a canonical representation of marginal structural incentives under the admissibility axioms.

Together with the integrability results of Section 0.9, this marginal representation yields the canonical structural decomposition of admissible relational potentials.

## 0.9 Representation Theory

This section establishes representation results for admissible relational potentials. Building on the marginal structural representation developed in Section 0.8 and the admissibility axioms of Section 0.7, we characterise the global form of relational potentials satisfying the structural requirements of the admissible class.

The central objects of the representation theory are the marginal structural fields

``` math
F(w) = \nabla\Phi_{G}(w),
```

which satisfy the locality and structural sufficiency conditions of Axioms A1–A6. The admissibility axioms therefore impose structural restrictions directly on the marginal field, while the regularity assumptions of Section 0.6 ensure that admissible marginal fields are continuously differentiable on an open neighbourhood of the admissible domain.

The results of this section establish that admissible marginal structural fields satisfying the compatibility conditions of Section 0.9.1 correspond uniquely (up to additive constants) to admissible relational potentials. Representation theorems therefore characterise the class of scalar functionals generated by admissible marginal structural fields.

In particular:

- Section 0.9.1 establishes integrability conditions under which admissible marginal structural fields correspond to relational potentials.

- Section 0.9.2 establishes local structural representations implied by the admissibility axioms.

- Section 0.9.3 establishes canonical normal forms within structural equivalence classes.

These results show that admissible relational potentials admit representations in terms of local structural variables associated with nodes and their neighbourhoods.

Representation results therefore identify canonical representatives of structural equivalence classes rather than particular analytic coordinate expressions.

### 0.9.0 Structural Equivalence

The representation results developed in this section are formulated in a coordinate-independent manner through an equivalence relation on admissible relational potentials. The admissibility axioms introduced earlier define a class of scalar functionals on the edge-weight domain

``` math
\Omega_{G} \subset \mathbb{R}^{\mid E \mid},
```

but structural properties of relational potentials depend only on marginal structural incentives and their local variation rather than on a particular analytic representation.

The structural investigations developed in subsequent papers of this series rely on geometric properties of relational potentials determined by their gradient and curvature operators. In particular, equilibrium configurations, local stability properties, and perturbation responses depend only on marginal structural functions and their derivatives. Relational potentials that generate identical marginal structural incentives therefore represent the same underlying relational architecture and should be regarded as equivalent descriptions of the same variational system.

These considerations motivate the introduction of structural equivalence on the admissible class of relational potentials.

### Definition 0.9.0 (Structural Equivalence)

Let $`G = (V,E)`$ be a finite undirected graph and let

``` math
\Phi_{1},\Phi_{2}:U \rightarrow \mathbb{R}
```

be admissible relational potentials defined on an open neighbourhood

``` math
U \subset \mathbb{R}^{\mid E \mid}
```

containing the admissible domain $`\Omega_{G}`$.

The functionals $`\Phi_{1}`$ and $`\Phi_{2}`$ are said to be **structurally equivalent**, written

``` math
\Phi_{1} \approx \Phi_{2},
```

if

``` math
\nabla\Phi_{1}(w) = \nabla\Phi_{2}(w)\text{for all }w \in U.
```

Structural equivalence therefore identifies relational potentials that generate identical marginal structural incentive fields.

For an admissible relational potential $`\Phi`$ , the corresponding structural equivalence class is denoted

``` math
\lbrack\Phi\rbrack = \{\Psi:\Psi \approx \Phi\}.
```

**Remark 0.9.0 (Structural Observables)**

Structurally equivalent relational potentials possess identical:

- stationary point sets,

- first-order optimality conditions,

- local stability properties,

- Hessian operators,

- susceptibility mappings where defined.

These quantities constitute the **operator-theoretic observables** of relational potentials and form the basis of the structural investigations developed in subsequent papers.

In particular, all structural results derived in the Network Potential Series depend only on the structural equivalence class $`\lbrack\Phi\rbrack`$rather than on a specific analytic representation of a relational potential.

**Proposition 0.9.0 (Characterisation of Structural Equivalence)**

Let $`\Phi_{1}`$ and $`\Phi_{2}`$ be admissible relational potentials defined on a connected admissible domain $`\Omega_{G}`$.

If

``` math
\Phi_{1} \approx \Phi_{2},
```

then there exists a constant $`C \in \mathbb{R}`$such that

``` math
\Phi_{1}(w) = \Phi_{2}(w) + C
```

for all $`w \in \Omega_{G}`$.

Proof

If

``` math
\nabla\Phi_{1}(w) = \nabla\Phi_{2}(w)
```

for all $`w \in \Omega_{G}`$, then

``` math
\nabla(\Phi_{1} - \Phi_{2})(w) = 0.
```

Since $`\Omega_{G}`$is convex and therefore path-connected, it follows that

``` math
\Phi_{1} - \Phi_{2} = C
```

for some constant $`C`$.

Thus, structurally equivalent relational potentials differ only by an additive constant. Structural equivalence classes therefore coincide precisely with **additive gauge classes** of admissible relational potentials.

Structural Equivalence Classes

Structural equivalence defines an equivalence relation on the class of admissible relational potentials.

For an admissible relational potential $`\Phi`$, we denote the corresponding equivalence class by

``` math
\lbrack\Phi\rbrack = \{\Psi:\Psi \approx \Phi\}.
```

The admissible class therefore decomposes into structural equivalence classes, each representing a single relational variational system independently of analytic representation.

Within each structural equivalence class, all relational potentials possess identical marginal structural functions and identical curvature operators. Consequently, equilibrium configurations, stability properties, and perturbation responses are invariants of the equivalence class.

Subsequent representation results identify canonical representatives of these equivalence classes.

### 0.9.1 Integrability Conditions

Marginal structural functions determine relational potentials through integration. In order for a family of marginal functions

``` math
F(w) = (F_{e}(w))_{e \in E}
```

to arise as the gradient of a scalar functional,

``` math
F(w) = \nabla\Phi_{G}(w),
```

the marginal functions must satisfy compatibility conditions ensuring equality of mixed partial derivatives.

Throughout this subsection we assume that the marginal field $`F`$ is defined on an open set

``` math
U \subset \mathbb{R}^{m}
```

containing the admissible domain

``` math
\Omega = \lbrack 0,1\rbrack^{m},
```

and that

``` math
F \in C^{1}(U).
```

We further assume that $`U`$ is open and simply connected. These assumptions ensure that the Poincaré Lemma applies to the marginal structural field.

**Compatibility Condition**

For all edges $`e,f \in E`$,

``` math
\frac{\partial F_{e}}{\partial w_{f}}(w) = \frac{\partial F_{f}}{\partial w_{e}}(w)\text{for all }w \in U.
```

These conditions ensure that the Jacobian matrix of $`F`$ is symmetric.

**Lemma 0.9.1 (Exactness of Closed Marginal 1-Forms)**

The integrability result below depends only on the regularity assumptions of Section 0.6 together with the compatibility conditions stated above. In combination with the locality and structural sufficiency axioms, this establishes the existence of admissible relational potentials corresponding to admissible marginal structural fields.

Let $`U \subset \mathbb{R}^{m}`$ be an open simply connected set and let

``` math
F:U \rightarrow \mathbb{R}^{m}
```

be a continuously differentiable vector field satisfying

``` math
\partial_{f}F_{e}(w) = \partial_{e}F_{f}(w)\text{for all }e,f \in E\text{ and all }w \in U.
```

Define the differential 1-form

``` math
\omega = \sum_{e \in E}^{}F_{e}(w)\text{ }dw_{e}.
```

Then $`\omega`$ is closed,

``` math
d\omega = 0,
```

and therefore exact. Consequently, there exists a twice continuously differentiable scalar function

``` math
\Phi_{G}:U \rightarrow \mathbb{R}
```

such that

``` math
F(w) = \nabla\Phi_{G}(w).
```

Moreover, $`\Phi_{G}`$ is unique up to an additive constant.

**Proof**

The compatibility conditions imply

``` math
\partial_{f}F_{e} = \partial_{e}F_{f},
```

which is equivalent to the closedness condition

``` math
d\omega = 0.
```

Since $`U`$is open and simply connected, the Poincaré Lemma implies that every closed 1-form on $`U`$is exact. Therefore, there exists a scalar function $`\Phi_{G}`$ such that

``` math
\omega = d\Phi_{G}.
```

Equating coefficients gives

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}} = F_{e}(w),
```

so

``` math
F(w) = \nabla\Phi_{G}(w).
```

If another potential $`\Psi_{G}`$ satisfies

``` math
\nabla\Psi_{G} = F,
```

then

``` math
\nabla(\Psi_{G} - \Phi_{G}) = 0,
```

so $`\Psi_{G} - \Phi_{G}`$ is constant on $`U`$.

**Structural Equivalence and Gauge Freedom**

The potential determined by a marginal field is unique only up to an additive constant. This freedom corresponds to a natural gauge normalisation for relational potentials.

Fixing a reference configuration $`w^{0} \in U`$ and imposing

``` math
\Phi_{G}(w^{0}) = 0
```

selects a unique representative within the equivalence class of structurally identical potentials.

**Consequence for Admissible Potentials**

Admissible relational potentials satisfy the regularity assumptions of Section 0.6. In particular,

``` math
\Phi_{G} \in C^{2}(U),
```

so, the marginal field

``` math
F(w) = \nabla\Phi_{G}(w)
```

automatically satisfies the compatibility conditions.

Conversely, Lemma 0.9.1 shows that any admissible marginal structural field satisfying the compatibility conditions determines a relational potential uniquely up to an additive constant.

Thus, admissible relational potentials are in one-to-one correspondence with admissible marginal structural functions up to additive constants.

### 0.9.2 Representation Theorem

The admissibility axioms imply that relational potentials admit representations in terms of local structural variables. In particular, admissible relational potentials are determined by marginal structural functions that depend only on local structural environments. Integration of admissible marginal functions therefore yields scalar functionals admitting local structural coordinate representations.

The following theorem characterises the global form of admissible relational potentials.

**Theorem 0.9.1 (Local Structural Representation)**

Let $`G = (V,E)`$ be a finite undirected graph and let

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

be an admissible relational potential.

Then there exist functions

``` math
U_{i}:\lbrack 0,1\rbrack^{\deg(i)} \times \mathbb{R}^{p_{i}} \times \mathbb{R}^{q_{i}} \rightarrow \mathbb{R}
```

such that

``` math
\Phi_{G}(w) = \sum_{i \in V}^{}U_{i}(w_{i*},S_{i}(w),R_{i}(w)),
```

where

``` math
w_{i*} = (w_{e})_{e \in \delta(i)}
```

is the vector of incident edge weights,

``` math
S_{i}(w)
```

denotes a collection of separation variables defined on the neighbourhood of node $`i`$,

``` math
R_{i}(w)
```

denotes a collection of redundancy variables defined on the neighbourhood of node $`i`$.

Moreover, the marginal structural field

``` math
\nabla\Phi_{G}(w)
```

uniquely determines the structural equivalence class $`\left\lbrack \Phi_{G} \right\rbrack`$ , and any two analytic representations of the above form correspond to structurally equivalent relational potentials.

**Proof**

By Theorem 0.8.1 the marginal structural functions of an admissible relational potential admit the representation

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w) = H_{e}(w_{e},S_{e}(w),R_{e}(w)).
```

By Axiom A1 (Locality), each marginal function depends only on weights in a finite neighbourhood $`N(e)`$.

By Proposition 0.9.1 (Integrability), the marginal field

``` math
F(w) = \nabla\Phi_{G}(w)
```

determines a scalar functional uniquely up to an additive constant.

Fix the reference point $`0 \in \Omega`$. For $`w \in \Omega`$, define

``` math
\Phi_{G}(w) = \int_{0}^{1}{\sum_{e \in E}^{}F_{e}}(tw)w_{e}\text{ }dt.
```

Differentiation yields

``` math
\nabla\Phi_{G}(w) = F(w),
```

so this construction reproduces the relational potential up to an additive constant.

Because each marginal function depends only on weights in a neighbourhood of the corresponding edge, each integrand term

``` math
F_{e}(tw)w_{e}
```

depends only on weights in that neighbourhood.

Grouping edge contributions by incident nodes yields a representation of the form

``` math
\Phi_{G}(w) = \sum_{i \in V}^{}U_{i}(w_{i*},S_{i}(w),R_{i}(w)).
```

Uniqueness up to additive constants follows from Proposition 0.9.0.

**Interpretation**

The representation theorem establishes that admissible relational potentials admit local structural coordinate representations determined by neighbourhood structure in the underlying graph.

Structural value at a node depends only on:

- incident tie strengths,

- separation variables,

- redundancy variables.

This representation formalises the locality principle and provides the structural basis for equilibrium analysis in subsequent papers.

In particular, admissible relational potentials form a class of local variational functionals on weighted graphs whose structural properties depend only on marginal structural fields and their derivatives.

### 0.9.3 Canonical Form

Among admissible representations, a canonical form may be obtained by separating intrinsic tie contributions from structural interaction terms. The structural equivalence relation introduced in Section 0.9.0 identifies relational potentials that generate identical marginal structural incentives and therefore represent the same relational variational system.

Accordingly, the admissible class of relational potentials decomposes into structural equivalence classes

``` math
\lbrack\Phi_{G}\rbrack = \{\Psi_{G}:\Psi_{G} \approx \Phi_{G}\},
```

each corresponding to a single relational variational system independently of analytic representation.

Since structurally equivalent relational potentials differ only by additive constants (Proposition 0.9.0), selecting a canonical representative amounts to fixing an additive gauge within the equivalence class.

The canonical representative is defined by the normalisation condition

``` math
{\widehat{\Phi}}_{G}(0) = 0.
```

In addition, the decomposition into structural components is fixed by the anchoring conditions

``` math
B_{e}(0) = 0,D_{e}(0) = 0.
```

These conditions eliminate additive ambiguity between structural components and ensure identifiability of the canonical decomposition.

The canonical normal form established below combines:

- the structural marginal decomposition of Section 0.8,

- the integrability conditions of Section 0.9.1, and

- the structural equivalence relations of Section 0.9.2.

Together these results show that admissible relational potentials admit canonical structural representations.

**Theorem 0.9.2 (Canonical Normal Form)**

Let $`G = (V,E)`$ be a finite undirected graph and let

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

be an admissible relational potential.

Then the structural equivalence class $`\left\lbrack \Phi_{G} \right\rbrack`$ contains a unique representative $`{\widehat{\Phi}}_{G}`$ satisfying

``` math
{\widehat{\Phi}}_{G}(0) = 0
```

that admits the decomposition

``` math
{\widehat{\Phi}}_{G}(w) = \sum_{e \in E}^{}C_{e}(w_{e}) + \sum_{e \in E}^{}B_{e}(S_{e}(w)) - \sum_{e \in E}^{}D_{e}(R_{e}(w)),
```

where

``` math
C_{e}:\lbrack 0,1\rbrack \rightarrow \mathbb{R}
```

are intrinsic cohesion functions,

``` math
B_{e}:\mathbb{R} \rightarrow \mathbb{R}
```

are separation functions,

``` math
D_{e}:\mathbb{R} \rightarrow \mathbb{R}
```

are redundancy functions,

and

``` math
{C_{e}'(w_{e}) > 0,C_{e}^{''}(w_{e}) < 0,
}{B_{e}'(S) \geq 0,D_{e}'(R) \geq 0,
}
```

together with the anchoring conditions

``` math
B_{e}(0) = 0,D_{e}(0) = 0.
```

**Proof**

By Axioms A1–A6 and the structural marginal decomposition theorem (Theorem 0.8.2), the marginal structural field of an admissible relational potential admits the representation

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w) = C_{e}'(w_{e}) + B_{e}'(S_{e}(w)) - D_{e}'(R_{e}(w)),
```

where the structural coordinate functions $`S_{e}(w)`$ and $`R_{e}(w)`$ depend only on weights in the structural neighbourhood $`N(e)`$.

By Lemma 0.9.1, any continuously differentiable marginal field satisfying the compatibility conditions determines a scalar potential uniquely up to an additive constant on the open simply connected neighbourhood $`U`$.

Let $`w^{0} = 0`$ be the reference configuration. Define

``` math
{\widehat{\Phi}}_{G}(w) = \int_{0}^{1}{\sum_{e \in E}^{}\left\lbrack C_{e}'(tw_{e}) + B_{e}'(S_{e}(tw)) - D_{e}'(R_{e}(tw)) \right\rbrack}w_{e}\text{ }dt.
```

Differentiation with respect to $`w_{e}`$ yields

``` math
\frac{\partial{\widehat{\Phi}}_{G}}{\partial w_{e}}(w) = C_{e}'(w_{e}) + B_{e}'(S_{e}(w)) - D_{e}'(R_{e}(w)),
```

so, this construction produces a structurally equivalent relational potential.

The normalisation condition

``` math
{\widehat{\Phi}}_{G}(0) = 0
```

removes the additive gauge freedom and uniquely determines the additive constant.

The anchoring conditions

``` math
B_{e}(0) = 0,D_{e}(0) = 0
```

remove additive ambiguity between structural components and ensure identifiability of the canonical decomposition.

Uniqueness then follows from Proposition 0.9.0, since structurally equivalent relational potentials differ only by additive constants.

**Remark 0.9.3 (Structural Interpretation)**

The canonical normal form separates three distinct structural components:

- intrinsic tie value determined by the functions $`C_{e}`$,

- structural opportunity determined by the functions $`B_{e}`$,

- structural overlap determined by the functions $`D_{e}`$.

These components correspond respectively to cohesion, mobility, and redundancy structural principles.

The canonical decomposition therefore separates intrinsic tie effects from structural interaction effects in a uniquely determined manner.

**Corollary 0.9.1 (Canonical Representative)**

For every admissible relational potential $`\Phi_{G}`$ , there exists a unique normalised representative

``` math
{\widehat{\Phi}}_{G} \in \lbrack\Phi_{G}\rbrack
```

admitting the canonical normal form.

**Corollary 0.9.2 (Structural Invariance)**

Let $`\Phi_{G}`$ be an admissible relational potential and let $`{\widehat{\Phi}}_{G}`$ denote its canonical representative.

Then:

- stationary point sets coincide,

- first-order optimality conditions coincide,

- Hessian operators coincide,

- susceptibility mappings coincide where defined.

Accordingly, structural results derived for $`{\widehat{\Phi}}_{G}`$ depend only on the structural equivalence class $`\left\lbrack \Phi_{G} \right\rbrack`$.

In particular, all operator-theoretic results developed in subsequent papers depend only on the marginal structural field and its derivatives and are therefore invariants of the equivalence class.

**Remark 0.9.4 (Relation to the Network Potential Functional)**

The Network Potential Functional introduced in Mack (2026) provides a concrete realisation of the canonical normal form in which:

- cohesion corresponds to logarithmic intrinsic functions $`C_{e}`$,

- mobility corresponds to brokerage-weighted separation functions $`B_{e}`$,

- redundancy corresponds to quadratic overlap penalties $`D_{e}`$.

The Network Potential Functional therefore constitutes a specific admissible relational potential expressed in canonical structural coordinates.

## 0.10 The Network Potential Functional

This section presents the Network Potential Functional as a concrete example of an admissible relational potential. The functional introduced in Mack (2026) serves as a motivating instance for the axiomatic framework developed in this paper and provides an explicit realisation of the canonical structural representation established in Section 0.9.

The Network Potential Functional integrates three structural principles:

- **cohesion**, representing stabilising effects of strong ties,

- **mobility**, representing structural separation between nodes,

- **redundancy**, representing local closure and alternative connectivity.

Together these components define a scalar potential on the space of admissible edge weights,

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R},
```

whose equilibria determine structural architecture in weighted networks.

The Network Potential Functional satisfies the admissibility axioms of Section 0.7 and therefore belongs to the admissible class characterised by the representation results of Section 0.9. In particular, the functional admits a canonical structural decomposition of the form established in Theorem 0.9.2 and therefore represents a canonical example of an admissible relational potential.

Within the structural equivalence framework of Section 0.9.0, the Network Potential Functional represents a particular analytic representative of its structural equivalence class. All structural properties of the functional depend only on its marginal structural field and curvature operators and are therefore invariant under additive gauge transformations.

The curvature operators associated with the Network Potential Functional provide the operator-theoretic objects analysed in subsequent papers of the Network Potential Series. In particular, equilibrium structure is determined by the Hessian operator and its local restrictions, while perturbation responses are governed by the associated susceptibility kernel introduced in Section 0.11.

### 0.10.1 Definition

Let $`G = (V,E)`$ be a finite undirected graph and let

``` math
\Omega_{G} = \lbrack 0,1\rbrack^{\mid E \mid}
```

denote the admissible domain of edge weights.

For each node $`i \in V`$, define the node potential

``` math
U_{i}(w) = \alpha\sum_{e \in \delta(i)}^{}{log(1 +}w_{e}) + \beta\text{ }M_{i}(w) - \gamma\text{ }T_{i}(w),
```

where:

- $`\delta(i)`$ denotes the set of edges incident to node $`i`$,

- $`M_{i}(w)`$ denotes a mobility (separation) measure associated with node $`i`$,

- $`T_{i}(w)`$ denotes a redundancy measure associated with node $`i`$,

- $`\alpha,\beta,\gamma > 0`$ are structural parameters.

The **Network Potential Functional** is defined by

``` math
\Phi_{G}(w) = \sum_{i \in V}^{}U_{i}(w).
```

The first term represents cohesion contributions arising from individual tie strengths. The second term represents structural mobility associated with nonredundant connectivity. The third term represents structural redundancy associated with alternative local paths.

This functional defines a scalar potential on the admissible weight domain whose stationary points determine equilibrium network architectures.

### 0.10.2 Verification of Axioms

The Network Potential Functional satisfies the admissibility axioms introduced in Section 0.7.

**Locality**

Marginal structural contributions depend only on local structural variables.

For each edge $`e = (i,j)`$ , the marginal function

``` math
F_{e}(w) = \frac{\partial\Phi_{G}}{\partial w_{e}}(w)
```

depends only on:

- the weight $`w_{e}`$,

- weights of edges incident to $`i`$ and $`j`$,

- local structural configurations involving nodes $`i`$ and $`j`$.

Thus, marginal functions depend only on neighbourhood edge weights, satisfying the locality axiom.

**Symmetry**

The Network Potential Functional is invariant under graph automorphisms.

Node potentials depend only on structural relationships among nodes and edge weights. Under any graph automorphism $`\pi`$,

``` math
\Phi_{G}(w^{\pi}) = \Phi_{G}(w).
```

Thus, the symmetry axiom is satisfied.

**Monotonicity**

Marginal structural contributions are nonnegative.

The cohesion term satisfies

``` math
\frac{\partial}{\partial w_{e}}log(1 + w_{e}) = \frac{1}{1 + w_{e}} > 0.
```

Mobility contributions are nondecreasing in tie strength, while redundancy contributions reduce marginal returns only through interaction effects with neighbouring ties.

Consequently

``` math
\frac{\partial\Phi_{G}}{\partial w_{e}}(w) \geq 0
```

for admissible parameter ranges.

Thus, the monotonicity axiom is satisfied.

**Diminishing Returns**

Individual ties exhibit diminishing marginal structural returns.

For the cohesion term,

``` math
\frac{\partial^{2}}{\partial w_{e}^{2}}\log(1 + w_{e}) = - \frac{1}{\left( 1+w_{e})^{2} \right.\ } < 0.
```

This strict concavity ensures diminishing marginal structural contributions for increasing tie strengths.

Interaction terms preserve negative curvature in the own-edge direction under admissible parameter ranges, so that

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}^{2}}(w) < 0
```

throughout the interior of the admissible domain.

Thus, the diminishing-return axiom is satisfied.

### 0.10.3 Canonical Status

The Network Potential Functional provides a canonical representative of the admissible class of relational potentials characterised in Sections 0.7–0.9.

The structural marginal decomposition derived in Theorem 0.8.1 corresponds directly to the three components of the Network Potential Functional:

- the cohesion component corresponds to the intrinsic tie contribution $`\log(1 + w_{e})`$,

- the mobility component corresponds to separation-based structural variables,

- the redundancy component corresponds to closure-based structural variables.

The representation theorem of Section 0.9 establishes that admissible relational potentials admit decompositions into cohesion, mobility, and redundancy components under mild regularity conditions. The Network Potential Functional therefore realises the canonical structural form predicted by the axiomatic theory.

In this sense the Network Potential Functional may be viewed as a minimal admissible relational potential capturing the essential structural mechanisms governing relational optimisation.

It provides a concrete instance of the general framework while remaining sufficiently simple to permit explicit equilibrium analysis and operator-based structural investigations.

## 0.11 Operator-Theoretic Structure

The variational framework developed in the preceding sections admits a natural operator-theoretic formulation in which equilibrium configurations are characterised by stationary conditions and stability properties are determined by associated curvature operators.

In this formulation, relational potentials generate marginal structural fields through the gradient operator

``` math
F(w) = \nabla\Phi_{G}(w),
```

while local structural behaviour is governed by the Hessian operator

``` math
H(w) = D^{2}\Phi_{G}(w).
```

Equilibrium configurations correspond to stationary points of the potential, and their stability properties are determined by spectral properties of the associated curvature operators. In particular, negative definiteness of the Hessian operator characterises relational rigidity, while invertibility determines the existence of well-defined equilibrium response operators.

This operator-theoretic viewpoint provides the structural framework for the analysis of relational equilibria developed in subsequent papers. Spectral properties of curvature operators determine structural differentiation, constrained equilibria are governed by reduced Hessian operators on feasible tangent spaces, and dynamical responses are described by linearised gradient-flow operators.

The present section introduces the fundamental operator objects associated with relational potentials and establishes the notation used throughout the remainder of the series.

### 0.11.1 Hessian Operator

Let

``` math
\Phi_{G}:\Omega_{G} \rightarrow \mathbb{R}
```

be an admissible relational potential and let

``` math
w \in \Omega_{G}^{\circ}.
```

The Hessian operator at $`w`$is defined by

``` math
H(w) = D^{2}\Phi_{G}(w),
```

that is,

``` math
H(w) = \left( \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \right)_{e,f \in E}
```

The Hessian operator describes the curvature of the relational potential and determines the local stability properties of equilibrium configurations.

At an interior equilibrium $`w^{*}`$, the Hessian operator governs the second-order behaviour of the functional through the quadratic approximation

``` math
\Phi_{G}(w^{*} + h) = \Phi_{G}(w^{*}) + \frac{1}{2}h^{\top}H(w^{*})h + o( \parallel h \parallel^{2}).
```

If the Hessian operator $`H(w^{*})`$ is **strictly negative definite**, meaning

``` math
h^{\top}H(w^{*})h < 0\text{for all }h \neq 0,
```

then the equilibrium configuration is a strict local maximiser of the relational potential. In this case the equilibrium is relationally rigid in the sense of Section 0.6.7.

The Hessian operator therefore serves as the primary stability operator for relational equilibria.

**Spectral Stability via Structural Interaction**

Under the locality assumptions of Section 0.7.5, cross-partial derivatives define an interaction graph on edges in which two edges $`e`$and $`f`$ are adjacent whenever

``` math
\frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \neq 0.
```

The Hessian operator may therefore be interpreted as a weighted adjacency operator on the interaction graph.

The following theorem provides a sufficient condition for negative definiteness of the Hessian operator.

**Theorem 0.11.1 (Interaction-Graph Gershgorin Condition)**

Let $`H(w)`$ be the Hessian operator of an admissible relational potential. Suppose that for all edges $`e \in E`$,

``` math
\mid H_{ee}(w) \mid > \sum_{f \neq e}^{} \mid H_{ef}(w) \mid .
```

Then all eigenvalues of $`H(w)`$ are strictly negative, and therefore the Hessian operator is strictly negative definite.

Moreover, defining

``` math
\mu = \underset{e \in E}{\min}\left( \mid H_{ee}(w) \mid - \sum_{f \neq e}^{} \mid H_{ef}(w) \mid \right) > 0,
```

we obtain the uniform spectral bound

``` math
H(w) \leq - \mu I.
```

Consequently, any interior equilibrium satisfying this condition is relationally rigid and therefore a strict local maximiser.

**Proof**

By Gershgorin’s Circle Theorem every eigenvalue $`\lambda`$ of $`H(w)`$ lies in a disc

``` math
\mid \lambda - H_{ee}(w) \mid \leq \sum_{f \neq e}^{} \mid H_{ef}(w) \mid .
```

Under strict diagonal dominance these discs lie entirely in the open negative real interval $`( - \infty,0)`$. Since $`H(w)`$ is symmetric, all eigenvalues are real, and therefore

``` math
\lambda < 0.
```

Thus, all eigenvalues of $`H(w)`$ are strictly negative, and therefore the Hessian operator is strictly negative definite.

The uniform spectral bound follows directly from the Gershgorin inequalities.

### 0.11.2 Incident Hessian

Local structural interactions are described by restrictions of the Hessian operator to local edge sets.

For a node $`i \in V`$, let

``` math
\delta(i) = \{ e \in E:e\ is\ incident\ to\ i\}
```

denote the set of edges incident to node $`i`$.

The incident Hessian operator at node $`i`$ is defined by the principal submatrix

``` math
H_{i}(w) = \left( \frac{\partial^{2}\Phi_{G}}{\partial w_{e}\partial w_{f}}(w) \right)_{e,f \in \delta(i)}
```

The incident Hessian describes curvature interactions among ties incident to a single node and therefore characterises local structural response.

Under the locality axiom, marginal structural functions depend only on weights in bounded neighbourhoods of each edge. Accordingly, incident Hessian operators provide natural local curvature operators for the analysis of structural differentiation.

In subsequent papers, spectral and monotonicity properties of incident Hessians will be used to analyse structural ordering relations among equilibrium tie strengths.

### 

### 0.11.3 Susceptibility Kernel

Perturbation responses of equilibrium configurations are governed by the inverse of the Hessian operator.

Let $`w^{*}`$ be an interior equilibrium configuration satisfying

``` math
\nabla\Phi_{G}(w^{*}) = 0,
```

and suppose that the Hessian operator $`H(w^{*})`$ is strictly negative definite.

Then $`H(w^{*})`$ is invertible and the **susceptibility kernel** is defined by

``` math
\chi(w^{*}) = H(w^{*})^{- 1}.
```

The susceptibility kernel determines first-order responses of equilibrium configurations to perturbations in structural parameters.

**Corollary 0.11.2 (Uniform Spectral Gap)**

Suppose there exists a constant $`\mu > 0`$ such that

``` math
H(w) \leq - \mu I\text{for all }w \in \Omega_{G}^{\circ}.
```

Then

``` math
\parallel H(w)^{- 1} \parallel \leq \mu^{- 1}.
```

Thus, the susceptibility operator is uniformly bounded on the admissible domain.

**Proof**

If

``` math
H(w) \leq - \mu I,
```

then all eigenvalues satisfy

``` math
\lambda \leq - \mu.
```

Hence eigenvalues of $`H(w)^{- 1}`$ satisfy

``` math
\mid \lambda^{- 1} \mid \leq \mu^{- 1},
```

giving the operator-norm bound.

**Equilibrium Response**

If the relational potential depends smoothly on a parameter $`\lambda`$ , equilibrium configurations satisfy

``` math
\nabla\Phi_{G}(w^{*}(\lambda),\lambda) = 0.
```

Differentiation with respect to $`\lambda`$ yields

``` math
\frac{dw^{*}}{d\lambda} = - H(w^{*})^{- 1}\partial_{\lambda}\nabla\Phi_{G}(w^{*},\lambda).
```

Thus, the susceptibility kernel describes how perturbations propagate through equilibrium tie strengths.

Negative definiteness of the Hessian operator ensures relational rigidity and structural stability of equilibrium configurations as defined in Section 0.6.7.

The susceptibility operator therefore provides a linear response theory for relational equilibria and forms the basis for the perturbation analysis developed in later papers.

## 0.12 Implications for the Network Potential Series

The axiomatic and representation results developed in this paper establish the general framework within which the subsequent investigations of the Network Potential Series are carried out. The structural, constrained, dynamical, and topological analyses developed in later papers depend fundamentally on the admissible class of relational potentials characterised here.

Paper 0 provides the functional setting in which relational architecture is interpreted as equilibrium structure of a variational system on weighted graphs. The admissibility axioms define the class of relational potentials to which the theory applies, while the structural marginal decomposition and representation theorems establish the canonical cohesion–mobility–redundancy structure governing marginal structural incentives.

Within this framework, the Network Potential Functional appears as a concrete representative of the admissible class, while the results of the subsequent papers describe general properties of equilibria arising from optimisation under admissible relational potentials.

The present section summarises the dependence of each subsequent paper on the foundational results established here.

### 0.12.1 Structural Differentiation

Paper I studies structural differentiation of equilibrium tie strengths through analysis of local curvature operators associated with relational potentials.

The results of Paper I depend on several elements established in the present paper:

- the admissible class of relational potentials defined by the axioms of Section 0.7,

- the marginal structural decomposition of Section 0.8,

- the representation results of Section 0.9,

- and the operator framework introduced in Section 0.11.

Under these conditions, equilibrium configurations generically partition incident ties into differentiated structural roles determined by local structural variables. Structural ordering relations among equilibrium tie strengths arise from monotone marginal responses governed by the curvature operators associated with admissible relational potentials.

The structural differentiation results of Paper I therefore apply not only to the Network Potential Functional but to the broader admissible class of relational potentials characterised in this paper.

### 0.12.2 Scarcity Geometry

Paper II studies relational optimisation under explicit resource constraints imposed through linear coupling among tie strengths.

The constrained optimisation problem takes the form

``` math
\underset{w \in \mathcal{W}_{A}}{max}\Phi_{G}(w),
```

where $`\Phi_{G}`$ is an admissible relational potential and $`\mathcal{W}_{A}`$ is a polyhedral feasible set.

The representation results of Section 0.9 ensure that constrained equilibria may be interpreted in terms of local structural variables, while the operator framework of Section 0.11 provides the basis for analysing stability through reduced-Hessian operators.

Under these conditions, constrained equilibria satisfy the Karush–Kuhn–Tucker system

``` math
\nabla\Phi_{G}(w^{*}) \in N_{\mathcal{W}_{A}}(w^{*}),
```

so that equilibrium architecture is determined jointly by structural marginal incentives and constraint-induced shadow prices.

The scarcity geometry developed in Paper II therefore applies to the entire admissible class of relational potentials rather than to a single functional specification.

### 0.12.3 Dynamics

Paper III develops dynamical formulations of relational optimisation through gradient-flow systems of the form

``` math
\dot{w} = \nabla\Phi_{G}(w).
```

The regularity conditions introduced in Section 0.6 ensure existence and uniqueness of solutions for these dynamical systems on compact domains.

Curvature properties of admissible relational potentials determine convergence behaviour of the resulting dynamics. Concave curvature regimes yield global convergence to equilibrium, while nonconcave regimes admit multiple equilibria and metastable configurations.

The operator framework introduced in Section 0.11 provides the basis for local stability analysis of equilibria through spectral properties of the Hessian operator.

Thus, the dynamical results of Paper III apply to all admissible relational potentials satisfying the axioms introduced in this paper.

### 0.12.4 Topological Endogeneity

Paper IV extends the framework beyond fixed graphs by allowing edge sets to vary together with edge weights.

In this setting optimisation takes place over pairs

``` math
(G,w),
```

where both topology and weights are determined endogenously.

The admissibility axioms established in Section 0.7 ensure that marginal structural incentives remain well defined for candidate edges, while the structural marginal decomposition of Section 0.8 provides the basis for evaluating edge-formation incentives.

Threshold conditions derived from marginal structural functions determine when new edges become structurally optimal.

The topological endogeneity results of Paper IV therefore extend the admissible relational-potential framework to mixed discrete–continuous optimisation problems.

### 0.12.5 Functional Generalisation

Paper V studies extensions of the Network Potential Functional obtained by replacing specific structural measures with alternative structural variables.

The admissible class of relational potentials defined in Section 0.7 provides the natural setting for this analysis. Representation results ensure that alternative structural measures may be incorporated without altering the fundamental structure of relational potentials.

In particular, higher-order redundancy measures and spectral structural variables may be incorporated while preserving locality and symmetry conditions.

The functional generalisations studied in Paper V therefore demonstrate the robustness of the structural differentiation mechanism across the admissible class of relational potentials.

## 0.13 Conclusion

This paper has established the axiomatic and representational foundations of relational potentials on weighted graphs. Within a variational framework in which weighted networks are interpreted as equilibrium configurations of scalar functionals defined on compact domains of admissible edge weights, relational architecture emerges as a structural consequence of optimisation.

The first contribution of the paper is the formal definition of relational potentials as smooth scalar functionals on the space of admissible edge-weight configurations. This formulation places relational optimisation within the setting of finite-dimensional variational analysis and provides a precise mathematical framework for interpreting weighted networks as equilibrium structures determined by optimisation under a global structural objective.

The second contribution is the introduction of an admissible class of relational potentials defined through locality, symmetry, monotonicity, diminishing-return conditions, and controlled structural interaction. These axioms characterise the class of relational potentials suitable for structural analysis and provide the functional setting within which the results of the Network Potential Series are developed.

The third contribution is the development of a structural marginal theory linking the admissibility axioms to canonical structural variables. The structural marginal decomposition theorem establishes that admissible relational potentials admit marginal representations in which structural incentives decompose into intrinsic tie contributions, separation-based contributions, and redundancy-based contributions. This decomposition provides the structural basis for the cohesion–mobility–redundancy interpretation of relational optimisation.

The fourth contribution is the representation theory developed in Section 0.9. Under the admissibility conditions, relational potentials admit representations in terms of local structural variables defined on neighbourhoods of nodes and edges. These results establish that cohesion, mobility, and redundancy arise as canonical structural components of admissible relational potentials rather than as features of a particular functional specification.

The fifth contribution is the demonstration that the Network Potential Functional introduced in Mack (2026) arises as a canonical example of an admissible relational potential. The functional realises the canonical cohesion–mobility–redundancy structure predicted by the axiomatic theory and provides a concrete instance within which equilibrium structure can be analysed explicitly.

Taken together, these results place the Network Potential Functional within a broader class of relational energy functionals and establish the mathematical foundations of relational optimisation on weighted graphs. The axiomatic and representation results developed here provide the functional framework within which the structural, constrained, dynamical, and topological investigations of subsequent papers are formulated.

In this sense, relational potentials may be interpreted not merely as scalar optimisation objectives but as variational generative principles for weighted network architecture. Equilibrium configurations correspond to structurally organised states of the network, and structural properties arise from the curvature and marginal structure of the underlying relational potential.

Paper 0 therefore provides the foundational layer of the Network Potential Series by establishing the admissible class of relational potentials and the canonical structural decomposition governing relational optimisation. Subsequent papers develop the structural, constrained, dynamical, and topological consequences of optimisation within this framework.

# Bibliography

Boyd, S. and Vandenberghe, L. (2004) *Convex Optimization*. Cambridge: Cambridge University Press.

Mack, I. (2026) Network Potential and Relational Optimisation: Balancing Cohesion, Brokerage, and Redundancy in Weighted Networks. Dissertation.

Monderer, D. and Shapley, L.S. (1996) ‘Potential games’, *Games and Economic Behavior*, 14(1), pp. 124–143.

Nash, J. (1951) ‘Non-cooperative games’, *Annals of Mathematics*, 54(2), pp. 286–295.

Rockafellar, R.T. (1970) *Convex Analysis*. Princeton: Princeton University Press.
