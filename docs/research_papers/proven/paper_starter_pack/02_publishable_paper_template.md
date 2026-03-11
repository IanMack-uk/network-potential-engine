# Paper Template — Theorem-First, Publication-Oriented Draft

## Working Title

**[Insert precise title reflecting only what is actually established]**

Examples:
- Local Response Positivity and Ordered Comparative Statics for a Certified Relational Potential Model
- Hessian-Coupling Structure and Certified Response Theory in an Admissible Network Potential Framework

## Abstract

Write the abstract only after the certification map is complete.

Recommended structure:
1. problem setting,
2. mathematical object of study,
3. main certified theorem(s),
4. exact scope qualifiers,
5. computational / code-certification interface,
6. one-sentence statement of what remains future work.

## 1. Introduction

### 1.1 Problem motivation
State the mathematical problem without overclaiming.

### 1.2 What this paper establishes
Use a numbered list of only those claims that are either:
- repo-certified, or
- classical and explicitly cited.

### 1.3 What this paper does not claim
Explicitly isolate:
- conjectural extensions,
- model-specific limitations,
- results awaiting certification.

### 1.4 Relation to repository certification workflow
Briefly explain how theorem documents, implementation modules, tests, and evidence scripts support the paper.

## 2. Mathematical Setup

### 2.1 Ambient spaces and variables
Define the state space, parameter space, and any graph/index sets.

### 2.2 Relational potential and derived operators
Define:
- the potential,
- gradient,
- Hessian,
- coupling operator,
- response/susceptibility operator if needed.

### 2.3 Equilibrium notion
Define the equilibrium concept and state when an equilibrium branch is assumed to exist.

## 3. Assumptions and Scope

State assumptions explicitly and minimally.

Suggested subsections:
- regularity assumptions,
- admissibility / locality assumptions,
- equilibrium existence assumptions,
- interiority / nondegeneracy / hyperbolicity assumptions,
- region/path assumptions if ordering is claimed,
- model-specific instantiation caveats.

## 4. Certified Structural Results

Present the earliest foundational certified results that the paper uses.

Possible order:
- Hessian-coupling identification,
- locality inheritance,
- response identity,
- positivity/ordering backbone.

Each proposition/theorem should have a status marker in the prose such as:
- **Certified in repository**
- **Classical**
- **Research statement / certification pending**

## 5. Main Theorem Section

Use the theorem section template in `04_theorem_section_template.md`.

## 6. Consequences and Interpretation

Translate the theorem carefully into mathematical consequences.
Do not introduce stronger claims than the theorem supports.

Distinguish:
- immediate corollaries,
- model-specific implications,
- broader interpretations that remain conjectural.

## 7. Certification Traceability

Provide a short paper-facing traceability note or appendix table linking:
- theorem docs,
- implementation modules,
- tests,
- scripts.

## 8. Discussion and Limits

Explain:
- current certification boundary,
- missing generalisations,
- what would need to be proved and certified next.

## 9. Conclusion

Summarise only established outcomes and separate future certification targets.

## Appendix A. Repository Source Map

Insert the completed source-map table from `06_repo_source_map_template.md`.

## Appendix B. Proof Dependency Ledger

List each theorem-like statement and the exact assumptions used.

