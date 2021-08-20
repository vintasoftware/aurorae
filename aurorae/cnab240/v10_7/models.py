# pylint: disable=unsubscriptable-object
from __future__ import annotations

import os
from typing import TYPE_CHECKING, List, Optional

from pydantic import Field as FieldSchema
from pydantic.main import BaseModel

import aurorae
from aurorae.cnab240.base import Line
from aurorae.cnab240.v10_7 import lambdas, types


if TYPE_CHECKING:
    from aurorae.payroll.models import Company, Employee, Payment


class BaseConfig:
    allow_population_by_field_name = True

    @classmethod
    def alias_generator(cls, field: str) -> str:
        if field not in cls._mapping:
            return field
        return cls._mapping[field]


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
    field_05_0: types.CNABRegistrationType = FieldSchema(
        description="Tipo de Inscrição da Empresa", code="G005"
    )
    field_06_0: types.RegistrationNumber = FieldSchema(
        description="Número de Inscrição da Empresa", code="G006"
    )
    field_07_0: types.BankConventionCode = FieldSchema(
        description="Código do Convênio no Banco", code="G007"
    )
    field_08_0: types.BankAgencyNumber = FieldSchema(
        description="Agência Mantenedora da Conta", code="G008"
    )
    field_09_0: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Agência", code="G009"
    )
    field_10_0: types.BankAccountNumber = FieldSchema(
        description="Número da Conta Corrente", code="G010"
    )
    field_11_0: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Conta", code="G011"
    )
    field_12_0: types.BankDigitCheck = FieldSchema(
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
        default=types.RemmitanceReturnCodeEnum.shipping,
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
        default=types.FileLayoutVersionNumberEnum.v10_3,
    )
    field_21_0: types.FileRecordDensity = FieldSchema(
        description="Densidade de Gravação do Arquivo",
        code="G020",
        default=types.FileRecordDensityEnum.d1600,
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

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True
        _mapping = {
            "field_01_0": "bank_code",
            "field_05_0": "registration_type",
            "field_06_0": "registration_number",
            "field_07_0": "bank_code",
            "field_08_0": "bank_agency",
            "field_09_0": "bank_agency_digit",
            "field_10_0": "bank_account_number",
            "field_11_0": "bank_account_digit",
            "field_12_0": "bank_account_agency_digit",
            "field_13_0": "company_name",
            "field_14_0": "bank_name",
        }


class CNABBatchHeader(Line):
    field_01_1: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação",
        code="G001",
    )
    field_02_1: types.SequentialServiceBatch = FieldSchema(
        default_factory=lambdas.get_field_G002_sequential,
        description="Lote de Serviço",
        code="G002",
    )
    field_03_1: types.EntryType = FieldSchema(
        default=types.EntryTypeEnum.batch_header,
        description="Tipo de Registro",
        code="G003",
    )
    field_04_1: types.OperationType = FieldSchema(
        default=types.OperationTypeEnum.credit_entry,
        description="Tipo da Operação",
        code="G028",
    )
    field_05_1: types.ServiceType = FieldSchema(
        default=types.ServiceTypeEnum.salary_payment,
        description="Tipo do Serviço",
        code="G025",
    )
    field_06_1: types.ReleaseMethod = FieldSchema(
        default=types.ReleaseMethodEnum.credit_in_checking_account,
        description="Forma de Lançamento",
        code="G029",
    )
    field_07_1: types.BatchLayoutVersionNumber = FieldSchema(
        default=types.BatchLayoutVersionNumberEnum.v0_46,
        description="Nº da Versão do Layout do Lote",
        code="G030",
    )
    field_08_1: types.FEBRABAN1 = FieldSchema(
        default="",
        description="Uso Exclusivo da FEBRABAN/CNAB",
        code="G004",
    )
    field_09_1: types.CNABRegistrationType = FieldSchema(
        description="Tipo de Inscrição da Empresa",
        code="G005",
    )
    field_10_1: types.RegistrationNumber = FieldSchema(
        description="Número de Inscrição da Empresa",
        code="G006",
    )
    field_11_1: types.BankConventionCode = FieldSchema(
        description="Código do Convênio no Banco",
        code="G007",
    )
    field_12_1: types.BankAgencyNumber = FieldSchema(
        description="Agência Mantenedora da Conta",
        code="G008",
    )
    field_13_1: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Agência",
        code="G009",
    )
    field_14_1: types.BankAccountNumber = FieldSchema(
        description="Número da Conta Corrente",
        code="G010",
    )
    field_15_1: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Conta",
        code="G011",
    )
    field_16_1: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Ag/Conta",
        code="G012",
    )
    field_17_1: types.CompanyName = FieldSchema(
        description="Nome da Empresa",
        code="G013",
    )
    field_18_1: types.Message = FieldSchema(
        description="Mensagem",
        default="",
        code="G031",
    )
    field_19_1: types.AddressName = FieldSchema(
        description="Nome da Rua, Av, Pça, Etc",
        default="",
        code="G032",
    )
    field_20_1: types.AddressNumber = FieldSchema(
        description="Número do Local",
        code="G032",
    )
    field_21_1: types.AddressDetails = FieldSchema(
        description="Casa, Apto, Sala, Etc",
        code="G032",
    )
    field_22_1: types.AddressCityName = FieldSchema(
        description="Nome da Cidade",
        code="G033",
    )
    field_23_1: types.AddressCEP = FieldSchema(
        description="CEP",
        code="G034",
    )
    field_24_1: types.AddressCEPComplement = FieldSchema(
        description="Complemento do CEP",
        code="G035",
    )
    field_25_1: types.AddressState = FieldSchema(
        description="Sigla do Estado",
        code="G036",
    )
    field_26_1: types.PaymentMethod = FieldSchema(
        default=types.PaymentMethodEnum.direct_debit,
        description="Indicativo da Forma de Pagamento do Serviço",
        code="P014",
    )
    field_27_1: types.FEBRABAN6 = FieldSchema(
        default="",
        description="Uso Exclusivo FEBRABAN/CNAB",
        code="G004",
    )
    field_28_1: types.ReturnOccurrenceCodes = FieldSchema(
        default="",
        description="Códigos das Ocorrências p/ Retorno",
        code="G059",
    )

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True
        _mapping = {
            "field_01_1": "bank_code",
            "field_09_1": "registration_type",
            "field_10_1": "registration_number",
            "field_11_1": "bank_code",
            "field_12_1": "bank_agency",
            "field_13_1": "bank_agency_digit",
            "field_14_1": "bank_account_number",
            "field_15_1": "bank_account_digit",
            "field_16_1": "bank_account_agency_digit",
            "field_17_1": "company_name",
            "field_19_1": "address_location",
            "field_20_1": "address_number",
            "field_21_1": "address_complement",
            "field_22_1": "address_city",
            "field_23_1": "address_cep",
            "field_24_1": "address_cep_complement",
            "field_25_1": "address_state",
        }


