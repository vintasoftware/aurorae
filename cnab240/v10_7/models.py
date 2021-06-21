import sys

sys.path.append("/home/sarai/Documents/vinta/vinta-pagamentos/cnab240")

from base import BaseLine, Field


class Field103B(Field):
    """
    Example of `initial_value`: {
        "Chave Pix": "",
        "Número (Nº do Local)": "1",
        "Complemento (Casa, Apto, Etc)": "Casa",
        "Bairro": "Candeias",
        "Nome da Cidade": "Recife",
        "CEP": "88420420",
        "Complemento do CEP": "",
        "Sigla do Estado": "PE"
    }
    """

    composed_fields = [
        # {"name": "Chave Pix", "pos_initial": 68, "pos_end": 127, "data_type": "alfa"},
        {
            "name": "Número (Nº do Local)",
            "pos_initial": 68,
            "pos_end": 72,
            "data_type": "num",
        },
        {
            "name": "Complemento (Casa, Apto, Etc)",
            "pos_initial": 73,
            "pos_end": 87,
            "data_type": "alfa",
        },
        {"name": "Bairro", "pos_initial": 88, "pos_end": 102, "data_type": "alfa"},
        {
            "name": "Nome da Cidade",
            "pos_initial": 103,
            "pos_end": 117,
            "data_type": "alfa",
        },
        {"name": "CEP", "pos_initial": 118, "pos_end": 122, "data_type": "num"},
        {
            "name": "Complemento do CEP",
            "pos_initial": 123,
            "pos_end": 125,
            "data_type": "alfa",
        },
        {
            "name": "Sigla do Estado",
            "pos_initial": 126,
            "pos_end": 127,
            "data_type": "alfa",
        },
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_fields = []
        for custom_column in self.composed_fields:
            custom_field = Field(
                name=custom_column["name"],
                pos_initial=custom_column["pos_initial"],
                pos_end=custom_column["pos_end"],
                data_type=custom_column["data_type"],
                default_value="",
                description="",
                code="",
                required=True,
            )
            self.custom_fields.append(custom_field)

    def validate(self, initial_value=None):
        super().validate(initial_value)
        for custom_field, custom_column in zip(
            self.custom_fields, self.composed_fields
        ):
            custom_field.validate(initial_value[custom_column["name"]])

        return None

    def to_cnab240_representation(self):
        self.formatted_value = ""
        for custom_field in self.custom_fields:
            self.formatted_value = (
                f"{self.formatted_value}{custom_field.to_cnab240_representation()}"
            )
        return self.formatted_value


class Field113B(Field):
    """
    Example of `initial_value`: {
        "Data do Vencimento (Nominal)": "",
        "Valor do Documento (Nominal)": "1",
        "Valor do Abatimento": "Casa",
        "Valor do Desconto": "Candeias",
        "Valor da Mora": "Recife",
        "Valor da Multa": "88420420",
        "Código/Documento do Favorecido": "",
        "Aviso ao Favorecido": "PE"
    }
    """

    composed_fields = [
        # {"name": "Chave Pix", "pos_initial": 128, "pos_end": 226, "data_type": "alfa"},
        {
            "name": "Data do Vencimento (Nominal)",
            "pos_initial": 128,
            "pos_end": 135,
            "data_type": "num",
        },
        {
            "name": "Valor do Documento (Nominal)",
            "pos_initial": 136,
            "pos_end": 150,
            "data_type": "num",
        },
        {
            "name": "Valor do Abatimento",
            "pos_initial": 151,
            "pos_end": 165,
            "data_type": "num",
        },
        {
            "name": "Valor do Desconto",
            "pos_initial": 166,
            "pos_end": 180,
            "data_type": "num",
        },
        {
            "name": "Valor da Mora",
            "pos_initial": 181,
            "pos_end": 195,
            "data_type": "num",
        },
        {
            "name": "Valor da Multa",
            "pos_initial": 196,
            "pos_end": 210,
            "data_type": "num",
        },
        {
            "name": "Código/Documento do Favorecido",
            "pos_initial": 211,
            "pos_end": 225,
            "data_type": "alfa",
        },
        {
            "name": "Aviso ao Favorecido",
            "pos_initial": 226,
            "pos_end": 226,
            "data_type": "num",
        },
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_fields = []
        for custom_column in self.composed_fields:
            custom_field = Field(
                name=custom_column["name"],
                pos_initial=custom_column["pos_initial"],
                pos_end=custom_column["pos_end"],
                data_type=custom_column["data_type"],
                default_value="",
                description="",
                code="",
                required=True,
            )
            self.custom_fields.append(custom_field)

    def validate(self, initial_value=None):
        super().validate(initial_value)
        for custom_field, custom_column in zip(
            self.custom_fields, self.composed_fields
        ):
            custom_field.validate(initial_value[custom_column["name"]])

        return None

    def to_cnab240_representation(self):
        self.formatted_value = ""
        for custom_field in self.custom_fields:
            self.formatted_value = (
                f"{self.formatted_value}{custom_field.to_cnab240_representation()}"
            )

        return self.formatted_value


class HeaderLine(BaseLine):
    """
    All fields must start with "field_"
    """

    field_01_0 = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.0",
    )
    field_02_0 = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value="0000",
        description="G002",
        code="02.0",
    )
    field_03_0 = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="0",
        description="G003",
        code="03.0",
    )
    field_04_0 = Field(
        name="Uso Exclusivo FEBRABAN / CNAB",
        pos_initial=9,
        pos_end=17,
        data_type="alfa",
        default_value="",
        description="G004",
        code="04.0",
    )
    field_05_0 = Field(
        name="Tipo de Inscrição da Empresa",
        pos_initial=18,
        pos_end=18,
        data_type="num",
        default_value=None,
        description="G005",
        code="05.0",
    )
    field_06_0 = Field(
        name="Número de Inscrição da Empresa",
        pos_initial=19,
        pos_end=32,
        data_type="num",
        default_value=None,
        description="G006",
        code="06.0",
    )
    field_07_0 = Field(
        name="Código do Convênio no Banco",
        pos_initial=33,
        pos_end=52,
        data_type="alfa",
        default_value=None,
        description="G007",
        code="07.0",
    )
    field_08_0 = Field(
        name="Agência Mantenedora da Conta",
        pos_initial=53,
        pos_end=57,
        data_type="num",
        default_value=None,
        description="G008",
        code="08.0",
    )
    field_09_0 = Field(
        name="Dígito Verificador da Agência",
        pos_initial=58,
        pos_end=58,
        data_type="alfa",
        default_value=None,
        description="G009",
        code="09.0",
    )
    field_10_0 = Field(
        name="Número da Conta Corrente",
        pos_initial=59,
        pos_end=70,
        data_type="num",
        default_value=None,
        description="G010",
        code="10.0",
    )
    field_11_0 = Field(
        name="Dígito Verificador da Conta",
        pos_initial=71,
        pos_end=71,
        data_type="alfa",
        default_value=None,
        description="G011",
        code="11.0",
    )
    field_12_0 = Field(
        name="Dígito Verificador da Ag/Conta",
        pos_initial=72,
        pos_end=72,
        data_type="alfa",
        default_value=None,
        description="G012",
        code="12.0",
    )
    field_13_0 = Field(
        name="Nome da Empresa",
        pos_initial=73,
        pos_end=102,
        data_type="alfa",
        default_value=None,
        description="G013",
        code="13.0",
    )
    field_14_0 = Field(
        name="Nome do Banco",
        pos_initial=103,
        pos_end=132,
        data_type="alfa",
        default_value=None,
        description="G014",
        code="14.0",
    )
    field_15_0 = Field(
        name="Uso Exclusivo FEBRABAN / CNAB",
        pos_initial=133,
        pos_end=142,
        data_type="alfa",
        default_value="",
        description="G004",
        code="15.0",
    )
    field_16_0 = Field(
        name="Código Remessa / Retorno",
        pos_initial=143,
        pos_end=143,
        data_type="num",
        default_value=None,
        description="G015",
        code="16.0",
    )
    field_17_0 = Field(
        name="Data de Geração do Arquivo",
        pos_initial=144,
        pos_end=151,
        data_type="num",
        default_value=None,
        description="G016",
        code="17.0",
    )
    field_18_0 = Field(
        name="Hora de Geração do Arquivo",
        pos_initial=152,
        pos_end=157,
        data_type="num",
        default_value=None,
        description="G017",
        code="18.0",
    )
    field_19_0 = Field(
        name="Número Seqüencial do Arquivo",
        pos_initial=158,
        pos_end=163,
        data_type="num",
        default_value=None,
        description="G018",
        code="19.0",
    )
    field_20_0 = Field(
        name="Número da Versão do Layout do Arquivo",
        pos_initial=164,
        pos_end=166,
        data_type="num",
        default_value="103",
        description="G019",
        code="20.0",
    )
    field_21_0 = Field(
        name="Densidade de Gravação do Arquivo",
        pos_initial=167,
        pos_end=171,
        data_type="num",
        default_value=None,
        description="G020",
        code="21.0",
    )
    field_22_0 = Field(
        name="Para Uso Reservado do Banco",
        pos_initial=172,
        pos_end=191,
        data_type="alfa",
        default_value=None,
        description="G021",
        code="22.0",
    )
    field_23_0 = Field(
        name="Para Uso Reservado da Empresa",
        pos_initial=192,
        pos_end=211,
        data_type="alfa",
        default_value=None,
        description="G022",
        code="23.0",
    )
    field_24_0 = Field(
        name="Uso Exclusivo FEBRABAN / CNAB",
        pos_initial=212,
        pos_end=240,
        data_type="alfa",
        default_value="",
        description="G004",
        code="24.0",
    )


