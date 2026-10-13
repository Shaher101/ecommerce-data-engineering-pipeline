# E-commerce Data Engineering Pipeline

An end-to-end data engineering project that ingests, validates, transforms, and stores e-commerce data in Microsoft SQL Server.

## Project Overview

This project demonstrates how to build a reliable data pipeline for an e-commerce business. It processes customer, product, order, and order-item data, applies data quality checks, and prepares analytics-ready tables.

## Architecture

**Data Sources → Python ETL → SQL Server → Data Warehouse → Analytics**
<img width="1672" height="940" alt="Architecture" src="https://github.com/user-attachments/assets/1b979fda-3425-44e1-bf47-55b9d1003338" />

Apache Airflow orchestrates the pipeline, while Docker provides a reproducible runtime environment.

## Tech Stack

- Python
- Pandas
- Microsoft SQL Server
- SQL
- Apache Airflow
- Docker and Docker Compose
- pytest
- Git and GitHub

## Key Features

- Data extraction from CSV files and, in a later phase, an API.
- Data cleaning and validation.
- Raw, staging, warehouse, and analytics layers.
- Data quality checks and rejected-record tracking.
- Automated workflow orchestration and retries.
- Logging and pipeline execution auditing.
- Automated tests and reproducible setup instructions.

## Data Model

The planned warehouse includes:

- `DimCustomer`
- `DimProduct`
- `DimDate`
- `FactSales`

The fact table will use a documented grain, such as one row per order item.

## Data Quality

The pipeline will validate required fields, duplicate identifiers, data types, business rules, and referential integrity.

Invalid records will be tracked with rejection reasons, and pipeline runs will record row counts and execution status.

## Repository Structure

- `data/` — sample input data
- `sql/` — SQL scripts and transformations
- `src/` — Python ETL modules
- `dags/` — Airflow DAGs
- `tests/` — automated tests
- `docs/` — architecture and project documentation

## Getting Started

1. Install the required tools and dependencies.
2. Configure the SQL Server connection using environment variables.
3. Create the required database, schemas, and tables.
4. Load the sample data.
5. Run the ETL pipeline and execute the tests.
6. Start Airflow using the documented Docker configuration.

Detailed setup instructions will be added as the implementation progresses.

## Testing

The project will include unit tests, integration tests, data quality checks, and rerun/idempotency tests.

## Results

This section will include verified pipeline run results, data quality metrics, sample SQL queries, and screenshots after implementation.

## Future Improvements

- API ingestion
- Incremental data loading
- CI/CD with GitHub Actions
- Cloud deployment
- Additional monitoring and alerting

## Author

Shaher Hashem

