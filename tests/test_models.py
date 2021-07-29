from datetime import datetime

import pytest
from freezegun.api import freeze_time
from pydantic import ValidationError

from cnab.cnab240.v10_7.models import CNABHeader, CNABTrailer


@freeze_time(datetime(2021, 7, 8, 13, 30, 50))
class TestModels:
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