class LoteHeader(BaseLine):
    field_01_1 = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.1",
    )
    field_02_1 = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value=None,
        description="G002",
        code="02.1",
    )
    field_03_1 = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="1",
        description="G003",
        code="03.1",
    )
    field_04_1 = Field(
        name="Tipo da Operação",
        pos_initial=9,
        pos_end=9,
        data_type="alfa",
        default_value="C",
        description="G028",
        code="04.1",
    )
    field_05_1 = Field(
        name="Tipo do Serviço",
        pos_initial=10,
        pos_end=11,
        data_type="num",
        default_value=None,
        description="G025",
        code="05.1",
    )
    field_06_1 = Field(
        name="Forma de Lançamento",
        pos_initial=12,
        pos_end=13,
        data_type="num",
        default_value=None,
        description="G029",
        code="06.1",
    )
    field_07_1 = Field(
        name="Nº da Versão do Layout do Lote",
        pos_initial=14,
        pos_end=16,
        data_type="num",
        default_value="046",
        description="G030",
        code="07.1",
    )
    field_08_1 = Field(
        name="Uso Exclusivo da FEBRABAN/CNAB",
        pos_initial=17,
        pos_end=17,
        data_type="alfa",
        default_value="",
        description="G004",
        code="08.1",
    )
    field_09_1 = Field(
        name="Tipo de Inscrição da Empresa",
        pos_initial=18,
        pos_end=18,
        data_type="num",
        default_value=None,
        description="G005",
        code="09.1",
    )
    field_10_1 = Field(
        name="Número de Inscrição da Empresa",
        pos_initial=19,
        pos_end=32,
        data_type="num",
        default_value=None,
        description="G006",
        code="10.1",
    )
    field_11_1 = Field(
        name="Código do Convênio no Banco",
        pos_initial=33,
        pos_end=52,
        data_type="alfa",
        default_value=None,
        description="G007",
        code="11.1",
    )
    field_12_1 = Field(
        name="Agência Mantenedora da Conta",
        pos_initial=53,
        pos_end=57,
        data_type="num",
        default_value=None,
        description="G008",
        code="12.1",
    )
    field_13_1 = Field(
        name="Dígito Verificador da Agência",
        pos_initial=58,
        pos_end=58,
        data_type="alfa",
        default_value=None,
        description="G009",
        code="13.1",
    )
    field_14_1 = Field(
        name="Número da Conta Corrente",
        pos_initial=59,
        pos_end=70,
        data_type="num",
        default_value=None,
        description="G010",
        code="14.1",
    )
    field_15_1 = Field(
        name="Dígito Verificador da Conta",
        pos_initial=71,
        pos_end=71,
        data_type="alfa",
        default_value="",
        description="G011",
        code="15.1",
    )
    field_16_1 = Field(
        name="Dígito Verificador da Ag/Conta",
        pos_initial=72,
        pos_end=72,
        data_type="alfa",
        default_value=None,
        description="G012",
        code="16.1",
    )
    field_17_1 = Field(
        name="Nome da Empresa",
        pos_initial=73,
        pos_end=102,
        data_type="alfa",
        default_value=None,
        description="G013",
        code="17.1",
    )
    field_18_1 = Field(
        name="Mensagem",
        pos_initial=103,
        pos_end=142,
        data_type="alfa",
        default_value=None,
        description="G031",
        code="18.1",
    )
    field_19_1 = Field(
        name="Nome da Rua, Av, Pça, Etc",
        pos_initial=143,
        pos_end=172,
        data_type="alfa",
        default_value=None,
        description="G032",
        code="19.1",
    )
    field_20_1 = Field(
        name="Número do Local",
        pos_initial=173,
        pos_end=177,
        data_type="num",
        default_value="103",
        description="G032",
        code="20.1",
    )
    field_21_1 = Field(
        name="Casa, Apto, Sala, Etc",
        pos_initial=178,
        pos_end=192,
        data_type="alfa",
        default_value=None,
        description="G032",
        code="21.1",
    )
    field_22_1 = Field(
        name="Nome da Cidade",
        pos_initial=193,
        pos_end=212,
        data_type="alfa",
        default_value=None,
        description="G033",
        code="22.1",
    )
    field_23_1 = Field(
        name="CEP",
        pos_initial=213,
        pos_end=217,
        data_type="num",
        default_value=None,
        description="G034",
        code="23.1",
    )
    field_24_1 = Field(
        name="Complemento do CEP",
        pos_initial=218,
        pos_end=220,
        data_type="alfa",
        default_value=None,
        description="G035",
        code="24.1",
    )
    field_25_1 = Field(
        name="Sigla do Estado",
        pos_initial=221,
        pos_end=222,
        data_type="alfa",
        default_value=None,
        description="G036",
        code="25.1",
    )
    field_26_1 = Field(
        name="Indicativo da Forma de Pagamento do Serviço",
        pos_initial=223,
        pos_end=224,
        data_type="num",
        default_value=None,
        description="P014",
        code="26.1",
    )
    field_27_1 = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=225,
        pos_end=230,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="27.1",
    )
    field_28_1 = Field(
        name="Códigos das Ocorrências p/ Retorno",
        pos_initial=231,
        pos_end=240,
        data_type="alfa",
        default_value=None,
        description="G059",
        code="28.1",
    )


