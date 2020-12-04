#!/usr/bin/python
# -*- coding: utf-8 -*-

from febraban_v10_7 import FEBRABAN_V10_7, MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7


def get_codigo_remessa_retorno(chave):
    if chave != "16.0":
        raise Exception("Wrong key")
    return '1'

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
    return '30'  # Pagamento Salários


def get_forma_de_lancamento():
    return '01'  # Crédito em Conta Corrente/Salário


def get_indicativo_da_forma_de_pagamento_do_servico():
    return '01'  # Débito em Conta Corrente


def get_tipo_de_movimento():
    return '0'  # Indica INCLUSÃO


def get_codigo_instrucao_movimento():
    return '00'  # Inclusão de Registro Detalhe Liberado


def get_complemento_tipo_servico():
    return '06'  # Pagamento de Salários


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


class Campo:

    def __init__(self, valor, campo_config):
        self.valor_default = campo_config.get("valor_default", None)
        self.valor_entrada = self.valor_default or valor
        self.valor_entrada = str(self.valor_entrada)
        self.posicao_inicio = campo_config["posicao_inicio"]
        self.posicao_fim = campo_config["posicao_fim"]
        self.formato = campo_config["formato"]
        self.nome = campo_config["nome"]
        self.total_posicoes = self.posicao_fim - self.posicao_inicio + 1

    def __str__(self):
        return self.formatar_campo()

    def formatar_campo(self):
        self.e_valido()

        if self.formato == "num":
          campo_formatado = self.valor_entrada.zfill(self.total_posicoes)
        elif self.formato == "alfa":
          campo_formatado = self.valor_entrada.ljust(self.total_posicoes, ' ')

        assert (len(campo_formatado) == self.total_posicoes), f"{self.nome} = {len(campo_formatado)} != {self.total_posicoes})"

        return campo_formatado

    def e_valido(self):
        if self.formato not in ["num", "alfa"]:
            raise Exception(f"Formato não permitido: {self.nome}")


class Linha:
    total_posicoes = 240
    campos = []

    def __init__(self, valores_entrada_mapeado, linha_config):
        """
        Ex. valores_entrada_mapeado:
            {
                "01.0": 123,
                "02.0": "testing"
            }
        """
        self.valores_entrada_mapeado = valores_entrada_mapeado
        self.linha_config = linha_config

    def __str__(self):
        return self.formatar_linha()

    def formatar_linha():
        self.gerar_campos()

        linha = ""
        for campo in self.campos:
            linha =+ str(campo)
        else:
            linha =+ "\n"

        assert(len(linha) == self.total_posicoes + 1)

        return linha

    def gerar_campos():
        campos_febraban = self.linha_config["campos"]

        for campo_id, campo_config in campos_febraban.items():
            campo = Campo(
                valor=self.valores_entrada_mapeado[campo_id],
                campo_config=campo_config
            )
            self.campos.append(campo)

        self.campos.sort(key=lambda campo: campo.posicao_inicio)

        return None


