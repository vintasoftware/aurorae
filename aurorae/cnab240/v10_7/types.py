# pylint: disable=unsubscriptable-object
from datetime import datetime
from decimal import Decimal
from enum import Enum, IntEnum
from typing import ClassVar, Union

from pydantic import BaseModel, conint, constr, validator


STR_FILL_VALUE = " "
INT_FILL_VALUE = "0"

REGISTRATION_TYPE_MAP = {
    "ISENTO/NAO INFORMADO": 0,
    "CPF": 1,
    "CGC/CNPJ": 2,
    "PIS/PASEP": 3,
    "OUTROS": 9,
}

# fmt: off
VALID_CHARACTERS = (
    "abcdefghijklmnopqrstuvxywz"
    "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
    "0123456789"
    ". "
)
# fmt: on


class CNABComposedField(BaseModel):
    def get_field_names(self):
        return self.__fields__.keys()

    def get_fields(self):
        fields = []
        for field_name in self.get_field_names():
            field = getattr(self, field_name)
            fields.append(field)
        return fields

    def as_fixed_width(self):
        formatted_value = ""
        for field in self.get_fields():
            formatted_value = f"{formatted_value}{field.as_fixed_width()}"

        assert len(formatted_value) == self._max_str_length

        return formatted_value


class CNABString(BaseModel):
    @property
    def value(self):
        value = self.__root__
        if isinstance(value, (CNABString, CNABComposedField)):
            value = value.as_fixed_width()
        return value

    @validator("__root__", pre=True, check_fields=False, allow_reuse=True)
    def validate_string(cls, value):  # noqa
        if not isinstance(value, (CNABString, CNABComposedField)):
            assert all(c in VALID_CHARACTERS for c in value), "Invalid characters"

        return value

    def as_fixed_width(self):
        return self.value.ljust(self._max_str_length, STR_FILL_VALUE).upper()


class CNABEnum(BaseModel):
    @property
    def value(self):
        return self.__root__.value

    def as_fixed_width(self):
        return str(self.value)


class CNABEnumFillInt(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__.value).rjust(self._max_str_length, INT_FILL_VALUE)


class CNABEnumAlphaFill(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__.value).ljust(self._max_str_length, STR_FILL_VALUE)


class PositiveInt(BaseModel):
    @property
    def value(self):
        return self.__root__

    @validator("__root__", pre=True, check_fields=False, allow_reuse=True)
    def validate_int(cls, value):  # noqa
        """Prevent coersion from float/decimal to int, allow coersion from string"""
        if isinstance(value, (Decimal, float)):
            raise ValueError(
                "value cannot be a float or Decimal, should be an integer instead"
            )

        return value


class CNABPositiveInt(PositiveInt):
    def as_fixed_width(self):
        return str(self.__root__).rjust(self._max_str_length, INT_FILL_VALUE)


class CNABAlphaPositiveInt(PositiveInt):
    def as_fixed_width(self):
        return str(self.__root__).ljust(self._max_str_length, STR_FILL_VALUE)


class CNABDate(BaseModel):
    _min_str_length: ClassVar[int] = 8
    _max_str_length: ClassVar[int] = 8

    __root__: constr(min_length=_min_str_length, max_length=_max_str_length)

    @validator("__root__", allow_reuse=True)
    def validate_date(cls, value):  # noqa
        try:
            datetime.strptime(value, "%d%m%Y")
        except ValueError:
            raise ValueError("{value} is not valid")
        else:
            return value

    def as_fixed_width(self):
        return self.__root__


class CNABTime(BaseModel):
    _min_str_length: ClassVar[int] = 6
    _max_str_length: ClassVar[int] = 6

    __root__: constr(min_length=_min_str_length, max_length=_max_str_length)

    @validator("__root__", allow_reuse=True)
    def validate_time(cls, value):  # noqa
        try:
            datetime.strptime(value, "%H%M%S")
        except ValueError:
            raise ValueError("{value} is not valid")
        else:
            return value

    def as_fixed_width(self):
        return self.__root__


