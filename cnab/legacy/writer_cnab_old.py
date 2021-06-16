#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from legacy.febraban_v10_7 import FEBRABAN_V10_7


def get_numero_aviso_debito():
    # @rsarai TODO is_valid this
    return " "


def get_num_sequencial_registro_lote():
    # TODO double check what is this
    return ""


def get_num_sequencial_do_arquivo():
    return str(len(os.listdir("../../generated_files")) + 1)


# @TODO Check this
def get_tipo_inscricao_favorecido(name):
    if name == "Isento / Não Informado":
        return "0"

    if name == "CPF":
        return "1"

    if name == "CGC / CNPJ":
        return "2"

    if name == "PIS / PASEP":
        return "3"

    if name == "Outros":
        return "9"


def get_codigo_remessa_retorno(chave):
    if chave != "16.0":
        raise Exception("Wrong key")
    return "1"


def get_data_geracao_do_arquivo():
    import datetime

    return datetime.datetime.now().strftime("%d%m%Y")


def get_hora_geracao_do_arquivo():
    import datetime

    return datetime.datetime.now().strftime("%H%M%S")


def get_numero_sequencial_do_arquivo():
    return 1


def get_densidade_de_gravacao_do_arquivo():
    # "01600" or "06250"
    return "01600"


def get_tipo_de_servico():
    return "30"  # Pagamento Salários


def get_forma_de_lancamento():
    return "01"  # Crédito em Conta Corrente/Salário


def get_indicativo_da_forma_de_pagamento_do_servico():
    return "01"  # Débito em Conta Corrente


def get_tipo_de_movimento():
    return "0"  # Indica INCLUSÃO


def get_codigo_instrucao_movimento():
    return "00"  # Inclusão de Registro Detalhe Liberado


def get_complemento_tipo_servico():
    return "06"  # Pagamento de Salários


def get_codigo_finalidade_da_ted():
    return "077"  # inter


def get_codigo_finalidade_complementar():
    """
    Código adotado para complemento da finalidade pagamento. A forma de utilização
    deverá ser acordada entre banco e cliente.
    """
    # TODO Check this with bank
    return ""


def get_aviso_ao_favorecido():
    return "2"  # Emite Aviso Somente para o Remetente


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


