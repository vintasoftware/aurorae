from febraban_v10_7 import FEBRABAN_V10_7, MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7

dados_arquivo = {
    "[Empresa] Nome da Empresa": "Vinta",
    "[Funcionarios] Nome funcionario": "Test",
    "[Pagamentos] Valor do Pagamento": "10000",
}


class WriterCNAB_v10_7:

    """
        qtd de lotes (?)
    """
    def __init__(self, data):
        self.data = data

    def montar_arquivo(self):
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

        info_funcionarios = self.data["info_funcionarios"]
        info_empresa = self.data["info_empresa"]

        # HEADER TXT
        campos = FEBRABAN_V10_7["header"]["campos"]
        montar_linha_header(campos, info_empresa)

        # LOTES
        campos = FEBRABAN_V10_7["header_lote"]["campos"]
        montar_linha_header_lote(campos, info_empresa)

        for info_usuario in info_funcionarios:
            campos = FEBRABAN_V10_7["lote_detalhe_segmento_a"]["campos"]
            montar_linha_registro_detalhe(campos, info_usuario)

            campos = FEBRABAN_V10_7["lote_detalhe_segmento_b"]["campos"]
            montar_linha_registro_detalhe(campos, info_usuario)

            campos = FEBRABAN_V10_7["lote_detalhe_segmento_c"]["campos"]
            montar_linha_registro_detalhe(campos, info_usuario)

        campos = FEBRABAN_V10_7["trailer_lote"]["campos"]
        montar_linha_trailer_lote(campos)

        # TRAILER TXT
        campos = FEBRABAN_V10_7["trailer"]["campos"]
        montar_linha_trailer(campos)
    
    def montar_linha_header(self, campos_febraban, info_empresa):
        linha = ""

        nome_campo_ordernados_lista = sorted(list(campos.keys()))
        for nome_campo in nome_campo_ordernados_lista:            
            entrada_campo = MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7[nome_campo]
            nome_campo_valor = info_empresa[pagamento_campo]
            nome_campo_valor_formato = formatar_campo(nome_campo_valor, campos[nome_campo])

            linha += nome_campo_valor_formato

    def montar_linha_header_lote(self):
      pass

    def montar_linha_registro_detalhe(self, campos, info_usuario):
        pass

    def montar_linha(self, campos_febraban, campos_entrada):
        linha = ""

        nome_campos_febraban_ordenados = sorted(list(campos_febraban.keys()))

        for nome_campo_febraban in nome_campos_febraban_ordenados:            
            nome_campo_entrada = MAPEAMENTO_CAMPOS_ENTRADA_FEBRABAN_V10_7[nome_campo_febraban]

            valor_entrada = campos_entrada[nome_campo_entrada]
            campo_febraban_config = campos_febraban[nome_campo_febraban]

            campo_formatado = formatar_campo(valor_entrada, campo_febraban_config)

            linha += campo_formatado

        return linha

    def formatar_campo(valor, campo_config):
        posicao_inicio = campos[nome_campo]["posicao_inicio"]
        posicao_fim = campos[nome_campo]["posicao_fim"]
        formato = campos[nome_campo]["formato"]
        
        total_posicoes = posicao_fim - posicao_inicio + 1

        if formato == "num":
          campo_formatado = valor.zfill(total_posicoes)
        elif formato == "alfa"
          campo_formatado = valor.ljust(total_posicoes, ' ')
        else:
          raise Exception("Formato não permitido")
        
        assert(len(campo_formatado == total_posicoes))

        return campo_formatado