class LoteDetalheSegmentoA(BaseLine):
    field_01_3A = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.3A",
    )
    field_02_3A = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value=None,
        description="G002",
        code="02.3A",
    )
    field_03_3A = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="3",
        description="G003",
        code="03.3A",
    )
    field_04_3A = Field(
        name="Nº Seqüencial do Registro no Lote",
        pos_initial=9,
        pos_end=13,
        data_type="num",
        default_value=None,
        description="G038",
        code="04.3A",
    )
    field_05_3A = Field(
        name="Código de Segmento do Reg. Detalhe",
        pos_initial=14,
        pos_end=14,
        data_type="alfa",
        default_value="A",
        description="G039",
        code="05.3A",
    )
    field_06_3A = Field(
        name="Tipo de Movimento",
        pos_initial=15,
        pos_end=15,
        data_type="num",
        default_value=None,
        description="G060",
        code="06.3A",
    )
    field_07_3A = Field(
        name="Código da Instrução p/ Movimento",
        pos_initial=16,
        pos_end=17,
        data_type="num",
        default_value=None,
        description="G061",
        code="07.3A",
    )
    field_08_3A = Field(
        name="Código da Câmara Centralizadora",
        pos_initial=18,
        pos_end=20,
        data_type="num",
        default_value=None,
        description="P001: Código adotado pela FEBRABAN, para identificar qual Câmara de Centralizadora será "
        "responsável pelo processamento dos pagamentos. ",
        code="08.3A",
    )
    field_09_3A = Field(
        name="Código do Banco do Favorecido",
        pos_initial=21,
        pos_end=23,
        data_type="num",
        default_value=None,
        description="P002",
        code="09.3A",
    )
    field_10_3A = Field(
        name="Ag. Mantenedora da Cta do Favor.",
        pos_initial=24,
        pos_end=28,
        data_type="num",
        default_value=None,
        description="G008",
        code="10.3A",
    )
    field_11_3A = Field(
        name="Dígito Verificador da Agência",
        pos_initial=29,
        pos_end=29,
        data_type="alfa",
        default_value=None,
        description="G009",
        code="11.3A",
    )
    field_12_3A = Field(
        name="Número da Conta Corrente",
        pos_initial=30,
        pos_end=41,
        data_type="num",
        default_value=None,
        description="G010",
        code="12.3A",
    )
    field_13_3A = Field(
        name="Dígito Verificador da Conta",
        pos_initial=42,
        pos_end=42,
        data_type="alfa",
        default_value=None,
        description="G011",
        code="13.3A",
    )
    field_14_3A = Field(
        name="Dígito Verificador da AG/Conta",
        pos_initial=43,
        pos_end=43,
        data_type="alfa",
        default_value=None,
        description="G012",
        code="14.3A",
    )
    field_15_3A = Field(
        name="Nome do Favorecido",
        pos_initial=44,
        pos_end=73,
        data_type="alfa",
        default_value=None,
        description="G013",
        code="15.3A",
    )
    field_16_3A = Field(
        name="Nº do Docum. Atribuído p/ Empresa",
        pos_initial=74,
        pos_end=93,
        data_type="alfa",
        default_value=None,
        description="G064",
        code="16.3A",
    )
    field_17_3A = Field(
        name="Data do Pagamento",
        pos_initial=94,
        pos_end=101,
        data_type="num",
        default_value=None,
        description="P009",
        code="17.3A",
    )
    field_18_3A = Field(
        name="Tipo da Moeda",
        pos_initial=102,
        pos_end=104,
        data_type="num",
        default_value=None,
        description="G040",
        code="18.3A",
    )
    field_19_3A = Field(
        name="Quantidade da Moeda",
        pos_initial=105,
        pos_end=119,
        data_type="num",
        default_value=None,
        description="G041",
        code="19.3A",
    )
    field_20_3A = Field(
        name="Valor do Pagamento",
        pos_initial=120,
        pos_end=134,
        data_type="num",
        default_value=None,
        description=None,
        code="P010",
    )
    field_21_3A = Field(
        name="Nº do Docum. Atribuído pelo Banco",
        pos_initial=135,
        pos_end=154,
        data_type="alfa",
        default_value=None,
        description="G043",
        code="21.3A",
    )
    field_22_3A = Field(
        name="Data Real da Efetivação Pagto",
        pos_initial=155,
        pos_end=162,
        data_type="num",
        default_value=None,
        description="P003",
        code="22.3A",
    )
    field_23_3A = Field(
        name="Valor Real da Efetivação do Pagto",
        pos_initial=163,
        pos_end=177,
        data_type="num",
        default_value=None,
        description="P004: A ser preenchido quando arquivo for de retorno (Código=2 no Header de Arquivo) e "
        "referir-se a uma confirmação de lançamento.",
        code="23.3A",
    )
    field_24_3A = Field(
        name="Outras Informações",
        pos_initial=178,
        pos_end=217,
        data_type="alfa",
        default_value=None,
        description="G031",
        code="24.3A",
    )
    field_25_3A = Field(
        name="Compl. Tipo Serviço",
        pos_initial=218,
        pos_end=219,
        data_type="alfa",
        default_value=None,
        description="P005",
        code="25.3A",
    )
    field_26_3A = Field(
        name="Codigo finalidade da TED",
        pos_initial=220,
        pos_end=224,
        data_type="alfa",
        default_value=None,
        description="P011",
        code="26.3A",
    )
    field_27_3A = Field(
        name="Complemento de finalidade pagto.",
        pos_initial=225,
        pos_end=226,
        data_type="alfa",
        default_value=None,
        description="P013",
        code="27.3A",
    )
    field_28_3A = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=227,
        pos_end=229,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="28.3A",
    )
    field_29_3A = Field(
        name="Aviso ao Favorecido",
        pos_initial=230,
        pos_end=230,
        data_type="num",
        default_value=None,
        description="P006",
        code="29.3A",
    )
    field_30_3A = Field(
        name="Códigos das Ocorrências para Retorno",
        pos_initial=231,
        pos_end=240,
        data_type="alfa",
        default_value=None,
        description="G059",
        code="30.3A",
    )


