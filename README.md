# NervaAPI

[![Ruff](https://github.com/Sn1F3rt/NervaAPI/actions/workflows/ruff.yml/badge.svg)](https://github.com/Sn1F3rt/NervaAPI/actions/workflows/ruff.yml)
[![License](https://img.shields.io/github/license/Sn1F3rt/NervaAPI)](LICENSE)

## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running](#running)
- [License](#license)

## About

NervaAPI is a RESTful API server for the Nerva blockchain. It provides a simple interface to interact with the Nerva blockchain using HTTP requests.

## Prerequisites

- Git
- Python >= 3.8
- MongoDB database
- [make](https://www.gnu.org/software/make/) (optional)

## Installation

1. Install [`uv`](https://docs.astral.sh/uv/) > https://docs.astral.sh/uv/getting-started/installation/

2. Clone the repository

   ```shell
    git clone https://github.com/Sn1F3rt/NervaAPI.git
   ```
   
3. Switch to the project directory

   ```shell
    cd NervaAPI
   ```
   
4. Create a virtual environment

   ```shell
   uv venv
   ```
   or if you have `make` installed

   ```shell
   make env
   ```
   
5. Install dependencies

   ```shell
    uv sync --no-dev
   ```
   or if you have `make` installed

   ```shell
   make prod
   ```

## Configuration

Copy the [`config.example.py`](config.example.py) file to `config.py` and update the variables.

## Running

### Development

```shell
uv run launcher.py
```

or if you have `make` installed

```shell
make
```

### Production

```shell
source .venv/bin/activate
hypercorn --bind 0.0.0.0:8000 launcher:app
```

or if you want to enable SSL support

```shell
source .venv/bin/activate
hypercorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:8000 launcher:app
```

The API server will be running at `http://localhost:8000`. The certificate and key files are required for SSL support.

## License

[GNU General Public License v3.0](LICENSE)

Copyright &copy; 2024 [Sayan "Sn1F3rt" Bhattacharyya](https://sn1f3rt.dev), [The Nerva Project](https://nerva.one)
