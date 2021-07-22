from connectors.legacy_spreadsheet.handler import LegacySpreadsheetHandler
from connectors.utils import parse_args


def generate_cnab_files():
    args = parse_args()

    handler = LegacySpreadsheetHandler(filename=args.filename)
    cnab = handler.get_cnab_file()
    cnab.generate_file()
    cnab.generate_html_file()
