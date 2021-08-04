from datetime import datetime

import pytest
from freezegun.api import freeze_time
from pydantic import ValidationError

from cnab.cnab240.v10_7 import lambdas, types
from cnab.cnab240.v10_7.models import (
    CNABBatchHeader,
    CNABBatchSegmentA,
    CNABBatchSegmentB,
    CNABBatchTrailer,
    CNABHeader,
    CNABTrailer,
)


@freeze_time(datetime(2021, 7, 8, 13, 30, 50))
class TestModels:
    def setup_method(self, __):
        lambdas.COUNT = 0

    def test_header_fixed_width(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }
        header = CNABHeader(header_data, line_number=1)

        expected_header = (
            "07700000         99999999900099977                  00001900000099999999 VINTA "
            "SERVICOS E SOLUCOES TECBANCO INTERMEDIUM                       1080720211330500"
            "0000110301600                                                                     "
        )
        assert header.as_fixed_width() == expected_header

    def test_header_error_on_field_01_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "7777",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_header_error_on_field_12_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "999",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_header_error_on_field_10_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "9999998888888",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_batch_header_fixed_width(self):
        batch_header_data = {
            "field_01_1": "77",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        batch_header = CNABBatchHeader(batch_header_data, line_number=1)
        expected_header = (
            "07700011C3001046 19999999900099977                  00001100000099999911VINTA "
            "SERVICOS E SOLUCOES TEC                                         RUA TEST RUA"
            "                  00123CASA           RECIFE              55999000PE01                "
        )
        assert batch_header.as_fixed_width() == expected_header

    def test_batch_header_fixed_width_with_custom_field_01_1(self):
        batch_header_data = {
            "field_01_1": "1",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        batch_header = CNABBatchHeader(batch_header_data, line_number=1)
        expected_header = (
            "00100011C3001046 19999999900099977                  00001100000099999911VINTA "
            "SERVICOS E SOLUCOES TEC                                         RUA TEST RUA"
            "                  00123CASA           RECIFE              55999000PE01                "
        )
        assert batch_header.as_fixed_width() == expected_header

    def test_batch_header_with_wrong_field_01_1(self):
        batch_header_data = {
            "field_01_1": "1111",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        with pytest.raises(ValidationError):
            CNABBatchHeader(batch_header_data, line_number=1)

    def test_batch_header_with_wrong_field_05_1_enum_value(self):
        batch_header_data = {
            "field_01_1": "1111",
            "field_05_1": "91",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        with pytest.raises(ValidationError):
            CNABBatchHeader(batch_header_data, line_number=1)

    def test_segment_a_fixed_width(self):
        batch_segment_a_data = {
            "field_01_3A": "77",
            "field_09_3A": "77",
            "field_10_3A": "0001",
            "field_11_3A": "9",
            "field_12_3A": "9999999",
            "field_13_3A": "0",
            "field_14_3A": "0",
            "field_15_3A": "Maria Fulana da Silva",
            "field_17_3A": "11062021",
            "field_20_3A": "1000",
            "field_22_3A": "11062021",
        }

        segment_a = CNABBatchSegmentA(batch_segment_a_data, line_number=1)

        expected_segment_a = (
            "0770001300001A00001807700001900000999999900MARIA FULANA DA SILVA                "
            "             11062021BRL000000000000000000000000001000                    110620"
            "21000000000000000                                        01          0          "
        )
        assert segment_a.as_fixed_width() == expected_segment_a

    def test_trailer_fixed_width(self):
        trailer_data = {"field_01_9": "77"}
        trailer = CNABTrailer(trailer_data, line_number=6)

        expected_trailer = expected_trailer = (
            "07799999         000001000006000000                                             "
            "                                                                                "
            "                                                                                "
        )
        assert trailer.as_fixed_width() == expected_trailer

    def test_trailer_error_on_field_01_9_with_size_bigger_than_expected(self):
        trailer_data = {"field_01_9": "9999"}
        with pytest.raises(
            ValidationError,
            match=r"(?s).*field_01_9.*ensure this value is less than or equal to 999.*",
        ):
            CNABTrailer(trailer_data, line_number=6)

    def test_trailer_error_on_field_01_9_with_invalid_number(self):
        trailer_data = {"field_01_9": "invalid_bank_code"}
        with pytest.raises(
            ValidationError, match=r"(?s).*field_01_9.*value is not a valid integer.*"
        ):
            CNABTrailer(trailer_data, line_number=6)

    def test_batch_detail_segment_b_as_fixed_width(self):
        batch_detail_segment_b = {
            "field_01_3B": "77",
            "field_08_3B": "99966699900",
        }
        batch_detail_segment_b_model = CNABBatchSegmentB(
            batch_detail_segment_b, line_number=4
        )
        expected_line = (
            "0770001300001B005100099966699900                                 "
            "                                                                  "
            "                                                                    "
            "                           00000000000000"
        )

        assert batch_detail_segment_b_model.as_fixed_width() == expected_line
        assert batch_detail_segment_b_model.field_02_3B == types.SequentialServiceBatch(
            __root__=1
        )  # noqa
        assert batch_detail_segment_b_model.field_03_3B == types.EntryType(
            __root__=3
        )  # noqa
        assert (
            batch_detail_segment_b_model.field_05_3B
            == types.DetailRecordSegmentType(__root__="B")
        )  # noqa

    def test_batch_detail_segment_b_as_fixed_width_with_custom_field_01_3B(self):
        batch_detail_segment_b = {
            "field_01_3B": "1",
            "field_08_3B": "99966699900",
        }
        batch_detail_segment_b_model = CNABBatchSegmentB(
            batch_detail_segment_b, line_number=4
        )

        assert batch_detail_segment_b_model.field_01_3B.as_fixed_width() == "001"

    def test_batch_detail_segment_b_with_wrong_field_01_3B(self):
        batch_detail_segment_b = {
            "field_01_3B": "11111111",
            "field_08_3B": "99966699900",
        }

        with pytest.raises(ValidationError):
            CNABBatchSegmentB(batch_detail_segment_b, line_number=4)

    def test_batch_trailer_fixed_width(self):
        batch_trailer_data = {
            "field_01_5": "77",
            "field_06_5": "1000",
        }

        batch_trailer = CNABBatchTrailer(batch_trailer_data, line_number=5)

        expected_batch_trailer = (
            "07700015         000004000000000000001000000000000000000000000000               "
            "                                                                                "
            "                                                                                "
        )
        assert batch_trailer.as_fixed_width() == expected_batch_trailer