class LoteDetalheSegmentoB(BaseLine):
    field_01_3B = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.3B",
    )
    field_02_3B = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value=None,
        description="G002",
        code="02.3B",
    )
    field_03_3B = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="3",
        description="G003",
        code="03.3B",
    )
    field_04_3B = Field(
        name="Nº Seqüencial do Registro no Lote",
        pos_initial=9,
        pos_end=13,
        data_type="num",
        default_value="3",
        description="G038",
        code="04.3B",
    )
    field_05_3B = Field(
        name="Código de Segmento do Reg. Detalhe",
        pos_initial=14,
        pos_end=14,
        data_type="alfa",
        default_value="B",
        description="G039",
        code="05.3B",
    )
    field_06_3B = Field(
        name="* Forma de Iniciação",
        pos_initial=15,
        pos_end=17,
        data_type="alfa",
        default_value=None,
        description="G100",
        code="06.3B",
    )
    field_07_3B = Field(
        name="Tipo de Inscrição do Favorecido",
        pos_initial=18,
        pos_end=18,
        data_type="num",
        default_value=None,
        description="G005",
        code="07.3B",
    )
    field_08_3B = Field(
        name="Nº de Inscrição do Favorecido",
        pos_initial=19,
        pos_end=32,
        data_type="num",
        default_value=None,
        description="G006",
        code="08.3B",
    )
    field_09_3B = Field(
        name="Informação 10",
        pos_initial=33,
        pos_end=67,
        data_type="alfa",
        default_value=None,
        description="G101",
        code="09.3B",
    )
    field_10_3B = Field103B(
        name="Informação 11",
        pos_initial=68,
        pos_end=127,
        data_type="alfa",
        default_value=None,
        description="G101",
        code="10.3B",
    )
    field_11_3B = Field113B(
        name="Informação 12",
        pos_initial=128,
        pos_end=226,
        data_type="alfa",
        default_value=None,
        description="G101",
        code="11.3B",
    )
    field_12_3B = Field(
        name="Uso Exclusivo para o SIAPE",
        pos_initial=227,
        pos_end=232,
        data_type="num",
        default_value=None,
        description="P012",
        code="12.3B",
    )
    field_13_3B = Field(
        name="Código ISPB",
        pos_initial=233,
        pos_end=240,
        data_type="num",
        default_value=None,
        description="P015",
        code="13.3B",
    )


