from pathlib import Path
import hashlib, json, sys

root=Path(".")
checks=[
 ("data/ibtracs_hagibis_2019.csv","7b7db0b31590f9b82b3955ec644c69d9db675368a7a992ea9aa3f41ea50dd644"),
]
ok=True
for path,expected in checks:
    actual=hashlib.sha256((root/path).read_bytes()).hexdigest()
    print(f"{path}: {actual}")
    ok &= actual==expected
for path in root.glob("metadata/*.json"):
    data=json.loads(path.read_text())
    if data.get("formal_pass") is True:
        print(f"FAIL: formal_pass true in {path}")
        ok=False
print("bundle_integrity:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
