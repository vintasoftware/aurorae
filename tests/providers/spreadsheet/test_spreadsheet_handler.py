import json

from providers.spreadsheet.handler import SpreadsheetHandler


class TestSpreadsheetHandler:
    def test_generates_spreadsheet_from_spreadsheet_data(self):
        input_filename = "./tests/fixtures/test_spreadsheet.xlsx"
        handler = SpreadsheetHandler(input_filename=input_filename)

        expected_json = {
            "company": {
                "company_name": " Vinta Servicos e Solucoes Tec",
                "registration_number": "99999999000999",
                "bank_name": "Banco Intermedium",
                "bank_code": "77",
                "bank_agency": "1",
                "bank_agency_digit": "9",
                "bank_account_number": "999999",
                "bank_account_digit": "9",
                "bank_account_agency_digit": "9",
                "address_location": "Avenida Agamenon Magalhaes",
                "address_number": "4318",
                "address_complement": "sala 1801",
                "address_cep": "52021",
                "address_cep_complement": "170",
                "address_city": "Recife",
                "address_state": "PE",
                "registration_type": "CGC/CNPJ",
            },
            "employees": [
                {
                    "name": "Maria Fulana da Silva",
                    "registration_number": "99999999999",
                    "bank_code": "77",
                    "bank_agency": "0001",
                    "bank_agency_digit": "9",
                    "bank_account_number": "9999999",
                    "bank_account_digit": "0",
                    "bank_account_agency_digit": "0",
                    "address_location": "Rua das Amelias",
                    "address_number": "123",
                    "address_complement": "1 Andar",
                    "address_district": "Centro",
                    "address_cep": "50050",
                    "address_cep_complement": "000",
                    "address_city": "Recife",
                    "address_state": "PE",
                    "registration_type": "CPF",
                }
            ],
            "payments": [
                {
                    "employee_name": "Maria Fulana da Silva",
                    "identification_number": "0001",
                    "payment_amount": "1000",
                    "payment_date": "11062021",
                }
            ],
        }

        assert json.loads(handler.spreadsheet.json()) == expected_json
