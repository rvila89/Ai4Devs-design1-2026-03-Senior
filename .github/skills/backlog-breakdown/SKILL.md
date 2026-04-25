---
name: backlog-breakdown
description: Use this skill when a specification already exists and you need to break it down into a structured, tool-neutral product backlog with stories, priorities, dependencies, acceptance criteria, and initial story point estimates. Trigger this for requests about backlog creation, ticket definition, backlog refinement, or turning a spec into planning-ready work items.
---

# Backlog Breakdown Skill

## Purpose
This skill converts `spec.md` into a traceable, planning-ready product backlog for spec-driven development. It is for backlog definition and refinement only, not implementation or code generation.

## When to use
Use this skill when:
- a written spec exists
- a team or solo developer needs backlog items before sprint planning
- the request mentions backlog definition, refinement, prioritization, tickets, stories, or transforming a spec into work items

Do not use this skill when the task is implementation, coding, debugging, or direct sprint selection from an already prepared backlog.

## Files to load
- Read `references/planning-assumptions.md` before starting.
- Read `references/backlog-rules.md` before decomposing the spec.
- Read `references/definition-of-ready.md` when assigning readiness states.
- Read `assets/product-backlog-template.json` only when formatting the final output.

## Workflow
1. Read `spec.md` and identify major capabilities, user workflows, constraints, and acceptance intent.
2. Extract the planning signals that matter most: user value, risk, dependencies, cross-team touchpoints, and open questions.
3. Decompose the spec into epics and stories, using tasks only when they improve planning clarity.
4. Apply priority and initial Fibonacci story point estimates.
5. Assign readiness states based on the definition of ready.
6. Capture assumptions, risks, and unresolved questions explicitly instead of inventing missing requirements.
7. Format the final backlog using `assets/product-backlog-template.json`.

## Gotchas
- Do not create implementation code or code-level tasks unless the spec explicitly requires planning-level technical tasks.
- Do not force precise estimates on ambiguous items.
- Do not decompose only by technical layer if a vertical slice is possible.
- Do not hide uncertainty; surface it in assumptions, risks, or readiness.
- Do not create backlog items that cannot be traced back to `spec.md`.

## Output requirements
- Keep the output tool-neutral.
- Ensure each item includes title, summary, business value, traceability, acceptance criteria, dependencies, assumptions, risks, priority, estimate, readiness, and discipline tags.
- Mark oversized items as split candidates.
- Distinguish facts from assumptions.

## Output location
Save the final backlog as `planning/product-backlog.json` inside the active spec folder
(e.g. `specs/<feature-name>/planning/product-backlog.json`).
The prompt can override this path when a different location is needed.

## Final validation
Before finalizing, confirm that:
- every item maps back to `spec.md`
- every story has acceptance criteria
- every item has priority and story points
- every oversized or unclear item is flagged
- the result can be used in either solo or team planning
