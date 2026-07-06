# Operating Model - Customer Engagements

> How we run **customer engagements** as a governed engineering practice - the same discipline across
> every workflow (wireless & wired, NAC, campus/switching, secure remote access). The lab is the
> reference environment where designs are validated before they reach a customer. Read alongside
> `PRACTICE-OVERVIEW.md` (the front door + the continuous-improvement loop) and
> `ENGAGEMENT-DOCUMENTATION-STANDARD.md` (the deliverable set).
>
> Acronyms are spelled out on first use; a glossary lives in `PRACTICE-OVERVIEW.md`.

## 1. What the practice is built from

The core capability is that engagements run like an engineering department rather than ad-hoc project
work, on reinforcing layers:

| Layer | What it is | Lives in |
|---|---|---|
| **Ground truth** | Inventory reconciled *from live* (Mist / ESXi / AD [Active Directory]): live is truth, the intent files are intent; a daily drift-check keeps them honest. | `lab-documentation/`, `automation-scripts/` (`reconcile_inventory.py`) |
| **Reference architecture + standards** | Validated Juniper Mist template set (WLAN/RF/switch/site/firmware/PSK) + interop playbook. Every change follows the template playbook. | `mist-reference-designs/` |
| **Engagement methodology** | A repeatable deliverable shape: Discovery -> ADR (Architecture Decision Record) -> Architecture Recommendation (executive-summary first) -> DESIGN -> topology drawing -> deployment/validation review. | `AEW/ENGAGEMENT-DOCUMENTATION-STANDARD.md`; sanitized exemplar `NAC-Starter/examples/sample-engagement/` |
| **Governance layer** | AEW (AI Engineering Workbench): Project_State schema + validator + status-board scanner wired into drift-checking - the structure that makes many engagements trackable and inheritable. | `AEW/` |
| **Productized knowledge** | Sanitized, customer-ready output: the public NAC-Starter kit and its sanitized worked example. | `NAC-Starter` (public) + its sanitized worked example `examples/sample-engagement/` |

## 2. Operating principles (guardrails)

The durable part - the reflexes that make the work safe to hand to a customer and repeatable next time.

- **Facts before assumptions; Git is the source of truth.** Live is truth, intent files are intent;
  reconcile continuously. Verify reads/writes against the object the system actually consumes, never
  the echo.
- **Validate to the wire, not to doc-conformance.** Reproduced-symptom is not root cause. If a finding
  implies a mature product is broadly broken, suspect your own setup first. *(The single most valuable
  reflex - the difference between a demo and something you would stake an engagement on.)*
- **Ground before you assert.** UI paths, facts, and system state are verified against official docs or
  the live system before being stated.
- **Architecture-first; approved artifacts immutable.** No speculative implementation; change goes
  through ADRs; linear history; commit logical units.
- **Standards must be explicitly inherited.** Committing a standard to a repository does not make a work
  context follow it; each grounding must say "read and follow this."
- **Defend the reference architecture.** Engagement work challenges deviations rather than merely
  implementing them - opinionated guardian, not order-taker.
- **Fix structural gaps quietly; escalate only genuine approvals.** A wrong assumption or stale-data
  slip is a signal that a gap exists; close it and hand back only real decisions.
- **Secrets discipline.** Secrets live only in a gitignored `credentials.yml`; scripts read them; never
  hardcode, print, or commit; verify presence, not value; never enter secrets in chat.

## 3. What changes in a customer / production context

The lab is where we earn the right to run fast; a customer is where the same discipline runs
deliberately. Three guardrails get **stronger**, and the autonomous mode gets **narrower**:

- **Authority becomes two-party.** In the lab there is a single Human Authority. At a customer, the
  customer owns production risk, change windows, and go/no-go; we own the engineering recommendation.
  Every write to their environment needs their change approval, a maintenance window, and a documented
  rollback - not just our sign-off.
- **Change is gated and reversible.** Dry-run -> inert / render-gate -> customer approval -> scheduled
  change -> verify -> backout plan ready. Baseline capture before any change so it is diffable and
  reversible.
- **Their data is protected.** Least-privilege, scoped access into their systems (read-only first);
  their secrets never land in our repositories; and the sanitization gate protects *their* identifiers
  before anything reaches a shared or public artifact.

## 4. Change & validation gates

- **Mist template playbook (binding):** golden object -> lint -> inert deploy -> render gate -> verify
  against the consuming object.
- **Review-before-public:** any public release (repositories, sanitized samples) gets a zero-tolerance
  sanitization scan **and** explicit Human-Authority approval before it goes out.
- **Least-privilege compute:** per-application grants; the assistant's own window is off-limits; the
  operating-system shell and elevated/admin surfaces stay with the operator.

## 5. The continuous-improvement loop

Each engagement makes the practice better without the models retraining on customer data. Improvements
are **proposed** by a project, **reviewed** by Human Authority, **adopted** into standards/designs/
memory, and **inherited** by the next engagement. The collective knowledge gets smarter and stays
accurate because nothing enters unvetted. See `PRACTICE-OVERVIEW.md` for the full loop.

## 6. Proof points

- **Cisco-free guest CoA (Change of Authorization) - wire-proven.** Root-caused (ClearPass ships an
  in-place Reauthenticate action only for Cisco/Tellabs) and proved the all-Juniper alternative: NAD
  (Network Access Device) Vendor=Juniper + `[Juniper Terminate Session]` yields a Disconnect-Request
  (code 40) on udp/3799.
- **Juniper Secure Connect certificate auth needs external RADIUS.** The SRX cannot validate client
  certs over LDAP; a real engineering finding, not a config workaround.
- **Public NAC-Starter kit** with a guided wizard, a repository-scoped executor, and a sanitized worked
  example - customer-ready, no private-repository access required.
- **Engagement documentation standard** codified and exemplified (a real engagement sanitized with zero residual
  identifiers).

## 7. Roles & authority

- **Human Authority** is the sole approval authority for our side; the **customer** owns production
  approval, change windows, and go/no-go. The assistant may recommend approval; it may not self-approve.
- **Coordinator model:** a coordinator context is the hub - it does cross-cutting governance and
  standards work directly and routes deep engagement work to specialized contexts.

---

*Throughline: customer engagements run as a governed engineering system - grounded in live truth,
driven by reference architecture, producing consistent documentation, under two-party authority - and
"validate to the wire" is the reflex that keeps the whole thing honest.*
