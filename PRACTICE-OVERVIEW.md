# Engineering Practice - Overview

> The front door to how we run customer engagements: the workflows (engagement types) we deliver, how
> the practice gets better with every engagement (a governed **continuous-improvement loop**), and
> where to find the detailed doc for each workflow. Companion docs: `OPERATING-MODEL.md` (how we work)
> and `ENGAGEMENT-DOCUMENTATION-STANDARD.md` (what we deliver).
>
> Acronyms are spelled out on first use; a glossary is at the end.

## 1. It runs like an engineering department, not a tool

The right mental model is an **engineering department**, not a piece of software. Work is divided into
roles, standards are written down, decisions are recorded, and knowledge lives in a shared library that
every project draws from and adds to.

| Engineering-department role | In this practice |
|---|---|
| Principal architect / design authority | Reference architectures + the Architecture Recommendation |
| Implementation engineer | The executor + deployment workflows (e.g., the NAC-Starter kit) |
| QA (Quality Assurance) / reviewer | Validation gates, render gate, "validate to the wire" |
| Standards & governance office | AEW (AI Engineering Workbench) + the Engagement Documentation Standard + ADRs (Architecture Decision Records) |
| Knowledge base / design library | Persistent memory + versioned repositories + sanitized exemplars |
| PMO (Project Management Office) / change control | Project_State, the status board, and Human Authority approval |

## 2. The continuous-improvement loop

The practice **improves itself with every engagement** - honestly, and without overclaiming. The AI
models do **not** retrain on your data; what gets smarter is the **collective knowledge base**. Each
engagement runs this loop:

1. **Deliver** the engagement to the documentation standard.
2. **Capture** - lessons, fixes, and better patterns are *proposed* to the collective.
3. **Review** - Human Authority vets each proposed improvement (nothing enters unvetted).
4. **Adopt** - approved improvements are merged into standards, reference designs, and memory.
5. **Inherit** - the next engagement starts from that improved baseline.

Because the review step is mandatory, the collective gets **smarter and stays accurate** - a bad
lesson from one project can't silently propagate into the next customer's design. That governance step
is the trust argument, not a limitation.

> **Honest one-liner:** *A continuous-improvement loop - projects propose improvements, the practice
> reviews and adopts them, and every future engagement runs on the better baseline.* It learns the way
> a disciplined engineering department learns (documented standards + a growing design library, under
> review), not by letting an algorithm quietly retrain itself on your network.

## 3. Workflows (engagement types)

The same operating model and guardrails apply to every workflow below; each has its own detailed doc.

| # | Workflow | What it covers | Detailed doc |
|---|---|---|---|
| 1 | **Wireless & wired (Mist) design + deploy** | Juniper Mist WLAN/RF/switch design, template rollout, optimization, best-practice audit. | `mist-reference-designs/` (templates + principles); NAC-Starter Phase 1 |
| 2 | **NAC & guest access** | Network Access Control - 802.1X, guest onboarding, and CoA (Change of Authorization) with Aruba ClearPass and/or Mist Access Assurance. | `NAC-Starter` (public kit + deployment guide); `lab-documentation/design/mist-clearpass-guest-coa/` |
| 3 | **Campus / switching architecture** | Layer-2/Layer-3 campus design, VLAN (Virtual LAN) segmentation, EVPN-VXLAN growth path. | Sanitized campus-switching exemplar (`NAC-Starter/examples/sample-engagement/`) |
| 4 | **Secure remote access** | Juniper SRX / Secure Connect VPN, certificate authentication to AD (Active Directory). | *Doc to be written* (grounded in the vSRX Secure Connect lab) |

## 4. The backbone every workflow shares

- **How we work:** `OPERATING-MODEL.md` - the guardrails, change/validation gates, and roles/authority.
- **What we deliver:** `ENGAGEMENT-DOCUMENTATION-STANDARD.md` - Discovery -> ADR -> Architecture
  Recommendation -> DESIGN -> topology drawing -> deployment/validation review.
- **Where it's proven:** the lab is the reference environment where designs are validated *before* they
  reach a customer.

## 5. Glossary

| Term | Meaning |
|---|---|
| **AEW** | AI Engineering Workbench - the standards + schema + governance layer for engagements |
| **ADR** | Architecture Decision Record - a recorded design decision with context, options, and validation |
| **NAC** | Network Access Control |
| **CoA** | Change of Authorization (RADIUS dynamic authorization; udp/3799) |
| **NAD** | Network Access Device (e.g., an access point acting as the RADIUS client) |
| **RADIUS** | Remote Authentication Dial-In User Service |
| **HLD / LLD** | High-Level Design / Low-Level Design |
| **VLAN** | Virtual LAN |
| **AD** | Active Directory |
| **PMO** | Project Management Office |
| **SOW** | Statement of Work |

---

*Start here, then open the workflow doc you need. The operating model and documentation standard apply
across all of them.*
