# Theta-Dependent-Curvature Local Ordering Theorem

## Purpose

This note develops the local ordering theory for the theta-dependent-curvature (TDC) model currently implemented in `network-potential-engine`.

Unlike the bootstrap model, the TDC model has curvature that varies with the exposure parameter \(\theta\). This makes the model a better prototype for the full structural differentiation theorem, because the coupling matrix and response map genuinely vary across parameter space.

The goal of this note is to:

1. define the TDC model clearly,
2. compute the gradient, Hessian, coupling operator, and mixed derivative block explicitly,
3. derive sufficient conditions for the pointwise theorem mechanism,
4. derive an analytic sup-norm bound for the equilibrium,
5. state a conditional local ordering theorem,
6. connect the theorem conditions to the current code and scan results.

---

## 1. Model definition

Let

\[
w = (w_1,\dots,w_n)^\top \in \mathbb{R}^n,
\qquad
\theta = (\theta_1,\dots,\theta_n)^\top \in \mathbb{R}^n.
\]

Define the theta-dependent-curvature potential by

\[
\Phi_{\mathrm{tdc}}(w,\theta)
=
\sum_{i=1}^n \theta_i w_i
-
\frac12 \sum_{i=1}^n (q+\alpha \theta_i) w_i^2
-
\frac{c}{2}\sum_{i=1}^{n-1}(w_i-w_{i+1})^2,
\]

where the parameters satisfy

\[
q>0,\qquad \alpha \ge 0,\qquad c \ge 0.
\]

Here:

- \(q\) is the baseline quadratic curvature,
- \(\alpha\) controls how curvature depends on \(\theta\),
- \(c\) is the nearest-neighbour coupling strength.

---

## 2. Equilibrium operator

Define the equilibrium operator

\[
F(w,\theta):=\nabla_w \Phi_{\mathrm{tdc}}(w,\theta).
\]

An equilibrium \(w^*(\theta)\) is defined by

\[
F(w^*(\theta),\theta)=0.
\]

Unlike the bootstrap model, the equilibrium map will generally not be globally linear in \(\theta\), because the curvature matrix now varies with \(\theta\).

---

## 3. Gradient

We compute the gradient componentwise.

### First component
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_1}
=
\theta_1
-
(q+\alpha\theta_1) w_1
-
c(w_1-w_2).
\]

So
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_1}
=
\theta_1-(q+\alpha\theta_1+c)w_1+c w_2.
\]

### Interior components \(2 \le i \le n-1\)
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_i}
=
\theta_i
-
(q+\alpha\theta_i) w_i
-
c(w_i-w_{i+1})
+
c(w_{i-1}-w_i).
\]

So
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_i}
=
\theta_i
-
(q+\alpha\theta_i+2c) w_i
+
c w_{i-1}
+
c w_{i+1}.
\]

### Final component
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_n}
=
\theta_n
-
(q+\alpha\theta_n) w_n
+
c(w_{n-1}-w_n).
\]

Equivalently,
\[
\frac{\partial \Phi_{\mathrm{tdc}}}{\partial w_n}
=
\theta_n
-
(q+\alpha\theta_n+c)w_n
+
c w_{n-1}.
\]

Thus \(F(w,\theta)\) is affine in \(w\), but with coefficients depending on \(\theta\).

In matrix form,

\[
F(w,\theta)=\theta-C(\theta)w,
\]

where \(C(\theta)\) is defined below.

---

## 4. Hessian

Define the raw Hessian

\[
H(\theta):=\nabla^2_{ww}\Phi_{\mathrm{tdc}}(w,\theta).
\]

Because \(\Phi_{\mathrm{tdc}}\) is quadratic in \(w\), the Hessian is independent of \(w\), but it does depend on \(\theta\).

Its entries are:

- diagonal:
  \[
  H_{11} = -(q+\alpha\theta_1+c),
  \qquad
  H_{nn} = -(q+\alpha\theta_n+c),
  \]
  \[
  H_{ii} = -(q+\alpha\theta_i+2c),
  \qquad 2\le i\le n-1;
  \]

- nearest-neighbour off-diagonal:
  \[
  H_{i,i+1}=H_{i+1,i}=c;
  \]

- all other entries are zero.

So

