# pylint: disable=unsubscriptable-object
from typing import ClassVar

import pytest
from pydantic.error_wrappers import ValidationError
from pydantic.types import conint, constr

from cnab.cnab240.v10_7.types import CNABAlphaPositiveInt, CNABPositiveInt, CNABString


class TestTypes:
    def test_cnab_positive_int(self):
        class PositiveIntField(CNABPositiveInt):
            _max_str_length: ClassVar[int] = 5
            _min_int: ClassVar[int] = 1
            _max_int: ClassVar[int] = 99999

            __root__: conint(ge=_min_int, le=_max_int)

        positive_int = PositiveIntField.parse_obj(10)
        assert positive_int.as_fixed_width() == "00010"

        positive_int = PositiveIntField.parse_obj("100")
        assert positive_int.as_fixed_width() == "00100"

        with pytest.raises(ValidationError):
            PositiveIntField.parse_obj(100.0)

        with pytest.raises(ValidationError):
            PositiveIntField.parse_obj(100.00)

        with pytest.raises(ValidationError):
            PositiveIntField.parse_obj("100,00")

        with pytest.raises(ValidationError):
            PositiveIntField.parse_obj("1.234,90")

    def test_cnab_alpha_positive_int(self):
        class AlphaPositiveIntField(CNABAlphaPositiveInt):
            _max_str_length: ClassVar[int] = 5
            _min_int: ClassVar[int] = 1
            _max_int: ClassVar[int] = 99999

            __root__: conint(ge=_min_int, le=_max_int)

        alpha_positive_int = AlphaPositiveIntField.parse_obj(10)
        assert alpha_positive_int.as_fixed_width() == "10   "

        alpha_positive_int = AlphaPositiveIntField.parse_obj("100")
        assert alpha_positive_int.as_fixed_width() == "100  "

        with pytest.raises(ValidationError):
            AlphaPositiveIntField.parse_obj(100.0)

        with pytest.raises(ValidationError):
            AlphaPositiveIntField.parse_obj(100.00)

        with pytest.raises(ValidationError):
            AlphaPositiveIntField.parse_obj("100,00")

        with pytest.raises(ValidationError):
            AlphaPositiveIntField.parse_obj("1.234,90")

    def test_cnab_string_raises_exception_for_special_characters(self):
        class StringField(CNABString):
            _max_str_length: ClassVar[int] = 10
            __root__: constr(max_length=_max_str_length)

        with pytest.raises(ValidationError):
            StringField.parse_obj("TEST!@")

    def test_cnab_string_is_valid(self):
        class StringField(CNABString):
            _max_str_length: ClassVar[int] = 30
            __root__: constr(max_length=_max_str_length)

        StringField.parse_obj("Test string . Ç 123 ç")
