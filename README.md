# aurorae

[![PyPi version](https://img.shields.io/pypi/v/aurorae.svg)](https://pypi.python.org/pypi/aurorae)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aurorae)](https://pypi.org/project/aurorae/)
[![CI](https://github.com/vintasoftware/aurorae/actions/workflows/actions.yaml/badge.svg)](https://github.com/vintasoftware/aurorae/actions/workflows/actions.yaml)
[![Coverage Status](https://coveralls.io/repos/github/vintasoftware/aurorae/badge.svg?branch=main)](https://coveralls.io/github/vintasoftware/aurorae?branch=main)
[![Documentation Status](https://readthedocs.org/projects/aurorae/badge/?version=latest)](https://aurorae.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

**aurorae** is a tool to generate fixed-width CNAB240 files to perform bulk payments.

### aurorae _does..._
- Generates CNAB240 files for bulk payments
- Allows easy extension of different types of input files

### aurorae _does not..._
- Address charge or as Brazilian banks call "cobrança"
- Address payments by PIX, we only support payments through bank information

But, pull requests are welcomed.

## How It Works
**aurorae** uses Python type hinting for data validation and generation of fixed-width CNAB 240 files. The library receives as inputs an spreadsheet that must be a match of the Pydantic model [Spreadsheet](https://github.com/vintasoftware/aurorae/blob/main/aurorae/providers/spreadsheet/models.py), a general handler parses the initial data to an intermediary representation used by the CNAB240 module to generate files. Different types of inputs are supported by library through the creation of new providers, check the [spreadsheet provider](https://github.com/vintasoftware/aurorae/tree/main/aurorae/providers/spreadsheet) for an example.

The historic and architecture details can be found on the [project's ADRs](https://github.com/vintasoftware/aurorae/blob/main/docs/adr/README.md).

## Requirements

- Python (>3)
- openpyxl (3.0.7)
- pydantic (>1.8.2)

## Installation

```
pip install aurorae
```

## Usage
To run aurorae with test data:
```bash
generate_cnab_sample
```

To run aurorae with your own data use:

```bash
generate_cnab_sample ~/source_spreadsheet.xlsx
```

## Documentation
https://aurorae.readthedocs.io

## Security
We take aurorae's security and our users' trust seriously, therefore we do not save any information (from payments or not) sent by users. If you believe you have found a security issue, please responsibly disclose by contacting: [flavio@vinta.com.br](flavio@vinta.com.br)

## Releases

See [CHANGELOG.md](https://github.com/vintasoftware/aurorae/blob/main/CHANGELOG.md).

## Credits

This project is maintained by [open-source contributors](https://github.com/vintasoftware/aurorae/blob/main/AUTHORS.rst) and [Vinta Software](https://www.vintasoftware.com/).

## Commercial Support

[Vinta Software](https://www.vintasoftware.com/) is always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br
