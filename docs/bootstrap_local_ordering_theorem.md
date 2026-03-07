# Bootstrap Local Ordering Theorem

## Purpose

This note gives a complete first proof of a **finite local weak ordering theorem** for the current bootstrap model used in `network-potential-engine`.

The goal is to prove, for this model class, that if the exposure parameter increases coordinatewise, then the equilibrium weight vector also increases coordinatewise.

---

## 1. Model definition

Let

\[
w = (w_1,\dots,w_n)^\top \in \mathbb{R}^n,
\qquad
\theta = (\theta_1,\dots,\theta_n)^\top \in \mathbb{R}^n.
\]

We define the bootstrap potential by

\[
\Phi(w,\theta)
=
\sum_{i=1}^n \theta_i w_i
-\frac{q}{2}\sum_{i=1}^n w_i^2
-\frac{c}{2}\sum_{i=1}^{n-1}(w_i-w_{i+1})^2,
\]

where

\[
q > 0,
\qquad
c \ge 0.
\]

This is the current toy model implemented in the symbolic layer.

---

## 2. Equilibrium operator

Define the equilibrium operator

\[
F(w,\theta) := \nabla_w \Phi(w,\theta).
\]

The equilibrium \(w^*(\theta)\) is defined as the stationary point satisfying

\[
F(w^*(\theta),\theta)=0.
\]

Because \(\Phi\) is strictly concave in \(w\) under the conditions proved below, this equilibrium is unique.

---

## 3. Gradient

For the bootstrap model,

\[
\Phi(w,\theta)
=
\sum_{i=1}^n \theta_i w_i
-\frac{q}{2}\sum_{i=1}^n w_i^2
-\frac{c}{2}\sum_{i=1}^{n-1}(w_i-w_{i+1})^2.
\]

Differentiating with respect to \(w_i\), we obtain:

### First component
\[
\frac{\partial \Phi}{\partial w_1}
=
\theta_1 - q w_1 - c(w_1-w_2).
\]

### Interior components \(2 \le i \le n-1\)
\[
\frac{\partial \Phi}{\partial w_i}
=
\theta_i - q w_i - c(w_i-w_{i+1}) + c(w_{i-1}-w_i).
\]

This simplifies to

\[
\frac{\partial \Phi}{\partial w_i}
=
\theta_i - q w_i + c w_{i-1} - 2c w_i + c w_{i+1}.
\]

### Final component
\[
\frac{\partial \Phi}{\partial w_n}
=
\theta_n - q w_n + c(w_{n-1}-w_n).
\]

So the equilibrium equation is a linear system in \(w\).

---

## 4. Hessian

Define the raw Hessian

\[
H := \nabla^2_{ww}\Phi.
\]

Because \(\Phi\) is quadratic in \(w\), the Hessian is constant in \(w\) and \(\theta\).

Its entries are:

- diagonal:
  \[
  H_{11}=-(q+c), \qquad H_{nn}=-(q+c),
  \]
  \[
  H_{ii}=-(q+2c), \qquad 2\le i\le n-1;
  \]

- nearest-neighbour off-diagonal:
  \[
  H_{i,i+1}=H_{i+1,i}=c;
  \]

- all other entries are zero.

Thus

\[
H=
\begin{bmatrix}
-(q+c) & c & 0 & \cdots & 0 \\
c & -(q+2c) & c & \ddots & \vdots \\
0 & c & -(q+2c) & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & c \\
0 & \cdots & 0 & c & -(q+c)
\end{bmatrix}.
\]

---

## 5. Coupling operator

Define the canonical coupling operator

\[
C := -H.
\]

Then

\[
C=
\begin{bmatrix}
q+c & -c & 0 & \cdots & 0 \\
-c & q+2c & -c & \ddots & \vdots \\
0 & -c & q+2c & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & -c \\
0 & \cdots & 0 & -c & q+c
\end{bmatrix}.
\]

This is the preferred operator for sign and matrix analysis.

---

## 6. Mixed derivative block

Define

\[
H_{w\theta} := D_\theta(\nabla_w \Phi).
\]

Because the \(\theta\)-dependence in \(\Phi\) is linear and separable,

\[
\Phi(w,\theta)=\sum_{i=1}^n \theta_i w_i + \text{terms independent of }\theta,
\]

we obtain

\[
\frac{\partial^2 \Phi}{\partial w_i \partial \theta_j} = \delta_{ij},
\]

where \(\delta_{ij}\) is the Kronecker delta.

Therefore

\[
H_{w\theta} = I_n.
\]

---

## 7. Structural facts about \(C\)

We now prove the key matrix properties.

### 7.1 Symmetry

Since \(H\) is symmetric, so is \(C=-H\).

### 7.2 Nonpositive off-diagonals

The only off-diagonal entries of \(C\) are \(-c\), and since \(c\ge 0\),

\[
-c \le 0.
\]

So \(C\) has nonpositive off-diagonal entries.

### 7.3 Strict diagonal dominance

For the first and last rows,

\[
|C_{11}| - \sum_{j\ne 1}|C_{1j}| = (q+c)-c = q > 0,
\]
and similarly for row \(n\).

For interior rows,

\[
|C_{ii}| - \sum_{j\ne i}|C_{ij}|
=
(q+2c) - (c+c)
=
q > 0.
\]

Thus every row has positive diagonal-dominance margin equal to \(q\). Hence \(C\) is strictly diagonally dominant by rows.

### 7.4 Consequence

Since \(C\) is symmetric, strictly diagonally dominant, and has nonpositive off-diagonals, it is a nonsingular M-matrix. In particular,

\[
C^{-1} \ge 0
\]

