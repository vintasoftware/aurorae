import argparse
import os
from datetime import datetime
from pathlib import Path


def parse_args(arguments=None):
    created_at = datetime.now().isoformat()

    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename", type=Path, help="input filename")
    parser.add_argument(
        "--output_filename",
        dest="output_filename",
        type=Path,
        default=f"cnab240-{created_at}.txt",
        help="output filename",
    )
    args = parser.parse_args(arguments)

    if not os.path.exists(args.input_filename):
        parser.error("The provided entry file does not exist")

    if Path(args.output_filename).suffix != ".txt":
        parser.error("Please provide a txt file as the output")

    return args
