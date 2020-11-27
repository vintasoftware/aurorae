from febraban_v10_7 import FEBRABAN_V10_7, MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7


class Campo:

    def __init__(self, dados_campo):
        self.valor_entrada = dados_campo["valor_entrada"]
        self.valor_default = campo_config["valor_default"]
        self.posicao_inicio = campo_config["posicao_inicio"]
        self.posicao_fim = campo_config["posicao_fim"]
        self.formato = campo_config["formato"]
        self.total_posicoes = self.posicao_fim - self.posicao_inicio + 1

    def __str__(self):
        return self.formatar_campo()

    def formatar_campo(self):
        self.e_valido(raise_exception=True)

        if self.formato == "num":
          campo_formatado = valor.zfill(self.total_posicoes)
        elif self.formato == "alfa"
          campo_formatado = valor.ljust(self.total_posicoes, ' ')

        assert(len(campo_formatado) == self.total_posicoes)

        return campo_formatado

    def e_valido(self):
        if self.formato not in ["num", "alfa"]:
            raise Exception("Formato não permitido")


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
    self.febraban_arquivo_config = FEBRABAN_V10_7

    def __init__(self, dados_entrada_mapeados):
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

    def gerar_header():
        linha = Linha(
            valores_entrada_mapeado=self.dados_entrada_mapeados,
            linha_config=self.febraban_arquivo_config
        )
        return linha

    def gerar_lote_header():
        pass

    def gerar_lote_registros_iniciais():
        # opcional
        pass

    def gerar_lote_detalhes_segmentos():
        for dados_funcionario_mapeado in self.dados_entrada_mapeados["funcionarios"]:
            yield gerar_lote_detalhe_segmento_a(dados_funcionario_mapeado)
            yield gerar_lote_detalhe_segmento_b(dados_funcionario_mapeado)

    def gerar_lote_detalhe_segmento_a():
        pass

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
