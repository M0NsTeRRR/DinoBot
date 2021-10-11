DinoBot is a discord manager for Lyon 2

![Python test](https://github.com/M0NsTeRRR/DinoBot/workflows/Python%20test/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Requirements
- Python (check version in setup.py)

# Setup
## Discord
Create a [discord bot](https://discord.com/developers/applications) and get the token

# Install
## Install dependencies
### Production

    $ pip install -e .

### Dev

    $ pip install -e .[dev]
    $ pre-commit install

## Configure

Fill `config.toml` with `config.example`

## Run

    $ python main.py -c config.toml

# Licence

The code is under CeCILL license.

You can find all details here: https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2021

Contributor(s):

-Ortega Ludovic - ludovic.ortega@adminafk.fr
