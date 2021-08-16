# aurora

[![CI](https://github.com/vintasoftware/aurora/actions/workflows/actions.yaml/badge.svg)](https://github.com/vintasoftware/aurora/actions/workflows/actions.yaml)
[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

**aurora** is a tool to generate fixed-width CNAB240 files to perform bulk payments

### aurora _does..._
- Generates CNAB240 files for bulk payments
- Allows easy extension of different types of input files

### aurora _does not..._
- Address charge or as brazilian banks call "cobrança"
- Address payments by PIX, we only support payments through bank information

But, pull requests are welcomed.

## How It Works
**aurora** uses Python type hinting for data validation and generation of fixed-width CNAB 240 files. The library receives as inputs an spreadsheet that must be a match of the Pydantic model [Spreadsheet](providers/spreadsheet/models.py), a general handler parses the initial data to an intermediary representation used by the CNAB240 module to generate files. Different types of inputs are supported by library through the creation of new providers, check the [spreadsheet provider](providers/spreadsheet) for an example.

A historic and architecture details can be found on the [project's ADRs](docs/adr/README.md) to better understand the architecture.

## Requirements

- Python (>3)
- openpyxl (3.0.7)

## Usage
To run aurora with test data:
```bash
poetry run generate sample/legacy_spreadsheet_sample.xlsx
```

## Security
We take Aurora's security and our users' trust very seriously, therefore we do not save any information (from payments or not) sent by users. If you believe you have found a security issue, please responsibly disclose by contacting: [flavio@vinta.com.br](flavio@vinta.com.br)

## Releases

See [CHANGELOG.md](/CHANGELOG.md).

## Credits

This project is maintained by [open-source contributors](/AUTHORS.rst) and [Vinta Software](https://www.vintasoftware.com/).

## Commercial Support

[Vinta Software](https://www.vintasoftware.com/) is always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br
