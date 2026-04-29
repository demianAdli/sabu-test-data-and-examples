# `jug_lca_buildings` Benchmarks

This folder contains performance logs for running the `jug_lca_buildings`
service on a large building dataset.

## Contents

- `sabu.log`: structured JSON Lines log for a benchmark run of the
  `/emissions` endpoint on the 100000-building input. The service log reports
  `100001` buildings in the resolved city.
- `summary.csv`: compact benchmark summary table extracted from `sabu.log`,
  with one row per recorded `/emissions` request.

## Recorded Run

The main uncached request was carried out on February 28, 2026. The structured
`ts` values in the log are UTC; the Werkzeug access log records the local server
time as February 28, 2026 at 15:57:34.

| Metric | Value |
| --- | ---: |
| Endpoint | `POST /emissions` |
| HTTP status | `201` |
| Input size | 100000-building benchmark |
| Buildings reported by service | `100001` |
| Cache hit | `false` |
| Request hash | `002df0f3a9fa` |
| Logged HTTP latency | `6431390 ms` (`6431.390 s`) |
| Approximate wall-clock duration | `1 h 47 min 11 s` |

## Main Timing Events

| Event | Logged duration |
| --- | ---: |
| City geometry parsing | `1569.099 s` |
| Construction enrichment | `3696.374 s` |
| Building emissions calculation | `1138.003 s` |
| Emission export payload preparation | `1138.065 s` |

The emissions calculation log reports `11.38 ms/building` and
`87.87 buildings/s` for the `100001` buildings.

Two later requests with the same `request_hash` were served from cache:

| Local time | Cache hit | HTTP latency |
| --- | --- | ---: |
| 16:10:17 | `true` | `17924 ms` |
| 16:11:39 | `true` | `34539 ms` |

The same values are also available in `summary.csv` for easier import into
spreadsheets, plotting tools, or paper/report tables.

Some timing columns are blank for cached requests because the cached responses
did not rerun the full geometry parsing, construction enrichment, or emissions
calculation workflow.

## Log Fields

Each line in `sabu.log` is one JSON object. The most useful fields are:

- `ts`: structured timestamp, recorded in UTC.
- `level`: log severity, such as `INFO`, `DEBUG`, or `ERROR`.
- `service`: service name, here `lca_buildings-api`.
- `env`: runtime environment, here `dev`.
- `logger`: component that emitted the log entry.
- `request_id`: identifier used to group log entries for one request.
- `msg`: human-readable event or progress message.
- `buildings`: number of buildings returned for completed requests, when
  present.
- `cache_hit`: whether the request used cached results, when present.
- `latency_ms`: HTTP request latency, when present.

## Representation Recommendation

Keeping the raw `sabu.log` file is useful because it preserves the full request
trace, progress events, cache behavior, and any warnings or errors. For papers,
reports, or quick comparison between benchmark runs, the best companion format
is the `summary.csv` file in this folder.

The current summary fields are:

- run label
- run date
- endpoint
- input building count
- cache status
- HTTP status
- total latency in milliseconds
- total latency in seconds
- approximate wall-clock duration
- geometry parsing time
- construction enrichment time
- emissions calculation time
- emission export payload preparation time
- milliseconds per building
- buildings per second
- request hash
- notes
