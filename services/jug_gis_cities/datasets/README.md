# `jug_gis_cities` Datasets

The [mock_data/](mock_data/) folder contains six synthetic input GeoPackages
for running the `mtl_fsa_gisoo` workflow with the example districts `T1A` and
`T2B`. The inventory below describes each file and its role in the workflow.

To use these inputs, update the `input_paths` entries in the main Sabu service's
`services/jug_gis_cities/src/jug_gis_cities/mtl_fsa_gisoo/workflow_config.py`
to point to the corresponding files in your local `datasets/mock_data/`
directory. Match each configured input to its role in the inventory below,
preserving the files' names, layer names, schemas, and CRS metadata.

## Input Inventory

Each file contains one spatial layer named after its filename without `.gpkg`.
Counts and CRS values below come from the supplied transfer note.

| File                                     | Role                                                | Geometry     | Features |  EPSG |
| ---------------------------------------- | --------------------------------------------------- | ------------ | -------: | ----: |
| `synthetic_assessment_role.gpkg`         | Property-assessment records                         | Point        |       18 |  4269 |
| `synthetic_auto_building.gpkg`           | Building footprints and heights                     | MultiPolygon |        4 |  4617 |
| `synthetic_auto_building_preserved.gpkg` | Preserved footprints for geometry restoration       | MultiPolygon |        4 |  4617 |
| `synthetic_predominant_uses.gpkg`        | Predominant-use records                             | MultiPolygon |       18 | 32188 |
| `synthetic_predominant_uses_dup.gpkg`    | Separate usage input for deduplication/intersection | MultiPolygon |       18 | 32188 |
| `synthetic_fsa.gpkg`                     | District boundaries                                 | MultiPolygon |        2 |  4269 |

## Schema and District Selection

Use `T1A` and `T2B` for these inputs. Montréal FSA codes in general service
documentation do not describe this example. Each selected value of `g_fsa`
must match exactly one boundary.

Significant fields include:

- Boundaries: `g_fsa`.
- Assessment: `id_provinc`, `roll_id`, and assessment/address attributes.
- Usage: `g_id_provi`, `g_sup_tota`, and `g_utilisat`.
- Buildings: `nrcan_id`, `bldgarea`, `_max`, and `_mean`.

Keep both the preserved-building and separate usage inputs, even when their
feature counts match another input. They serve distinct workflow roles.

If you use `JUG_GIS_CITIES_MTL_FSA_DATA_DIR` to set the data root, ensure that
the paths constructed in `workflow_config.py` resolve to these mock files.
Setting the environment variable alone does not select the synthetic inputs;
the `input_paths` entries must also reference them. See the
[direct Python guide](../examples/direct_python/README.md) for PyQGIS setup
and execution commands.

## Dataset Limitation

The provided test dataset is a compact example intended to demonstrate execution of the workflow. It does not reproduce the full range of data irregularities and preprocessing complexities encountered in the Montréal case study.
