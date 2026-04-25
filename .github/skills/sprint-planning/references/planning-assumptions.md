# Planning Assumptions

## Hard constraints
- The workflow focuses on planning artifacts only and must not produce implementation code.
- `spec.md` is the source of truth for scope, scenarios, constraints, and acceptance intent.
- Product backlog creation must happen before sprint backlog selection.
- Outputs must remain tool-neutral so they can later map to Jira, Linear, or GitHub Issues.
- Every backlog or sprint item must preserve traceability to `spec.md`.

## Planning defaults
- The workflow must support both solo and team planning modes.
- Estimation uses Fibonacci story points: 1, 2, 3, 5, 8, 13.
- Items above 8 points should normally be split before sprint commitment.
- The agent should prefer vertical slices of user value over purely technical decomposition.
- The agent should preserve a visible reserve for uncertainty instead of maximizing utilization.

## Assumptions to validate
- `spec.md` contains enough detail to infer backlog-ready stories and acceptance criteria.
- If the spec is incomplete, the agent should record assumptions and open questions rather than inventing facts.
- Cross-team considerations may involve product, engineering, QA, design, security, and operations, while solo mode may combine those responsibilities into one person.
- Sprint planning assumes a written sprint goal and a usable capacity figure are available.

## Decision rules
- Separate facts from assumptions in every output.
- Flag unclear, blocked, or oversized items instead of forcing false precision.
- Prefer a coherent, goal-aligned sprint slice over filling every remaining point of capacity.