class CNABBatchSegmentA(Line):
    field_01_3A: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação", code="G001"
    )
    field_02_3A: types.SequentialServiceBatch = FieldSchema(
        description="Lote de Serviço",
        code="G002",
        default_factory=lambdas.get_field_G002_sequential,
    )
    field_03_3A: types.EntryType = FieldSchema(
        description="Tipo de Registro", code="G003", default=types.EntryTypeEnum.details
    )
    field_04_3A: types.RecordSequentialNumber = FieldSchema(
        description="Nº Seqüencial do Registro no Lote",
        code="G038",
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
    field_11_3A: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Agência", code="G009"
    )
    field_12_3A: types.BankAccountNumber = FieldSchema(
        description="Número da Conta Corrente", code="G010"
    )
    field_13_3A: types.BankDigitCheck = FieldSchema(
        description="Dígito Verificador da Conta", code="G011"
    )
    field_14_3A: types.BankDigitCheck = FieldSchema(
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
    field_24_3A: types.Message = FieldSchema(
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

    _nested_mapping = {
        "field_01_3A": "company.bank_code",
        "field_09_3A": "employee.bank_code",
        "field_10_3A": "employee.bank_agency",
        "field_11_3A": "employee.bank_agency_digit",
        "field_12_3A": "employee.bank_account_number",
        "field_13_3A": "employee.bank_account_digit",
        "field_14_3A": "employee.bank_account_agency_digit",
        "field_15_3A": "employee.name",
        "field_17_3A": "payment.payment_date",
        "field_20_3A": "payment.payment_amount",
        "field_22_3A": "payment.payment_date",
    }

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True
        _mapping = {"field_04_3A": "record_number"}

    def __init__(self, payment: Payment, record_number: int, line_number: int) -> None:
        employee = payment.employee
        company = payment.company

        initial_data = {
            "payment": payment.dict(),
            "company": company.dict(),
            "employee": employee.dict(),
        }

        data = self._map_nested_values(initial_data)
        data["record_number"] = record_number
        super().__init__(data, line_number=line_number)

    def _map_nested_values(self, initial_data: dict) -> None:
        data = {}
        for key, nested_path in self._nested_mapping.items():
            [entity_key, field_key] = nested_path.split(".")

            entity = initial_data[entity_key]
            data[key] = entity[field_key]

        return data


class CNABBatchSegmentB(Line):
    field_01_3B: types.BankCode = FieldSchema(
        name="Código do Banco na Compensação",
        code="G001",
    )
    field_02_3B: types.SequentialServiceBatch = FieldSchema(
        default_factory=lambdas.get_field_G002_sequential,
        name="Lote de Serviço",
        code="G002",
    )
    field_03_3B: types.EntryType = FieldSchema(
        default=types.EntryTypeEnum.details,
        name="Tipo de Registro",
        code="G003",
    )
    field_04_3B: types.RecordSequentialNumber = FieldSchema(
        name="Nº Seqüencial do Registro no Lote",
        code="G038",
    )
    field_05_3B: types.DetailRecordSegmentType = FieldSchema(
        default=types.DetailRecordSegmentTypeEnum.segment_b,
        name="Código de Segmento do Reg. Detalhe",
        code="G039",
    )
    field_06_3B: types.InitiationForm = FieldSchema(
        default=types.InitiationFormEnum.bank_info,
        name="* Forma de Iniciação",
        code="G100",
    )
    field_07_3B: types.CNABRegistrationType = FieldSchema(
        name="Tipo de Inscrição do Favorecido",
        code="G005",
    )
    field_08_3B: types.RegistrationNumber = FieldSchema(
        name="Nº de Inscrição do Favorecido",
        code="G006",
    )
    field_09_3B: types.Information10 = FieldSchema(
        default="",
        name="Informação 10",
        code="G101",
    )
    field_10_3B: types.Information11 = FieldSchema(
        default="",
        name="Informação 11",
        code="G101",
    )
    field_11_3B: types.Information12 = FieldSchema(
        default="",
        name="Informação 12",
        code="G101",
    )
    field_12_3B: types.SIAPE6 = FieldSchema(
        default=0,
        name="Uso Exclusivo para o SIAPE",
        code="P012",
    )
    field_13_3B: types.ISPBCode = FieldSchema(
        default=0,
        name="Código ISPB",
        code="P015",
    )

    def _get_information_10(self, employee: Employee):
        return types.Information10.parse_obj(employee.address_location.value)

    def _get_information_11(self, employee: Employee):
        return types.ComposedAddressInformation.parse_obj(employee)

    def _get_information_12(self, payment: Payment):
        return types.ComposedPaymentInformation.parse_obj(payment)

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True

        _mapping = {
            "field_01_3B": "bank_code",
            "field_04_3B": "record_number",
            "field_07_3B": "registration_type",
            "field_08_3B": "registration_number",
            "field_09_3B": "information_10",
            "field_10_3B": "information_11",
            "field_11_3B": "information_12",
        }

    def __init__(self, payment: Payment, record_number: int, line_number: int) -> None:
        employee = payment.employee
        initial_data = employee.dict()
        initial_data["record_number"] = record_number
        initial_data["information_10"] = self._get_information_10(employee)
        initial_data["information_11"] = self._get_information_11(employee)
        initial_data["information_12"] = self._get_information_12(payment)
        super().__init__(initial_data, line_number)


class CNABBatchSegmentC(Line):
    pass


class CNABBatchTrailer(Line):
    field_01_5: types.BankCode = FieldSchema(
        description="Código do Banco na Compensação", code="G001"
    )
    field_02_5: types.SequentialServiceBatch = FieldSchema(
        description="Lote de Serviço",
        code="G002",
        default_factory=lambdas.get_field_G002_sequential,
    )
    field_03_5: types.EntryType = FieldSchema(
        description="Tipo de Registro",
        code="G003",
        default=types.EntryTypeEnum.batch_trailer,
    )
    field_04_5: types.FEBRABAN9 = FieldSchema(
        description="Uso Exclusivo FEBRABAN/CNAB", code="G004", default=""
    )
    field_05_5: types.RecordsNumber = FieldSchema(
        description="Quantidade de Registros do Lote", code="G057"
    )
    field_06_5: types.ValuesSum = FieldSchema(
        description="Somatória dos Valores", code="P007"
    )
    field_07_5: types.CurrencyAmountSum = FieldSchema(
        description="Somatória de Quantidade de Moedas", code="G058", default=0
    )
    field_08_5: types.DebitNotificationNumber = FieldSchema(
        description="Número Aviso de Débito ", code="G066", default=0
    )
    field_09_5: types.FEBRABAN165 = FieldSchema(
        description="Uso Exclusivo FEBRABAN/CNAB", code="G004", default=""
    )
    field_10_5: types.ReturnOccurrenceCodes = FieldSchema(
        description="Códigos das Ocorrências para Retorno", code="G059", default=""
    )

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True
        _mapping = {
            "field_01_5": "bank_code",
            "field_05_5": "total_batch_lines",
            "field_06_5": "payment_amount_sum",
        }

    def __init__(
        self,
        company: Company,
        sum_payment_values: str,
        total_batch_lines: int,
        line_number,
    ):

        initial_data = company.dict()
        initial_data["total_batch_lines"] = total_batch_lines
        initial_data["payment_amount_sum"] = sum_payment_values
        super().__init__(initial_data, line_number)


class CNABBatchRecord(BaseModel):
    segment_a: CNABBatchSegmentA
    segment_b: CNABBatchSegmentB
    segment_c: Optional[CNABBatchSegmentC]

    def as_fixed_width(self):
        fixed_width_str = (
            f"{self.segment_a.as_fixed_width()}\n"
            f"{self.segment_b.as_fixed_width()}\n"
        )
        return fixed_width_str

    def as_html(self):
        html_result = f"{self.segment_a.as_html()}{self.segment_b.as_html()}"
        return html_result


class CNABBatch(BaseModel):
    header: CNABBatchHeader
    records: List[CNABBatchRecord]
    trailer: CNABBatchTrailer

    def as_fixed_width(self):
        fixed_width_str = ""

        fixed_width_str += f"{self.header.as_fixed_width()}\n"
        for record in self.records:
            fixed_width_str += f"{record.as_fixed_width()}"
        fixed_width_str += f"{self.trailer.as_fixed_width()}\n"

        return fixed_width_str

    def as_html(self):
        html_result = ""

        html_result += f"{self.header.as_html()}"
        for record in self.records:
            html_result += f"{record.as_html()}"
        html_result += f"{self.trailer.as_html()}"

        return html_result


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

    class Config(BaseConfig):
        validate_all = True
        validate_assignment = True
        _mapping = {"field_01_9": "bank_code", "field_06_9": "total_file_lines"}

    def __init__(self, company: Company, total_file_lines: int, line_number: int):
        initial_data = company.dict()
        initial_data["total_file_lines"] = total_file_lines
        super().__init__(initial_data, line_number)


class CNABFile(BaseModel):
    header: CNABHeader
    batches: List[CNABBatch]
    trailer: CNABTrailer

    def as_fixed_width(self):
        fixed_width_str = ""

        fixed_width_str += f"{self.header.as_fixed_width()}\n"
        for batch in self.batches:
            fixed_width_str += f"{batch.as_fixed_width()}"
        fixed_width_str += f"{self.trailer.as_fixed_width()}"

        return fixed_width_str

    def as_html(self):
        html_result = ""

        html_result += f"{self.header.as_html()}"
        for batch in self.batches:
            html_result += f"{batch.as_html()}"
        html_result += f"{self.trailer.as_html()}"

        return html_result

    def generate_file(self, output_filename):
        file_path = f"{output_filename}"

        with open(os.path.expanduser(file_path), "w") as f:
            file_content = self.as_fixed_width()
            f.write(file_content)

    def generate_html_file(self, output_filename):
        file_path = f"{output_filename.with_suffix('.html')}"

        root_path = os.path.dirname(aurorae.__file__)
        stylesheet_filename = os.path.join(root_path, "staticfiles/styles.css")

        with open(os.path.expanduser(file_path), "w") as f:
            html_content = self.as_html()
            f.write("<html><head>")
            f.write(f"<link href='{stylesheet_filename}' rel='stylesheet'>")
            f.write("</head><body>")
            f.write(html_content)
            f.write("</body></html>")
