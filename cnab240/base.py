import random
import colorsys


class BaseLine:
    total_positions = 240
    formatted_value = ""
    errors = []

    def __init__(self, initial_data):
        self.initial_data = initial_data

    def get_field_names(self):
        field_names = filter(lambda field_name: field_name.startswith("field_"), dir(self))
        return list(field_names)

    def formatted_data(self):
        """
        This method requires that all the formatted values from the fields must be
        already formatted and with the right amount of positions. The field values
        are instantiated after calling `.is_valid()`.
        """
        if not self.is_valid():
            raise Exception(f"The `initial_data` is not valid {self.errors}")

        for field in self.get_fields():
            self.formatted_value = f"{self.formatted_value}{field.to_cnab240_representation()}"

        assert len(self.formatted_value) == self.total_positions

        return self.formatted_value

    def formatted_html(self):
        formatted_html = ""
        for field in self.get_fields():
            field_representation = field.to_cnab240_representation().replace(" ", "_")
            span_width = (field.pos_end - field.pos_initial + 1) * 8

            field_html_representation = (
                f"<span style='background-color: aliceblue; width: {span_width}px' "
                f"id='{field.field_name}' "
                f"data-tooltip='{field.code} - {field.name}'>"
                f"{field_representation}"
                f"</span>"
            )
            formatted_html = f"{formatted_html}{field_html_representation}"
        return f"<div class='{self.__class__.__name__}'>{formatted_html}</div>"

    def get_fields(self):
        fields = []
        for field_name in self.get_field_names():
            field = getattr(self, field_name)
            field.field_name = field_name
            fields.append(field)
        return fields

    def is_valid(self, raise_exception=False):
        if not self.initial_data:
            self.errors.append(
                Exception(
                    'Cannot call `.is_valid()` as no `initial_data={}` keyword argument was '
                    'passed when instantiating the Header instance.'
                )
            )

        for field in self.get_fields():
            initial_value = self.initial_data.get(field.field_name)

            try:
                field.validate(initial_value=initial_value)
            except Exception as field_error:
                self.errors.append(f"{field.field_name}: {field_error}")

        if self.errors and raise_exception:
            raise Exception(self.errors)

        return not any(self.errors)


class Field:
    """
    This class is only responsible to know on how to format the initial value to be written on the file.
    """
    formatted_value = ""
    field_name = None
    initial_value = None

    def __init__(self, name, pos_initial, pos_end, data_type, default_value, description, code, required=False):
        self.name = name
        self.pos_initial = pos_initial
        self.pos_end = pos_end
        self.data_type = data_type
        self.default_value = default_value
        self.description = description
        self.code = code
        self.required = required

    def __str__(self):
        return self.formatted_value

    @property
    def length(self):
        return self.pos_end - self.pos_initial + 1

    def get_initial_value(self):
        if self.initial_value:
            initial_value = self.initial_value
        elif self.default_value:
            initial_value = self.default_value
        else:
            initial_value = ""

        return initial_value

    def validate(self, initial_value=None):
        self.initial_value = initial_value
        errors = []

        if self.data_type not in ["num", "alfa"]:
            errors.append(Exception(f"Formato invalido: {self.data_type}"))

        if self.required:
            if self.data_type == "num" and not self.initial_value.isdigit():
                errors.append(
                    Exception("Este campo aceita somente números")
                )

        if not self.initial_value and self.required:
            errors.append(
                Exception(
                    f"O campo '{self.field_name}' é obrigatório"
                )
            )

        if self.initial_value and (len(self.initial_value) > self.length):
            errors.append(
                Exception(
                    f"A quantidade total de caracteres do valor '{self.initial_value}' da coluna '{self.name}' "
                    f"é invalida: Total permitido '{self.length}'."
                )
            )

        if errors:
            raise Exception({self.field_name: errors})

        return None

    def to_cnab240_representation(self):
        initial_value = self.get_initial_value()

        if self.data_type == "num":
            self.formatted_value = initial_value.zfill(self.length)
        elif self.data_type == "alfa":
            self.formatted_value = initial_value.ljust(self.length, " ")

        return self.formatted_value
