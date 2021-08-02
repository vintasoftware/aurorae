# pylint: disable=unsubscriptable-object
from typing import Optional

from pydantic import Field as FieldSchema
from pydantic.main import BaseModel

from cnab.cnab240.base import Line
from cnab.cnab240.v10_7 import lambdas, types


class CNABHeader(Line):
    field_01_0: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação", code="G001"
    )
    field_02_0: types.ServiceBatch = FieldSchema(
        default=types.ServiceBatchEnum.file_header,
        description="Lote de Serviço",
        code="G002",
    )
    field_03_0: types.EntryType = FieldSchema(
        default=types.EntryTypeEnum.file_header,
        description="Tipo de Registro",
        code="G003",
    )
    field_04_0: types.FEBRABAN9 = FieldSchema(
        default="", description="Uso Exclusivo FEBRABAN / CNAB", code="G004"
    )
    field_05_0: types.CompanyRegistrationType = FieldSchema(
        description="Tipo de Inscrição da Empresa", code="G005"
    )
    field_06_0: types.CompanyRegistrationNumber = FieldSchema(
        description="Número de Inscrição da Empresa", code="G006"
    )
    field_07_0: types.BankConventionCode = FieldSchema(
        description="Código do Convênio no Banco", code="G007"
    )
    field_08_0: types.BankAgencyNumber = FieldSchema(
        description="Agência Mantenedora da Conta", code="G008"
    )
    field_09_0: types.BankAgencyDigitCheck = FieldSchema(
        description="Dígito Verificador da Agência", code="G009"
    )
    field_10_0: types.BankAccountNumber = FieldSchema(
        description="Número da Conta Corrente", code="G010"
    )
    field_11_0: types.BankAccountDigitCheck = FieldSchema(
        description="Dígito Verificador da Conta", code="G011"
    )
    field_12_0: types.BankAgencyAccountDigitCheck = FieldSchema(
        description="Dígito Verificador da Ag/Conta", code="G012"
    )
    field_13_0: types.CompanyName = FieldSchema(
        description="Nome da Empresa", code="G013"
    )
    field_14_0: types.BankName = FieldSchema(description="Nome do Banco", code="G014")
    field_15_0: types.FEBRABAN10 = FieldSchema(
        default="", description="Uso Exclusivo FEBRABAN / CNAB", code="G004"
    )
    field_16_0: types.RemmitanceReturnCode = FieldSchema(
        description="Código Remessa / Retorno",
        default_factory=lambdas.get_field_G015,
        code="G015",
    )
    field_17_0: types.CNABDate = FieldSchema(
        description="Data de Geração do Arquivo",
        default_factory=lambdas.get_field_G016,
        code="G016",
    )
    field_18_0: types.CNABTime = FieldSchema(
        description="Hora de Geração do Arquivo",
        default_factory=lambdas.get_field_G017,
        code="G017",
    )
    field_19_0: types.FileSequentialNumber = FieldSchema(
        description="Número Seqüencial do Arquivo",
        code="G018",
        default_factory=lambdas.get_field_G018,
    )
    field_20_0: types.FileLayoutVersionNumber = FieldSchema(
        description="Número da Versão do Layout do Arquivo",
        code="G019",
        default_factory=lambdas.get_field_G019,
    )
    field_21_0: types.FileRecordDensity = FieldSchema(
        description="Densidade de Gravação do Arquivo",
        code="G020",
        default_factory=lambdas.get_field_G020,
    )
    field_22_0: types.BankReservedField = FieldSchema(
        default="", description="Para Uso Reservado do Banco", code="G021"
    )
    field_23_0: types.CompanyReservedField = FieldSchema(
        default="", description="Para Uso Reservado da Empresa", code="G022"
    )
    field_24_0: types.FEBRABAN29 = FieldSchema(
        default="", description="Uso Exclusivo FEBRABAN / CNAB", code="G004"
    )

    class Config:
        use_enum_values = True
        validate_all = True


class CNABBatchHeader(Line):
    pass


