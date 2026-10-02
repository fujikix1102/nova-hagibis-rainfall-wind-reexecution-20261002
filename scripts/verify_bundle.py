from pathlib import Path
import hashlib, json, sys

root=Path(".")
checks=[
 ("data/ibtracs_hagibis_2019.csv","bd9ba59e6f52b95704cc21d26eea16aeeeddaa726e99a962403acb0064633e3f"),
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
