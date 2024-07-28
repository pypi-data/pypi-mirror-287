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

Create a Python virtual env, like:

```sh
python3 -m venv ddc
pip3 install setuptools
pip3 install -r requirements.txt
pip install . (install the cli in the virtual env)
```

## CI variables

To use Defectdojo CLI in a CI context, there is DEFECTDOJO prefixed environment variables you could set.

```sh
DEFECTDOJO_URL
DEFECTDOJO_API_KEY
```
