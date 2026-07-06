# Engagement Documentation Standard

> Every engagement (and every reusable reference design) produces this documentation package. It is
> the deliverable set a professional Professional-Services engagement hands a customer, mapped onto the
> AEW `customer-template/` phases. Exemplars: `NAC-Starter/examples/sample-engagement/` and
> `lab-documentation/design/mist-clearpass-guest-coa/`.

## Required artifacts

| # | Artifact | AEW phase | Purpose / audience |
|---|---|---|---|
| 1 | **Discovery notes** | `01_Discovery` | What the customer has and needs; requirements, constraints, "what we need from them". |
| 2 | **ADR(s)** — decision records | `02_Engineering` | Each material design decision: context, options, trade-offs, decision, **validation**, revisit triggers. |
| 3 | **Architecture Recommendation** (with **Executive Summary**) | `03_HLD` | The recommended design and *why*, opening with a leadership-readable exec summary; options considered and set aside. |
| 4 | **DESIGN** — low-level design | `04_LLD` | Components, flows, exact config, ports, constraints. Implementable. |
| 5 | **Topology / flow drawing** | `03_HLD`/`04_LLD` | A real diagram (SVG/drawio), not ASCII. Auth flow / traffic flow / trust chain as needed. |
| 6 | **Baseline capture** | `05_Mist`/`06_Config` | Live pre-change state (config export) so change is diffable and reversible. |
| 7 | **Deployment / validation review** | `07_Deployment`/`08_Review` | What was deployed and **how the design was validated** — to the observable effect (wire/packet/behavior), not doc-conformance. |

## Standards

- **Validate to ground truth.** Every design claim that can be tested must have evidence (a packet, a
  behavior, a schema-validated render) — recorded in the ADR's *Validation* section and/or the
  deployment review, "reflected in config, not just documented."
- **Exec summary is mandatory** in the Architecture Recommendation (audience includes non-engineers).
- **Drawings are real files** (SVG/drawio), version-controlled next to the design.
- **Secrets never in the package** — reference `credentials.yml`; scrub before any external share.
- **Traceability:** the Recommendation cites the ADR(s); the DESIGN cites the Recommendation; the
  validation review cites the acceptance criteria.

## Minimum bar (small designs)

A compact reference design may collapse to four files (as in
`lab-documentation/design/mist-clearpass-guest-coa/`): `Architecture-Recommendation.md` (with exec
summary), `DESIGN.md`, one `ADR` (with the validation evidence), and one topology/flow `.svg` — plus a
pointer to the validation log. That is the floor; do not ship a design with fewer.
