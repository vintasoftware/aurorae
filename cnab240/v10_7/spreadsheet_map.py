# TODO confirm
# G066
from cnab240.v10_7.models import Field103B, Field113B

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
            "column_name": "* Dígito Verificador da Agência",
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
            "column_name": "* Dígito Verificador da Agência",
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
        "field_23_1": {
            "name": "CEP",
            "sheet_name": "Empresa",
            "column_name": "CEP",
        },
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
        "field_08_3A": {
            "name": "Código da Câmara Centralizadora",
            "sheet_name": "Funcionários",
            "column_name": "* Código da Câmara Centralizadora",
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
            "column_name": "* Dígito Verificador da Agência",
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
        "field_16_3A": {
            "name": "Nº do Docum. Atribuído p/ Empresa",
            "sheet_name": "Pagamentos",
            "column_name": "Nº do Docum. Atribuído p/ Empresa",  # TALVEZ ISSO SEJA GERADO
        },
        "field_17_3A": {
            "name": "Data do Pagamento",
            "sheet_name": "Pagamentos",
            "column_name": "Data do Pagamento",
        },
        "field_19_3A": {
            "name": "Quantidade da Moeda",
            "sheet_name": "Pagamentos",
            "column_name": "Quantidade da Moeda",
        },
        "field_20_3A": {
            "name": "Valor do Pagamento",
            "sheet_name": "Pagamentos",
            "column_name": "Valor do Pagamento",
        },
        "field_21_3A": {
            "name": "Nº do Docum. Atribuído pelo Banco",
            "sheet_name": "Pagamentos",
            "column_name": "* Nº do Docum. Atribuído pelo Banco",  # TALVEZ ISSO SEJA GERADO
        },
    },
    "lote_detalhe_segmento_b": {
        "field_01_3B": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Funcionários",
            "column_name": "Código do Banco do Favorecido",
        },
        "field_06_3B": {
            "name": "Forma de Iniciação",
            "sheet_name": "Funcionários",
            "column_name": "* Forma de Iniciação",  # Confuso # TODO check with bank
        },
        "field_07_3B": {
            "name": "Tipo de Inscrição do Favorecido",
            "sheet_name": "Funcionários",
            "column_name": "* Tipo de Inscrição do Favorecido",
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
            "column_name": Field103B.custom_columns
        },
        "field_11_3B": {
            "name": "Informação 12",
            "sheet_name": "Pagamentos",
            "column_name": Field113B.custom_columns
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
        },
    },
    "trailer": {
        "field_01_9": {
            "name": "Código do Banco na Compensação",
            "sheet_name": "Empresa",
            "column_name": "* Código do Convênio no Banco",
        },
    }
}


