# DefectDojo CLI

[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)

A CLI wrapper for [DefectDojo](https://github.com/DefectDojo/django-DefectDojo)

## Fork

This has been forked from <https://github.com/adiffpirate/defectdojo-cli>.

## Installation

Simply run:

```sh
python3 -m pip install defectdojo-cli2
```

## Usage

```sh
defectdojo --help
```

## Development

Install poetry

```sh
poetry env use /usr/local/bin/python3 # = your full path to the Python executable.
poetry install

```

## CI variables

To use Defectdojo CLI in a CI context, there is DEFECTDOJO prefixed environment variables you could set.

```sh
DEFECTDOJO_URL
DEFECTDOJO_API_KEY
DEFECTDOJO_PRODUCT_ID
DEFECTDOJO_ENGAGEMENT_ID
DEFECTDOJO_TEST_TYPE
```
