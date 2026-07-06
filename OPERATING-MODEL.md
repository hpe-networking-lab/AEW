# Lab Engineering Operating Model

> How this lab runs as a **governed engineering platform** rather than a collection of gear: the
> layers we build in, the guardrails that hold it together, and the proof points that show the model
> works. This is a durable reference — it captures the operating model and the reflexes behind it, and
> supersedes ad-hoc practice. Companion to `ENGAGEMENT-DOCUMENTATION-STANDARD.md`.

## 1. The platform, in layers

The core accomplishment is not any single deliverable — it is that the lab now behaves like an
engineering system. That system has distinct, reinforcing layers:

| Layer | What it is | Lives in |
|---|---|---|
| **Ground truth** | Inventory reconciled *from live* (Mist / ESXi / AD): live is truth, YAMLs are intent; a daily drift-check keeps them honest. Printable lab reference (hosts, VMs, Tailscale, MCP/tool surface). | `lab-documentation/`, `automation-scripts/` (`reconcile_inventory.py`) |
| **Reference architecture + standards** | Validated Mist template set (WLAN/RF/switch/site/firmware/PSK) + interop playbook. Every change follows the template playbook. | `mist-reference-designs/` |
| **Engagement methodology** | A repeatable deliverable shape: Discovery -> ADR -> Architecture Recommendation (exec-summary first) -> DESIGN -> topology drawing -> deploy/validation review. | `AEW/ENGAGEMENT-DOCUMENTATION-STANDARD.md`; exemplar `mckinney-isd/` |
| **AIOS runtime** | The systems-engineering backbone: an ADR-driven, stdlib-only runtime (secret store, provider transport, SQLite persistence, networked transport, remote auth, remote Git, observability, application shell). | `AIOS/` |
| **AEW governance layer** | Project_State schema + validator + status-board scanner wired into drift-checking — the structure that makes many engagements trackable and inheritable. | `AEW/` |
| **Productized knowledge** | Sanitized, customer-ready output: the public NAC-Starter kit and its sanitized worked example. | `NAC-Starter` (public), `AEW`/`mckinney-isd` (sanitized exemplars) |

## 2. Operating principles (guardrails)

The durable part. These are the reflexes that make the work safe to hand to a customer and repeatable
next time.

- **Facts before assumptions; Git is the source of truth.** Live is truth, YAML is intent; reconcile
  continuously. Verify reads/writes against the object the system actually consumes, never the echo.
- **Validate to the wire, not to doc-conformance.** Reproduced-symptom is not root cause. If a finding
  implies a mature product is broadly broken, suspect your own setup first. *(The single most valuable
  reflex — the difference between a demo and something you would stake an engagement on.)*
- **Ground before you assert.** UI paths, facts, and system state are verified against official docs or
  the live machine before being stated.
- **Architecture-first; approved artifacts immutable.** No speculative implementation; change goes
  through ADRs; linear history; commit logical units. Respect the project boundary — a project stays
  itself and neighboring projects do not bleed in.
- **Standards must be explicitly inherited.** Committing a standard to a repo does not make a chat
  follow it; each grounding must say "read and follow this." (Closes the standards-inheritance gap.)
- **Human Authority is preserved.** Claude recommends; it does not self-approve. Review-before-public,
  secrets discipline, and least-privilege machine control all funnel to explicit sign-off.
- **Defend the reference architecture.** Engagement work challenges deviations rather than merely
  implementing them — opinionated guardian, not order-taker.
- **Fix structural gaps quietly; escalate only genuine approvals.** A wrong assumption or stale-data
  slip is a signal that a gap exists; close it automatically and hand back only real decisions.
- **Secrets discipline.** Secrets live only in a gitignored `credentials.yml`; scripts read them; never
  hardcode, print, or commit; verify presence, not value; never enter secrets in chat.

## 3. Change & validation gates

- **Mist template playbook (binding):** golden object -> lint -> inert deploy -> render gate -> verify
  against the consuming object.
- **Review-before-public:** any public push (repos, sanitized samples) gets a zero-tolerance
  sanitization scan **and** explicit Human-Authority approval before release.
- **Least-privilege compute:** per-application grants; Claude's own window is off-limits; the Windows
  shell (Start/search) and elevated/admin surfaces stay with the operator.

## 4. Proof points

Evidence the model produces results a customer would accept:

- **Cisco-free guest CoA — wire-proven.** Root-caused (ClearPass ships in-place Reauthenticate only for
  Cisco/Tellabs) and proved the all-Juniper alternative: NAD Vendor=Juniper + `[Juniper Terminate
  Session]` yields a Disconnect-Request (code 40) on udp/3799.
- **Juniper Secure Connect cert-auth needs external RADIUS.** The SRX cannot validate client certs over
  LDAP; a real engineering finding, not a config workaround.
- **Public NAC-Starter kit** with a guided wizard, repo-scoped executor, and a sanitized worked example
  — customer-ready, no private-repo access required.
- **Engagement documentation standard** codified and exemplified (McKinney sanitized to Westfield with
  zero residual identifiers).

## 5. Roles & authority

- **Human Authority** is the sole approval authority. Claude may recommend approval; it may not
  self-approve.
- **Coordinator model:** the coordinator context is the hub — it does cross-cutting governance and
  standards work directly and routes deep engagement work to specialized contexts.

---

*Throughline: the lab is a governed engineering system — grounded in live truth, driven by reference
architecture, producing consistent engagement documentation, under Human Authority — and "validate to
the wire" is the reflex that keeps the whole thing honest.*
