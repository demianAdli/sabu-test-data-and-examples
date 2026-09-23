# `jug_gis_cities` Supporting Documentation

## Workflow and Configuration

The `mtl_fsa_gisoo` component cleans and integrates footprints/heights,
assessment points, and predominant-use polygons within each selected FSA.
Preserved footprints support geometry restoration; a separate usage input
supports deduplication/intersection. The
[input inventory](../datasets/README.md) describes the six files and schemas.

All example paths follow this repository's `services/jug_gis_cities/`
organization. The category-first paths in the transfer note have been adapted
to this service-specific layout.

| Environment variable | Meaning in this repository |
| --- | --- |
| `JUG_GIS_CITIES_MTL_FSA_DATA_DIR` | Absolute path to `services/jug_gis_cities/datasets/`; the workflow appends `mock_data/` |
| `JUG_GIS_CITIES_MTL_FSA_OUTPUT_DIR` | Output root, usually `services/jug_gis_cities/results/`; the workflow appends the FSA |
| `JUG_GIS_CITIES_QGIS_PATH` | QGIS prefix matching the active interpreter and installation |
| `LOG_DIR_BASE` | Optional log directory, usually `services/jug_gis_cities/benchmarks/` |
| `LOG_FILE_NAME` | Optional log filename, such as `jug_gis_cities.log` |

The main service README mentions a `pyqgis44` environment. The transfer note
records `C:/QGIS_I~1/OSGeo4W/apps/qgis-ltr` as a historical QGIS prefix. Neither is
an exact reproducible version lock or a portable installation path. Use a
matching standalone PyQGIS environment and record its actual versions.

## Output Interpretation

The preliminary GeoPackage contains the integrated, unstandardized attributes.
`contract_adapter.py` defines selection, renaming, and ordering of standardized
fields, with numeric IDs starting at `100000`. Standardized outputs carry
building attributes, provenance, FSA, area, and identifiers for downstream
assessment; they contain no carbon-calculation results.

Null attributes are retained by default. The optional `--drop-null-fields`
selection changes which features survive standardization. Generated UUIDs
vary between runs. Consult the [results guide](../results/README.md) for the
published artifacts, CRS, provenance, and preliminary export procedure.

## Source References

The supplied main-repository transfer note is the technical source for these
instructions. The following paths are relative to the **main Sabu root**:

- `services/jug_gis_cities/README.md`: local installation and direct execution.
- `services/jug_gis_cities/src/jug_gis_cities/__main__.py`: command-line interface.
- `services/jug_gis_cities/src/jug_gis_cities/mtl_fsa_gisoo/`: `workflow.py`,
  `workflow_config.py`, `contract_adapter.py`, and `output_cleanup.py`.
- `services/jug_gis_cities/src/jug_gis_cities/application/`: execution
  orchestration and `fsa_batch_runner.py`.
- `services/jug_gis_cities/draft_cities/test_config_mtl_fsa.py`: synthetic
  configuration reference, not a test runner.
- `libs/citygisoo/README.md`: standalone PyQGIS setup.
- `libs/citygisoo/src/citygisoo/`: cleaning, feature processing, schema
  management, and contract-adapter implementation.
- `services/jug_gis_cities/pyproject.toml`, `libs/sabu_chassis/pyproject.toml`,
  and `libs/citygisoo/pyproject.toml`: declared dependencies.

## Dataset Limitation

The provided test dataset is a compact example intended to demonstrate execution of the workflow. It does not reproduce the full range of data irregularities and preprocessing complexities encountered in the Montréal case study.
