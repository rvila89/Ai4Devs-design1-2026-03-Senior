# Backlog Rules

## Decomposition rules
- Start from user value and workflow outcomes, not implementation layers.
- Create epics only for major capability areas.
- Create stories for slices of user or business value.
- Create tasks only when they improve planning clarity, dependency visibility, or cross-team coordination.
- Prefer vertical slices over component-only breakdowns.

## Priority rules
Use these labels:
- P0: essential for the first meaningful increment or critical risk reduction
- P1: important and likely next after P0
- P2: useful but deferrable
- P3: optional, exploratory, or future-facing

Assign priority based on:
- user value
- dependency criticality
- risk reduction
- learning value
- time sensitivity

## Estimation rules
Use Fibonacci story points: 1, 2, 3, 5, 8, 13.
- 1: tiny, well-understood change
- 2: small, low-risk item
- 3: moderate item with limited uncertainty
- 5: meaningful item with some coordination or unknowns
- 8: large item with notable uncertainty; review carefully before sprint selection
- 13: too large for normal sprint selection; split strongly recommended

## Acceptance criteria rules
Every story must include acceptance criteria that are:
- observable
- testable
- specific enough for planning
- free of hidden implementation assumptions

## Cross-team rules
Tag items with one or more of:
- product
- engineering
- QA
- design
- security
- operations

## Examples
### Good story
- A returning user can resume a saved planning draft and see which backlog items still need clarification.

### Weak story
- Build planning backend logic.

### Good acceptance criteria
- The user can reopen a saved draft from the planning dashboard.
- The draft shows last updated time and unresolved items.
- The draft can be resumed without losing previously entered information.

### Weak acceptance criteria
- The feature works correctly.

## Gotchas and edge cases
- Do not split stories into technical layers unless that improves planning decisions.
- Do not estimate unknown work as medium by default.
- Do not create tasks solely to make the backlog look detailed.
- If a story exceeds 8 points or bundles multiple outcomes, flag it for splitting.
