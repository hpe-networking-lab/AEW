#!/usr/bin/env python3
"""Workbench status board: find every Project_State.yaml under /lab/github, validate it, and
summarize phase / open blockers / pending gates. Read-only. stdlib + PyYAML only.
Exit nonzero if any Project_State is invalid."""
import os, glob, yaml, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from validate_project_state import validate, load, SCHEMA
schema=load(SCHEMA)
found=[p for p in glob.glob("/lab/github/**/Project_State.yaml",recursive=True)
       if "/ai-engineering-workbench/customer-template/" not in p]
bad=0
print(f"Engagement status board ({len(found)} Project_State file(s)):")
if not found:
    print("  (none yet - engagements adopt customer-template/ and add 00_Project/Project_State.yaml)")
for p in sorted(found):
    try:
        inst=load(p); errs=validate(inst,schema)
        repo=p.split("/lab/github/")[1].split("/")[0]
        if errs:
            bad+=1; print(f"  [INVALID] {repo}: {errs[0]}"+(f" (+{len(errs)-1} more)" if len(errs)>1 else "")); continue
        ob=[b for b in inst.get("blockers",[]) if b.get("status")=="open"]
        pg=[g for g in inst.get("approval_gates",[]) if g.get("status")=="pending"]
        print(f"  {repo}: phase={inst.get('current_phase')} open_blockers={len(ob)} pending_gates={len(pg)}")
    except Exception as e:
        bad+=1; print(f"  [ERROR] {p}: {str(e)[:80]}")
sys.exit(1 if bad else 0)
