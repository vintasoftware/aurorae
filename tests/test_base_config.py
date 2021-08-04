import pytest
from pydantic import ValidationError

from cnab.cnab240.base import Line
from cnab.cnab240.v10_7.models import BaseConfig


class TestBaseConfig:
    def test_mapping_works_with_valid_data(self):
        class TestLine(Line):
            name: str
            age: int

            class Config(BaseConfig):
                _mapping = {"name": "_name", "age": "_age"}

        line = TestLine(initial_data={"_name": "TEST NAME", "_age": 20}, line_number=1)
        assert line.name == "TEST NAME"
        assert line.age == 20

    def test_mapping_raises_validation_error_on_missing_key(self):
        class TestLine(Line):
            name: str
            age: int

            class Config(BaseConfig):
                _mapping = {"name": "_name", "age": "_age"}

        with pytest.raises(ValidationError):
            TestLine(initial_data={"_name": "TEST NAME"}, line_number=1)

    def test_mapping_raises_validation_error_on_invalid_mapping(self):
        class TestLine(Line):
            name: str
            age: int

            class Config(BaseConfig):
                _mapping = {"name": "_name", "age": "_age", "invalid": "_invalid"}

        with pytest.raises(ValidationError):
            TestLine(initial_data={"_name": "TEST NAME", "_age": 20}, line_number=1)