class LoteDetalheSegmentoC(BaseLine):
    field_01_3C = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.3C",
    )
    field_02_3C = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value=None,
        description="G002",
        code="02.3C",
    )
    field_03_3C = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="3",
        description="G003",
        code="03.3C",
    )
    field_04_3C = Field(
        name="Nº Seqüencial do Registro no Lote",
        pos_initial=9,
        pos_end=13,
        data_type="num",
        default_value="3",
        description="G038",
        code="04.3C",
    )
    field_05_3C = Field(
        name="Código de Segmento do Reg. Detalhe",
        pos_initial=14,
        pos_end=14,
        data_type="alfa",
        default_value="C",
        description="G039",
        code="05.3C",
    )
    field_06_3C = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=15,
        pos_end=17,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="06.3C",
    )
    field_07_3C = Field(
        name="Valor do IR",
        pos_initial=18,
        pos_end=32,
        data_type="num",
        default_value=None,
        description="G050",
        code="07.3C",
    )
    field_08_3C = Field(
        name="Valor do ISS",
        pos_initial=33,
        pos_end=47,
        data_type="num",
        default_value=None,
        description="G051",
        code="08.3C",
    )
    field_09_3C = Field(
        name="Valor do IOF",
        pos_initial=48,
        pos_end=62,
        data_type="num",
        default_value=None,
        description="G052",
        code="09.3C",
    )
    field_10_3C = Field(
        name="Valor Outras Deduções",
        pos_initial=63,
        pos_end=77,
        data_type="num",
        default_value=None,
        description="G053",
        code="10.3C",
    )
    field_11_3C = Field(
        name="Valor Outras Acréscimos",
        pos_initial=78,
        pos_end=92,
        data_type="num",
        default_value=None,
        description="G054",
        code="11.3C",
    )
    field_12_3C = Field(
        name="Agência do Favorecido",
        pos_initial=93,
        pos_end=97,
        data_type="num",
        default_value=None,
        description="G008",
        code="12.3C",
    )
    field_13_3C = Field(
        name="Dígito Verificador da Agência",
        pos_initial=98,
        pos_end=98,
        data_type="alfa",
        default_value=None,
        description="G009",
        code="13.3C",
    )
    field_14_3C = Field(
        name="Número Conta Corrente",
        pos_initial=99,
        pos_end=110,
        data_type="num",
        default_value=None,
        description="G010",
        code="14.3C",
    )
    field_15_3C = Field(
        name="Dígito Verificador da Conta",
        pos_initial=111,
        pos_end=111,
        data_type="alfa",
        default_value=None,
        description="G011",
        code="15.3C",
    )
    field_16_3C = Field(
        name="Dígito Verificador Agência/Conta",
        pos_initial=112,
        pos_end=112,
        data_type="alfa",
        default_value=None,
        description="G012",
        code="16.3C",
    )
    field_17_3C = Field(
        name="Valor do INSS",
        pos_initial=113,
        pos_end=127,
        data_type="num",
        default_value=None,
        description="G055",
        code="17.3C",
    )
    field_18_3C = Field(
        name="Número Conta Pagamento Creditada",
        pos_initial=128,
        pos_end=147,
        data_type="num",
        default_value=None,
        description="P016",
        code="18.3C",
    )
    field_19_3C = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=148,
        pos_end=240,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="18.3C",
    )


