from unittest import mock

import pytest

from cnab.cnab240.v10_7 import lambdas
from connectors.legacy_spreadsheet.mapping import MODELS_SPREADSHEET_MAP
from connectors.legacy_spreadsheet.utils import parse_data_from


class TestLegacySpreadsheet:
    def setup_method(self, __):
        lambdas.COUNT = 0

    @pytest.mark.usefixtures("spreadsheet_data")
    def test_parse_data_from_with_header(self, spreadsheet_data):
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
    def test_parse_data_from_lote_detalhe_segmento_a(self, spreadsheet_data):
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

    @pytest.mark.usefixtures("spreadsheet_data")
    def test_parse_data_from_lote_detalhe_segmento_b(self, spreadsheet_data):
        spreadsheet_map = {
            "lote_detalhe_segmento_b": MODELS_SPREADSHEET_MAP["lote_detalhe_segmento_b"]
        }
        parsed_data = parse_data_from(spreadsheet_data, spreadsheet_map)

        assert parsed_data == {
            "lote_detalhe_segmento_b": [
                {
                    "field_01_3B": "00",
                    "field_08_3B": "99988877700",
                    "field_09_3B": "Rua da Aleatoriedade ",
                    "field_10_3B": {
                        "Número (Nº do Local)": "000",
                        "Complemento (Casa, Apto, Etc)": "Casa",
                        "Bairro": "Bairro",
                        "Nome da Cidade": "Cidade",
                        "CEP": "00000",
                        "Complemento do CEP": "000",
                        "Sigla do Estado": "PE",
                    },
                    "field_11_3B": {
                        "Data do Vencimento (Nominal)": "11062021",
                        "Valor do Documento (Nominal)": "1",
                        "Valor do Abatimento": "0",
                        "Valor do Desconto": "0",
                        "Valor da Mora": "0",
                        "Valor da Multa": "0",
                        "Código/Documento do Favorecido": "1",
                        "Aviso ao Favorecido": "0",
                    },
                    "field_13_3B": "0",
                },
                {
                    "field_01_3B": "00",
                    "field_08_3B": "99988877700",
                    "field_09_3B": "Rua da Aleatoriedade ",
                    "field_10_3B": {
                        "Número (Nº do Local)": "000",
                        "Complemento (Casa, Apto, Etc)": "Casa",
                        "Bairro": "Bairro",
                        "Nome da Cidade": "Cidade",
                        "CEP": "00000",
                        "Complemento do CEP": "000",
                        "Sigla do Estado": "PE",
                    },
                    "field_11_3B": {
                        "Data do Vencimento (Nominal)": "11062021",
                        "Valor do Documento (Nominal)": "1",
                        "Valor do Abatimento": "0",
                        "Valor do Desconto": "0",
                        "Valor da Mora": "0",
                        "Valor da Multa": "0",
                        "Código/Documento do Favorecido": "1",
                        "Aviso ao Favorecido": "0",
                    },
                    "field_13_3B": "0",
                },
            ]
        }

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_header_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_header = (
            "07700000         99999999900099977                  00001900000099999999 VINTA "
            "SERVICOS E SOLUCOES TECBANCO INTERMEDIUM                       1080720211330500"
            "0000110301600                                                                     "
        )
        assert cnab.header.formatted_data() == expected_header

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_lote_header_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_lote_header = (
            "07700011C3001046 99999999900099977                  00001900000099999999 VINTA "
            "SERVICOS E SOLUCOES TEC                                        AVENIDA AGAMENON"
            " MAGALHAES    04318SALA 1801      RECIFE              52021170PE01                "
        )
        assert cnab.lote.header.formatted_data() == expected_lote_header

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_lote_segment_a_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_segmento_a = (
            "0770001300001A00001807700001900000999999900MARIA FULANA DA SILVA                "
            "             11062021BRL000000000000000000000000001000                    110620"
            "21000000000000000                                        01          0          "
        )
        assert cnab.lote.children[0].segmento_a.formatted_data() == expected_segmento_a

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_lote_segment_b_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_segmento_b = (
            "0770001300002B05 100099999999999RUA DAS AMELIAS                    001231 ANDAR "
            "       CENTRO         RECIFE         50050000PE110620210000000000000010000000000"
            "000000000000000000000000000000000000000000000000001              000000000000000"
        )
        assert cnab.lote.children[0].segmento_b.formatted_data() == expected_segmento_b

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_lote_trailer_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_lote_trailer = (
            "07700015         000004000000000000001000000000000000000000                     "
            "                                                                                "
            "                                                                                "
        )
        assert cnab.lote.trailer.formatted_data() == expected_lote_trailer

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_trailer_formatted_data(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()
        expected_trailer = (
            "07799999         000001000006000000                                             "
            "                                                                                "
            "                                                                                "
        )
        assert cnab.trailer.formatted_data() == expected_trailer

    @pytest.mark.usefixtures("legacy_spreadsheet_handler")
    def test_generate_cnab_files(self, legacy_spreadsheet_handler):
        cnab = legacy_spreadsheet_handler.get_cnab_file()

        with open("./tests/fixtures/test_cnab.txt", "r") as f:
            expected_cnab_file = f.read()

        with mock.patch("builtins.open", mock.mock_open()) as mock_file:
            cnab.generate_file()

        handler = mock_file()

        assert handler.write.call_count == 1

        expected_call = handler.write.call_args[0][0]
        assert expected_call == expected_cnab_file
