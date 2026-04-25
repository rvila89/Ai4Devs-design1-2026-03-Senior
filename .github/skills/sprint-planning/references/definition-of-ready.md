# Definition of Ready

A backlog item is ready for sprint selection only when the checks below pass.

## Required checks
- The item has a clear user or business outcome.
- The item is traceable to a requirement, scenario, or constraint in `spec.md`.
- The item has explicit, testable acceptance criteria.
- Dependencies are known, manageable, or explicitly documented.
- The item is small enough to estimate credibly.
- The item has a Fibonacci story point estimate.
- Risks, assumptions, and open questions are documented.
- The item has clear discipline ownership tags, such as product, engineering, QA, design, security, or operations.
- The item can be understood without hidden context.
- The item is small enough for a sprint or marked as needing to be split.

## Readiness outcomes
- `ready`: all checks pass.
- `needs-clarification`: information is missing or ambiguous.
- `needs-splitting`: the item is too large for reliable sprint commitment.

## Gotchas
- Do not mark an item as ready only because it sounds important.
- Do not treat vague acceptance criteria as sufficient.
- Do not assume unresolved dependencies will sort themselves out during the sprint.
