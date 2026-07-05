#!/usr/bin/env python3
"""Validate a Project_State.yaml against schemas/Project_State.schema.yaml.
Schema-driven (reads required/enums from the schema). stdlib + PyYAML only.
Usage: validate_project_state.py [path]  (default: the customer-template instance). Exit nonzero on invalid."""
import sys, os, yaml
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA=os.path.join(ROOT,"schemas","Project_State.schema.yaml")
def load(p): return yaml.safe_load(open(p))
def validate(inst, schema):
    props=schema["properties"]; errs=[]
    have=set(inst) if isinstance(inst,dict) else set()
    for m in set(schema["required"])-have: errs.append(f"missing top-level field: {m}")
    if schema.get("additionalProperties") is False:
        for x in have-set(props): errs.append(f"unexpected top-level field: {x}")
    for key in ("project","customer","audit"):
        v=inst.get(key)
        if not isinstance(v,dict): errs.append(f"{key} must be an object"); continue
        for x in set(v)-set(props[key]["properties"]): errs.append(f"{key}: unexpected field '{x}'")
    cp=inst.get("current_phase")
    if cp not in props["current_phase"]["enum"]: errs.append(f"current_phase '{cp}' not allowed")
    for key in ("phases","approval_gates","artifacts","blockers"):
        arr=inst.get(key)
        if not isinstance(arr,list): errs.append(f"{key} must be an array"); continue
        it=props[key]["items"]
        for i,item in enumerate(arr):
            if not isinstance(item,dict): errs.append(f"{key}[{i}] not an object"); continue
            for m in set(it["required"])-set(item): errs.append(f"{key}[{i}] missing '{m}'")
            for f,fs in it["properties"].items():
                if f in item and "enum" in fs and item[f] not in fs["enum"]:
                    errs.append(f"{key}[{i}].{f}='{item[f]}' not in {fs['enum']}")
    return errs
if __name__=="__main__":
    target=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,"customer-template","00_Project","Project_State.yaml")
    errs=validate(load(target), load(SCHEMA))
    if errs:
        print(f"INVALID: {target}"); [print("  -",e) for e in errs]; sys.exit(1)
    print(f"VALID: {target}"); sys.exit(0)
