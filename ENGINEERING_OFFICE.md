# Engineering Office - AI Engineering Workbench (AEW) Grounding

Read this first. This repo defines the **schema/structure layer** for engagements. It does NOT run
customer work and does NOT hold secrets.

**Scope:** build and maintain `schemas/`, `customer-template/`, `tools/`, `specification/`. Schema-first,
additive, validated. stdlib + PyYAML only (no heavy deps). Never modify customer orgs.

**Where it lives:** github.com/hpe-networking-lab/AEW, cloned at
`/lab/github/AEW` on the Utility (192.168.86.44). Commit/push from there.

## Standards (binding)
At self-ground, read and follow all of `mist-reference-designs/best-practices/` (the whole folder,
binding as it grows). Deviations from the reference architecture are called out and justified
(REVIEW-POSTURE); every schema change ships with a validator run and a spec update (VALIDATION);
check the capabilities index before saying a tool doesn't exist (TOOLSET-AWARENESS). Updates to these
standards apply automatically - no re-grounding.

## Method
Work in disciplined increments. Each change: update the schema/model, update the validator + spec,
run `python3 tools/validate_project_state.py`, keep the tree clean, commit a logical unit.

## Sharing fixes system-wide
Reusable lessons -> a proposal in `mist-reference-designs/proposals/` (never self-promote). The
coordinator promotes; every chat inherits on next self-ground.

## Style
Concise and opinionated. Anything to copy/paste is a single clean fenced code block.

## Engineering method (binding)

At self-ground, read and follow `lab-documentation/reference/ENGINEERING-METHOD.md` — the
order-of-authority discipline for any vendor-product work: vendor doc / reference config → the
device's own outputs (metadata, traceoptions, stats are documentation) → controlled lab
confirmation; never live trial-and-error, and hardest to hold under a deadline. Binding for
build and operate chats alike; updates apply without re-issuing this grounding.
