from openpyxl import load_workbook

from cnab240.v10_7.spreadsheet_map import MODELS_SPREADSHEET_MAP


def worksheet_dict_reader(worksheet):
    rows = worksheet.iter_rows(values_only=True)
    header = next(rows)
    for row in rows:
        if not any(row):
            return

        yield dict(zip(header, row))


def get_spreadsheet_data():
    workbook = load_workbook(filename="/Users/marcosfelipe/Marcos Felipe/Professional/Companies/vinta/projects/vinta-pagamentos/dados-pagamentos.xlsx", read_only=True, data_only=True)
    dados_empresa = worksheet_dict_reader(workbook["Empresa"])
    dados_funcionarios = worksheet_dict_reader(workbook["Funcionários"])
    dados_pagamentos = worksheet_dict_reader(workbook["Pagamentos"])

    return {
        "Empresa": list(dados_empresa),
        "Funcionários": list(dados_funcionarios),
        "Pagamentos": list(dados_pagamentos)
    }


def get_initial_data(spreadsheet_data):
    initial_data = {}
    invalid_field_maps = []

    # Models
    for model_name, fields in MODELS_SPREADSHEET_MAP.items():
        model_initial_data = {}

        # Fields
        for field_name, mapped_data in fields.items():
            # Sheet Rows
            sheet_rows = spreadsheet_data[mapped_data["sheet_name"]]
            for row in sheet_rows:
                try:
                    if isinstance(mapped_data["column_name"], list):
                        # Multiple fields mapped as one column
                        for mapped_column in mapped_data["column_name"]:
                            custom_column_name = mapped_column[0]
                            try:
                                model_initial_data[field_name] = {
                                    custom_column_name: row[custom_column_name]
                                }
                            except KeyError:
                                error_msg = (
                                    f"The column '{custom_column_name}' doesn't "
                                    f"exists on the '{mapped_data['sheet_name']}' sheet."
                                )
                                invalid_field_maps.append({field_name: error_msg})
                    else:
                        data = row[mapped_data["column_name"]]
                        model_initial_data[field_name] = data
                except KeyError:
                    error_msg = (
                        f"The column '{mapped_data['column_name']}' doesn't "
                        f"exists on the '{mapped_data['sheet_name']}' sheet."
                    )
                    invalid_field_maps.append({field_name: error_msg})

        initial_data[model_name] = model_initial_data

    if invalid_field_maps:
        raise Exception(invalid_field_maps)

    return initial_data


def get_lote_header_initial_data(spreadsheet_data):
    pass


def get_lote_detalhe_segmento_a_initial_data(spreadsheet_data):
    pass


def get_lote_detalhe_segmento_b_initial_data(spreadsheet_data):
    pass


def get_lote_detalhe_segmento_c_initial_data(spreadsheet_data):
    pass


def get_lote_trailer_initial_data(spreadsheet_data):
    pass


def get_trailer_initial_data(spreadsheet_data):
    pass


def get_test():
    pass
