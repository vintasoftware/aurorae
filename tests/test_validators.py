import pytest

from aurorae.providers.exceptions import EmptyFile, InvalidFileType
from aurorae.providers.spreadsheet.validators import (
    is_spreadsheet_empty,
    is_spreadsheet_too_big,
    is_spreadsheet_type_xlsx,
    validate_spreadsheet,
)


class TestValidators:
    def test_validate_file_type_is_valid(self):
        filename = "./tests/fixtures/test_spreadsheet.xlsx"
        assert is_spreadsheet_type_xlsx(filename) is True

    def test_validate_file_type_is_invalid(self):
        filename = "./tests/fixtures/test_fake_xlsx_spreadsheet.xlsx"
        assert is_spreadsheet_type_xlsx(filename) is False

    def test_validate_file_is_empty(self):
        filename = "./tests/fixtures/test_empty_spreadsheet.xlsx"
        assert is_spreadsheet_empty(filename) is True

    def test_validate_file_is_not_empty(self):
        filename = "./tests/fixtures/test_spreadsheet.xlsx"
        assert is_spreadsheet_empty(filename) is False

    def test_validate_file_is_less_than_5_mb(self):
        filename = "./tests/fixtures/test_spreadsheet.xlsx"
        assert is_spreadsheet_too_big(filename) is False

    def test_validate_spreadsheet_raises_empty_file_exception(self):
        filename = "./tests/fixtures/test_empty_spreadsheet.xlsx"
        with pytest.raises(EmptyFile):
            validate_spreadsheet(filename)

    def test_validate_spreadsheet_raises_invalid_type_exception(self):
        filename = "./tests/fixtures/test_fake_xlsx_spreadsheet.xlsx"
        with pytest.raises(InvalidFileType):
            validate_spreadsheet(filename)