entrywise.

This is the key sign fact behind monotonicity.

---

## 8. Existence and uniqueness of equilibrium

The equilibrium equation is

\[
F(w,\theta)=0.
\]

Because \(F\) is affine in \(w\), we may write it as

\[
F(w,\theta)=\theta - Cw.
\]

So the equilibrium condition is

\[
\theta - Cw = 0,
\]

equivalently

\[
Cw = \theta.
\]

Since \(C\) is nonsingular, the equilibrium exists and is unique, with explicit formula

\[
w^*(\theta)=C^{-1}\theta.
\]

Thus the solution map is globally linear in \(\theta\).

---

## 9. Response identity

Differentiating

\[
w^*(\theta)=C^{-1}\theta
\]

with respect to \(\theta\), we obtain

\[
D_\theta w^*(\theta)=C^{-1}.
\]

This agrees with the general response identity

\[
D_\theta w^*(\theta)=C^{-1}H_{w\theta},
\]

because in the bootstrap model

\[
H_{w\theta}=I_n.
\]

So indeed

\[
D_\theta w^*(\theta)=C^{-1}I_n=C^{-1}.
\]

Since \(C^{-1}\ge 0\), we conclude

\[
D_\theta w^*(\theta)\ge 0
\]

entrywise.

---

## 10. Pointwise monotonicity

Let \(v\in \mathbb{R}^n\) satisfy

\[
v \succeq 0,
\]

meaning \(v_i\ge 0\) for all \(i\).

Then

\[
D_\theta w^*(\theta)\,v
=
C^{-1}v.
\]

Because \(C^{-1}\ge 0\) entrywise and \(v\ge 0\) entrywise, it follows that

\[
C^{-1}v \succeq 0.
\]

Hence

\[
v \succeq 0
\quad\Longrightarrow\quad
D_\theta w^*(\theta)\,v \succeq 0.
\]

This proves pointwise directional weak monotonicity.

---

## 11. Finite local weak ordering theorem

We now prove the finite ordering statement.

Let \(\theta,\theta'\in\mathbb{R}^n\) satisfy

\[
\theta' \succeq \theta.
\]

Then

\[
\theta' - \theta \succeq 0.
\]

Using the explicit formula for the equilibrium,

\[
w^*(\theta') - w^*(\theta)
=
C^{-1}\theta' - C^{-1}\theta
=
C^{-1}(\theta'-\theta).
\]

Since \(C^{-1}\ge 0\) entrywise and \(\theta'-\theta\ge 0\) entrywise, we conclude

\[
w^*(\theta') - w^*(\theta)\succeq 0.
\]

Therefore

\[
\theta' \succeq \theta
\quad\Longrightarrow\quad
w^*(\theta') \succeq w^*(\theta).
\]

This proves finite local weak ordering. In fact, for this bootstrap model the statement is global, not merely local, because the solution map is linear and \(C\) is constant.

---

## 12. Theorem statement

### Bootstrap Local Ordering Theorem

Let

\[
\Phi(w,\theta)
=
\sum_{i=1}^n \theta_i w_i
-\frac{q}{2}\sum_{i=1}^n w_i^2
-\frac{c}{2}\sum_{i=1}^{n-1}(w_i-w_{i+1})^2,
\]

with \(q>0\) and \(c\ge 0\). Define the equilibrium \(w^*(\theta)\) by

\[
\nabla_w \Phi(w^*(\theta),\theta)=0.
\]

Then:

1. the equilibrium exists and is unique;
2. the raw Hessian \(H=\nabla^2_{ww}\Phi\) is constant and negative definite;
3. the coupling operator \(C=-H\) is a symmetric strictly diagonally dominant Z-matrix;
4. \(H_{w\theta}=I_n\);
5. the response identity is
   \[
   D_\theta w^*(\theta)=C^{-1};
   \]
6. since \(C^{-1}\ge 0\), the equilibrium map is monotone:
   \[
   \theta' \succeq \theta
   \quad\Longrightarrow\quad
   w^*(\theta') \succeq w^*(\theta).
   \]

---

## 13. Interpretation

This theorem gives the first complete proved instance of the structural ordering mechanism:

- exposure enters linearly,
- curvature is stable,
- the coupling matrix has inverse-positive structure,
- and equilibrium outcomes inherit the exposure ordering.

This bootstrap theorem is the first fully proved model in the project and serves as the template for more general local monotonicity theorems.

---

## 14. Relation to the codebase

The proof corresponds directly to the current project modules:

- `symbolic/potential.py` defines \(\Phi\),
- `symbolic/gradient.py` defines \(F=\nabla_w\Phi\),
- `symbolic/hessian.py` defines \(H\),
- `symbolic/mixed_derivatives.py` defines \(H_{w\theta}\),
- `symbolic/operators.py` defines \(C=-H\),
- `numeric/equilibrium.py` solves for \(w^*(\theta)\),
- `numeric/response.py` computes \(C^{-1}H_{w\theta}\),
- `theorem/pointwise.py` checks the pointwise theorem conditions,
- `theorem/local_scan.py` gives numerical evidence of local finite ordering along sampled parameter lines.

---

## 15. What remains beyond the bootstrap theorem

The bootstrap theorem is fully proved because the model has:

- constant Hessian,
- identity mixed derivative block,
- and an explicit linear equilibrium map.

The next challenge is to extend this to richer model classes where:

- \(H\) depends on \(\theta\),
- the sign structure of \(C^{-1}\) must persist on a neighborhood,
- and the finite local ordering theorem must be proved by combining:
  - local branch existence,
  - response identity,
  - neighborhood sign persistence,
  - and path integration.