# Try to handle fields "field_11_3B"-like in a different way
CUSTOM_FIELDS_MAPPING = {
    "header": {
        "field_02_0": {
            "name": "Lote de Serviço",
            "lambda": "default",
        },
        "field_03_0": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_0": {
            "name": "Uso Exclusivo FEBRABAN / CNAB",
            "lambda": "default",
        },
        "field_15_0": {
            "name": "Uso Exclusivo FEBRABAN / CNAB",
            "lambda": "default",
        },
        "field_16_0": {
            "name": "Código Remessa / Retorno",
            "lambda": "get_codigo_remessa_retorno",
        },
        "field_17_0": {
            "name": "Data de Geração do Arquivo",
            "lambda": "get_data_geracao_do_arquivo",
        },
        "field_18_0": {
            "name": "Hora de Geração do Arquivo",
            "lambda": "get_hora_geracao_do_arquivo",
        },
        "field_19_0": {
            "name": "Número Seqüencial do Arquivo",
            "lambda": "get_num_sequencial_do_arquivo",
        },
        "field_20_0": {
            "name": "Número da Versão do Layout do Arquivo",
            "lambda": "default",
        },
        "field_21_0": {
            "name": "Densidade de Gravação do Arquivo",
            "lambda": "get_densidade_de_gravacao_do_arquivo",
        },
        "field_22_0": {
            "name": "Para Uso Reservado do Banco",
            "lambda": "default",
        },
        "field_23_0": {
            "name": "Para Uso Reservado da Empresa",
            "lambda": "default",
        },
        "field_24_0": {
            "name": "Uso Exclusivo FEBRABAN / CNAB",
            "lambda": "default",
        }
    },
    "lote_header": {
        "field_02_1": {
            "name": "Lote de Serviço",
            "lambda": "get_sequencial_lote_de_servico",
        },
        "field_03_1": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_1": {
            "name": "Tipo da Operação",
            "lambda": "default",
        },
        "field_05_1": {
            "name": "Tipo do Serviço",
            "lambda": "get_tipo_de_servico",
        },
        "field_06_1": {
            "name": "Forma de Lançamento",
            "lambda": "get_forma_de_lancamento",
        },
        "field_07_1": {
            "name": "Nº da Versão do Layout do Lote",
            "lambda": "default",
        },
        "field_08_1": {
            "name": "Uso Exclusivo da FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_26_1": {
            "name": "Indicativo da Forma de Pagamento do Serviço",
            "lambda": "get_indicativo_da_forma_de_pagamento_do_servico",
        },
        "field_27_1": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_28_1": {
            "name": "Códigos das Ocorrências p/ Retorno",
            "lambda": "default",
        }
    },
    "lote_detalhe_segmento_a": {
        "field_02_3A": {
            "name": "Lote de Serviço",
            "lambda": "get_sequencial_lote_de_servico",
        },
        "field_03_3A": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_3A": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "get_sequencial_registro_no_lote",
        },
        "field_05_3A": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_06_3A": {
            "name": "Tipo de Movimento",
            "lambda": "get_tipo_de_movimento",
        },
        "field_07_3A": {
            "name": "Código da Instrução p/ Movimento",
            "lambda": "get_codigo_instrucao_movimento",
        },
        "field_18_3A": {
            "name":"Tipo da Moeda",
            "lambda": "get_tipo_de_moeda",
        },
        "field_22_3A": {
            "name": "Data Real da Efetivação Pagto",
            "lambda": "default",
        },
        "field_23_3A": {
            "name": "Valor Real da Efetivação do Pagto",
            "lambda": "default",
        },
        "field_24_3A": {
            "name": "Outras Informações",
            "lambda": "default",
        },
        "field_25_3A": {
            "name": "Compl. Tipo Serviço",
            "lambda": "get_tipo_de_servico",
        },
        "field_26_3A": {
            "name": "Codigo finalidade da TED",
            "lambda": "get_codigo_finalidade_da_ted",
        },
        "field_27_3A": {
            "name": "Complemento de finalidade pagto.",
            "lambda": "default",
        },
        "field_28_3A": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_29_3A": {
            "name": "Aviso ao Favorecido",
            "lambda": "default",
        },
        "field_30_3A": {
            "name": "Códigos das Ocorrências para Retorno",
            "lambda": "default",
        }
    },
    "lote_detalhe_segmento_b": {
        "field_02_3B": {
            "name": "Lote de Serviço",
            "lambda": "get_sequencial_lote_de_servico",
        },
        "field_03_3B": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_3B": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "get_sequencial_registro_no_lote",
        },
        "field_05_3B": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_12_3B": {
            "name": "Uso Exclusivo para o SIAPE",
            "lambda": "default",
        }
    },
    "lote_detalhe_segmento_c": {
        "field_02_3C": {
            "name": "Lote de Serviço",
            "lambda": "get_sequencial_lote_de_servico",
        },
        "field_03_3C": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_3C": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "get_sequencial_registro_no_lote",
        },
        "field_05_3C": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_06_3C": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_19_3C": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        }
    },
    "lote_trailer": {
        "field_02_5": {
            "name": "Lote de Serviço",
            "lambda": "get_sequencial_lote_de_servico",
        },
        "field_03_5": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_5": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_05_5": {
            "name": "Quantidade de Registros do Lote",
            "lambda": "get_qtde_registros_do_lote",
        },
        "field_06_5": {
            "name": "Somatória dos Valores",
            "params": True,
            "lambda": "get_somatorio_dos_valores",
        },
        "field_07_5": {
            "name": "Somatória de Quantidade de Moedas",
            "params": True,
            "lambda": "get_somatorio_quantidade_de_moedas",
        },
        "field_08_5": {
            "name": "Número Aviso de Débito ",
            "lambda": "get_numero_aviso_debito",
        },
        "field_09_5": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_10_5": {
            "name": "Códigos das Ocorrências para Retorno",
            "lambda": "default",
        }
    },
    "trailer": {
        "field_02_9": {
            "name": "Lote de Serviço",
            "lambda": "default",
        },
        "field_03_9": {
            "name": "Tipo de Registro",
            "lambda": "default",
        },
        "field_04_9": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        },
        "field_05_9": {
            "name": "Quantidade de Lotes do Arquivo",
            "lambda": "get_qtde_de_lotes_do_arquivo",
        },
        "field_06_9": {
            "name": "Quantidade de Registros do Arquivo",
            "lambda": "get_qtde_registros_do_arquivo",
        },
        "field_07_9": {
            "name": "Qtde de Contas p/ Conc. (Lotes)",
            "lambda": "default",
        },
        "field_08_9": {
            "name": "Uso Exclusivo FEBRABAN/CNAB",
            "lambda": "default",
        }
    }
}