class LoteTrailer(BaseLine):
    field_01_5 = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.5",
    )
    field_02_5 = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value=None,
        description="G002",
        code="02.5",
    )
    field_03_5 = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="5",
        description="G003",
        code="03.5",
    )
    field_04_5 = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=9,
        pos_end=17,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="04.5",
    )
    field_05_5 = Field(
        name="Quantidade de Registros do Lote",
        pos_initial=18,
        pos_end=23,
        data_type="num",
        default_value=None,
        description="G057",
        code="05.5",
    )
    field_06_5 = Field(
        name="Somatória dos Valores",
        pos_initial=24,
        pos_end=41,
        data_type="num",
        default_value=None,
        description="P007",
        code="06.5",
    )
    field_07_5 = Field(
        name="Somatória de Quantidade de Moedas",
        pos_initial=42,
        pos_end=59,
        data_type="num",
        default_value=None,
        description="G058",
        code="07.5",
    )
    field_08_5 = Field(
        name="Número Aviso de Débito ",
        pos_initial=60,
        pos_end=65,
        data_type="alfa",
        default_value=None,
        description="G066",
        code="08.5",
    )
    field_09_5 = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=66,
        pos_end=230,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="09.5",
    )
    field_10_5 = Field(
        name="Códigos das Ocorrências para Retorno",
        pos_initial=231,
        pos_end=240,
        data_type="alfa",
        default_value=None,
        description="G059",
        code="10.5",
    )


