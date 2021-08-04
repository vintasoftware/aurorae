from providers.legacy_spreadsheet.handler import LegacySpreadsheetHandler
from providers.utils import parse_args


def generate_cnab_files():
    args = parse_args()

    handler = LegacySpreadsheetHandler(input_filename=args.input_filename)
    cnab = handler.get_cnab_file()
    cnab.generate_file(output_filename=args.output_filename)
    cnab.generate_html_file(output_filename=args.output_filename)
