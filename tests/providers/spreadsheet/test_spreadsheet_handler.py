from providers.spreadsheet.handler import SpreadsheetHandler


class TestSpreadsheetHandler:
    def test_generates_spreadsheet_from_spreadsheet_data(self):
        input_filename = "./tests/fixtures/test_spreadsheet.xlsx"
        handler = SpreadsheetHandler(input_filename=input_filename)

        assert (
            handler.spreadsheet.company.company_name == " Vinta Servicos e Solucoes Tec"
        )
        assert handler.spreadsheet.employees[0].name == "Maria Fulana da Silva"
        assert handler.spreadsheet.payments[0].payment_amount == "1000"
