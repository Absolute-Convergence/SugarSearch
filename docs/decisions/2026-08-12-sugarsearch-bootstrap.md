# SugarSearch Bootstrap and Identity Boundary

- **Status:** accepted
- **Date:** 2026-08-12
- **Scope:** repository lineage, product identity, package names, commands, and
  historical-document handling

## Context

SugarSearch begins as an independent continuation of the Hyperloop repository
at upstream commit `f55c62fa8d89cbb32d1f35de7ce5168a69bd180a`. The inherited
implementation is a working local multi-objective black-box optimizer, not a
blank scaffold. A continuation needs clear provenance and a clear namespace so
new SugarSearch releases cannot be mistaken for Hyperloop v0.1.1.

## Decision

- Preserve the full upstream Git history and MIT license.
- Keep the inherited repository as the `upstream` remote. Do not retain it as
  `origin`, which could make an accidental push target the source project.
- Use `https://github.com/Absolute-Convergence/SugarSearch.git` as `origin`.
  Its generated initial commit was unrelated to the inherited history, so it
  was connected with a merge using Git's `ours` strategy. That preserves the
  GitHub-created commit as provenance while retaining the audited SugarSearch
  tree and full Hyperloop lineage.
- Use `SugarSearch` for the product and GUI name.
- Use `sugarsearch` for the distribution, Python package, module command, and
  installed optimizer command.
- Use `sugarsearch_workers` for bundled opaque workers and
  `sugarsearch-synthetic-worker` for the installed synthetic worker command.
- Use four-part release numbering in the form `0.0.0.1`, beginning with
  package version `0.0.1.0` and release tag `v0.0.1.0`. Hyperloop's `v0.1.0`
  and `v0.1.1` tags remain historical upstream releases, not SugarSearch
  releases.
- Make a clean namespace break. Do not ship temporary Hyperloop import or CLI
  aliases unless a concrete compatibility consumer is identified later.
- Preserve old planning, release, GUI, and dated decision records with their
  original terminology. They are provenance, not current SugarSearch policy.
- Do not change the imported configuration, worker, trial, Pareto, or
  persistence semantics as part of the identity bootstrap.

## Consequences

Existing Hyperloop consumers must update imports and command names to use
SugarSearch. That is acceptable because this is a new repository and product,
not an in-place Hyperloop patch release. New public-contract work requires a
separate decision; the rename itself does not authorize networking,
concurrency, resume behavior, new algorithms, or SugarBot coupling.
