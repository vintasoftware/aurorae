from cnab.cnab240.v10_7.legacy_models import Field103B, Field113B


MODELS_SPREADSHEET_MAP = {
    "header": {
        "field_01_0": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_05_0": {
            "name": "Tipo de Inscrição da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Tipo de Inscrição da Empresa",
        },
        "field_06_0": {
            "name": "Número de Inscrição da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Número de Inscrição da Empresa",
        },
        "field_07_0": {
            "name": "Código do Convênio no Banco",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_08_0": {
            "name": "Agência Mantenedora da Conta",
            "sheet_name": "Empresa",
            "column_name": "* Agência Mantenedora da Conta ",
        },
        "field_09_0": {
            "name": "Dígito Verificador da Agência",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Agência",
        },
        "field_10_0": {
            "name": "Número da Conta Corrente",
            "sheet_name": "Empresa",
            "column_name": "* Número da Conta Corrente",
        },
        "field_11_0": {
            "name": "Dígito Verificador da Conta",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Conta",
        },
        "field_12_0": {
            "name": "Dígito Verificador da Ag/Conta",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Ag/Conta",
        },
        "field_13_0": {
            "name": "Nome da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Nome da Empresa",
        },
        "field_14_0": {
            "name": "Nome do Banco",
            "sheet_name": "Empresa",
            "column_name": "* Nome do Banco",
        },
    },
    "lote_header": {
        "field_01_1": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_09_1": {
            "name": "Tipo de Inscrição da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Tipo de Inscrição da Empresa",
        },
        "field_10_1": {
            "name": "Número de Inscrição da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Número de Inscrição da Empresa",
        },
        "field_11_1": {
            "name": "Código do Convênio no Banco",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_12_1": {
            "name": "Agência Mantenedora da Conta",
            "sheet_name": "Empresa",
            "column_name": "* Agência Mantenedora da Conta ",
        },
        "field_13_1": {
            "name": "Dígito Verificador da Agência",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Agência",
        },
        "field_14_1": {
            "name": "Número da Conta Corrente",
            "sheet_name": "Empresa",
            "column_name": "* Número da Conta Corrente",
        },
        "field_15_1": {
            "name": "Dígito Verificador da Conta",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Conta",
        },
        "field_16_1": {
            "name": "Dígito Verificador da Ag/Conta",
            "sheet_name": "Empresa",
            "column_name": "* Dígito Verificador da Ag/Conta",
        },
        "field_17_1": {
            "name": "Nome da Empresa",
            "sheet_name": "Empresa",
            "column_name": "* Nome da Empresa",
        },
        "field_19_1": {
            "name": "Nome da Rua, Av, Pça, Etc",
            "sheet_name": "Empresa",
            "column_name": "Logradouro (Nome da Rua, Av, Pça, Etc)",
        },
        "field_20_1": {
            "name": "Número do Local",
            "sheet_name": "Empresa",
            "column_name": "Número (Número do Local)",
        },
        "field_21_1": {
            "name": "Casa, Apto, Sala, Etc",
            "sheet_name": "Empresa",
            "column_name": "Complemento (Casa, Apto, Sala, Etc)",
        },
        "field_22_1": {
            "name": "Nome da Cidade",
            "sheet_name": "Empresa",
            "column_name": "Nome da Cidade",
        },
        "field_23_1": {"name": "CEP", "sheet_name": "Empresa", "column_name": "CEP"},
        "field_24_1": {
            "name": "Complemento do CEP",
            "sheet_name": "Empresa",
            "column_name": "Complemento do CEP",
        },
        "field_25_1": {
            "name": "Sigla do Estado",
            "sheet_name": "Empresa",
            "column_name": "Sigla do Estado",
        },
    },
    "lote_detalhe_segmento_a": {
        "field_01_3A": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_09_3A": {
            "name": "Código do Banco do Favorecido",
            "sheet_name": "Funcionários",
            "column_name": "Código do Banco do Favorecido",
        },
        "field_10_3A": {
            "name": "Ag. Mantenedora da Cta do Favor.",
            "sheet_name": "Funcionários",
            "column_name": "* Ag. Mantenedora da Cta do Favor.",
        },
        "field_11_3A": {
            "name": "Dígito Verificador da Agência",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da Agência",
        },
        "field_12_3A": {
            "name": "Número da Conta Corrente",
            "sheet_name": "Funcionários",
            "column_name": "* Número da Conta Corrente",
        },
        "field_13_3A": {
            "name": "Dígito Verificador da Conta",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da Conta",
        },
        "field_14_3A": {
            "name": "Dígito Verificador da AG/Conta",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da AG/Conta",
        },
        "field_15_3A": {
            "name": "Nome do Favorecido",
            "sheet_name": "Funcionários",
            "column_name": "Nome do Favorecido",
        },
        "field_17_3A": {
            "name": "Data do Pagamento",
            "sheet_name": "Pagamentos",
            "column_name": "Data do Pagamento",
        },
        "field_20_3A": {
            "name": "Valor do Pagamento",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do Pagamento",
        },
        "field_22_3A": {
            "name": "Data Real da Efetivação Pagto",
            "sheet_name": "Pagamentos",
            "column_name": "Data Real da Efetivação Pagto",
        },
    },
    "lote_detalhe_segmento_b": {
        "field_01_3B": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Funcionários",
            "column_name": "Código do Banco do Favorecido",
        },
        "field_08_3B": {
            "name": "Nº de Inscrição do Favorecido",
            "sheet_name": "Funcionários",
            "column_name": "* Nº de Inscrição do Favorecido",
        },
        "field_09_3B": {
            "name": "Informação 10",
            "sheet_name": "Funcionários",
            "column_name": "Logradouro (Nome da Rua, Av, Pça, Etc)",
        },
        "field_10_3B": {
            "name": "Informação 11",
            "sheet_name": "Funcionários",
            "column_name": Field103B.composed_fields,
        },
        "field_11_3B": {
            "name": "Informação 12",
            "sheet_name": "Pagamentos",
            "column_name": Field113B.composed_fields,
        },
        "field_13_3B": {
            "name": "Código ISPB",
            "sheet_name": "Pagamentos",
            "column_name": "Código ISPB",
        },
    },
    "lote_detalhe_segmento_c": {
        "field_01_3C": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
        "field_07_3C": {
            "name": "Valor do IR",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do IR",
        },
        "field_08_3C": {
            "name": "Valor do ISS",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do ISS",
        },
        "field_09_3C": {
            "name": "Valor do IOF",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do IOF",
        },
        "field_10_3C": {
            "name": "Valor Outras Deduções",
            "sheet_name": "Pagamentos",
            "column_name": "Valor Outras Deduções",
        },
        "field_11_3C": {
            "name": "Valor Outras Acréscimos",
            "sheet_name": "Pagamentos",
            "column_name": "Valor Outros Acréscimos",
        },
        "field_12_3C": {
            "name": "Agência do Favorecido",
            "sheet_name": "Funcionários",
            "column_name": "* Ag. Mantenedora da Cta do Favor.",
        },
        "field_13_3C": {
            "name": "Dígito Verificador da Agência",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da Agência",
        },
        "field_14_3C": {
            "name": "* Número da Conta Corrente",
            "sheet_name": "Funcionários",
            "column_name": "* Número da Conta Corrente",
        },
        "field_15_3C": {
            "name": "Dígito Verificador da Conta",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da Conta",
        },
        "field_16_3C": {
            "name": "Dígito Verificador Agência/Conta",
            "sheet_name": "Funcionários",
            "column_name": "* Dígito Verificador da AG/Conta",
        },
        "field_17_3C": {
            "name": "Valor do INSS",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do INSS",
        },
        "field_18_3C": {
            "name": "Número Conta Pagamento Creditada",
            "sheet_name": "Pagamentos",
            "column_name": "Número Conta Pagamento Creditada",
        },
    },
    "lote_trailer": {
        "field_01_5": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        }
    },
    "trailer": {
        "field_01_9": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
    },
}
