# pytest-fabric
A pytest plugin for testing Microsoft Fabric Notebooks and data quality.

## Use Cases:
- Run tests in a CI/CD pipeline via a Docker container
- Run tests in a CI/CD pipeline via a Fabric workspace
- Run tests directly from a notebook in Fabric
- Run data quality tests on a dataset

## Features:
- Unit tests
- Data quality tests
- Upload tests to Azure DevOps
- PEP302 import hooks for Fabric Notebooks

## Non-Goals:
- Testing non-python code including magic commands