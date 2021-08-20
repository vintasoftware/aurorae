import os

from openpyxl import load_workbook

from aurorae.providers.exceptions import EmptyFile, InvalidFileSize, InvalidFileType


def is_spreadsheet_type_xlsx(filename):
    """
    List of file signatures: https://en.wikipedia.org/wiki/List_of_file_signatures
    """
    xlsx_sig = b"\x50\x4B\x03\04"

    with open(filename, "rb") as f:
        file_bytes = f.read(4)
        return file_bytes == xlsx_sig


def is_spreadsheet_empty(filename):
    workbook = load_workbook(filename=filename, read_only=True)
    return all(sheet["A1"].value is None for sheet in workbook)


def is_spreadsheet_too_big(filename):
    max_size = 5242880
    return os.path.getsize(filename) > max_size


def validate_spreadsheet(filename):
    if is_spreadsheet_too_big(filename):
        raise InvalidFileSize
    if not is_spreadsheet_type_xlsx(filename):
        raise InvalidFileType
    if is_spreadsheet_empty(filename):
        raise EmptyFile
