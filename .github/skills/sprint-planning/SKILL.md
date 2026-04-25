---
name: sprint-planning
description: Use this skill when a product backlog already exists and you need to select, prioritize, estimate, and sequence a sprint backlog under a sprint goal and capacity constraint. Trigger this for requests about sprint planning, weekly planning, selecting tickets for a sprint, balancing capacity, or choosing goal-aligned backlog items.
---

# Sprint Planning Skill

## Purpose
This skill turns a prepared product backlog into a goal-aligned sprint backlog for solo or team delivery. It is a planning skill only and must not generate implementation code.

## When to use
Use this skill when:
- a product backlog already exists
- a sprint or short planning window must be defined
- the user needs ticket selection, prioritization, sequencing, capacity balancing, or sprint backlog creation

Do not use this skill when the work is backlog generation from a raw spec or direct implementation.

## Files to load
- Read `references/planning-assumptions.md` before starting.
- Read `references/sprint-goal.md` before selecting any items.
- Read `references/team-capacity.md` before checking scope.
- Read `references/definition-of-ready.md` before including borderline items.
- Read `references/sprint-planning-rules.md` before sequencing and deferring work.
- Read `references/estimation-guide.md` if estimates need interpretation or calibration.
- Read `assets/sprint-backlog-template.json` only when formatting the final output.

## Workflow
1. Read the sprint goal and identify the smallest meaningful increment it implies.
2. Read team or solo capacity and determine effective usable capacity.
3. Review the existing product backlog and exclude items that clearly do not support the sprint goal.
4. Check readiness and remove or flag items that need clarification or splitting.
5. Sequence the remaining items based on dependencies, blockers, and delivery logic.
6. Select a coherent sprint slice that fits effective capacity.
7. Defer remaining items with explicit reasons.
8. Format the result using `assets/sprint-backlog-template.json`.

## Gotchas
- Do not fill capacity just because points remain.
- Do not include non-ready items silently.
- Do not commit oversized items without flagging the need to split them.
- Do not choose disconnected work that fails to produce a meaningful sprint outcome.
- Do not hide blockers, handoff risks, or review bottlenecks.

## Output requirements
- Keep the output tool-neutral.
- Include selected items, deferred items, capacity usage, assumptions, and risks.
- Show why each selected item supports the sprint goal.
- Make dependencies and blockers visible.
- Support both solo and team planning modes.

## Output location
Save the final sprint backlog as `planning/sprint-backlog.json` inside the active spec folder
(e.g. `specs/<feature-name>/planning/sprint-backlog.json`).
The prompt can override this path when a different location is needed.

## Final validation
Before finalizing, confirm that:
- all selected items support the sprint goal
- selected story points do not exceed effective usable capacity
- dependencies are sequenced safely
- deferred items include explicit reasons
- major planning risks are visible
