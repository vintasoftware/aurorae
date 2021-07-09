import pytest

from connectors.legacy_spreadsheet.spreadsheet_map import MODELS_SPREADSHEET_MAP
from connectors.legacy_spreadsheet.worksheet_handler import parse_data_from


@pytest.mark.usefixtures("spreadsheet_data")
def test_parse_data_from_with_header(spreadsheet_data):
    spreadsheet_map = {"header": MODELS_SPREADSHEET_MAP["header"]}
    parsed_data = parse_data_from(spreadsheet_data, spreadsheet_map)

    assert parsed_data == {
        "header": [
            {
                "field_01_0": "77",
                "field_05_0": "2",
                "field_06_0": "00000000000000",
                "field_07_0": "77",
                "field_08_0": "1",
                "field_09_0": "0",
                "field_10_0": "888888",
                "field_11_0": "1",
                "field_12_0": "1",
                "field_13_0": " Random Company",
                "field_14_0": "Banco",
            },
            {},
        ]
    }


@pytest.mark.usefixtures("spreadsheet_data")
def test_parse_data_from_lote_detalhe_segmento_a(spreadsheet_data):
    spreadsheet_map = {
        "lote_detalhe_segmento_a": MODELS_SPREADSHEET_MAP["lote_detalhe_segmento_a"]
    }
    parsed_data = parse_data_from(spreadsheet_data, spreadsheet_map)

    assert parsed_data == {
        "lote_detalhe_segmento_a": [
            {
                "field_01_3A": "77",
                "field_09_3A": "00",
                "field_10_3A": "0000",
                "field_11_3A": "0",
                "field_12_3A": "0000000",
                "field_13_3A": "0",
                "field_14_3A": "0",
                "field_15_3A": "Nome da Fulana Silva",
                "field_17_3A": "11062021",
                "field_20_3A": "1000",
                "field_22_3A": "11062021",
            },
            {
                "field_01_3A": "77",
                "field_09_3A": "00",
                "field_10_3A": "0000",
                "field_11_3A": "0",
                "field_12_3A": "1111111",
                "field_13_3A": "0",
                "field_14_3A": "0",
                "field_15_3A": "Outro da Fulana Silva",
                "field_17_3A": "11062021",
                "field_20_3A": "1000",
                "field_22_3A": "11062021",
            },
        ]
    }
