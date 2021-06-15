from pathlib import Path
from openpyxl import load_workbook


def worksheet_dict_reader(worksheet):
    rows = worksheet.iter_rows(values_only=True)
    header = next(rows)
    for row in rows:
        if not any(row):
            return
        yield dict(zip(header, row))


def get_spreadsheet_data(filename: Path) -> dict:
    workbook = load_workbook(filename=filename, read_only=True, data_only=True)
    dados_empresa = worksheet_dict_reader(workbook["Empresa"])
    dados_funcionarios = worksheet_dict_reader(workbook["Funcionários"])
    dados_pagamentos = worksheet_dict_reader(workbook["Pagamentos"])

    return {
        "Empresa": list(dados_empresa),
        "Funcionários": list(dados_funcionarios),
        "Pagamentos": list(dados_pagamentos),
    }


def parse_data_from(spreadsheet_data: dict, spreadsheet_map: dict) -> dict:
    from .parser import fill_data
    errors = []
    parsed_data = {}

    for segment_name, segment_fields in spreadsheet_map.items():
        for field_name, field_specs in segment_fields.items():
            sheet_name = field_specs["sheet_name"]
            related_column_name = field_specs["column_name"]
            sheet_rows = spreadsheet_data[sheet_name]
            data, invalid_field_maps = get_field_based_on(
                field_name, related_column_name, sheet_rows, fill_data
            )
            if invalid_field_maps:
                errors += invalid_field_maps
                continue

            if not parsed_data.get(segment_name):
                parsed_data[segment_name] = {}
            parsed_data[segment_name].update(data)

    if invalid_field_maps:
        raise Exception(invalid_field_maps)

    return parsed_data


def get_field_based_on(
        field_name: str,
        origin_spreadsheet_name: str,
        sheet_rows: dict,
        fillData
    ):
    initial_data = {}
    invalid_field_maps = []
    is_composed_field = isinstance(origin_spreadsheet_name, list)

    for row in sheet_rows:
        try:
            if is_composed_field:
                # Multiple fields mapped as one column
                composed_fields = {}
                composed_fields_definition = origin_spreadsheet_name
                for composed_field_def in composed_fields_definition:
                    composed_column_name = composed_field_def["name"]
                    try:
                        composed_fields[composed_column_name] = row[
                            composed_column_name
                        ]
                    except KeyError:
                        error_msg = (
                            f"The column '{composed_column_name}' doesn't "
                            f"exists on the '{origin_spreadsheet_name}' sheet."
                        )
                        invalid_field_maps.append({field_name: error_msg})
                initial_data = fillData(
                    initial_data,
                    field_name,
                    composed_fields
                )
            else:
                data = row[origin_spreadsheet_name]
                initial_data = fillData(
                    initial_data,
                    field_name,
                    str(data)
                )
        except KeyError:
            error_msg = (
                f"The column '{origin_spreadsheet_name}' doesn't "
                f"exists on the '{origin_spreadsheet_name}' sheet."
            )
            invalid_field_maps.append({field_name: error_msg})

    return initial_data, invalid_field_maps


