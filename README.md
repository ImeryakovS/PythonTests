
## About this project

[![CI](https://github.com/ImeryakovS/PythonTests/actions/workflows/ci.yml/badge.svg)](https://github.com/ImeryakovS/PythonTests/actions)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-yellow)
[![Allure Report](https://img.shields.io/badge/Allure-Report-purple)](https://imeryakovs.github.io/PythonTests/allure-report/index.html)
![Docker Compose](https://img.shields.io/badge/Docker--Compose-enabled-blue?logo=docker)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project focuses on automated testing of the Grafana backend using Python + Pytest.
Both positive and negative API scenarios are covered, with active use of decorators and fixtures.

## Features

- A **Grafana** container is launched via `docker-compose`
- API and SQL tests are executed using `pytest`
- Allure reports with history are generated and deployed on [GithubPages](https://imeryakovs.github.io/PythonTests/allure-report/index.html )
- CI/CD is implemented with GitHub Actions
- Environment variables control database configuration and Grafana connection

## Tech Stack

- Python 3.11+
- Pytest
- Requests
- Allure (allure-pytest)
- Docker, Docker Compose
- GitHub Actions

### Project Structure:

- `config/` — settings.py contains configuration settings

- `data/` — includes test artifacts required for execution. users.json, dashboards.json, organizations.json are generated automatically based on templates

- `helpers/` — contains decorators and utility functions for cleaning up test data via fixtures

- `services/` — classes that group API methods by domain

- `tests/` — test scenarios

- Global fixtures are located in `conftest.py`

## How to Run Tests Locally

> Important 1: Please change the credentials in Config/settings.py (BASIC_AUTH) if you are not using the default Grafana admin credentials.
> 
> Important 2: SQL tests will only pass if you are using a local version of Grafana or running Grafana and the tests inside the same Docker container (they must share the same file system).
> 
> Important 3: Please change URL (localhost:3000) in Config/settings.py (BASE_URL) to your current URL if you use cloud Grafana or another settings

### Requirements:

1) Python 3.11
2) Allure 2.32.0
3) Grafana latest version
4) Docker latest version

## Install Python

1. Install Python (from scoop): `scoop install python`
2. Install virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (windows, cmd)
4. Install dependencies: `pip install -r requirements.txt`
5. Install requests module: `pip install requests`

### How to Install Grafana
You can choose one of the following options:

1) Install Grafana locally by following instructions from the official Grafana repository
2) Install Grafana in a Docker container using the provided Dockerfile

If you choose the Docker-based setup:

1) Open a terminal from the root project directory (e.g., *\PythonTests)
2) Run `docker-compose up grafana` to start Grafana in a container
3) Open your browser and go to: http://localhost:3000

#### Useful Docker Commands
1) Cleans up containers and volumes - `docker-compose down -v --remove-orphans`
2) Builds and starts Grafana, the test-runner, and runs tests - `docker-compose up --build`
3) View real-time logs for all containers - `docker-compose logs -f`
4) View real-time logs for Grafana only - `docker-compose logs -f grafana`


### How to start tests
1) Start Grafana and ensure it's available at: `http://localhost:3000/`
2) Clone this repository on your machine
3) Navigate to the project folder (e.g., *\PythonTests)
4) Run autotests: `pytest`

### CI/CD Integration
The tests are fully integrated into GitHub Actions. The pipeline is triggered manually.

During the CI/CD run, an Allure report is generated and automatically published to GitHub Pages.
Reports link - https://imeryakovs.github.io/PythonTests/allure-report/index.html 

All CI settings are located in [ci.yml](./.github/workflows/ci.yml)