class GerarArquivoCNAB240_V10_7:
    LOTES_DE_SERVICO_CAMPOS = [
        "02.1",
        "02.9",
        "02.5",
        "02.3C",
        "02.3B",
        "02.3A",
        "02.1",
        "02.0",
    ]

    def __init__(self, dados_entrada_mapeados):
        self.febraban_arquivo_config = FEBRABAN_V10_7
        self.dados_entrada_mapeados = dados_entrada_mapeados

    def gerar_arquivo(self):
        arquivo = open("cnab240.txt", "w")

        arquivo.write(self.gerar_header())
        arquivo.write(self.gerar_lote_header())
        for lote_detalhe_segmento in self.gerar_lote_detalhes_segmentos():
            arquivo.write(lote_detalhe_segmento)
        arquivo.write(self.gerar_lote_trailer())
        arquivo.write(self.gerar_trailer())

        arquivo.close()
        return None

    def gerar_header(self):
        campos_do_header = FEBRABAN_V10_7["header"]["campos"]
        linha = self.gerar_linha(campos_do_header)
        return linha

    def gerar_linha(self, campos_do_segmento, index=None):
        fields = list(campos_do_segmento.keys())
        fields.sort()

        line = ""
        for key in fields:
            value = None
            field_config = campos_do_segmento[key]
            real_data_location = MAPPED_FEBRABAN_V10_7_WITH_SPREADSHEET[key]

            if real_data_location.get("tipo", None):
                """
                Significa que o campo tem um correspondente na planilha de entrada
                """
                planilha = real_data_location["tipo"]
                name = real_data_location["field_na_planilha_de_entrada"]
                value = self.dados_entrada_mapeados[planilha][name]
                campo = Field(value, campo_config=field_config)
                line += str(campo)
            else:
                """
                Significa que o campo NÃO tem um correspondente na planilha de entrada
                e precisa ser gerado
                """
                has_default_value = field_config["default"]
                if has_default_value:
                    has_default_value = (
                        " " if has_default_value == "Brancos" else has_default_value
                    )
                    campo = Field(has_default_value, campo_config=field_config)
                    line += str(campo)
                    continue

                """
                Não tem default e precisa ser gerado
                """
                if key in self.LOTES_DE_SERVICO_CAMPOS:
                    value = index
                    campo = Field(value, campo_config=field_config)
                    line += str(campo)
                    continue

                if key == "16.0":
                    value = get_codigo_remessa_retorno(key)

                if key == "05.1":
                    value = get_tipo_de_servico()

                if key == "06.1":
                    value = get_forma_de_lancamento()

                if key == "26.1":
                    value = get_indicativo_da_forma_de_pagamento_do_servico()

                if key == "05.5":
                    value = "1"

                if key == "06.5":
                    somatoria_dos_valuees = 0
                    for pg in self.dados_entrada_mapeados["Pagamentos"]:
                        somatoria_dos_valuees += int(pg["Valor do Pagamento"])
                    value = somatoria_dos_valuees

                if key == "07.5":
                    somatoria_dos_valuees = 0
                    for pg in self.dados_entrada_mapeados["Pagamentos"]:
                        somatoria_dos_valuees += int(pg["Quantidade da Moeda"])
                    value = somatoria_dos_valuees

                if key == "08.5":
                    value = get_numero_aviso_debito()

                if key in [
                    "18.1",
                    "27.1",
                    "28.1",
                    "04.5",
                    "09.5",
                    "10.5",
                    "22.0",
                    "23.0",
                    "24.0",
                ]:
                    value = " "

                if key == "17.0":
                    value = get_data_geracao_do_arquivo()

                if key == "18.0":
                    value = get_hora_geracao_do_arquivo()

                if key == "19.0":
                    value = get_num_sequencial_do_arquivo()

                if key == "21.0":
                    value = get_densidade_de_gravacao_do_arquivo()

                assert value, f"Campo {key} não pode ser None"
                campo = Field(value, campo_config=field_config)
                line += str(campo)
                continue
        return line

    def gerar_linha_detalhamento(
        self, index, campos_do_segmento, dados_pagamento, dados_funcionario
    ):
        local_dados_entrada_mapeados = {
            "Empresa": self.dados_entrada_mapeados["Empresa"],
            "Funcionários": dados_funcionario,
            "Pagamentos": dados_pagamento,
        }
        fields = list(campos_do_segmento.keys())
        fields.sort()

        line = ""
        for key in fields:
            field_config = campos_do_segmento[key]
            real_data_location = MAPPED_FEBRABAN_V10_7_WITH_SPREADSHEET[key]

            if real_data_location.get("tipo", None):
                """
                Significa que o campo tem um correspondente na planilha de entrada
                """
                planilha = real_data_location["tipo"]
                name = real_data_location["field_na_planilha_de_entrada"]
                if key == "06.3B":
                    # @rsarai TODO remove this when get an answer from bank
                    line += "  "
                    continue

                if key == "07.3B":
                    value = local_dados_entrada_mapeados[planilha][name]
                    line += get_tipo_inscricao_favorecido(value)
                    continue

                if key == "10.3B":
                    custom_fields_config = real_data_location[
                        "field_na_planilha_de_entrada"
                    ]
                    for field_name, specs in custom_fields_config:
                        value = local_dados_entrada_mapeados[planilha][field_name]
                        campo_config = {
                            "value_default": None,
                            "pos_initial": specs[0],
                            "pos_end": specs[1],
                            "data_type": specs[2],
                            "name": field_name,
                        }
                        campo = Field(value, campo_config=campo_config)
                        line += str(campo)
                    continue

                if key == "11.3B":
                    custom_fields_config = real_data_location[
                        "field_na_planilha_de_entrada"
                    ]
                    for field_name, specs in custom_fields_config:
                        if field_name == "Aviso ao Favorecido":
                            line += get_aviso_ao_favorecido()
                        else:
                            value = local_dados_entrada_mapeados[planilha][field_name]
                            campo_config = {
                                "value_default": None,
                                "pos_initial": specs[0],
                                "pos_end": specs[1],
                                "data_type": specs[2],
                                "name": field_name,
                            }
                            campo = Field(value, campo_config=campo_config)
                            line += str(campo)
                    continue

                value = local_dados_entrada_mapeados[planilha][name]
                campo = Field(value, campo_config=field_config)
                line += str(campo)
            else:
                has_default_value = field_config["default"]
                if has_default_value:
                    has_default_value = (
                        " " if has_default_value == "Brancos" else has_default_value
                    )
                    campo = Field(has_default_value, campo_config=field_config)
                    line += str(campo)
                    continue

                if key in self.LOTES_DE_SERVICO_CAMPOS:
                    value = index
                    campo = Field(value, campo_config=field_config)
                    line += str(campo)
                    continue

                if key == "18.3A":
                    line += get_tipo_de_moeda()
                    continue

                if key == "04.3C":
                    line += get_num_sequencial_registro_lote()
                    continue

                if key == "06.3A":
                    line += get_tipo_de_movimento()
                    continue

                if key == "07.3A":
                    line += get_codigo_instrucao_movimento()
                    continue

                if key == "26.3A":
                    line += get_codigo_finalidade_da_ted()
                    continue

                if key == "25.3A":
                    line += get_tipo_de_servico()
                    continue

                if key in [
                    "22.3A",
                    "23.3A",
                    "24.3A",
                    "30.3A",
                    "29.3A",
                    "28.3A",
                    "27.3A",
                ]:
                    value = " "
                    campo = Field(value, campo_config=field_config)
                    line += str(campo)
                    continue

                print(f"Could not map {key}")
                # assert key, f"Could not map {key} "
        return line

    def gerar_lote_header(self, index):
        campos_do_header = FEBRABAN_V10_7["header_lote"]["campos"]
        linha = self.gerar_linha(campos_do_header, index)
        return linha

    def gerar_lote_registros_iniciais(self):
        # opcional
        pass

    def gerar_lote_detalhes_segmentos(self):
        for dados_funcionario_mapeado in self.dados_entrada_mapeados["funcionarios"]:
            yield self.gerar_lote_detalhe_segmento_a(dados_funcionario_mapeado)
            yield self.gerar_lote_detalhe_segmento_b(dados_funcionario_mapeado)

    def gerar_lote_detalhe_segmento_a(self, index, dados_pagamento, dados_funcionario):
        campos_do_header = FEBRABAN_V10_7["lote_detalhe_segmento_a"]["campos"]
        linha = self.gerar_linha_detalhamento(
            index, campos_do_header, dados_pagamento, dados_funcionario
        )
        return linha

    def gerar_lote_detalhe_segmento_b(self, index, dados_pagamento, dados_funcionario):
        campos_do_header = FEBRABAN_V10_7["lote_detalhe_segmento_b"]["campos"]
        linha = self.gerar_linha_detalhamento(
            index, campos_do_header, dados_pagamento, dados_funcionario
        )
        return linha

    def gerar_lote_detalhe_segmento_c(self, index, dados_pagamento, dados_funcionario):
        campos_do_header = FEBRABAN_V10_7["lote_detalhe_segmento_c"]["campos"]
        linha = self.gerar_linha_detalhamento(
            index, campos_do_header, dados_pagamento, dados_funcionario
        )
        return linha

    def gerar_lote_registros_finais(self):
        # opcional
        pass

    def gerar_lote_trailer(self, index):
        campos_do_header = FEBRABAN_V10_7["trailer_lote"]["campos"]
        linha = self.gerar_linha(campos_do_header, index)
        return linha

    def gerar_trailer(self):
        campos_do_header = FEBRABAN_V10_7["trailer"]["campos"]
        linha = self.gerar_linha(campos_do_header)
        return linha