class TrailerLine(BaseLine):
    """
    All fields must start with "field_"
    """

    field_01_9 = Field(
        name="Código do Banco na Compensação",
        pos_initial=1,
        pos_end=3,
        data_type="num",
        default_value=None,
        description="G001",
        code="01.9",
    )
    field_02_9 = Field(
        name="Lote de Serviço",
        pos_initial=4,
        pos_end=7,
        data_type="num",
        default_value="9999",
        description="G002",
        code="02.9",
    )
    field_03_9 = Field(
        name="Tipo de Registro",
        pos_initial=8,
        pos_end=8,
        data_type="num",
        default_value="9",
        description="G003",
        code="03.9",
    )
    field_04_9 = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=9,
        pos_end=17,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="04.9",
    )
    field_05_9 = Field(
        name="Quantidade de Lotes do Arquivo",
        pos_initial=18,
        pos_end=23,
        data_type="num",
        default_value=None,
        description="G049",
        code="05.9",
    )
    field_06_9 = Field(
        name="Quantidade de Registros do Arquivo",
        pos_initial=24,
        pos_end=29,
        data_type="num",
        default_value=None,
        description="G056",
        code="06.9",
    )
    field_07_9 = Field(
        name="Qtde de Contas p/ Conc. (Lotes)",
        pos_initial=30,
        pos_end=35,
        data_type="num",
        default_value=None,
        description="G037",
        code="07.9",
    )
    field_08_9 = Field(
        name="Uso Exclusivo FEBRABAN/CNAB",
        pos_initial=36,
        pos_end=240,
        data_type="alfa",
        default_value=None,
        description="G004",
        code="08.9",
    )
