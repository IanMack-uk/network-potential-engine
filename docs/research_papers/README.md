# Publishable Paper Starter Pack

This folder is a **from-scratch paper authoring pack** for a theorem-driven paper in the `network-potential-engine` project.

It is designed for use with **Cascade in Windsurf** as a repository-searching research assistant, with the following goals:

1. identify the exact theorem/certification spine already present in the codebase;
2. collate the assumptions, theorem documents, tests, and evidence scripts needed to support a paper;
3. draft a paper at **professional academic standard**;
4. separate **repo-certified**, **classical**, and **research / conjectural** material;
5. produce a theorem section that is suitable for later polishing into publishable form.

## Included files

- `01_cascade_windsurf_instruction_brief.md`  
  Main brief for Cascade. Tells it how to search the repository, what persona to adopt, and what outputs to return.

- `02_publishable_paper_template.md`  
  A paper skeleton for a theorem-first mathematics paper.

- `03_theorem_input_dossier_template.md`  
  Structured form for collecting theorem data from the repository.

- `04_theorem_section_template.md`  
  A paper-ready theorem section template.

- `05_professional_academic_standard.md`  
  Editorial and rigor standard expected for publication-oriented drafting.

- `06_repo_source_map_template.md`  
  Traceability table connecting theorem claims to theorem docs, modules, tests, and scripts.

- `07_author_to_cascade_handoff_note.md`  
  Short copy-paste note you can give to Cascade at the start of the task.

- `reference_chatgpt_paper_improvement_template.md`  
  Your uploaded improvement-oriented template, preserved as a reference.

## Repo-grounding assumptions built into this pack

This pack is aligned with the current repo-certified theorem spine that appears in the repository materials, including the A1-E3 workflow, the B1 Hessian-coupling theorem, and supporting tests/scripts such as the TDC full workflow and pointwise theorem-check utilities.

Representative internal anchors visible in the repository include:

- the improvement template itself under `docs/research_papers/unproven/...`,
- the Paper 1 strengthening plan enumerating A1-E3 theorem docs and their associated tests/scripts,
- `docs/theorems/framework/B1_hessian_coupling_theorem.md`, which defines the canonical coupling operator via `C(w, θ) = -H(w, θ)`,
- `src/network_potential_engine/scripts/check_tdc_full_workflow.py`, which wires together A1-E3 and S1-S3 evidence stages,
- `src/network_potential_engine/theorem/pointwise.py`, which packages pointwise theorem-style checks for equilibrium, coupling, and response matrices.

## How to use

1. Give `01_cascade_windsurf_instruction_brief.md` to Cascade.
2. Ask Cascade to fill out `03_theorem_input_dossier_template.md` and `06_repo_source_map_template.md` from the repository.
3. Once the dossier is complete, use `02_publishable_paper_template.md` and `04_theorem_section_template.md` as the basis for drafting.
4. Keep `05_professional_academic_standard.md` visible during editing.