if __name__ == "__main__":
    x = {
        "Empresa": {
            "Nome da Empresa": "Vinta",
            "* Tipo de Inscrição da Empresa": "1",
            "* Número de Inscrição da Empresa": "3232312",
            "* Nome do Banco": "banco inter",
            "* Código do Convênio no Banco": "231",
            "* Agência Mantenedora da Conta ": "123",
            "* Dígito Verificador da Agência": "2",
            "* Número da Conta Corrente": "123341",
            "* Dígito Verificador da Conta": "2",
            "* Dígito Verificador da Ag/Conta": "1",
            "Logradouro (Nome da Rua, Av, Pça, Etc)": "asdfasdf",
            "Número (Número do Local)": "23",
            "Complemento (Casa, Apto, Sala, Etc)": "dfasfdasdf",
            "Nome da Cidade": "asfdasf",
            "CEP": "212",
            "Complemento do CEP": "231",
            "Sigla do Estado": "df",
        },
        "Funcionários": [
            {
                "Nome do Favorecido": "Marcos Felipe",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "04077152151",
                "* Código da Câmara Centralizadora": "123",
                "Código do Banco do Favorecido": "123",
                "* Ag. Mantenedora da Cta do Favor.": "123",
                "* Dígito Verificador da Agência": "1",
                "* Número da Conta Corrente": "33333",
                "* Dígito Verificador da Conta": "3",
                "* Dígito Verificador da AG/Conta": "1",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "asdfasdf",
                "Número (Nº do Local)": "23",
                "Complemento (Casa, Apto, Etc)": "asdfasdf",
                "Bairro": "asdffd",
                "Nome da Cidade": "ffffffff",
                "Sigla do Estado": "as",
                "CEP": "23123",
                "Complemento do CEP": "asf",
            }
        ],
        "Pagamentos": [
            {
                "Funcionário": "Marcos Felipe",
                "Nº do Docum. Atribuído p/ Empresa": "33333",
                "* Nº do Docum. Atribuído pelo Banco": "33333",
                "* Tipo da Moeda": "R$",
                "Código ISPB": "1231",
                "Quantidade da Moeda": "123123",
                "Valor do Pagamento": "33333",
                "Data do Pagamento": "12122020",
                "Valor Real da Efetivação do Pagto": "123123",
                "Data do Vencimento (Nominal)": "12122020",
                "Valor do Documento (Nominal)": "123",
                "Valor do Abatimento": "123",
                "Valor do Desconto": "123",
                "Valor da Mora": "123",
                "Valor da Multa": "123",
                "Código/Documento do Favorecido": "123",
                "Valor do IR": "123",
                "Valor do ISS": "333",
                "Valor do IOF": "123",
                "Valor Outras Deduções": "123",
                "Valor Outros Acréscimos": "123",
                "Agência do Favorecido": "123",
                "Dígito Verificador da Agência": "123",
                "Número Conta Corrente": "123",
                "Dígito Verificador da Conta": "123",
                "Dígito Verificador Agência/Conta": "123",
                "Valor do INSS": "123",
                "Número Conta Pagamento Creditada": "123",
            }
        ],
    }

    # x = get_spreadsheet_data()
    pagamentos = x["Pagamentos"]
    funcionarios = x["Funcionários"]

    cnab = GerarArquivoCNAB240_V10_7(x)
    print(cnab.gerar_header())

    for i, _ in enumerate(pagamentos):
        dados_pagamento = pagamentos[i]
        dados_funcionario = funcionarios[i]
        print(cnab.gerar_lote_header(i + 1))
        print(
            cnab.gerar_lote_detalhe_segmento_a(
                i + 1, dados_pagamento, dados_funcionario
            )
        )
        print(
            cnab.gerar_lote_detalhe_segmento_b(
                i + 1, dados_pagamento, dados_funcionario
            )
        )
        print(
            cnab.gerar_lote_detalhe_segmento_c(
                i + 1, dados_pagamento, dados_funcionario
            )
        )
        print(cnab.gerar_lote_trailer(i + 1))

# Header (primeira linha)
# 	[
# 		Lote Header de Lote
# 		Lote Registros iniciais do lote (opcional)
# 		Lote Detalhe Segmento A (Obrigatório - Remessa / Retorno)
# 		Lote Detalhe Segmento B (Obrigatório - Remessa / Retorno)
# 		Lote Detalhe Segmento C (Opcional - Remessa / Retorno)
# 		Lote Registros finais do lote (opcional)
# 		Lote Trailer de Lote
# 	] * X
# Trailer (última linha)

# TODO:
# - Implement file trailer
# - Fix fields that are being generated: 04.3A, 12.3B, 06.3C, 19.3C
# - Double check mapping fields
# - Parse data
