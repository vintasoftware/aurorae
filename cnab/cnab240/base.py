from pydantic.fields import PrivateAttr
from pydantic.main import BaseModel


class Line(BaseModel):
    _total_positions: int = PrivateAttr(default=240)
    _formatted_value: str = PrivateAttr(default="")
    _line_number: int = PrivateAttr()

    def __init__(self, initial_data, line_number):  # noqa
        self._line_number = line_number
        super().__init__(**initial_data)

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
