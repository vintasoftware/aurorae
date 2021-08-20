from providers.spreadsheet.handler import SpreadsheetHandler
from providers.utils import parse_args


def generate_cnab_files():
    args = parse_args()

    handler = SpreadsheetHandler(input_filename=args.input_filename)
    cnab = handler.get_cnab_file()
    cnab.generate_file(output_filename=args.output_filename)
    cnab.generate_html_file(output_filename=args.output_filename)