\[
H(\theta)=
\begin{bmatrix}
-(q+\alpha\theta_1+c) & c & 0 & \cdots & 0 \\
c & -(q+\alpha\theta_2+2c) & c & \ddots & \vdots \\
0 & c & -(q+\alpha\theta_3+2c) & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & c \\
0 & \cdots & 0 & c & -(q+\alpha\theta_n+c)
\end{bmatrix}.
\]

Thus \(H(\theta)\) varies with \(\theta\).

---

## 5. Coupling operator

Define the canonical coupling operator

\[
C(\theta):=-H(\theta).
\]

Then

\[
C(\theta)=
\begin{bmatrix}
q+\alpha\theta_1+c & -c & 0 & \cdots & 0 \\
-c & q+\alpha\theta_2+2c & -c & \ddots & \vdots \\
0 & -c & q+\alpha\theta_3+2c & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & -c \\
0 & \cdots & 0 & -c & q+\alpha\theta_n+c
\end{bmatrix}.
\]

This is the main matrix for the local ordering theory.

---

## 6. Mixed derivative block

Define

\[
H_{w\theta}(w,\theta):=D_\theta(\nabla_w \Phi_{\mathrm{tdc}}(w,\theta)).
\]

From the gradient formulas, we obtain

\[
\frac{\partial^2 \Phi_{\mathrm{tdc}}}{\partial w_i \partial \theta_j}
=
\begin{cases}
1-\alpha w_i, & i=j,\\
0, & i\neq j.
\end{cases}
\]

Therefore,

\[
H_{w\theta}(w,\theta)
=
\operatorname{diag}(1-\alpha w_1,\dots,1-\alpha w_n).
\]

This is a major difference from the bootstrap model, where \(H_{w\theta}=I_n\).

---

## 7. Structural facts about \(C(\theta)\)

We now derive sufficient conditions for the pointwise theorem mechanism.

### 7.1 Symmetry

Since \(H(\theta)\) is symmetric, so is \(C(\theta)\).

### 7.2 Nonpositive off-diagonals

The only off-diagonal entries of \(C(\theta)\) are \(-c\), so if \(c\ge 0\), then

\[
-c \le 0.
\]

Thus \(C(\theta)\) always has nonpositive off-diagonal entries.

### 7.3 Diagonal-dominance margins

For the first row,

\[
|C_{11}(\theta)| - \sum_{j\ne 1}|C_{1j}(\theta)|
=
(q+\alpha\theta_1+c)-c
=
q+\alpha\theta_1.
\]

For the final row,

\[
|C_{nn}(\theta)| - \sum_{j\ne n}|C_{nj}(\theta)|
=
q+\alpha\theta_n.
\]

For interior rows,

\[
|C_{ii}(\theta)| - \sum_{j\ne i}|C_{ij}(\theta)|
=
(q+\alpha\theta_i+2c) - (c+c)
=
q+\alpha\theta_i.
\]

Therefore the row-wise diagonal-dominance margins are exactly

\[
q+\alpha\theta_i.
\]

So \(C(\theta)\) is strictly diagonally dominant if

\[
q+\alpha\theta_i > 0
\qquad\text{for all }i.
\]

This is the key neighborhood condition.

### 7.4 M-matrix consequence

If
\[
q+\alpha\theta_i > 0 \quad \forall i,
\]
then \(C(\theta)\) is a strictly diagonally dominant Z-matrix, hence a nonsingular M-matrix. Therefore

\[
C(\theta)^{-1}\ge 0
\]

entrywise.

---

## 8. Equilibrium equation

Since \(F(w,\theta)\) is affine in \(w\), the equilibrium equation can be written as

\[
F(w,\theta)=\theta - C(\theta)w = 0.
\]

Thus the equilibrium satisfies

\[
C(\theta)w^*(\theta)=\theta,
\]

so

\[
w^*(\theta)=C(\theta)^{-1}\theta,
\]

whenever \(C(\theta)\) is nonsingular.

This gives an explicit equilibrium formula, but unlike the bootstrap case the map is no longer linear in \(\theta\), because \(C(\theta)\) itself depends on \(\theta\).

---

## 9. Response identity

The general response identity is

\[
D_\theta w^*(\theta)=C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta).
\]

For the TDC model, we already computed

\[
H_{w\theta}(w,\theta)
=
\operatorname{diag}(1-\alpha w_1,\dots,1-\alpha w_n).
\]

