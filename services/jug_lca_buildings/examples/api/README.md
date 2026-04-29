# `jug_lca_buildings` API Tutorial

This tutorial shows how to run the `jug_lca_buildings` Flask API locally and send building GeoJSON datasets to the emissions endpoint.

The API example depends on PyPI packages, including:

- `jug_lca_buildings`
- `sabu_chassis`
- `flask`
- `flask-smorest`

Install the required packages in the Python environment that will run Flask. For example:

```powershell
python -m pip install jug_lca_buildings sabu_chassis flask flask-smorest
```

Run all commands from this folder:

```text
services/jug_lca_buildings/examples/api
```

## Run the API in PowerShell

The following commands clear the local API runtime folder and log file, set the Flask environment variables, and start the API on `http://127.0.0.1:8080`.

```powershell
Remove-Item -Recurse -Force .\.runtime\jug_lca_buildings -ErrorAction SilentlyContinue
Remove-Item .\logs\test_sabu.log -ErrorAction SilentlyContinue
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run --host=127.0.0.1 --port=8080
```

When the server is running, open the Swagger UI in a browser:

```text
http://127.0.0.1:8080/swagger-ui
```

## Run the API in Git Bash

Use the Git Bash version if you prefer a Bash-style shell on Windows.

```bash
rm -rf ./.runtime/jug_lca_buildings
rm -f ./logs/test_sabu.log
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=127.0.0.1 --port=8080
```

The API will be available at:

```text
http://127.0.0.1:8080
```

## Test the API from Git Bash

If you want to get results directly in Git Bash instead of using Postman, use `curl`.

Small datasets are included in:

```text
services/jug_lca_buildings/datasets/
```

For quick tests, use one of these local files:

- `sabu_test_city_1_building.geojson`
- `sabu_test_city_10_buildings.geojson`

From `services/jug_lca_buildings/examples/api`, send the 1-building dataset:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_1_building.geojson"
```

Send the 10-building dataset:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_10_buildings.geojson"
```

To save the response to a JSON file:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_10_buildings.geojson" \
  -o emissions_result_10_buildings.json
```

For larger datasets, download the GeoJSON files from Zenodo:

- https://zenodo.org/records/19501061
- https://zenodo.org/records/19500482

After downloading a larger GeoJSON file, replace the dataset path in the `curl` command with the path to that file.

## Test the API with Postman

1. Start the API with the PowerShell or Git Bash commands above.
2. Open Postman and create a new request.
3. Set the request method to `POST`.
4. Set the URL to:

```text
http://127.0.0.1:8080/emissions
```

5. Open the `Headers` tab and add:

```text
Content-Type: application/json
```

6. Open the `Body` tab.
7. Select `raw`.
8. Select `JSON` as the body format.
9. Open one of the GeoJSON datasets from `services/jug_lca_buildings/datasets/`, copy its full JSON content, and paste it into the Postman body.
10. Click `Send`.

For a quick first request, use `sabu_test_city_1_building.geojson`. After confirming the API works, try `sabu_test_city_10_buildings.geojson` or a larger dataset downloaded from Zenodo.

The response body contains the calculated emissions result. The response headers also include `X-Request-ID`, which can be useful when matching a Postman request to the API logs.