class BankCode(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 3
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999

    __root__: conint(ge=_min_int, le=_max_int)


class ServiceBatchEnum(str, Enum):
    file_header = "0000"
    file_trailer = "9999"


class ServiceBatch(CNABEnum):
    __root__: ServiceBatchEnum


class SequentialServiceBatch(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 4
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 9998

    __root__: conint(ge=_min_int, le=_max_int)


class EntryTypeEnum(IntEnum):
    file_header = 0
    batch_header = 1
    batch_initial_records = 2
    details = 3
    batch_final_records = 4
    batch_trailer = 5
    file_trailer = 9


class EntryType(CNABEnum):
    __root__: EntryTypeEnum


class RegistrationTypeEnum(Enum):
    exempt = "ISENTO/NAO INFORMADO"
    cpf = "CPF"
    cnpj = "CGC/CNPJ"
    pis = "PIS/PASEP"
    others = "OUTROS"


class CNABRegistrationTypeEnum(IntEnum):
    exempt = 0
    cpf = 1
    cnpj = 2
    pis = 3
    others = 9


class RegistrationType(CNABEnum):
    __root__: RegistrationTypeEnum


class CNABRegistrationType(CNABEnum):
    __root__: CNABRegistrationTypeEnum

    @validator("__root__", pre=True, allow_reuse=True)
    def validate_registration_type(cls, root_value):  # noqa
        if isinstance(root_value, RegistrationTypeEnum):
            return REGISTRATION_TYPE_MAP[root_value.value]
        return root_value


class RegistrationNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 14
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankConventionCode(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 20
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankAgencyNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 5
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999

    __root__: conint(ge=_min_int, le=_max_int)


class BankAccountNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 12
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankDigitCheck(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 9
    __root__: constr(max_length=_max_str_length)

    @validator("__root__")
    def valid_int(cls, v):  # noqa
        try:
            v_as_int = int(v)
        except ValueError:
            return ""

        if v_as_int > cls._max_int:
            raise ValueError(f"{v_as_int} is greater than the max value {cls._max_int}")

        if v_as_int < cls._min_int:
            raise ValueError(f"{v_as_int} is smaller than the min value {cls._min_int}")

        return v


class CompanyName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class BankName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class RecipientName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class RemmitanceReturnCodeEnum(IntEnum):
    shipping = 1
    returning = 2


class RemmitanceReturnCode(CNABEnum):
    __root__: RemmitanceReturnCodeEnum


class FileSequentialNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 6
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999999

    __root__: conint(ge=_min_int, le=_max_int)


class FileRecordDensityEnum(str, Enum):
    d1600 = "1600"
    d6250 = "6250"


class FileRecordDensity(CNABEnumFillInt):
    _max_str_length: ClassVar[int] = 5
    __root__: FileRecordDensityEnum


class BankReservedField(CNABString):
    _max_str_length: ClassVar[int] = 20
    __root__: constr(max_length=_max_str_length)


class CompanyReservedField(CNABString):
    _max_str_length: ClassVar[int] = 20
    __root__: constr(max_length=_max_str_length)


class FEBRABAN1(CNABString):
    _max_str_length = 1
    __root__: constr(max_length=_max_str_length)


class FEBRABAN6(CNABString):
    _max_str_length = 6
    __root__: constr(max_length=_max_str_length)


class FEBRABAN3(CNABString):
    _max_str_length: ClassVar[int] = 3
    __root__: constr(max_length=_max_str_length)


class FEBRABAN9(CNABString):
    _max_str_length: ClassVar[int] = 9
    __root__: constr(max_length=_max_str_length)


class FEBRABAN10(CNABString):
    _max_str_length: ClassVar[int] = 10
    __root__: constr(max_length=_max_str_length)


class FEBRABAN165(CNABString):
    _max_str_length = 165
    __root__: constr(max_length=_max_str_length)


class FEBRABAN205(CNABString):
    _max_str_length = 205
    __root__: constr(max_length=_max_str_length)


class FEBRABAN29(CNABString):
    _max_str_length: ClassVar[int] = 29
    __root__: constr(max_length=_max_str_length)


class SmallAddressCityName(CNABString):
    _max_str_length = 15
    __root__: constr(max_length=_max_str_length)


class AddressDistrict(CNABString):
    _max_str_length = 15
    __root__: constr(max_length=_max_str_length)


class RebateAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class DiscountAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class ArrearsAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class FineAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class InformationRegistrationType(CNABString):
    _max_str_length: ClassVar[int] = 15
    __root__: constr(max_length=_max_str_length)


class OperationTypeEnum(str, Enum):
    credit_entry = "C"
    debit_entry = "D"
    conciliation_statement = "E"
    cash_management_statement = "G"
    information_securities_secured_from_bank = "I"
    shipping_file = "R"
    return_file = "T"


class OperationType(CNABEnum):
    __root__: OperationTypeEnum


class ServiceTypeEnum(str, Enum):
    charge = "01"
    electronic_payment_slip = "03"
    bank_reconciliation = "04"
    debts = "05"
    check_custody = "06"
    cash_management = "07"
    query_margin_nformation = "08"
    registration_of_consignment_rRetention = "09"
    dividend_payment = "10"
    consignment_maintenance = "11"
    consignment_of_installments = "12"
    consignment_disallowance_inss = "13"
    inquiry_taxes_payable = "14"
    supplier_payment = "20"
    payment_of_bills_taxes = "22"
    interoperability_payment_institution_accounts = "23"
    buy = "25"
    buy_rotary = "26"
    payer_claim = "29"
    salary_payment = "30"
    payment_fees = "32"
    payment_stipend = "33"
    payment_prebends = "34"
    vendor = "40"
    forward_seller = "41"
    payment_of_insured = "50"
    payment_of_transit_traveler_expenses = "60"
    authorized_payment = "70"
    accredited_payment = "75"
    remuneration_payment = "77"
    payment_of_authorized_representatives = "80"
    payment_benefits = "90"
    miscellaneous_payments = "98"


class ServiceType(CNABEnum):
    __root__: ServiceTypeEnum


class ReleaseMethodEnum(str, Enum):
    credit_in_checking_account = "01"
    administrative_payment_check = "02"
    doc_ted = "03"
    card_salary = "04"
    credit_in_account_savings = "05"
    op_disposition = "10"
    payment_of_accounts_and_tributos_with_bar_code = "11"
    tax_DARF_normal = "16"
    tax_GPS = "17"
    tax_DARF_simple = "18"
    tax_IPTU_city = "19"
    payment_with_authentication = "20"
    tax_DARJ = "21"
    tax_GARE_SP_ICMS = "22"
    tax_GARE_SP_DR = "23"
    tax_GARE_SP_ITCMD = "24"
    tax_IPVA = "25"
    tax_licenciamento = "26"
    tax_DPVAT = "27"
    settlement_of_securities_of_the_bank = "30"
    payment_of_securities_from_other_banks = "31"
    current_account_statement = "40"
    TED_other_entitlement = "41"
    TED_same_ownership = "43"
    TED_transfer_from_investment_account = "44"
    PIX = "45"
    PIX_qr_code = "47"
    debit_checking_account = "50"
    statement_for_cash_management = "70"
    deposit_judicial_in_account_current = "71"
    deposit_judicial_in_savings = "72"
    statement_of_investment_account = "73"
    payment_of_municipal_taxes_ISS_own_bank = "80"
    payment_of_municipal_taxes_ISS_other_bank = "81"


class ReleaseMethod(CNABEnum):
    __root__: ReleaseMethodEnum


class BatchLayoutVersionNumberEnum(str, Enum):
    v0_46 = "046"


class BatchLayoutVersionNumber(CNABEnum):
    __root__: BatchLayoutVersionNumberEnum


class FileLayoutVersionNumberEnum(str, Enum):
    v10_3 = "103"


class FileLayoutVersionNumber(CNABEnum):
    __root__: FileLayoutVersionNumberEnum


class Message(CNABString):
    _max_str_length = 40
    __root__: constr(max_length=_max_str_length)


class AddressName(CNABString):
    _max_str_length = 30
    __root__: constr(max_length=_max_str_length)


class AddressNumber(CNABPositiveInt):
    _max_str_length = 5
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999

    __root__: conint(ge=_min_int, le=_max_int)


class DetailRecordSegmentTypeEnum(str, Enum):
    segment_a = "A"
    segment_b = "B"
    segment_c = "C"


class DetailRecordSegmentType(CNABEnum):
    __root__: DetailRecordSegmentTypeEnum


class PersonName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class RecordSequentialNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 5
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999
    __root__: conint(ge=_min_int, le=_max_int)


class InitiationFormEnum(str, Enum):
    pix_phone = "01"
    pix_email = "02"
    pix_cpf_cnpj = "03"
    random_key = "04"
    bank_info = "05"


class InitiationForm(CNABEnumAlphaFill):
    _max_str_length: ClassVar[int] = 3
    __root__: InitiationFormEnum


class SIAPE6(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 6
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999

    __root__: conint(ge=_min_int, le=_max_int)


class ISPBCode(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 8
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 99999999

    __root__: conint(ge=_min_int, le=_max_int)


class AddressDetails(CNABString):
    _max_str_length = 15
    __root__: constr(max_length=_max_str_length)


class AddressCityName(CNABString):
    _max_str_length = 20
    __root__: constr(max_length=_max_str_length)


class AddressCEP(CNABPositiveInt):
    _max_str_length = 5
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 99999

    __root__: conint(ge=_min_int, le=_max_int)


class AddressCEPComplement(CNABPositiveInt):
    _max_str_length = 3
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999

    __root__: conint(ge=_min_int, le=_max_int)


class AddressState(CNABString):
    _max_str_length = 2
    __root__: constr(max_length=_max_str_length)


class PaymentMethodEnum(str, Enum):
    direct_debit = "01"
    loan_financing_debit = "02"
    credit_card_debit = "03"


class PaymentMethod(CNABEnum):
    __root__: PaymentMethodEnum


class MovimentationTypeEnum(IntEnum):
    inclusion = 0
    consultation = 1
    suspension = 2
    chargeback = 3
    reactivation = 4
    update = 5
    liquidation = 7
    exclusion = 9


class MovimentationType(CNABEnum):
    __root__: MovimentationTypeEnum


class MovimentationInstructionCodeEnum(str, Enum):
    inclusion_of_cleared_detail_record = "00"
    inclusion_of_blocked_detail_record = "09"
    change_payment_from_cleared_to_blocked = "10"
    change_blocked_from_payment_to_cleared = "11"
    change_in_security_value = "17"
    payment_date_change = "19"
    direct_payment_to_supplier = "23"
    wallet_maintenance_do_not_pay = "25"
    wallet_withdrawal_do_not_pay = "27"
    reversal_by_return_from_central_clearing_house = "33"
    payer_claim = "40"
    delete_previously_added_detail_record = "99"


class MovimentationInstructionCode(CNABEnum):
    __root__: MovimentationInstructionCodeEnum


class CentralClearingHouseCodeEnum(str, Enum):
    TED = "018"
    DOC = "700"
    # Used when it's necessary to send TED using the ISPB code
    # of the Recipient Financial Institution. In this case, it's mandatory to fill
    # the field "ISPB Code" - field 26.3B,
    # of the Payment Segment, as described in Note P015.
    TED_ISPB = "988"
    PIX = "009"


class CentralClearingHouseCode(CNABEnum):
    __root__: CentralClearingHouseCodeEnum


class CurrencyEnum(str, Enum):
    national_treasury_bonus_tr = "BTN"
    real = "BRL"
    us_dollar = "USD"
    portuguese_shield = "PTE"
    french_franc = "FRF"
    swiss_franc = "CHF"
    japanese_yen = "JPY"
    general_price_index = "IGP"
    general_market_price_index = "IGM"
    pound_sterling = "GBP"
    italian_lira = "ITL"
    german_mark = "DEM"
    daily_referential_rate = "TRD"
    standard_capital_unit = "UPC"
    standard_financing_unit = "UPF"
    tax_reference_unit = "UFR"
    european_currenc = "XEU"


class Currency(CNABEnum):
    __root__: CurrencyEnum


class CurrencyAmount(CNABPositiveInt):
    _max_str_length = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class PaymentAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankOrCompanyIssuedDocNumber(CNABString):
    _max_str_length: ClassVar[int] = 20
    __root__: constr(max_length=_max_str_length)


class PaymentEffectiveAmount(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 15
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class ServiceTypeComplementEnum(str, Enum):
    account_credit = "01"
    payment_of_rent_condominium = "02"
    payment_of_duplicate_securities = "03"
    payment_of_dividends = "04"
    payment_of_school_tuition = "05"
    salary_payment = "06"
    payment_to_suppliers = "07"
    transactions_of_foreign_exchange_funds_stock_exchange = "08"
    transfer_of_collection_payment_of_taxes = "09"
    international_transfer_in_real = "10"
    doc_for_savings = "11"
    doc_for_judicial_deposit = "12"
    others = "13"
    stipend_payment = "16"
    remuneration_to_the_member = "17"
    pagamento_of_fees = "18"
    payment_of_prebend = "19"


class ServiceTypeComplement(CNABEnum):
    __root__: ServiceTypeComplementEnum


class TEDFinalityCode(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 5
    __root__: constr(max_length=_max_str_length)


class PaymentFinalityComplement(CNABString):
    _max_str_length: ClassVar[int] = 2
    __root__: constr(max_length=_max_str_length)


class NotifyRecipientEnum(str, Enum):
    no_notification = 0
    notify_only_sender = 2
    notify_only_recipient = 5
    notify_sender_and_recipient = 6
    notify_recipient_and_2_copies_to_sender = 7


class NotifyRecipient(CNABEnum):
    __root__: NotifyRecipientEnum


class ReturnOccurrenceCodes(CNABString):
    _max_str_length = 10
    __root__: constr(max_length=_max_str_length)


class RecordsNumber(CNABPositiveInt):
    _max_str_length = 6
    _min_int = 0
    _max_int = 999999
    __root__: conint(ge=_min_int, le=_max_int)


class ValuesSum(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 18
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999999
    __root__: conint(ge=_min_int, le=_max_int)


class CurrencyAmountSum(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 18
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999999999999999
    __root__: conint(ge=_min_int, le=_max_int)


class DebitNotificationNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 6
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 999999

    __root__: conint(ge=_min_int, le=_max_int)


class ComposedAddressInformation(CNABComposedField):
    _max_str_length: ClassVar[int] = 60

    address_number: AddressNumber
    address_complement: AddressDetails
    address_district: AddressDistrict
    address_city: SmallAddressCityName
    address_cep: AddressCEP
    address_cep_complement: AddressCEPComplement
    address_state: AddressState


class ComposedPaymentInformation(CNABComposedField):
    _max_str_length: ClassVar[int] = 99

    payment_date: CNABDate
    payment_amount: PaymentAmount
    rebate_amount: RebateAmount
    discount_amount: DiscountAmount
    arrears_amount: ArrearsAmount
    fine_amount: FineAmount
    registration_type: InformationRegistrationType
    notify_recipient: NotifyRecipient


class PIXTXID(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class PIXKey(CNABString):
    _max_str_length: ClassVar[int] = 60
    __root__: constr(max_length=_max_str_length)


class Information10(CNABString):
    _max_str_length: ClassVar[int] = 35
    __root__: Union[AddressName, PIXTXID]


class Information11(CNABString):
    _max_str_length: ClassVar[int] = 60
    __root__: Union[PIXKey, Message, ComposedAddressInformation]


class Information12(CNABString):
    _max_str_length: ClassVar[int] = 99
    __root__: Union[PIXKey, ComposedPaymentInformation]
