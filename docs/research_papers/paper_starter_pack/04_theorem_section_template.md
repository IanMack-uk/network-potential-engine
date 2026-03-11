# Theorem Section Template

## [Section X]. [Insert theorem-section title]

### 1. Setup and standing notation

Fix [ambient space / graph / admissible class / parameter regime].
Let [define principal objects in the exact order they are needed].

State explicitly whether the paper is working:
- at arbitrary `(w, θ)`,
- at an equilibrium branch `w*(θ)`,
- at a fixed point `θ`,
- on a certified region/path,
- in a model-specific instantiation.

### 2. Definitions used in the theorem

Definition 1. [Object]

Definition 2. [Object]

Definition 3. [Object]

Each definition should be paper-facing and consistent with repository notation.

### 3. Assumptions

Assumption A1. [Regularity / admissibility]

Assumption A2. [Existence / equilibrium branch]

Assumption A3. [Interiority / nondegeneracy / hyperbolicity]

Assumption A4. [Locality / sign structure / region assumptions]

Do not include assumptions that the proof does not actually use.

### 4. Main theorem

**Theorem X ([precise theorem title]).**
Assume A1-Ak. Then [state the exact conclusion].

Recommended theorem-writing rules:
- separate hypotheses from conclusions cleanly;
- avoid mixing notation definitions into the theorem statement;
- specify whether the conclusion is local/global/model-specific;
- avoid “it is easy to see” or other informal proof shortcuts;
- if a claim is certified only in a particular instantiation, say so in the theorem or immediately after it.

### 5. Proof

**Proof.**
Proceed in numbered steps.

1. **Object well-definedness.**  
   Establish existence/well-definedness of the objects used.

2. **Structural identity.**  
   Invoke the exact theorem/code identity needed.

3. **Intermediate sign / locality / invertibility step.**  
   State the precise dependency used here.

4. **Conclusion.**  
   Derive the theorem statement without introducing new assumptions.

5. **Status note if needed.**  
   If part of the interpretation exceeds current certification, terminate the proof before that point and move the stronger statement to a remark labelled as research or conjectural.

\(\square\)

### 6. Remarks

Recommended remark types:

- **Remark (Certification status).**  
  State whether the theorem is framework-level, model-level, or only certified in a specific instantiation.

- **Remark (Boundary of interpretation).**  
  Distinguish what follows rigorously from what is only heuristic or future work.

- **Remark (Implementation traceability).**  
  Point to theorem docs, modules, tests, and check scripts.

### 7. Optional corollary

Only include if it follows immediately and cleanly.

**Corollary.** [Precise consequence]

**Proof.** Immediate from Theorem X and [dependency].

