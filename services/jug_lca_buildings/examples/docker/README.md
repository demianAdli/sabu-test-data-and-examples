# `jug_lca_buildings` Docker Example

This folder contains a Docker Compose example for running the
`jug_lca_buildings` Flask API from the published Docker image.

The Compose file uses:

- Image: `demianadli/jug_lca_buildings:0.1.1`
- Container port: `5000`
- Host port: `8080`
- API base URL: `http://127.0.0.1:8080`
- Swagger UI: `http://127.0.0.1:8080/swagger-ui`
- Persistent artifact volume: `jug_lca_buildings_data`

Run the commands below from this folder:

```text
services/jug_lca_buildings/examples/docker
```

## Docker Compose

### PowerShell

Start the service:

```powershell
docker compose up -d
```

Check the container status:

```powershell
docker compose ps
```

Follow logs:

```powershell
docker compose logs -f
```

Send the 1-building sample dataset to the API:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8080/emissions" `
  -ContentType "application/json" `
  -InFile "..\..\datasets\sabu_test_city_1_building.geojson"
```

Send the 10-building sample dataset to the API:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8080/emissions" `
  -ContentType "application/json" `
  -InFile "..\..\datasets\sabu_test_city_10_buildings.geojson"
```

Stop the service while keeping the named artifact volume:

```powershell
docker compose down
```

Stop the service and delete the named artifact volume:

```powershell
docker compose down --volumes
```

### Bash

Start the service:

```bash
docker compose up -d
```

Check the container status:

```bash
docker compose ps
```

Follow logs:

```bash
docker compose logs -f
```

Send the 1-building sample dataset to the API:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_1_building.geojson"
```

Send the 10-building sample dataset to the API:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_10_buildings.geojson"
```

Stop the service while keeping the named artifact volume:

```bash
docker compose down
```

Stop the service and delete the named artifact volume:

```bash
docker compose down --volumes
```

## Docker Without Compose

Use these commands if you want to run the same image directly with `docker run`.

### PowerShell

Create the artifact volume:

```powershell
docker volume create jug_lca_buildings_data
```

Start the container:

```powershell
docker run -d `
  --name jug_lca_buildings `
  --restart unless-stopped `
  -p 8080:5000 `
  -e LOG_DIR_BASE=/app `
  -e JUG_LCA_ARTIFACTS_DIR=/app/data/jug_lca_buildings `
  -v jug_lca_buildings_data:/app/data/jug_lca_buildings `
  demianadli/jug_lca_buildings:0.1.1
```

Follow logs:

```powershell
docker logs -f jug_lca_buildings
```

Stop and remove the container:

```powershell
docker stop jug_lca_buildings
docker rm jug_lca_buildings
```

Remove the artifact volume if you no longer need cached artifacts:

```powershell
docker volume rm jug_lca_buildings_data
```

### Bash

Create the artifact volume:

```bash
docker volume create jug_lca_buildings_data
```

Start the container:

```bash
docker run -d \
  --name jug_lca_buildings \
  --restart unless-stopped \
  -p 8080:5000 \
  -e LOG_DIR_BASE=/app \
  -e JUG_LCA_ARTIFACTS_DIR=/app/data/jug_lca_buildings \
  -v jug_lca_buildings_data:/app/data/jug_lca_buildings \
  demianadli/jug_lca_buildings:0.1.1
```

Follow logs:

```bash
docker logs -f jug_lca_buildings
```

Stop and remove the container:

```bash
docker stop jug_lca_buildings
docker rm jug_lca_buildings
```

Remove the artifact volume if you no longer need cached artifacts:

```bash
docker volume rm jug_lca_buildings_data
```

## See Results

The Docker container runs the same API used by the local API example. After the
container is running, send a `POST` request to:

```text
http://127.0.0.1:8080/emissions
```

The response body contains the calculated emissions result. The response headers
also include `X-Request-ID`, which can help match a request to container logs.

### Bash

Print the result in the terminal:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_1_building.geojson"
```

Save the result to a JSON file:

```bash
curl -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_10_buildings.geojson" \
  -o emissions_result_10_buildings.json
```

If `jq` is installed, pretty-print the response:

```bash
curl -s -X POST "http://127.0.0.1:8080/emissions" \
  -H "Content-Type: application/json" \
  --data-binary "@../../datasets/sabu_test_city_1_building.geojson" \
  | jq
```

### Postman

1. Start the container with Docker Compose or `docker run`.
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
9. Open one of the GeoJSON datasets from `services/jug_lca_buildings/datasets/`,
   copy its full JSON content, and paste it into the Postman body.
10. Click `Send`.

For a quick first request, use `sabu_test_city_1_building.geojson`. After
confirming the API works, try `sabu_test_city_10_buildings.geojson` or a larger
dataset downloaded from Zenodo.

## Notes

- If port `8080` is already in use, change the host side of the port mapping.
  For example, use `8081:5000` and call `http://127.0.0.1:8081/emissions`.
- The first request for a payload may be slower because artifacts are generated.
  Later requests can reuse cached artifacts from the Docker volume.
- Larger GeoJSON datasets can be downloaded from the Zenodo records listed in
  `services/jug_lca_buildings/datasets/README.md`.
