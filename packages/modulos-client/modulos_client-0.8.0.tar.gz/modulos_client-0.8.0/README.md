# Modulos Client

[![PyPI version](https://img.shields.io/pypi/v/modulos-client.svg)](https://pypi.org/project/modulos-client/)

This tool provides a Programmatic interface to interact with the Modulos platform.

## Documentation

The documentation can be found on [docs.modulos.ai](https://docs.modulos.ai)

## Installation

```sh
# install from PyPI
pip install modulos-client
```
## API Key

Generate your API key [here](`https://app.modulos.ai/tokens`)

## Usage

```python
import os
from modulos_client import Modulos

client = Modulos(
    # This is the default and can be omitted
    api_key=os.environ.get("MODULOS_API_KEY"),
)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `MODULOS_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

