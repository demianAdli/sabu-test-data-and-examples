# Direct Python Benchmark Runners

This folder contains direct Python runners for exercising the
`jug_lca_buildings` application class without going through Docker or an API
server.

Run the commands from the repository main root:

```powershell
cd C:\Users\a_adli\docker_projects\sabu-test-data-and-examples
```

The examples below use PowerShell line continuations with the backtick
character.

## JSON Console Output

Use `run_cls_perf` when you want the result printed directly to the console as
JSON.

### Ten-building payload

```powershell
python -m services.jug_lca_buildings.examples.direct_python.run_cls_perf `
  --test-id sabu_n10 `
  --payload ".\services\jug_lca_buildings\datasets\sabu_test_city_10_buildings.geojson" `
  --artifact-dir ".\services\jug_lca_buildings\examples\direct_python\perf_runs\cls_artifacts" `
  --cold
```

### One-building payload

```powershell
python -m services.jug_lca_buildings.examples.direct_python.run_cls_perf `
  --test-id sabu_n1 `
  --payload ".\services\jug_lca_buildings\datasets\sabu_test_city_1_building.geojson" `
  --artifact-dir ".\services\jug_lca_buildings\examples\direct_python\perf_runs\cls_artifacts" `
  --cold
```

The console output includes the request hash, cache-hit status, and emissions
data.

## CSV Output

Use `run_cls_perf_csv` when you want the result exported as a cached CSV report.
The command prints the CSV file path after the report is generated.

### Ten-building payload

```powershell
python -m services.jug_lca_buildings.examples.direct_python.run_cls_perf_csv `
  --test-id sabu_n10_csv `
  --payload ".\services\jug_lca_buildings\datasets\sabu_test_city_10_buildings.geojson" `
  --artifact-dir ".\services\jug_lca_buildings\examples\direct_python\perf_runs\cls_artifacts" `
  --cold
```

## Options

- `--test-id`: label for the run.
- `--payload`: GeoJSON or JSON payload file to process.
- `--artifact-dir`: cache/output directory used by the application service.
- `--cold`: deletes the artifact cache before the run, so the run starts cold.
- `--with-logging`: enables `jugs_chassis` file logging.
- `--log-dir-base`: base directory for logs when `--with-logging` is used.

Omit `--cold` when you want to reuse the artifact cache and check warm-cache
behavior.
