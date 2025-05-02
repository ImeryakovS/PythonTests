
## About this project

[![CI](https://github.com/ImeryakovS/PythonTests/actions/workflows/ci.yml/badge.svg)](https://github.com/ImeryakovS/PythonTests/actions)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-yellow)
[![Allure Report](https://img.shields.io/badge/Allure-Report-purple)](https://imeryakovs.github.io/PythonTests/allure-report/index.html)

This project focuses on automated testing of the Grafana backend using Python + Pytest.
Both positive and negative API scenarios are covered, with active use of decorators and fixtures.

### Project Structure:

- config/ — settings.py contains configuration settings

- data/ — includes test artifacts required for execution. users.json and dashboards.json are generated automatically based on templates

- helpers/ — contains decorators and utility functions for cleaning up test data via fixtures

- services/ — classes that group API methods by domain

- tests/ — test scenarios

- Global fixtures are located in conftest.py.

### How to Run Tests Locally
Instructions for local test execution are provided inside the project (e.g. README.md or comments). The framework supports easy local execution via Pytest.

### Requirements

1) Python 3.11
2) Allure 2.32.0

## Install Python

1. Install Python (from scoop): `scoop install python`
2. Install virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (windows, cmd)
4. Install pytest: `pip install pytest`
5. Install dependencies: `pip install -r requirements.txt`

### How to run the tests:

1) Install Grafana locally: https://github.com/grafana/grafana (choose any convenient method)
2) Start Grafana and ensure it's available at: `http://localhost:3000/`
3) Clone this repository on your machine
4) Navigate to the project folder and 
5) Run autotests: `pytest`

### CI/CD Integration
The tests are fully integrated into GitHub Actions. The pipeline is triggered manually.

During the CI/CD run, an Allure report is generated and automatically published to GitHub Pages.
Reports link - https://imeryakovs.github.io/PythonTests/allure-report/index.html 

All CI settings are located in [ci.yml](./.github/workflows/ci.yml)
### Python tests



> The repository is a work in progress.
> A well-structured README, along with CI/CD integration and Allure reporting, will be added soon.
