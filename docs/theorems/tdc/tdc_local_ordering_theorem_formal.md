# Formal Local Ordering Results for the Theta-Dependent-Curvature Model

## Definition 1 (Theta-dependent-curvature model)

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

Define
\[
F(w,\theta):=\nabla_w\Phi_{\mathrm{tdc}}(w,\theta),
\]
and define an equilibrium \(w^*(\theta)\) by
\[
F(w^*(\theta),\theta)=0.
\]

## Proposition 2 (Gradient form)

The equilibrium operator has the form
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

## Proposition 3 (Hessian and coupling operator)

Let
\[
H(\theta):=\nabla_{ww}^2\Phi_{\mathrm{tdc}}(w,\theta).
\]
Then
\[
C(\theta)=-H(\theta).
\]

Explicitly,
\[
H(\theta)=
\begin{bmatrix}
-(q+\alpha\theta_1+c) & c & 0 & \cdots & 0\\
c & -(q+\alpha\theta_2+2c) & c & \ddots & \vdots\\
0 & c & -(q+\alpha\theta_3+2c) & \ddots & 0\\
\vdots & \ddots & \ddots & \ddots & c\\
0 & \cdots & 0 & c & -(q+\alpha\theta_n+c)
\end{bmatrix}.
\]

## Proposition 4 (Mixed derivative block)

Define
\[
H_{w\theta}(w,\theta):=
D_\theta(\nabla_w\Phi_{\mathrm{tdc}}(w,\theta)).
\]
Then
\[
H_{w\theta}(w,\theta)
=
\operatorname{diag}(1-\alpha w_1,\dots,1-\alpha w_n).
\]

## Proposition 5 (Equilibrium equation)

Whenever \(C(\theta)\) is nonsingular, the equilibrium satisfies
\[
C(\theta)w^*(\theta)=\theta,
\]
hence
\[
w^*(\theta)=C(\theta)^{-1}\theta.
\]

## Proposition 6 (Response identity)

Whenever \(w^*(\theta)\) is differentiable in \(\theta\),
\[
D_\theta w^*(\theta)
=
C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta).
\]

## Lemma 7 (Diagonal-dominance margins)

For each row \(i\), the diagonal-dominance margin of \(C(\theta)\) is
\[
q+\alpha\theta_i.
\]

Consequently, if
\[
q+\alpha\theta_i>0
\qquad\text{for all }i,
\]
then \(C(\theta)\) is a strictly diagonally dominant Z-matrix.

## Lemma 8 (Inverse positivity)

If
\[
q+\alpha\theta_i>0
\qquad\text{for all }i,
\]
then \(C(\theta)\) is a nonsingular M-matrix, and therefore
\[
C(\theta)^{-1}\ge 0
\]
entrywise.

## Lemma 9 (Mixed-block positivity condition)

If
\[
1-\alpha w_i^*(\theta)\ge 0
\qquad\text{for all }i,
\]
then
\[
H_{w\theta}(w^*(\theta),\theta)\ge 0
\]
entrywise.

## Corollary 10 (Pointwise response positivity)

If
\[
q+\alpha\theta_i>0
\qquad\text{for all }i,
\]
and
\[
1-\alpha w_i^*(\theta)\ge 0
\qquad\text{for all }i,
\]
then
\[
D_\theta w^*(\theta)\ge 0
\]
entrywise.

## Lemma 11 (Analytic inverse bound)

Define
\[
m(\theta):=\min_i(q+\alpha\theta_i).
\]
If
\[
m(\theta)>0,
\]
then
\[
\|C(\theta)^{-1}\|_\infty \le \frac{1}{m(\theta)}.
\]

## Lemma 12 (Analytic equilibrium bound)

If
\[
m(\theta)>0,
\]
then
\[
\|w^*(\theta)\|_\infty
\le
\frac{\|\theta\|_\infty}{m(\theta)}.
\]

## Corollary 13 (Analytic sufficient condition for mixed-block positivity)

If
\[
m(\theta)>0
\]
and
\[
\alpha\,\frac{\|\theta\|_\infty}{m(\theta)}\le 1,
\]
then
\[
1-\alpha w_i^*(\theta)\ge 0
\qquad\text{for all }i.
\]

Hence
\[
H_{w\theta}(w^*(\theta),\theta)\ge 0.
\]

## Definition 14 (Admissible region)

Define
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

## Proposition 15 (Pointwise positivity on the admissible region)

If
\[
\theta\in\mathcal R,
\]
then
\[
C(\theta)^{-1}\ge 0,
\qquad
H_{w\theta}(w^*(\theta),\theta)\ge 0,
\qquad
D_\theta w^*(\theta)\ge 0
\]
entrywise.

## Lemma 16 (Segment certificate)

Let \(\theta^L,\theta^R\in\mathbb R^n\). Define
\[
m_{\mathrm{seg}}
:=
\min_i\bigl(q+\alpha\min(\theta^L_i,\theta^R_i)\bigr),
\]
and
\[
M_{\mathrm{seg}}
:=
\max\bigl(\|\theta^L\|_\infty,\|\theta^R\|_\infty\bigr).
\]

If
\[
m_{\mathrm{seg}}>0
\qquad\text{and}\qquad
\alpha\,\frac{M_{\mathrm{seg}}}{m_{\mathrm{seg}}}\le 1,
\]
then the full segment
\[
[\theta^L,\theta^R]
=
\{\theta^L+t(\theta^R-\theta^L):t\in[0,1]\}
\]
is contained in \(\mathcal R\).

## Theorem 17 (Local ordering theorem on the admissible region)

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

Since \(\gamma([0,1])\subseteq\mathcal R\), Proposition 15 implies
\[
D_\theta w^*(\gamma(t))\ge 0
\qquad\text{for all }t\in[0,1].
\]
Therefore
\[
w^*(\theta')-w^*(\theta)
=
\int_0^1 D_\theta w^*(\gamma(t))(\theta'-\theta)\,dt.
\]
Since
\[
\theta'-\theta\succeq 0
\]
and the matrix
\[
D_\theta w^*(\gamma(t))
\]
is entrywise nonnegative for every \(t\in[0,1]\), the integrand is entrywise nonnegative for every \(t\). Hence
\[
w^*(\theta')-w^*(\theta)\succeq 0.
\]
This proves the claim.

## Proposition 18 (Computational certification of the current sampled path)

For the sampled path
\[
[0.0,-0.1,-0.2]
\to
[0.1,0.0,-0.1]
\to
[0.2,0.1,0.0]
\to
[0.3,0.2,0.1]
\to
[0.4,0.3,0.2],
\]
the current implementation verifies that:

1. every sampled point lies in \(\mathcal R\);
2. every consecutive segment is certified to lie in \(\mathcal R\);
3. every consecutive endpoint pair satisfies the local theorem hypothesis;
4. every consecutive equilibrium difference is coordinatewise nonnegative.

Therefore the sampled path is fully consistent with Theorem 17.

## Remark 19

The admissible region \(\mathcal R\) is sufficient but not necessarily sharp. A broader local theorem would follow from improved bounds on
\[
\|w^*(\theta)\|_\infty
\]
or from sharper structural estimates for \(C(\theta)^{-1}\).