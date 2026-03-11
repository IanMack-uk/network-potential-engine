# Section X. Certified Local Weak Ordering from Sign-Controlled Equilibrium Response

## 1. Setup and standing notation

Let (W`\subseteq`{=tex}`\mathbb{R}`{=tex}\^n) and
(`\Theta`{=tex}`\subseteq`{=tex}`\mathbb{R}`{=tex}\^n) denote admissible
state and parameter sets, and let\
(`\Omega`{=tex}*`\Phi `{=tex}`\subseteq `{=tex}W`\times `{=tex}`\Theta`{=tex})
be a domain on which a relational potential (`\Phi `{=tex}:
`\Omega`{=tex}*`\Phi `{=tex}`\to `{=tex}`\mathbb{R}`{=tex}) is defined.

Define the equilibrium operator (F(w,`\theta`{=tex}) :=
`\nabla`{=tex}\_w `\Phi`{=tex}(w,`\theta`{=tex})).

Let

-   (H(w,`\theta`{=tex}) :=
    `\nabla`{=tex}\^2\_{ww}`\Phi`{=tex}(w,`\theta`{=tex})) denote the
    state Hessian
-   (H\_{w`\theta`{=tex}}(w,`\theta`{=tex}) :=
    `\nabla`{=tex}\^2\_{w`\theta`{=tex}}`\Phi`{=tex}(w,`\theta`{=tex}))
    denote the mixed derivative block.

An equilibrium for parameter (`\theta`{=tex}) is any point
(w\^\*(`\theta`{=tex})`\in `{=tex}W) satisfying

(F(w\^\*(`\theta`{=tex}),`\theta`{=tex})=0.)

Throughout this section we study the equilibrium correspondence along a
parameter path and derive a **local weak ordering result** for
equilibria.

The paper works along a certified equilibrium branch
(`\theta `{=tex}`\mapsto `{=tex}w\^\*(`\theta`{=tex})) and on a
certified admissible region (R`\subseteq`{=tex}`\Theta`{=tex}).

------------------------------------------------------------------------

# 2. Definitions used in the theorem

## Definition 1 (Equilibrium response operator)

Let (w\^\*(`\theta`{=tex})) be an equilibrium branch.

The equilibrium response operator is

(D\_`\theta `{=tex}w\^\*(`\theta`{=tex}).)

Under differentiability and nondegeneracy conditions,

(D\_`\theta `{=tex}w\^*(`\theta`{=tex})=C(`\theta`{=tex})^{-1}H\_{w`\theta`{=tex}}(w^*(`\theta`{=tex}),`\theta`{=tex}))

where

(C(`\theta`{=tex}):=-H(w\^\*(`\theta`{=tex}),`\theta`{=tex}).)

------------------------------------------------------------------------

## Definition 2 (Admissible parameter region)

A subset (R`\subseteq`{=tex}`\Theta`{=tex}) is an admissible parameter
region if

1.  equilibrium (w\^\*(`\theta`{=tex})) exists,
2.  (H(w\^\*(`\theta`{=tex}),`\theta`{=tex})) is nonsingular,
3.  the response identity holds.

------------------------------------------------------------------------

## Definition 3 (Segment certificate)

Let (`\theta`{=tex},`\theta`{=tex}'`\in`{=tex}`\Theta`{=tex}).

The segment certificate for ((`\theta`{=tex},`\theta`{=tex}')) requires
the segment

(`\gamma`{=tex}(t)=`\theta`{=tex}+t(`\theta`{=tex}'-`\theta`{=tex}))

to lie entirely in the admissible region (R).

------------------------------------------------------------------------

# 3. Assumptions

## Assumption A1 (Regularity)

(`\Phi`{=tex}`\in `{=tex}C\^2_w(`\Omega`{=tex}*`\Phi`{=tex})) and
(`\Phi`{=tex}`\in `{=tex}C\^1*`\theta`{=tex}(`\Omega`{=tex}\_`\Phi`{=tex})).

Consequently (F,H,H\_{w`\theta`{=tex}}) exist and are continuous.

------------------------------------------------------------------------

## Assumption A2 (Equilibrium stationarity)

Equilibria satisfy

(F(w\^\*(`\theta`{=tex}),`\theta`{=tex})=0.)

------------------------------------------------------------------------

## Assumption A3 (Interior nondegeneracy)

For every (`\theta`{=tex})

(H(w\^\*(`\theta`{=tex}),`\theta`{=tex}))

is nonsingular.

------------------------------------------------------------------------

## Assumption A4 (Sign-controlled response)

Along the admissible region (R)

(C(`\theta`{=tex})\^{-1}`\ge0`{=tex})

and

(H\_{w`\theta`{=tex}}(w\^\*(`\theta`{=tex}),`\theta`{=tex})`\ge0`{=tex}.)

These imply

(D\_`\theta `{=tex}w\^\*(`\theta`{=tex})`\ge0`{=tex}.)

------------------------------------------------------------------------

# 4. Main theorem

**Theorem (Local weak ordering from sign-controlled equilibrium
response).**

Let Assumptions A1--A4 hold.

Let (`\theta`{=tex}'`\succeq`{=tex}`\theta`{=tex}) and assume the
segment

(`\gamma`{=tex}(t)=`\theta`{=tex}+t(`\theta`{=tex}'-`\theta`{=tex}))

lies entirely in the admissible region (R).

Then

(w\^*(`\theta`{=tex}')-w\^*(`\theta`{=tex})`\ge0`{=tex})

componentwise.

------------------------------------------------------------------------

# 5. Proof

**Step 1 --- Well-defined response**

Under A1--A3 the response identity holds

(D\_`\theta `{=tex}w\^*(`\theta`{=tex})=C(`\theta`{=tex})^{-1}H\_{w`\theta`{=tex}}(w^*(`\theta`{=tex}),`\theta`{=tex}).)

**Step 2 --- Sign structure**

A4 implies

(D\_`\theta `{=tex}w\^\*(`\theta`{=tex})`\ge0`{=tex}.)

**Step 3 --- Path integral**

Let

(`\gamma`{=tex}(t)=`\theta`{=tex}+t(`\theta`{=tex}'-`\theta`{=tex})).

Then

(w\^\*(`\theta`{=tex}')-w\^*(`\theta`{=tex}) =`\int`{=tex}*0\^1
D*`\theta `{=tex}w\^*(`\gamma`{=tex}(t))(`\theta`{=tex}'-`\theta`{=tex})dt.)

**Step 4 --- Positivity**

Since

(D\_`\theta `{=tex}w\^\*(`\gamma`{=tex}(t))`\ge0`{=tex})

and

(`\theta`{=tex}'-`\theta`{=tex}`\ge0`{=tex}),

the integrand is nonnegative.

Therefore

(w\^*(`\theta`{=tex}')-w\^*(`\theta`{=tex})`\ge0`{=tex}.)

(`\square`{=tex})

------------------------------------------------------------------------

# 6. Remarks

**Certification status.**

This theorem corresponds to the A1--E3 certified theorem chain
implemented in the repository.

**Structural route.**

Inverse positivity can arise from Z-matrix structure, diagonal
dominance, and M-matrix conditions.

**Implementation traceability.**

Symbolic modules construct derivatives, theorem helpers construct
admissible regions and segment certificates, and certification scripts
verify each stage.
