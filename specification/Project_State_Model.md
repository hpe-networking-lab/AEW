# Project_State Model

## Purpose
`Project_State` is the single machine-readable record of where a customer engagement stands. Tools
(the Engineering Office drift-check, generators) read/validate it; humans read the same file.

## Scope
State only - not customer data, BOM, HLD/LLD, or Mist config. One `Project_State.yaml` per engagement,
under `00_Project/`.

## Top-level fields
`version`, `project`, `customer`, `current_phase`, `phases`, `approval_gates`, `artifacts`, `blockers`,
`audit`. The top level is closed (no extra fields).

## Lifecycle phases
`00_Project -> 01_Discovery -> 02_Engineering -> 03_HLD -> 04_LLD -> 05_Mist -> 06_Config ->
07_Deployment -> 08_Review`. `current_phase` names where the engagement is now; `phases[]` carries each
phase's status (`not_started`/`in_progress`/`blocked`/`complete`/`approved`).

## Approval gate behavior
Each gate binds to a phase (`required_for_phase`) and holds a status
(`not_required`/`pending`/`approved`/`rejected`). A phase should not advance past a gate that is
`pending` or `rejected` - the Human Authority approves gates.

## Artifact status behavior
Each artifact (`path`,`type`) carries `missing`/`placeholder`/`draft`/`review`/`approved`/`generated`,
tracking a deliverable from empty to produced.

## Blocker behavior
Each blocker (`id`,`description`) has `severity` (`low`->`critical`) and `status`
(`open`/`resolved`/`deferred`). Open `high`/`critical` blockers gate advancement.

## Audit behavior
`created_by`/`last_updated_by`/`last_reviewed_by` record responsibility. Not a full history (git carries that).
