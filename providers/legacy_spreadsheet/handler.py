import copy

from cnab.cnab240.v10_7 import lambdas
from cnab.cnab240.v10_7.custom_fields import CUSTOM_FIELDS_MAPPING
from cnab.cnab240.v10_7.legacy_models import CNAB240File
from providers.legacy_spreadsheet.mapping import MODELS_SPREADSHEET_MAP
from providers.legacy_spreadsheet.utils import get_spreadsheet_data, parse_data_from
from providers.legacy_spreadsheet.validators import validate_spreadsheet


INITIAL_DATA_DICT = {
    "header": [],
    "trailer": [],
    "lote_header": [],
    "lote_trailer": [],
    "lote_detalhe_segmento_c": [],
    "lote_detalhe_segmento_b": [],
    "lote_detalhe_segmento_a": [],
}


class LegacySpreadsheetHandler:
    def __init__(self, input_filename):
        validate_spreadsheet(input_filename)
        self.initial_data = self.generate_initial_data_with_connectors(input_filename)

    def get_cnab_file(self):
        return CNAB240File(self.initial_data)

    def generate_initial_data_with_connectors(self, filename):
        """
        Fetches data from the spreadsheet and builds in values
        for the keys on INITIAL_DATA_DICT. Returning a dict with
        the following format
        {
            "header": [{"field_01_0": "value", ... }],
            "trailer": [{"field_01_9": "value", ... }],
            "lote_header": [{"field_01_1": "value", ... }],
            "lote_trailer": [{"field_01_5": "value", ... }],
            "lote_detalhe_segmento_c": [{"field_01_3C": "value", ... }],
            "lote_detalhe_segmento_b": [{"field_01_3B": "value", ... }],
            "lote_detalhe_segmento_a": [{"field_01_3A": "value", ... }],
        }

        :param filename: the spreadsheet file path
        :type filename: str
        """
        spreadsheet_data = get_spreadsheet_data(filename)
        input_fields_data = parse_data_from(spreadsheet_data, MODELS_SPREADSHEET_MAP)
        custom_fields_data = self.get_calculated_fields_data(input_fields_data)

        keys = INITIAL_DATA_DICT.keys()
        initial_data = copy.deepcopy(INITIAL_DATA_DICT)
        for key in keys:
            input_fields_content = input_fields_data[key]
            input_fields_content = [info for info in input_fields_content if info]
            custom_fields_content = custom_fields_data[key]

            if key in ["lote_header", "lote_trailer"]:
                input_fields_content = [input_fields_content[0]]

            assert len(input_fields_content) == len(
                custom_fields_content
            ), f"{key}: has different count of input fields and custom fields"

            for _input, _custom in zip(input_fields_content, custom_fields_content):
                segment = {}
                segment.update(_input)
                segment.update(_custom)
                initial_data[key].append(segment)

        return initial_data

    def get_calculated_fields_data(self, spreadsheet_data):
        """
        Fields need to be generated in sequence. In particular,the trailers
        and the lote_detalhe_segmentos need information from previous lines.
        """
        initial_data = copy.deepcopy(INITIAL_DATA_DICT)
        invalid_field_maps = []

        for segment_name in ["header", "lote_header"]:
            fields = CUSTOM_FIELDS_MAPPING[segment_name]
            model_initial_data, errs = self._generate_line(fields, spreadsheet_data)
            initial_data[segment_name] = [model_initial_data]
            invalid_field_maps += errs

        for _ in spreadsheet_data["lote_detalhe_segmento_a"]:
            for segment_name in [
                "lote_detalhe_segmento_a",
                "lote_detalhe_segmento_b",
                "lote_detalhe_segmento_c",
            ]:
                fields = CUSTOM_FIELDS_MAPPING[segment_name]
                model_initial_data, errs = self._generate_line(fields, spreadsheet_data)
                invalid_field_maps += errs
                initial_data[segment_name] += [model_initial_data]

        for segment_name in ["lote_trailer", "trailer"]:
            fields = CUSTOM_FIELDS_MAPPING[segment_name]
            model_initial_data, errs = self._generate_line(fields, spreadsheet_data)
            initial_data[segment_name] = [model_initial_data]
            invalid_field_maps += errs

        if invalid_field_maps:
            raise Exception(invalid_field_maps)

        return initial_data

    def _generate_line(self, fields, spreadsheet_data):
        invalid_field_maps = []
        model_initial_data = {}
        for field_name, field_specs in fields.items():
            lambda_func_name = field_specs["lambda"]
            try:
                if lambda_func_name == "default":
                    # For the fields to get the default value this values must be none or ''
                    # doing this to ease development
                    model_initial_data[field_name] = ""
                else:
                    has_params = field_specs.get("params", False)
                    method_to_call = getattr(lambdas, lambda_func_name)

                    if has_params:
                        model_initial_data[field_name] = method_to_call(
                            spreadsheet_data
                        )
                    else:
                        model_initial_data[field_name] = method_to_call()
            except KeyError:
                error_msg = (
                    f"The column '{field_specs['lambda']}' doesn't "
                    f"exists on the '{lambdas.__file__}' sheet."
                )
                invalid_field_maps.append({field_name: error_msg})
        return model_initial_data, invalid_field_maps
