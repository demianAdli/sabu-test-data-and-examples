# Regression and Numerical Equivalence

This folder records a numerical-equivalence check for `jug_lca_buildings`.
The same fixed 100-building GeoJSON input and the same packaged calculation
datasets were used in all three execution modes.

## Execution Modes and Files

| Execution mode      | Output                                     | Execution log                |
| ------------------- | ------------------------------------------ | ---------------------------- |
| Direct Python       | `direct-python/emissions_report.csv`       | `direct-python/sabu.log`     |
| Local REST API      | `local-api/emissions_report.csv`           | `local-api/sabu-api.log`     |
| Dockerized REST API | `docker-api/sabu-docker-100-buildings.csv` | `docker-api/sabu-docker.log` |

The direct Python invocation executes `LCACarbonWorkflow` directly. The local
REST API adds the API, serialization, validation, and orchestration boundaries.
The Dockerized REST API additionally adds the containerized runtime
environment.

The direct Python and local REST API outputs were identical. The Dockerized
REST API output showed negligible numerical differences, with an average
absolute difference of 3.82395 × 10⁻⁵ kg CO₂eq and a maximum absolute
difference of 0.0010 kg CO₂eq per reported value. The logs are included as
execution records. Timestamps may differ because the host and container can use
different time zones, including UTC. These timestamp differences do not affect
the emissions results and were not used in the numerical-equivalence
assessment.

This check verifies consistency across execution modes. It does not
independently validate the underlying carbon-accounting methodology.
