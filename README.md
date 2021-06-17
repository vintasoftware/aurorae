# vinta-pagamentos

A Python implementation of the CNAB240 file to perform bulk payments.

**Disclaimer**: This project is a work in progress. 


## Requirements

- Python (>3)
- openpyxl (3.0.7)

## Working in development mode
To ease the development mode of the library we are using code as a package: 
- Clone the repo
- Inside a virtualenv and on the root folder of the project run `pip install -e .`. We are installing the library locally in editable model ([details here](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode)). 

## Running with test data

- Run `python cnab/cnab240/writer.py`