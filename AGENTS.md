# SugarSearch Repository Compass

Last updated: 2026-08-12.

## Current Working Point

- SugarSearch is an independent continuation of Hyperloop, imported from
  upstream commit `f55c62fa8d89cbb32d1f35de7ce5168a69bd180a` with full history.
- The active product identity is `SugarSearch`; the distribution, import
  package, and installed command are `sugarsearch`.
- The imported optimizer behavior is intentionally unchanged during the
  bootstrap. Historical Hyperloop documents remain under `docs/upstream`,
  `docs/planning_baseline_v01`, `docs/planning_baseline_v02`, and older dated
  decisions.
- Current version is `0.0.1.0`. SugarSearch uses four-part versions in the
  form `0.0.0.1`, with release tags prefixed by `v`. The SugarSearch `origin`
  is `https://github.com/Absolute-Convergence/SugarSearch.git`; the inherited
  repository is the `upstream` remote.
- The verified bootstrap is published on `origin/main`; annotated release tag
  `v0.0.1.0` identifies the first SugarSearch continuation release.
- No SugarBot integration is implemented. Use
  `docs/sugarbot-integration-horizon.md` as the non-binding direction.

## Product and Architecture Rules

- Keep execution local-first. Do not add a cloud dependency by default.
- Treat workers as opaque processes. Do not import or inspect worker internals.
- Preserve immutable public configuration, candidate, record, Pareto-front,
  and result contracts.
- Only the controller may authorize a worker launch. Trials remain sequential
  until an explicit architecture decision changes that rule.
- Persist one immutable record for every attempted execution and preserve the
  append-only evidence model.
- Return the complete mixed-direction Pareto front. Do not invent a weighted
  universal winner.
- Keep GUI and reporting code downstream of authoritative optimizer results.
- Keep bundled or future SugarBot adapters outside the `sugarsearch` core
  package. SugarBot remains a separate runtime, not an imported implementation
  detail.
- Record public JSON, CLI, worker, result, persistence, or dependency changes
  in `docs/decisions` before implementation.
- Do not rewrite historical Hyperloop records to look SugarSearch-native.

## Verification

Use the repository environment and Python 3.13.14:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
.\.venv\Scripts\python.exe tools\check_monoliths.py
.\.venv\Scripts\python.exe -m build
```

Run the four-trial installed-command smoke after an editable or wheel install:

```powershell
.\.venv\Scripts\Activate.ps1
sugarsearch config.json --output-dir runs
```

## Next Work

- Ratify the capability audit priorities before expanding the inherited MVP.
- Decide the first SugarSearch-native user problem before adding SugarBot
  coupling, networking, concurrency, persistence changes, or new algorithms.
