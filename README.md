# vinta-pagamentos

A Python implementation of the CNAB240 file to perform bulk payments.

**Disclaimer**: This project is a work in progress. 


## Requirements

- Python (>3)
- openpyxl (3.0.7)

## Working in development mode

To ease the development mode of the library we are using code as a package: 
- Clone the repo
- Inside the root folder of the project run `mkdir generated_files`
- [Install Poetry](https://python-poetry.org/docs/#installation) 
- Inside a virtualenv and on the root folder of the project run `poetry install`. This will install all dependencies and install the library locally in editable mode. 

## Running with test data
- Run `poetry run generate test_data/test_data.xlsx`

## Pre-commit hooks
- Run `poetry run pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

