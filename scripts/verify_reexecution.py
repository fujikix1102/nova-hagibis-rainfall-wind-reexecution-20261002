from pathlib import Path
import hashlib, json, sys

root = Path(__file__).parents[1]
required = [
    root / "metadata" / "nova_meteorology_production_audit_20261002_v1.json",
    root / "metadata" / "wind_addition_analysis_contract_20261002.json",
    root / "data" / "ibtracs_hagibis_2019.csv",
]
ok = True
for path in required:
    if not path.is_file():
        print("MISSING", path)
        ok = False
audit = json.loads(required[0].read_text()) if required[0].is_file() else {}
if audit.get("formal_pass") is not False:
    print("FAIL formal_pass must remain false")
    ok = False
result = audit.get("result", {})
if result.get("audit_status") not in {"RECORDED", "UNVERIFIED"}:
    print("FAIL unexpected audit status")
    ok = False
expected = "bd9ba59e6f52b95704cc21d26eea16aeeeddaa726e99a962403acb0064633e3f"
if required[2].is_file():
    actual = hashlib.sha256(required[2].read_bytes()).hexdigest()
    print("filtered_csv_sha256:", actual)
    ok &= actual == expected
print("reexecution_verification:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
