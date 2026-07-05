# AI Engineering Workbench (AEW)

The **machine-readable structure layer** for AI-assisted engineering engagements. AEW provides:

- **`schemas/`** — canonical, validated data models. First: `Project_State` (the state of an engagement).
- **`customer-template/`** — the reusable engagement skeleton (nine numbered phases `00_Project`->`08_Review`). A new engagement is a copy of this.
- **`tools/`** — validators/utilities (stdlib + PyYAML only) the drift-check can run.
- **`specification/`** — concise engineering specs for each model.

## How it fits
- **ACEM** = the methodology (how we work).
- **AEW** = the structure/schema (the machine-readable shape of an engagement).
- **Customer projects** (Love Field, McKinney) = instances that adopt `customer-template/` and carry a `Project_State.yaml`.
- The Engineering Office drift-check validates each engagement's `Project_State.yaml` against `schemas/Project_State.schema.yaml`, surfacing phase/gate/blocker status automatically.

Source of truth: GitHub `hpe-networking-lab/AEW` (cloned at `/lab/github/AEW`).
