# shelly-upgrade

A tiny Python script to upgrade Shelly smart home devices. When run it will instruct all devices listed to perform a firmware upgrade, useful if you have many of these.

## Install

1. Clone the repo
2. Install requirements with [Poetry](https://python-poetry.org/docs/): `poetry install`

## Usage

Create a text file in the same directory as the script called `shellies.txt`. List the shellies in this file, either IP address or hostname, one per line. Then run `poetry run python main.py`.
