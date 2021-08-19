from datetime import datetime
from pathlib import PosixPath

import pytest
from freezegun.api import freeze_time

from aurorae.providers.utils import parse_args


@freeze_time(datetime(2021, 7, 29, 13, 30, 50))
class TestUtils:
    def test_parse_args_with_input_and_output_filenames(self):
        argv = (
            "aurorae/sample/spreadsheet_sample.xlsx "
            "--output_filename=generated_files/filetest.txt".split()
        )
        args = parse_args(argv)
        assert args.input_filename == PosixPath(
            "aurorae/sample/spreadsheet_sample.xlsx"
        )
        assert args.output_filename == PosixPath("generated_files/filetest.txt")

    def test_parse_args_invalid_input_filename(self):
        argv = (
            "sample/invalid_spreadsheet.xlsx "
            "--output_filename=generated_files/filetest.txt".split()
        )

        with pytest.raises(SystemExit) as excinfo:
            parse_args(argv)
            assert str(excinfo.value) == r"^The provided input file does not exist$"

    def test_parse_args_default_output_filename(self):
        argv = "aurorae/sample/spreadsheet_sample.xlsx".split()
        args = parse_args(argv)
        assert args.output_filename == PosixPath(
            "generated_files/cnab240-2021-07-29T13:30:50.txt"
        )

    def test_only_accepts_txt_as_file_extension(self):
        argv = (
            "aurorae/sample/spreadsheet_sample.xlsx "
            "--output_filename=generated_files/filetest".split()
        )

        with pytest.raises(SystemExit) as excinfo:
            parse_args(argv)
            assert str(excinfo.value) == r"^Please provide a txt file as the output$"
