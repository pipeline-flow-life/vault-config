---
template: water-source-assessment
type: workflow
version: 0.1
status: draft
reference_run: Well Water Test 2026-06-29 (Google Drive, Pipeline/)
data_location: google-drive   # test results live in Drive, never in this repo
---

# Template: Water Source Assessment

Assess a water source (dug well, drilled well, cistern, rainwater catchment) for its intended use, track results over time, and turn flags into to-dos.

## Inputs
- source_id, source_type (dug well, drilled well, cistern, catchment), location
- intended_use (irrigation, livestock, household non-potable, potable)
- test_date, test_method (strip kit, lab), kit_name

## Results table (one row per parameter)
| grouping | order | test | measure | result | flag |
- grouping: kit panel (for example 16-in-1, 4-in-1, single tests)
- flag: blank, questionable, fail, or follow-up

## Stages
1. Baseline: run the full panel, record every parameter including zeros
2. Flag: mark results outside the threshold for the intended use
3. Plan: create a to-do per flag (retest, lab confirm, remediate)
4. Remediate: log actions against the source
5. Retest: same panel, same method, compare to baseline
6. Close: record the use the source is cleared for

## Ticket fields
status, source, intended_use, tests[] (date, method, results link), flags[], todos[], cleared_for

## Guardrails
- Strip kits are screening only; anything flagged for potable use gets a lab test
- Results stay in Drive; this file holds structure only
