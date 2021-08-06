from providers.spreadsheet.models import Spreadsheet
from providers.spreadsheet.utils import get_spreadsheet_data


class SpreadsheetHandler:
    def __init__(self, input_filename):
        spreadsheet_data = get_spreadsheet_data(input_filename)
        self.spreadsheet = Spreadsheet.parse_obj(spreadsheet_data)
