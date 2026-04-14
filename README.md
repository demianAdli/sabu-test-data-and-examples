# Sabu Test Data and Examples

This repository provides test datasets, example workflows, and reproducibility materials for the **Sabu (Joint Utility for Generic carbon-emission Simulation)** framework.

## About Sabu

Sabu is a microservice-based software framework designed to support disaggregated carbon-emissions evaluation across urban systems. It adopts a modular architecture in which domain-specific workflows are implemented as independent services with well-defined interfaces.

The framework emphasizes:

- modular service development and isolation
- explicit data contracts and interoperability
- scalability through containerized execution
- extensibility for future domain integration

**Main Sabu repository:**  
https://github.com/demianAdli/sabu

---

## Purpose of This Repository

This repository serves as a **companion resource** to the main Sabu framework. Its goal is to support:

- testing of Sabu services with **GeoJSON datasets of varying sizes**
- demonstration of **typical execution workflows**
- sharing of **example output tables** (e.g., emissions results)
- providing **scripts and command-line examples** (Python, PowerShell, Bash, curl)
- documenting **performance benchmarks and logs**
- enabling **reproducibility of experiments**

This separation keeps the main Sabu repository focused on architecture and implementation, while this repository focuses on **usage, validation, and experimentation**.

---

## Repository Structure

```text
sabu-test-data-and-examples/
|-- services/
|   `-- jug_lca_buildings/
|       |-- examples/    # Execution examples (direct Python, API, Docker)
|       |-- datasets/    # Input GeoJSON datasets (1 to large-scale cases)
|       |-- results/     # Example outputs and processed tables
|       |-- benchmarks/  # Performance results and configurations
|       |-- scripts/     # Helper scripts and command-line utilities
|       `-- docs/        # Service-specific documentation
|
|-- shared/
|   `-- docs/            # Cross-service documentation and notes
|
|-- README.md
|-- LICENSE
`-- CITATION.cff
```

### Design Principles

- **Service-oriented organization**: Each service maintains its own datasets, results, and examples
- **Separation of concerns**: Inputs, outputs, scripts, and documentation are clearly organized
- **Extensibility**: Additional services (e.g., `jug_gis_validation`) can be added without restructuring
- **Reproducibility-focused**: Materials are curated to support validation and experimentation

---

## Current Coverage

This repository currently includes materials for:

- `jug_lca_buildings`  
  A life-cycle carbon estimation service for buildings within the Sabu framework.

Planned future additions include:

- `jug_gis_validation`
- `jug_gis_cities`
- `jug_sim`

---

## Execution Modes

Examples are provided for multiple ways of interacting with Sabu services:

- **Direct Python execution**
- **API-based interaction** (e.g., using `curl` or Postman)
- **Docker-based execution**

Refer to the `examples/` and `scripts/` directories within each service for details.

---

## Reproducibility and Benchmarking

The repository includes:

- datasets ranging from small samples to large-scale inputs
- representative output tables used for validation
- performance benchmarks and execution logs
- scripts to reproduce selected experiments

These materials are intended to support:

- testing and validation
- performance evaluation
- replication of experimental results

---

## Notes on Data

Some datasets (especially large GeoJSON files) may be:

- reduced to representative subsets
- compressed
- or selectively included to keep the repository manageable

---

## Citation

If you use Sabu or materials from this repository in your research, please refer to the citation information provided in `CITATION.cff`.

---

## License

This repository is distributed under the terms specified in the `LICENSE` file.