class CNABBatchSegmentA(Line):
    field_01_3A: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação", code="G001"
    )
    field_02_3A: types.SequentialServiceBatch = FieldSchema(
        description="Lote de Serviço",
        code="G002",
        default_factory=lambdas.get_field_G002,
    )
    field_03_3A: types.EntryType = FieldSchema(
        description="Tipo de Registro", code="G003", default=types.EntryTypeEnum.details
    )
    field_04_3A: types.RecordSequentialNumber = FieldSchema(
        description="Nº Seqüencial do Registro no Lote",
        code="G038",
        default_factory=lambdas.get_field_G038,
    )
    field_05_3A: types.DetailRecordSegmentType = FieldSchema(
        description="Código de Segmento do Reg. Detalhe",
        code="G039",
        default=types.DetailRecordSegmentTypeEnum.segment_a,
    )
    field_06_3A: types.MovimentationType = FieldSchema(
        description="Tipo de Movimento",
        code="G060",
        default=types.MovimentationTypeEnum.inclusion,
    )
    field_07_3A: types.MovimentationInstructionCode = FieldSchema(
        description="Código da Instrução p/ Movimento",
        code="G061",
        default=types.MovimentationInstructionCodeEnum.inclusion_of_cleared_detail_record,
    )
    field_08_3A: types.CentralClearingHouseCode = FieldSchema(
        description="Código da Câmara Centralizadora",
        code="P001",
        default=types.CentralClearingHouseCodeEnum.TED,
    )
    field_09_3A: types.BankCode = FieldSchema(
        description="Código do Banco do Favorecido", code="P002"
    )
    field_10_3A: types.BankAgencyNumber = FieldSchema(
        description="Ag. Mantenedora da Cta do Favor.", code="G008"
    )
    field_11_3A: types.BankAgencyDigitCheck = FieldSchema(
        description="Dígito Verificador da Agência", code="G009"
    )
    field_12_3A: types.BankAccountNumber = FieldSchema(
        description="Número da Conta Corrente", code="G010"
    )
    field_13_3A: types.BankAccountDigitCheck = FieldSchema(
        description="Dígito Verificador da Conta", code="G011"
    )
    field_14_3A: types.BankAgencyAccountDigitCheck = FieldSchema(
        description="Dígito Verificador da AG/Conta", code="G012"
    )
    field_15_3A: types.PersonName = FieldSchema(
        description="Nome do Favorecido", code="G013"
    )
    field_16_3A: types.BankOrCompanyIssuedDocNumber = FieldSchema(
        description="Nº do Docum. Atribuído p/ Empresa", code="G064", default=""
    )
    field_17_3A: types.CNABDate = FieldSchema(
        description="Data do Pagamento", code="P009"
    )
    field_18_3A: types.Currency = FieldSchema(
        description="Tipo da Moeda", code="G040", default=types.CurrencyEnum.real
    )
    field_19_3A: types.CurrencyAmount = FieldSchema(
        description="Quantidade da Moeda", code="G041", default=0
    )
    field_20_3A: types.PaymentAmount = FieldSchema(
        description="Valor do Pagamento", code="P010"
    )
    field_21_3A: types.BankOrCompanyIssuedDocNumber = FieldSchema(
        description="Nº do Docum. Atribuído pelo Banco", code="G043", default=""
    )
    field_22_3A: types.CNABDate = FieldSchema(
        description="Data Real da Efetivação Pagto", code="P003"
    )
    field_23_3A: types.PaymentEffectiveAmount = FieldSchema(
        description="Valor Real da Efetivação do Pagto", code="P004", default=0
    )
    field_24_3A: types.AdditionalInformation = FieldSchema(
        description="Outras Informações", code="G031", default=""
    )
    field_25_3A: types.ServiceTypeComplement = FieldSchema(
        description="Compl. Tipo Serviço",
        code="P005",
        default=types.ServiceTypeComplementEnum.account_credit,
    )
    field_26_3A: types.TEDFinalityCode = FieldSchema(
        description="Codigo finalidade da TED", code="P011", default=""
    )
    field_27_3A: types.PaymentFinalityComplement = FieldSchema(
        description="Complemento de finalidade pagto.", code="P013", default=""
    )
    field_28_3A: types.FEBRABAN3 = FieldSchema(
        description="Uso Exclusivo FEBRABAN/CNAB", code="G004", default=""
    )
    field_29_3A: types.NotifyRecipient = FieldSchema(
        description="Aviso ao Favorecido",
        code="P006",
        default=types.NotifyRecipientEnum.no_notification,
    )
    field_30_3A: types.ReturnOccurrenceCodes = FieldSchema(
        description="Códigos das Ocorrências para Retorno", code="G059", default=""
    )

    class Config:
        validate_all = True


class CNABBatchSegmentB(Line):
    pass


class CNABBatchSegmentC(Line):
    pass


class CNABBatchTrailer(Line):
    pass


class CNABBatchRecords(BaseModel):
    segment_a: CNABBatchSegmentA
    segment_b: CNABBatchSegmentB
    segment_c: Optional[CNABBatchSegmentC]


class Batch(BaseModel):
    header: CNABBatchHeader
    records: CNABBatchRecords
    trailer: CNABBatchTrailer


class CNABTrailer(Line):
    field_01_9: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação", code="G001"
    )
    field_02_9: types.ServiceBatch = FieldSchema(
        default=types.ServiceBatchEnum.file_trailer,
        description="Lote de Serviço",
        code="G002",
    )
    field_03_9: types.EntryType = FieldSchema(
        default=types.EntryTypeEnum.file_trailer,
        description="Tipo de Registro",
        code="G003",
    )
    field_04_9: types.FEBRABAN9 = FieldSchema(
        default="", description="Uso Exclusivo FEBRABAN/CNAB", code="G004"
    )
    field_05_9: types.RecordsNumber = FieldSchema(
        description="Quantidade de Lotes do Arquivo",
        code="G049",
        default_factory=lambdas.get_field_G049,
    )
    field_06_9: types.RecordsNumber = FieldSchema(
        description="Quantidade de Registros do Arquivo", code="G056"
    )
    field_07_9: types.RecordsNumber = FieldSchema(
        default=0, description="Qtde de Contas p/ Conc. (Lotes)", code="G037"
    )
    field_08_9: types.FEBRABAN205 = FieldSchema(
        default="", description="Uso Exclusivo FEBRABAN/CNAB", code="G004"
    )

    def __init__(self, initial_data, line_number):
        initial_data["field_06_9"] = line_number
        super().__init__(initial_data, line_number)

    class Config:
        validate_all = True
