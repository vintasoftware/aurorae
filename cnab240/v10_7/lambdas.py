import os


def get_numero_aviso_debito():
    # @rsarai TODO is_valid this
    return " "


def get_camara_centralizadora():
    """
    '018' = TED (STR,CIP)
    '700' = DOC (COMPE)
    “988”- TED (STR/CIP) – Utilizado quando for necessário o envio de TED utilizando
    o código ISPB da Instituição Financeira Destinatária. Neste caso é obrigatório o
    preenchimento do campo “Código ISPB” – Campo 26.3B, do Segmento de Pagamento,
    conforme descrito na Nota P015.
    “009” – PIX (SPI)
    """
    return '018'


def get_num_sequencial_registro_lote():
    # TODO double check what is this
    return ""


def get_num_sequencial_do_arquivo():
    return str(len(os.listdir("generated_files")) + 1)


def get_codigo_remessa_retorno():
    return "1"


def get_densidade_de_gravacao_do_arquivo():
    # "01600" or "06250"
    return "01600"


def get_data_geracao_do_arquivo():
    import datetime

    return datetime.datetime.now().strftime("%d%m%Y")


def get_hora_geracao_do_arquivo():
    import datetime

    return datetime.datetime.now().strftime("%H%M%S")


def get_tipo_de_servico():
    return "30"  # Pagamento Salários


def get_forma_iniciacao():
    """
    “01” – Chave Pix – tipo Telefone
    “02” – Chave Pix – tipo Email
    “03” – Chave Pix – tipo CPF/CNPJ
    “04” – Chave Aleatória
    “05” – Dados bancários
    """
    return '05'


def get_complemento_tipo_de_servico():
    """
    '01' = Crédito em Conta
    '02' = Pagamento de Aluguel/Condomínio
    '03' = Pagamento de Duplicata/Títulos
    '04' = Pagamento de Dividendos
    '05' = Pagamento de Mensalidade Escolar
    '06' = Pagamento de Salários
    '07' = Pagamento a Fornecedores
    '08' = Operações de Câmbios/Fundos/Bolsa de Valores
    '09' = Repasse de Arrecadação/Pagamento de Tributos
    '10' = Transferência Internacional em Real
    '11' = DOC para Poupança
    '12' = DOC para Depósito Judicial
    '13' = Outros
    ‘16’ = Pagamento de bolsa auxílio
    ‘17’ = Remuneração à cooperado
    ‘18’ = Pagamento de honorários
    ‘19’ = Pagamento de prebenda (Remuneração a padres e sacerdotes)
    """
    return "01"  # Pagamento Salários


def get_forma_de_lancamento():
    return "01"  # Crédito em Conta Corrente/Salário


def get_indicativo_da_forma_de_pagamento_do_servico():
    return "01"  # Débito em Conta Corrente


def get_tipo_de_movimento():
    return "0"  # Indica INCLUSÃO


def get_codigo_instrucao_movimento():
    return "00"  # Inclusão de Registro Detalhe Liberado


def get_codigo_finalidade_da_ted():
    return ""


def get_tipo_de_moeda():
    """
    "BTN" = Bônus do Tesouro Nacional + TR
    "BRL" = Real
    "USD" = Dólar Americano
    "PTE" = Escudo Português
    "FRF" = Franco Francês
    "CHF" = Franco Suíço
    "JPY" = Ien Japonês
    "IGP" = Índice Geral de Preços
    "IGM" = Índice Geral de Preços de Mercado
    "GBP" = Libra Esterlina
    "ITL" = Lira Italiana
    "DEM" = Marco Alemão
    "TRD" = Taxa Referencial Diária
    "UPC" = Unidade Padrão de Capital
    "UPF" = Unidade Padrão de Financiamento
    "UFR" = Unidade Fiscal de Referência
    "XEU" = Unidade Monetária Européia
    """
    return "BRL"


def get_sequencial_lote_de_servico():
    return '0001'


COUNT = 0


def get_sequencial_registro_no_lote():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def get_qtde_registros_do_arquivo():
    """
    Somatório dos tipos de registro
    No nosso caso, número de registros do lote + loteheader + lotetrailer + header + trailer
    Qtd de linhas do arquivo
    """
    return str(COUNT + 2 + 2)


def get_qtde_de_lotes_do_arquivo():
    return '1'


def get_qtde_registros_do_lote():
    """
    Somatório dos tipos de registro
    No nosso caso, número de registros do lote + loteheader + lotetrailer
    """
    return str(COUNT + 2)


def get_somatorio_dos_valores(spreadsheet_data):
    somatorio = 0
    for data_pagamento in spreadsheet_data["lote_detalhe_segmento_a"]:
        str_pagamento = str(data_pagamento["field_20_3A"])
        somatorio += int(str_pagamento)
    return str(somatorio)


# def get_somatorio_quantidade_de_moedas(spreadsheet_data):
#     somatorio = 0
#     for data_pagamento in spreadsheet_data["lote_detalhe_segmento_a"]:
#         str_pagamento = str(data_pagamento["field_19_3A"])
#         somatorio += int(str_pagamento)
#     return str(somatorio)


def get_codigo_finalidade_complementar():
    pass


def get_tipo_inscricao_favorecido():
    """
        '0' = Isento / Não Informado
        '1' = CPF
        '2' = CGC / CNPJ
        '3' = PIS / PASEP
        '9' = Outros
    """
    return '1'