So at equilibrium,

\[
D_\theta w^*(\theta)
=
C(\theta)^{-1}\operatorname{diag}(1-\alpha w_1^*(\theta),\dots,1-\alpha w_n^*(\theta)).
\]

This is the central pointwise response formula for the model.

---

## 10. Sufficient condition for pointwise monotonicity

Suppose \(\theta\) is such that:

1. \(q+\alpha\theta_i > 0\) for all \(i\), so \(C(\theta)\) is a nonsingular M-matrix and
   \[
   C(\theta)^{-1}\ge 0;
   \]

2. \(1-\alpha w_i^*(\theta)\ge 0\) for all \(i\), so
   \[
   H_{w\theta}(w^*(\theta),\theta)\ge 0
   \]
   entrywise.

Then
\[
D_\theta w^*(\theta)
=
C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta)\ge 0
\]
entrywise.

Hence for every \(v\succeq 0\),
\[
D_\theta w^*(\theta)\,v \succeq 0.
\]

This proves pointwise directional weak monotonicity.

---

## 11. Analytic bound lemma

We now derive a simple analytic sufficient condition for the mixed-block positivity requirement.

Define the minimum curvature margin

\[
m(\theta):=\min_i (q+\alpha\theta_i).
\]

If \(m(\theta)>0\), then \(C(\theta)\) is strictly diagonally dominant and invertible. Using the standard infinity-norm bound for inverses of strictly diagonally dominant matrices, we obtain

\[
\|C(\theta)^{-1}\|_\infty \le \frac{1}{m(\theta)}.
\]

Since

\[
w^*(\theta)=C(\theta)^{-1}\theta,
\]

it follows that

\[
\|w^*(\theta)\|_\infty
\le
\|C(\theta)^{-1}\|_\infty \|\theta\|_\infty
\le
\frac{\|\theta\|_\infty}{m(\theta)}.
\]

Therefore, a sufficient condition for

\[
1-\alpha w_i^*(\theta)\ge 0
\quad\text{for all }i
\]

is

\[
\alpha\,\|w^*(\theta)\|_\infty \le 1.
\]

Using the bound above, it is enough to require

\[
\alpha\,\frac{\|\theta\|_\infty}{m(\theta)} \le 1.
\]

So we have proved the following.

### Lemma (analytic sufficient condition)
If

\[
m(\theta)=\min_i(q+\alpha\theta_i)>0
\]

and

\[
\alpha\,\frac{\|\theta\|_\infty}{m(\theta)} \le 1,
\]

then

\[
1-\alpha w_i^*(\theta)\ge 0
\quad\text{for all }i.
\]

Consequently,

\[
H_{w\theta}(w^*(\theta),\theta)\ge 0.
\]

---

## 12. Conditional local weak ordering theorem

We now state the local theorem in conditional form.

### Theorem (conditional local ordering for the TDC model)

Let \(\theta_0\in\mathbb{R}^n\). Suppose there exists a neighborhood \(U\ni\theta_0\) such that for every \(\theta\in U\):

1. the equilibrium \(w^*(\theta)\) exists;
2. \(q+\alpha\theta_i > 0\) for all \(i\), so \(C(\theta)\) is a nonsingular M-matrix and
   \[
   C(\theta)^{-1}\ge 0;
   \]
3. \(1-\alpha w_i^*(\theta)\ge 0\) for all \(i\), so
   \[
   H_{w\theta}(w^*(\theta),\theta)\ge 0.
   \]

