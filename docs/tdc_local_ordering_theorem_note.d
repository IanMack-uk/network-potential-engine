# A Local Ordering Theorem on an Admissible Region for the Theta-Dependent-Curvature Model

## 1. Model

Let
\[
w=(w_1,\dots,w_n)^\top\in\mathbb R^n,
\qquad
\theta=(\theta_1,\dots,\theta_n)^\top\in\mathbb R^n,
\]
and define
\[
\Phi_{\mathrm{tdc}}(w,\theta)
=
\sum_{i=1}^n \theta_i w_i
-\frac12\sum_{i=1}^n (q+\alpha\theta_i)w_i^2
-\frac{c}{2}\sum_{i=1}^{n-1}(w_i-w_{i+1})^2,
\]
with parameters
\[
q>0,\qquad \alpha\ge 0,\qquad c\ge 0.
\]

Define the equilibrium operator
\[
F(w,\theta):=\nabla_w\Phi_{\mathrm{tdc}}(w,\theta),
\]
and let \(w^*(\theta)\) denote an equilibrium satisfying
\[
F(w^*(\theta),\theta)=0.
\]

## 2. Structural formulas

The gradient has the form
\[
F(w,\theta)=\theta-C(\theta)w,
\]
where
\[
C(\theta)=
\begin{bmatrix}
q+\alpha\theta_1+c & -c & 0 & \cdots & 0\\
-c & q+\alpha\theta_2+2c & -c & \ddots & \vdots\\
0 & -c & q+\alpha\theta_3+2c & \ddots & 0\\
\vdots & \ddots & \ddots & \ddots & -c\\
0 & \cdots & 0 & -c & q+\alpha\theta_n+c
\end{bmatrix}.
\]

Equivalently, if
\[
H(\theta):=\nabla_{ww}^2\Phi_{\mathrm{tdc}}(w,\theta),
\]
then
\[
C(\theta)=-H(\theta).
\]

The mixed derivative block is
\[
H_{w\theta}(w,\theta)
:=
D_\theta(\nabla_w\Phi_{\mathrm{tdc}}(w,\theta))
=
\operatorname{diag}(1-\alpha w_1,\dots,1-\alpha w_n).
\]

Whenever \(C(\theta)\) is nonsingular, the equilibrium satisfies
\[
C(\theta)w^*(\theta)=\theta,
\qquad
w^*(\theta)=C(\theta)^{-1}\theta.
\]

The pointwise response identity is
\[
D_\theta w^*(\theta)
=
C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta).
\]

## 3. Matrix structure

For each row \(i\), the diagonal-dominance margin of \(C(\theta)\) is
\[
q+\alpha\theta_i.
\]

Hence, if
\[
q+\alpha\theta_i>0
\qquad\text{for all }i,
\]
then \(C(\theta)\) is a strictly diagonally dominant Z-matrix, and therefore a nonsingular M-matrix. In particular,
\[
C(\theta)^{-1}\ge 0
\]
entrywise.

Moreover, if
\[
1-\alpha w_i^*(\theta)\ge 0
\qquad\text{for all }i,
\]
then
\[
H_{w\theta}(w^*(\theta),\theta)\ge 0
\]
entrywise.

Combining these two facts with the response identity yields
\[
D_\theta w^*(\theta)\ge 0
\]
entrywise.

## 4. An analytic bound

Set
\[
m(\theta):=\min_i(q+\alpha\theta_i).
\]

If \(m(\theta)>0\), then
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
\|C(\theta)^{-1}\|_\infty\,\|\theta\|_\infty
\le
\frac{\|\theta\|_\infty}{m(\theta)}.
\]

Therefore a sufficient condition for
\[
1-\alpha w_i^*(\theta)\ge 0
\quad\text{for all }i
\]
is
\[
\alpha\,\frac{\|\theta\|_\infty}{m(\theta)}\le 1.
\]

## 5. The admissible region

Define the admissible region
\[
\mathcal R
:=
\left\{
\theta\in\mathbb R^n:
m(\theta)>0
\ \text{and}\
\alpha\,\frac{\|\theta\|_\infty}{m(\theta)}\le 1
\right\},
\qquad
m(\theta):=\min_i(q+\alpha\theta_i).
\]

For every \(\theta\in\mathcal R\),

1. \(C(\theta)\) is a nonsingular M-matrix, so
   \[
   C(\theta)^{-1}\ge 0;
   \]

2. the analytic bound implies
   \[
   1-\alpha w_i^*(\theta)\ge 0
   \qquad\text{for all }i,
   \]
   hence
   \[
   H_{w\theta}(w^*(\theta),\theta)\ge 0.
   \]

Therefore, on \(\mathcal R\),
\[
D_\theta w^*(\theta)=C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta)\ge 0
\]
entrywise.

## 6. Local ordering theorem on the admissible region

### Theorem
Let \(\theta,\theta'\in\mathcal R\). Assume that the line segment
\[
\gamma(t)=\theta+t(\theta'-\theta),
\qquad t\in[0,1],
\]
is contained in \(\mathcal R\). If
\[
\theta'\succeq\theta
\]
in the coordinatewise order, then
\[
w^*(\theta')\succeq w^*(\theta).
\]

### Proof
Since \(\gamma([0,1])\subseteq\mathcal R\), we have
\[
D_\theta w^*(\gamma(t))\ge 0
\qquad\text{for all }t\in[0,1].
\]
Hence
\[
w^*(\theta')-w^*(\theta)
=
\int_0^1 D_\theta w^*(\gamma(t))(\theta'-\theta)\,dt.
\]
Because \(\theta'-\theta\succeq 0\) and the matrix
\[
D_\theta w^*(\gamma(t))
\]
is entrywise nonnegative for every \(t\), the integrand is entrywise nonnegative for every \(t\). Therefore
\[
w^*(\theta')-w^*(\theta)\succeq 0.
\]
This proves the claim.

## 7. Computational status

The current implementation verifies, for the sampled TDC scan presently used in the project, that:

- every sampled point lies in the admissible region \(\mathcal R\);
- the curvature margins \(q+\alpha\theta_i\) remain positive;
- the mixed-block margins \(1-\alpha w_i^*(\theta)\) remain positive;
- the response matrix
  \[
  C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta)
  \]
  remains entrywise nonnegative;
- and the sampled finite equilibrium differences remain entrywise nonnegative.

Thus the code provides strong evidence that the theorem applies on the sampled local path.

## 8. Remaining gap to a broader theorem

This note gives a theorem on the explicit admissible region \(\mathcal R\). The broader remaining task is to prove larger, less conservative neighborhood statements by improving the bound
\[
\|w^*(\theta)\|_\infty
\le
\frac{\|\theta\|_\infty}{m(\theta)},
\]
or by deriving sharper structure-specific estimates for \(w^*(\theta)\).