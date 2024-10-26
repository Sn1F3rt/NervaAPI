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
   
4. Install dependencies

   ```shell
    uv sync --no-dev
   ```

## Configuration

Copy the [`config.example.py`](config.example.py) file to `config.py` and update the variables.

## Running

```shell
uv run launcher.py
```

## License

[GNU General Public License v3.0](LICENSE)

Copyright &copy; 2024 [Sayan "Sn1F3rt" Bhattacharyya](https://sn1f3rt.dev), [The Nerva Project](https://nerva.one)