class GerarArquivoCNAB240_V10_7:
    LOTES_DE_SERVICO_CAMPOS = ["02.1", "02.9", "02.5", "02.3C", "02.3B", "02.3A", "02.1", "02.0"]

    def __init__(self, dados_entrada_mapeados):
        self.febraban_arquivo_config = FEBRABAN_V10_7
        self.dados_entrada_mapeados = dados_entrada_mapeados

    def gerar_arquivo():
        arquivo = open("cnab240.txt", "w")

        arquivo.write(self.gerar_header())
        arquivo.write(self.gerar_lote_header())
        for lote_detalhe_segmento in self.gerar_lote_detalhes_segmentos():
            arquivo.write(lote_detalhe_segmento)
        arquivo.write(self.gerar_lote_trailer())
        arquivo.write(self.gerar_trailer())

        arquivo.close()
        return None

    def gerar_header(self, index):
        campos_do_header = FEBRABAN_V10_7["header"]["campos"]
        linha = self.gerar_linha(campos_do_header)
        return linha

    def gerar_linha(self, campos_do_segmento):
        fields = list(campos_do_segmento.keys())
        fields.sort()

        line = ""
        for key in fields:
            field_config = campos_do_segmento[key]
            real_data_location = MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7[key]

            if real_data_location.get("tipo", None):
                """
                    Significa que o campo tem um correspondente na planilha de entrada
                """
                planilha = real_data_location["tipo"]
                name = real_data_location["field_na_planilha_de_entrada"]
                valor = self.dados_entrada_mapeados[planilha][name]
                campo = Campo(valor, campo_config=field_config)
                line += str(campo)
            else:
                """
                    Significa que o campo NÃO tem um correspondente na planilha de entrada
                    e precisa ser gerado
                """
                has_default_value = field_config["default"]
                if has_default_value:
                    has_default_value = " " if has_default_value == "Brancos" else has_default_value
                    campo = Campo(has_default_value, campo_config=field_config)
                    line += str(campo)
                    continue

                """Não tem default e precisa ser gerado"""
                if key in self.LOTES_DE_SERVICO_CAMPOS:
                    valor = index
                    campo = Campo(valor, campo_config=field_config)
                    line += str(campo)
                    continue

                if key == "16.0":
                    valor = get_codigo_remessa_retorno(key)

                if key == "05.1":
                    valor = get_tipo_de_servico()

                if key == "06.1":
                    valor = get_forma_de_lancamento()

                if key == "26.1":
                    valor = get_indicativo_da_forma_de_pagamento_do_servico()

                campo = Campo(valor, campo_config=field_config)
                line += str(campo)
                continue
        return line

    def gerar_linha_detalhamento(self, index, campos_do_segmento, dados_pagamento, dados_funcionario):
        fields = list(campos_do_segmento.keys())
        fields.sort()

        line = ""
        for key in fields:
            field_config = campos_do_segmento[key]
            real_data_location = MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7[key]

            if real_data_location.get("tipo", None):
                """
                    Significa que o campo tem um correspondente na planilha de entrada
                """
                planilha = real_data_location["tipo"]
                name = real_data_location["field_na_planilha_de_entrada"]
                valor = self.dados_entrada_mapeados[planilha][name]
                campo = Campo(valor, campo_config=field_config)
                line += str(campo)
            else:

                if key in self.LOTES_DE_SERVICO_CAMPOS:
                    valor = index
                    campo = Campo(valor, campo_config=field_config)
                    line += str(campo)
                    continue

    def gerar_lote_header(self):
        campos_do_header = FEBRABAN_V10_7["header_lote"]["campos"]
        linha = self.gerar_linha(campos_do_header)
        return linha

    def gerar_lote_registros_iniciais():
        # opcional
        pass

    def gerar_lote_detalhes_segmentos():
        for dados_funcionario_mapeado in self.dados_entrada_mapeados["funcionarios"]:
            yield gerar_lote_detalhe_segmento_a(dados_funcionario_mapeado)
            yield gerar_lote_detalhe_segmento_b(dados_funcionario_mapeado)

    def gerar_lote_detalhe_segmento_a(self, index, dados_pagamento, dados_funcionario):
        campos_do_header = FEBRABAN_V10_7["lote_detalhe_segmento_a"]["campos"]
        linha = gerar_linha_detalhamento(index, campos_do_header, dados_funcionario, dados_pagamento)
        return linha

    def gerar_lote_detalhe_segmento_b():
        pass

    def gerar_lote_detalhe_segmento_c():
        # opcional
        pass

    def gerar_lote_registros_finais():
        # opcional
        pass

    def gerar_lote_trailer():
        pass

    def gerar_trailer():
        pass





if __name__ == "__main__":
    x = {
        "Empresa": {'Nome da Empresa': 'Vinta', '* Tipo de Inscrição da Empresa': '1', '* Número de Inscrição da Empresa': '3232312', '* Código do Convênio no Banco': '231', '* Agência Mantenedora da Conta ': '123', '* Dígito Verificador da Agência': '2', '* Número da Conta Corrente': '123341', '* Dígito Verificador da Conta': '2', '* Dígito Verificador da Ag/Conta': '1', 'Logradouro (Nome da Rua, Av, Pça, Etc)': 'asdfasdf', 'Número (Número do Local)': '23', 'Complemento (Casa, Apto, Sala, Etc)': 'dfasfdasdf', 'Nome da Cidade': 'asfdasf', 'CEP': '212', 'Complemento do CEP': '231', 'Sigla do Estado': 'df', "Nome do Banco": "banco inter"}
        "Funcionários": []
        "Pagamentos": []
    }
    cnab = GerarArquivoCNAB240_V10_7(x)
    print(cnab.gerar_header())
    for i, _ in enumerate(pagamentos):
        dados_pagamento = pagamentos[i]
        dados_funcionario = funcionarios[i]

        print(cnab.gerar_lote_header(i + 1))
        print(cnab.gerar_lote_detalhe_segmento_a(i + 1, dados_pagamento, dados_funcionario))