# Third-party re-execution

## Scope

This repository verifies the published Typhoon Hagibis rainfall/wind audit bundle. It does not redistribute the large GPM source files and does not make causal or formal calibration claims.

## Local run

```bash
python scripts/verify_reexecution.py
```

## Expected checks

- Published files exist.
- Filtered IBTrACS CSV SHA-256 matches the manifest.
- Production audit keeps `formal_pass: false`.
- Diagnostic status is explicit and fail-closed.

The GPM files can be re-downloaded from the source URL in the metadata ledgers and checked against their recorded SHA-256 values. Earthdata authentication may be required.
