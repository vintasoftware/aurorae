from openpyxl import load_workbook
from febraban_v10_7 import MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7


def worksheet_dict_reader(worksheet):
    rows = worksheet.iter_rows(values_only=True)
    header = next(rows)
    for row in rows:
        if not any(row):
            return

        yield dict(zip(header, row))


def get_spreadsheet_data():
    workbook = load_workbook(filename="dados-pagamentos.xlsx", read_only=True, data_only=True)
    dados_empresa = worksheet_dict_reader(workbook["Empresa"])
    dados_funcionarios = worksheet_dict_reader(workbook["Funcionários"])
    dados_pagamentos = worksheet_dict_reader(workbook["Pagamentos"])

    return {
        "Empresa": list(dados_empresa)[0],
        "Funcionários": list(dados_funcionarios),
        "Pagamentos": list(dados_pagamentos)
    }
