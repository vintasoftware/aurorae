# Try to handle fields "field_11_3B"-like in a different way
CUSTOM_FIELDS_MAPPING = {
    "header": {
        "field_02_0": {"name": "Lote de Serviço", "lambda": "default"},
        "field_03_0": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_0": {"name": "Uso Exclusivo FEBRABAN / CNAB", "lambda": "default"},
        "field_15_0": {"name": "Uso Exclusivo FEBRABAN / CNAB", "lambda": "default"},
        "field_16_0": {"name": "Código Remessa / Retorno", "lambda": "get_field_G015"},
        "field_17_0": {
            "name": "Data de Geração do Arquivo",
            "lambda": "get_field_G016",
        },
        "field_18_0": {
            "name": "Hora de Geração do Arquivo",
            "lambda": "get_field_G017",
        },
        "field_19_0": {
            "name": "Número Seqüencial do Arquivo",
            "lambda": "get_field_G018",
        },
        "field_20_0": {
            "name": "Número da Versão do Layout do Arquivo",
            "lambda": "default",
        },
        "field_21_0": {
            "name": "Densidade de Gravação do Arquivo",
            "lambda": "get_field_G020",
        },
        "field_22_0": {"name": "Para Uso Reservado do Banco", "lambda": "default"},
        "field_23_0": {"name": "Para Uso Reservado da Empresa", "lambda": "default"},
        "field_24_0": {"name": "Uso Exclusivo FEBRABAN / CNAB", "lambda": "default"},
    },
    "lote_header": {
        "field_02_1": {"name": "Lote de Serviço", "lambda": "get_field_G002"},
        "field_03_1": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_1": {"name": "Tipo da Operação", "lambda": "default"},
        "field_05_1": {"name": "Tipo do Serviço", "lambda": "get_field_G025"},
        "field_06_1": {"name": "Forma de Lançamento", "lambda": "get_field_G029"},
        "field_07_1": {"name": "Nº da Versão do Layout do Lote", "lambda": "default"},
        "field_08_1": {"name": "Uso Exclusivo da FEBRABAN/CNAB", "lambda": "default"},
        "field_26_1": {
            "name": "Indicativo da Forma de Pagamento do Serviço",
            "lambda": "get_field_P014",
        },
        "field_27_1": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_28_1": {
            "name": "Códigos das Ocorrências p/ Retorno",
            "lambda": "default",
        },
    },
    "lote_detalhe_segmento_a": {
        "field_02_3A": {
            "name": "Lote de Serviço",
            "lambda": "get_field_G002",
        },
        "field_03_3A": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_3A": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "get_field_G038",
        },
        "field_05_3A": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_06_3A": {"name": "Tipo de Movimento", "lambda": "get_field_G060"},
        "field_07_3A": {
            "name": "Código da Instrução p/ Movimento",
            "lambda": "get_field_G061",
        },
        "field_08_3A": {
            "name": "Código da Câmara Centralizadora",
            "lambda": "get_field_P001",
        },
        "field_16_3A": {
            "name": "Nº do Docum. Atribuído p/ Empresa",
            "lambda": "default",
        },
        "field_18_3A": {"name": "Tipo da Moeda", "lambda": "get_field_G040"},
        "field_19_3A": {"name": "Quantidade da Moeda", "lambda": "default"},
        "field_21_3A": {
            "name": "Nº do Docum. Atribuído pelo Banco",
            "lambda": "default",
        },
        "field_23_3A": {
            "name": "Valor Real da Efetivação do Pagto",
            "lambda": "default",
        },
        "field_24_3A": {"name": "Outras Informações", "lambda": "default"},
        "field_25_3A": {"name": "Compl. Tipo Serviço", "lambda": "get_field_P005"},
        "field_26_3A": {"name": "Codigo finalidade da TED", "lambda": "get_field_P011"},
        "field_27_3A": {
            "name": "Complemento de finalidade pagto.",
            "lambda": "default",
        },
        "field_28_3A": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_29_3A": {"name": "Aviso ao Favorecido", "lambda": "default"},
        "field_30_3A": {
            "name": "Códigos das Ocorrências para Retorno",
            "lambda": "default",
        },
    },
    "lote_detalhe_segmento_b": {
        "field_02_3B": {
            "name": "Lote de Serviço",
            "lambda": "get_field_G002",
        },
        "field_03_3B": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_3B": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "get_field_G038",
        },
        "field_05_3B": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_06_3B": {"name": "Forma de Iniciação", "lambda": "get_field_G100"},
        "field_07_3B": {
            "name": "Tipo de Inscrição do Favorecido",
            "lambda": "get_field_G005",
        },
        "field_12_3B": {"name": "Uso Exclusivo para o SIAPE", "lambda": "default"},
    },
    "lote_detalhe_segmento_c": {
        "field_02_3C": {
            "name": "Lote de Serviço",
            "lambda": "get_field_G002",
        },
        "field_03_3C": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_3C": {
            "name": "Nº Seqüencial do Registro no Lote",
            "lambda": "default",
        },
        "field_05_3C": {
            "name": "Código de Segmento do Reg. Detalhe",
            "lambda": "default",
        },
        "field_06_3C": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_19_3C": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
    },
    "lote_trailer": {
        "field_02_5": {
            "name": "Lote de Serviço",
            "lambda": "get_field_G002",
        },
        "field_03_5": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_5": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_05_5": {
            "name": "Quantidade de Registros do Lote",
            "lambda": "get_field_G057",
        },
        "field_06_5": {
            "name": "Somatória dos Valores",
            "params": True,
            "lambda": "get_field_P007",
        },
        "field_07_5": {
            "name": "Somatória de Quantidade de Moedas",
            "lambda": "default",
        },
        "field_08_5": {"name": "Número Aviso de Débito ", "lambda": "default"},
        "field_09_5": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_10_5": {
            "name": "Códigos das Ocorrências para Retorno",
            "lambda": "default",
        },
    },
    "trailer": {
        "field_02_9": {"name": "Lote de Serviço", "lambda": "default"},
        "field_03_9": {"name": "Tipo de Registro", "lambda": "default"},
        "field_04_9": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
        "field_05_9": {
            "name": "Quantidade de Lotes do Arquivo",
            "lambda": "get_field_G049",
        },
        "field_06_9": {
            "name": "Quantidade de Registros do Arquivo",
            "lambda": "get_field_G056",
        },
        "field_07_9": {"name": "Qtde de Contas p/ Conc. (Lotes)", "lambda": "default"},
        "field_08_9": {"name": "Uso Exclusivo FEBRABAN/CNAB", "lambda": "default"},
    },
}
