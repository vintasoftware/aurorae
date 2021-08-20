from aurorae.payroll.models import Payroll
from aurorae.providers.spreadsheet import validators
from aurorae.providers.spreadsheet.models import Spreadsheet
from aurorae.providers.spreadsheet.utils import get_spreadsheet_data


class SpreadsheetHandler:
    def __init__(self, input_filename):
        validators.validate_spreadsheet(input_filename)
        self.spreadsheet = self.get_spreadsheet(input_filename)
        self.payroll = self.get_payroll()

    def get_spreadsheet(self, input_filename):
        spreadsheet_data = get_spreadsheet_data(input_filename)
        return Spreadsheet.parse_obj(spreadsheet_data)

    def get_payroll(self):
        return Payroll.parse_obj(self.spreadsheet.dict())

    def get_cnab_file(self):
        return self.payroll.get_cnab_file()
