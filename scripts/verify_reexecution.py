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
expected = "7b7db0b31590f9b82b3955ec644c69d9db675368a7a992ea9aa3f41ea50dd644"
if required[2].is_file():
    actual = hashlib.sha256(required[2].read_bytes()).hexdigest()
    print("filtered_csv_sha256:", actual)
    ok &= actual == expected
print("reexecution_verification:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