Then the equilibrium map is locally monotone on \(U\): for any \(\theta,\theta'\in U\),
\[
\theta' \succeq \theta
\quad\Longrightarrow\quad
w^*(\theta') \succeq w^*(\theta).
\]

### Proof

For \(\theta,\theta'\in U\), define
\[
\gamma(t)=\theta+t(\theta'-\theta),\qquad t\in[0,1].
\]

Then
\[
w^*(\theta')-w^*(\theta)
=
\int_0^1 D_\theta w^*(\gamma(t))(\theta'-\theta)\,dt.
\]

Since \(\theta'-\theta \succeq 0\), and by hypothesis
\[
D_\theta w^*(\gamma(t))
=
C(\gamma(t))^{-1}H_{w\theta}(w^*(\gamma(t)),\gamma(t))\ge 0
\]
entrywise for all \(t\in[0,1]\), the integrand is entrywise nonnegative for all \(t\). Therefore the integral is entrywise nonnegative, so

\[
w^*(\theta')-w^*(\theta)\succeq 0.
\]

Hence
\[
\theta' \succeq \theta \Longrightarrow w^*(\theta') \succeq w^*(\theta).
\]

---

## 13. What the code has verified so far

The current code has not yet proved the full theorem symbolically for all \(\theta\). But it has verified the theorem mechanism at concrete parameter values and along sampled lines.

For the tested scan in the current implementation:

- the equilibrium exists at every sampled point,
- the row-wise diagonal-dominance margins remain positive,
- \(C(\theta)\) remains symmetric with nonpositive off-diagonals,
- \(R(\theta)=C(\theta)^{-1}H_{w\theta}(\theta)\) remains entrywise nonnegative,
- the finite equilibrium differences
  \[
  w^*(\theta(t_{k+1}))-w^*(\theta(t_k))
  \]
  remain entrywise nonnegative,
- the sufficient-condition margins
  \[
  q+\alpha\theta_i
  \quad\text{and}\quad
  1-\alpha w_i^*(\theta)
  \]
  remain positive on the sampled line,
- and the analytic bound
  \[
  \|w^*(\theta)\|_\infty \le \frac{\|\theta\|_\infty}{m(\theta)}
  \]
  holds at the tested basepoint.

For the current scan, the code reports:

- minimum sampled curvature margin:
  \[
  0.96,
  \]
- minimum sampled mixed-block margin:
  \[
  \approx 0.931483.
  \]

Thus the code gives strong evidence that the sufficient conditions hold on the sampled neighborhood, with visible slack.

---

## 14. Relation to the full programme theorem

This model is much closer to the full structural differentiation theorem than the bootstrap model, because:

- the curvature depends on \(\theta\),
- the coupling matrix varies with \(\theta\),
- the mixed derivative block is nontrivial,
- and neighborhood persistence of the sign structure is no longer automatic.

The remaining gap is now clear:

> move from sampled computational persistence to a fully rigorous neighborhood proof.

That requires proving that the conditions

\[
q+\alpha\theta_i > 0
\quad\text{and}\quad
1-\alpha w_i^*(\theta)\ge 0
\]

hold throughout an explicit neighborhood.

The analytic bound lemma above is the first step in that direction.

---

## 15. Relation to the codebase

This note corresponds to the current code modules as follows:

- `symbolic/potential.py` defines \(\Phi_{\mathrm{tdc}}\),
- `symbolic/gradient.py` defines \(F=\nabla_w\Phi_{\mathrm{tdc}}\),
- `symbolic/hessian.py` defines \(H(\theta)\),
- `symbolic/mixed_derivatives.py` defines \(H_{w\theta}(w,\theta)\),
- `symbolic/operators.py` defines \(C(\theta)=-H(\theta)\),
- `symbolic/tdc_equilibrium.py` defines the explicit symbolic equilibrium map,
- `numeric/equilibrium.py` solves for \(w^*(\theta)\),
- `numeric/response.py` computes \(R(\theta)=C(\theta)^{-1}H_{w\theta}(\theta)\),
- `theorem/pointwise.py` checks the pointwise theorem conditions,
- `theorem/local_scan.py` checks sampled neighborhood persistence and finite differences,
- `theorem/tdc_conditions.py` checks the explicit sufficient conditions,
- `theorem/tdc_neighborhood.py` summarizes those conditions over a scan,
- `theorem/tdc_bounds.py` computes the analytic bound quantities.

---

## 16. Next mathematical task

The next real proof task is to derive an explicit neighborhood \(U\) on which the sufficient conditions hold.

That means proving bounds of the form:

1. \(q+\alpha\theta_i > 0\) for all \(\theta\in U\),
2. \(1-\alpha w_i^*(\theta)\ge 0\) for all \(\theta\in U\),

using either:

- a direct neighborhood bound on \(\theta\),
- the analytic equilibrium bound
  \[
  \|w^*(\theta)\|_\infty \le \frac{\|\theta\|_\infty}{m(\theta)},
  \]
- or a combination of analytic estimates and continuity.

Once those are proved, the conditional local ordering theorem above becomes a genuine local theorem for the TDC model.