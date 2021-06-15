# vinta-pagamentos

A Python implementation of the CNAB240 file to perform bulk payments.

**Disclaimer**: This project is a work in progress. 


## Requirements

- Python (>3)
- openpyxl (3.0.7)

## Installation
- Clone the repo
- Inside a virtualenv run `pip install -r requirements.txt`

## Running with test data

- Change occurences of `sys.path.append` to be your local path
- Run `python cnab240/writer.py`