# Direct Python Execution

These instructions run the current `mtl_fsa_gisoo` component using the main
Sabu checkout and this repository's service-specific folders.

## Environment

Use Python 3.10–3.12 configured for standalone PyQGIS, including QGIS
Processing/native providers and matching GDAL/Qt resources. Activate that
environment so `python` resolves to its interpreter before proceeding.
Installing the service with pip alone does not configure standalone PyQGIS.
See `libs/citygisoo/README.md` in the main Sabu checkout for environment setup.

The transfer note records `sabu-chassis` 0.1.1, `citygisoo` 0.3, and
`jug_gis_cities` 0.1.0. Editable installation resolves declared dependencies,
including GeoPandas, Shapely ≥2, PyProj, pandas, requests, Flask 3.1.1,
flask-smorest 0.46.1, and marshmallow. These observations are not an exact
environment lock; see [configuration notes](../../docs/README.md).

## Install and Configure

In PowerShell, replace both repository placeholders and the QGIS prefix with
absolute paths for your environment. The six prepared files must already be
in `services/jug_gis_cities/datasets/mock_data/` in this repository.

```powershell
Set-Location "<sabu-root>"
python -m pip install -e .\libs\sabu_chassis
python -m pip install -e .\libs\citygisoo
python -m pip install -e .\services\jug_gis_cities

$exampleRepo = "<sabu-test-data-and-examples-root>"
$serviceDir = "$exampleRepo\services\jug_gis_cities"
$env:JUG_GIS_CITIES_MTL_FSA_DATA_DIR = "$serviceDir\datasets"
$env:JUG_GIS_CITIES_MTL_FSA_OUTPUT_DIR = "$serviceDir\results"
$env:JUG_GIS_CITIES_QGIS_PATH = "<matching-QGIS-prefix>"
$env:LOG_DIR_BASE = "$serviceDir\benchmarks"
$env:LOG_FILE_NAME = "jug_gis_cities.log"
```

`JUG_GIS_CITIES_MTL_FSA_DATA_DIR` points to the parent of `mock_data`, and the
output root receives an FSA subdirectory automatically. The active
`mtl_fsa_gisoo/workflow_config.py` already selects the synthetic filenames.

The repository includes historical mock outputs and separate real-data FSA
logs. For a new mock run, select a fresh output root and a descriptive log
filename before execution, for example:

```powershell
$env:JUG_GIS_CITIES_MTL_FSA_OUTPUT_DIR = "$serviceDir\results\new_run"
$env:LOG_FILE_NAME = "jug_gis_cities_new_run.log"
```

## Run Both Districts and Standardize

```powershell
python -m jug_gis_cities --component mtl_fsa_gisoo --mode standardize --all-fsas --max-workers 2
```

With the supplied boundary input, this runs `T1A` and `T2B`, including the
preliminary workflow and subsequent standardization. Use `--fsas T1A T2B`
instead of `--all-fsas` to select them explicitly.

## Run One District Independently

```powershell
python -m jug_gis_cities --component mtl_fsa_gisoo --mode independent --fsa T1A
```

This produces the preliminary GeoPackage. It does not apply the contract
adapter. A separate independent run is unnecessary when standardized mode
has already retained that preliminary file.

## Options and Results

- `--drop-null-fields FIELD ...`: optionally remove features missing selected
  standardized attributes during standardization. Default execution does not
  remove features based on null attributes.
- `--cleanup-outputs`: delete intermediates after success, retaining the
  boundary, repaired buildings, assessment layer, repaired usage layer,
  preliminary result, and standardized outputs. Without this option all
  intermediates remain.
- `--keep-output KEY`: repeat to retain additional intermediate outputs when
  cleanup is enabled. Use keys from `workflow_config.py` in the main checkout.

See [results](../../results/README.md) for output paths and the separate
Python export procedure for preliminary GeoJSON, and
[benchmarks](../../benchmarks/README.md) for timing scope and run metadata.
