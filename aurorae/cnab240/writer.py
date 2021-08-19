import os
from pathlib import Path

import aurorae
from aurorae.providers.spreadsheet.handler import SpreadsheetHandler
from aurorae.providers.utils import parse_args


def generate_cnab_files():
    args = parse_args()

    handler = SpreadsheetHandler(input_filename=args.input_filename)
    cnab = handler.get_cnab_file()
    cnab.generate_file(output_filename=args.output_filename)
    cnab.generate_html_file(output_filename=args.output_filename)


def generate_cnab_sample():
    root_path = os.path.dirname(aurorae.__file__)

    output_filename = "aurorae_cnab.txt"
    input_filename = os.path.join(root_path, "sample/spreadsheet_sample.xlsx")

    handler = SpreadsheetHandler(input_filename=input_filename)
    cnab = handler.get_cnab_file()

    cnab.generate_file(output_filename=Path(output_filename))
    print(f"New CNAB file generated: {output_filename}")

    cnab.generate_html_file(output_filename=Path(output_filename))
    html_file = f"{Path(output_filename).with_suffix('.html')}"
    print(f"New CNAB debug file generated: {html_file}")
