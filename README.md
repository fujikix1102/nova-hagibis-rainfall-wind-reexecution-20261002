# NOVA: Typhoon Hagibis rainfall and wind re-execution

Public reproducibility bundle for a descriptive analysis of Typhoon Hagibis (2019).

## Scope

- JMA official event and rainfall records
- NASA GPM IMERG daily precipitation
- NOAA IBTrACS track, wind, and pressure
- UTC-aligned descriptive comparison
- Track-proximity rainfall within 2 coordinate degrees

This repository does not claim rainfall causality, sensor calibration, hazard prediction, return periods, or formal physical validation. `formal_pass: false` is intentional.

## Data policy

The large original GPM files are not redistributed here. Their SHA-256 values and source metadata are preserved in the local NOVA audit ledger. The filtered IBTrACS event CSV is included.

## Re-execution

Use the JSON ledgers in `metadata/` to reproduce the fixed time basis, units, bounding box, source hashes, and claim boundary. All dates in the joined analysis are UTC calendar dates.

## Source URLs

- NOAA IBTrACS: https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/csv/ibtracs.ALL.list.v04r01.csv
- JMA Typhoon 1919 report: https://www.data.jma.go.jp/stats/data/bosai/report/2019/20191012/20191012.html
- NASA GPM IMERG data service: https://data.gesdisc.earthdata.nasa.gov/

## License and reuse

Source data remain subject to their original terms. This repository contains audit metadata and derived descriptive outputs.
