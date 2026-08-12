# SugarBot Integration Horizon

This document is direction, not an implemented contract. SugarSearch and
SugarBot remain independent today.

## Architectural Fit

SugarSearch already treats every evaluated system as an opaque process:
candidate values go in as command-line flags and one row of numeric metrics
comes back through a trial-specific CSV file. That is a useful first bridge to
SugarBot because it avoids importing SugarBot internals or weakening either
project's ownership boundaries.

The first integration should be an adapter outside the `sugarsearch` core. The
adapter would translate a SugarSearch candidate into an accepted SugarBot run
configuration, invoke the supported local SugarBot surface, extract declared
numeric objectives from the authoritative report, and write the exact metrics
CSV SugarSearch already understands.

## Staged Direction

1. **Re-discover the live SugarBot contract.** Start with `--help` and
   `--onramp`, then verify current report fields and exit behavior against a
   real local run. Do not design against remembered or copied schemas.
2. **Build a narrow opaque-worker adapter.** Keep it outside `sugarsearch` and
   make accepted Data CSV, Layout JSON, and Logic JSON explicit inputs. Preserve
   the full SugarBot result package separately; the one-row metrics CSV is only
   SugarSearch's optimization observation.
3. **Add provenance and deterministic validation.** Record the SugarSearch
   candidate, accepted artifact identities, adapter version, SugarBot runtime
   version, report location, and failure reason for every trial.
4. **Add richer machine-readable results only by decision.** SugarBot reports
   contain more information than one CSV row. Define a versioned result
   envelope before exposing traces, objective components, diversity, geometry,
   or Pareto details directly to SugarSearch.
5. **Integrate with SugarStudio at its deployment boundary.** If the workflow
   becomes LAN-accessible, SugarDeploy remains the API boundary and SugarBot
   remains loopback-only. Do not expose SugarBot's raw service port through
   SugarSearch.

## Required Gates Before Implementation

- A concrete user workflow that explains what SugarSearch varies and what
  SugarBot evaluates.
- A versioned mapping from candidate parameters to SugarBot inputs.
- A declared metric catalog with direction, units, missing-value behavior, and
  eligibility rules.
- Cancellation and timeout behavior across both processes.
- Isolation rules for per-trial artifacts and secrets.
- A small deterministic end-to-end fixture before any large search run.

## Explicit Non-Goals for the Bootstrap

- No SugarBot imports in the `sugarsearch` package.
- No new network listener.
- No LAN exposure of a loopback SugarBot runtime.
- No model-generated artifact promotion or bypass of deterministic validation.
- No reduction of the full SugarBot report to a claimed universal winner.
