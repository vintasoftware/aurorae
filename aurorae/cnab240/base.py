from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.fields import PrivateAttr


class Line(BaseModel):
    _total_positions: int = PrivateAttr(default=240)
    _formatted_value: str = PrivateAttr(default="")
    _line_number: int = PrivateAttr()

    def __init__(self, initial_data, line_number):  # noqa
        self._line_number = line_number
        self.validate_mapping()
        super().__init__(**initial_data)

    def validate_mapping(self):
        mapping = self.get_field_mapping()
        if not mapping:
            return

        mapping_set = set(mapping.keys())
        fields_set = set(self.get_field_names())

        diff = mapping_set.difference(fields_set)
        if not diff:
            return

        raise (
            ValidationError(
                [
                    ErrorWrapper(
                        Exception(
                            f"Config mapping keys: {diff} do not match valid fields"
                        ),
                        loc="config_mapping",
                    )
                ],
                model=self.__class__,
            )
        )

    def get_field_mapping(self):
        config = getattr(self, "Config")

        if not config:
            return None

        return getattr(config, "_mapping", None)

    def get_field_names(self):
        return self.__fields__.keys()

    def get_fields(self):
        fields = []
        for field_name in self.get_field_names():
            field = getattr(self, field_name)
            fields.append(field)
        return fields

    def get_field_info(self, field_name):
        field = self.__fields__[field_name]
        return field.field_info

    def as_fixed_width(self):
        for field in self.get_fields():
            self._formatted_value = f"{self._formatted_value}{field.as_fixed_width()}"

        assert len(self._formatted_value) == self._total_positions

        return self._formatted_value

    def as_html(self):
        formatted_html = f"<span class='line-number'>{self._line_number}.</span>"
        for field_name in self.get_field_names():
            field = getattr(self, field_name)
            field_info = self.get_field_info(field_name)

            field_tooltip = (
                f"{field_info.extra['code']} - "
                f"{field_name} - "
                f"{field_info.description}\n"
            )
            field_representation = field.as_fixed_width().replace(" ", "_")

            field_html_representation = (
                f"<span id='{field_name}' "
                f"data-tooltip='{field_tooltip}'>"
                f"{field_representation}"
                f"</span>"
            )
            formatted_html = f"{formatted_html}{field_html_representation}"
        return f"<div class='{self.__class__.__name__}'>{formatted_html}</div>"
