# `jug_gis_cities` Results

This folder contains historical example outputs for `T1A` and `T2B`, copied
from `D:/GIS/mtl_gisoo_fsa_data/output_data/` on 2026-09-23, plus separate
preliminary GeoJSON exports made from those copied GeoPackages. The source
files had modification dates of 2026-09-21. No cleaning or standardization
workflow was rerun during this transfer.

These artifacts illustrate the output structure. Their exact input checksums
and generation environment were not recorded with the source artifacts, so
they are not verified results for the files that will be added to `datasets/`.
[artifact_inventory.csv](artifact_inventory.csv) records source paths,
SHA-256 checksums, feature counts, and CRS for the published files.

## Output Layout

For each `<FSA>` (`T1A` or `T2B`), paths are relative to the configured output
root:

```text
<FSA>/
|-- mtl_<FSA>_gisoo/
|   |-- mtl_<FSA>_gisoo.gpkg
|   `-- mtl_<FSA>_gisoo.geojson
`-- mtl_<FSA>_gisoo_standardized/
    |-- mtl_<FSA>_gisoo_standardized.gpkg
    `-- mtl_<FSA>_gisoo_standardized.geojson
```

| Artifact | Origin | Meaning |
| --- | --- | --- |
| Preliminary `.gpkg` | Independent workflow, also retained by standardized mode | Integrated attributes before contract standardization |
| Preliminary `.geojson` | Separate export described below | Unstandardized attributes exported from the preliminary GeoPackage |
| Standardized `.gpkg` and `.geojson` | Standardized mode | Selected and renamed building attributes, provenance, FSA, area, and identifiers |

The CLI does **not** automatically generate preliminary GeoJSON. A second
workflow run is unnecessary to obtain its source when standardized mode has
already retained the preliminary GeoPackage. Additional intermediate files
may remain after a local run; this published collection contains only the
preliminary and standardized results.

The published T1A files each contain 13 features; T2B files each contain 5.
All four GeoPackages and their GeoJSON counterparts use EPSG:4617. The
GeoJSON files include explicit CRS metadata and retain source coordinates;
they are not RFC 7946 exports reprojected to WGS 84. These are observed
properties of the historical examples, not promised counts for future runs.
None of these files contains carbon-calculation results.

## Preliminary GeoJSON Export

The preliminary files were exported using GDAL 3.12.4 Python bindings
(`osgeo.gdal.VectorTranslate`) from the local QGIS installation. The export
preserves all attribute values and feature identifiers, uses the source CRS
(EPSG:4617 here), and applies no reprojection or contract adaptation. Coordinate
serialization uses 15 decimal places. GeoPackage field types and constraints
are not encoded as a database schema in GeoJSON.

After following the [execution guide](../examples/direct_python/README.md),
use the same configured Python environment with its GDAL bindings to export
new preliminary results. In PowerShell, the following reads the output root
from `JUG_GIS_CITIES_MTL_FSA_OUTPUT_DIR`. It refuses to replace an existing
GeoJSON; use a fresh output directory for a new run. For a single-district
run, change the tuple to `("T1A",)`.

```powershell
@'
import os
from pathlib import Path
from osgeo import gdal

gdal.UseExceptions()
root = Path(os.environ["JUG_GIS_CITIES_MTL_FSA_OUTPUT_DIR"])
for fsa in ("T1A", "T2B"):
    name = f"mtl_{fsa}_gisoo"
    source = root / fsa / name / f"{name}.gpkg"
    destination = source.with_suffix(".geojson")
    if destination.exists():
        raise FileExistsError(destination)
    exported = gdal.VectorTranslate(
        str(destination), str(source), format="GeoJSON", layers=[name],
        options=["-preserve_fid"],
        layerCreationOptions=["RFC7946=NO", "COORDINATE_PRECISION=15"],
    )
    if exported is None:
        raise RuntimeError(f"Export failed: {source}")
    exported = None
    print(destination)
'@ | python -
```

## Related Materials

- [Input descriptions](../datasets/README.md).
- [Configuration and interpretation](../docs/README.md).
- [Historical timing records](../benchmarks/README.md).
