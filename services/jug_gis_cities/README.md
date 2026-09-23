# `jug_gis_cities`

This folder contains test-input documentation, execution examples, results,
and timing materials for the `jug_gis_cities` service in the Sabu framework.

The current `mtl_fsa_gisoo` component uses CityGISOO/PyQGIS to clean and
integrate building footprints and heights, property-assessment records, and
predominant-use polygons by Forward Sortation Area (FSA). It can then
standardize the result for downstream building carbon assessment.

## Where to Look

- [datasets/](datasets/README.md): input descriptions and the `mock_data/`
  folder where the six prepared GeoPackages should be added manually.
- [examples/](examples/README.md): direct Python execution instructions.
- [results/](results/README.md): historical T1A/T2B outputs and separately
  exported preliminary GeoJSON files, with provenance and export details.
- [benchmarks/](benchmarks/README.md): historical execution log, timing
  summary, and notes for recording new measurements.
- [docs/](docs/README.md): configuration, output interpretation, source
  references, and dataset limitations.

## Required Inputs

The example requires six GeoPackages: assessment records, building footprints
and heights, preserved footprints, predominant uses, a separate usage input,
and FSA boundaries. Their filenames, layers, schemas, and CRS metadata must
be preserved. The supplied districts are `T1A` and `T2B`; each selected FSA
must match exactly one boundary. See the [input inventory](datasets/README.md).

Input files are not included in this initial structure. Add the prepared files
to `datasets/mock_data/` before running the example.

## Execution and Outputs

Use Python 3.10–3.12 configured for standalone PyQGIS and install the three
local Sabu packages with that interpreter. The example runs
`python -m jug_gis_cities --component mtl_fsa_gisoo` in `standardize` mode for
both districts, or in `independent` mode for a selected district.

Each district has its own output subdirectory. Independent execution produces
a preliminary GeoPackage. Standardized execution retains that file and adds
a standardized GeoPackage and GeoJSON containing building attributes,
provenance, FSA, area, and identifiers. These outputs contain no
carbon-calculation results. Preliminary GeoJSON requires a separate export.

For a first run, start with [examples/README.md](examples/README.md), then
follow the linked setup and execution instructions.

## Dataset Limitation

The provided test dataset is a compact example intended to demonstrate execution of the workflow. It does not reproduce the full range of data irregularities and preprocessing complexities encountered in the Montréal case study.
