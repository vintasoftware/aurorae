# pylint: disable=unsubscriptable-object
from datetime import datetime
from enum import Enum, IntEnum
from typing import ClassVar

from pydantic import BaseModel, conint, constr
from pydantic.class_validators import validator
from pydantic.types import condecimal


STR_FILL_VALUE = " "
INT_FILL_VALUE = "0"


class CNABString(BaseModel):
    def as_fixed_width(self):
        return self.__root__.ljust(self._max_str_length, STR_FILL_VALUE).upper()


class CNABEnum(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__.value)


class CNABPositiveInt(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__).rjust(self._max_str_length, INT_FILL_VALUE)


class CNABAlphaPositiveInt(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__).ljust(self._max_str_length, STR_FILL_VALUE)


class CNABDate(BaseModel):
    _min_str_length: ClassVar[int] = 8
    _max_str_length: ClassVar[int] = 8

    __root__: constr(min_length=_min_str_length, max_length=_max_str_length)

    @validator("__root__")
    def validate_date(cls, value):  # noqa
        try:
            datetime.strptime(value, "%d%m%Y")
        except ValueError:
            raise ValueError("{value} is not valid")
        else:
            return value

    def as_fixed_width(self):
        return self.__root__


class CNABDecimal(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__).rjust(self._max_digits, INT_FILL_VALUE)


class CNABTime(BaseModel):
    _min_str_length: ClassVar[int] = 6
    _max_str_length: ClassVar[int] = 6

    __root__: constr(min_length=_min_str_length, max_length=_max_str_length)

    @validator("__root__")
    def validate_date(cls, value):  # noqa
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


class CompanyRegistrationTypeEnum(IntEnum):
    exempt = 0
    cpf = 1
    cnpj = 2
    pis = 3
    others = 9


class CompanyRegistrationType(CNABEnum):
    __root__: CompanyRegistrationTypeEnum


class CompanyRegistrationNumber(CNABPositiveInt):
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


class BankAgencyDigitCheck(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class BankAccountNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 12
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankAccountDigitCheck(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class BankAgencyAccountDigitCheck(CNABAlphaPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 0
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class CompanyName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class BankName(CNABString):
    _max_str_length: ClassVar[int] = 30
    __root__: constr(max_length=_max_str_length)


class RemmitanceReturnCode(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class FileSequentialNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 6
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999999

    __root__: conint(ge=_min_int, le=_max_int)


class FileLayoutVersionNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 3
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999

    __root__: conint(ge=_min_int, le=_max_int)


class FileRecordDensity(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 5
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 99999

    __root__: conint(ge=_min_int, le=_max_int)


class BankReservedField(CNABString):
    _max_str_length: ClassVar[int] = 20
    __root__: constr(max_length=_max_str_length)


class CompanyReservedField(CNABString):
    _max_str_length: ClassVar[int] = 20
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


class FEBRABAN29(CNABString):
    _max_str_length: ClassVar[int] = 29
    __root__: constr(max_length=_max_str_length)


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


class CurrencyAmount(CNABDecimal):
    _max_digits: ClassVar[int] = 15
    _decimal_places: ClassVar[int] = 5

    __root__: condecimal(max_digits=_max_digits, decimal_places=_decimal_places)


class PaymentAmount(CNABDecimal):
    _max_digits: ClassVar[int] = 15
    _decimal_places: ClassVar[int] = 2

    __root__: condecimal(max_digits=_max_digits, decimal_places=_decimal_places)


class BankOrCompanyIssuedDocNumber(CNABString):
    _max_str_length: ClassVar[int] = 20
    __root__: constr(max_length=_max_str_length)


class PaymentEffectiveAmount(CNABDecimal):
    _max_digits: ClassVar[int] = 15
    _decimal_places: ClassVar[int] = 2

    __root__: condecimal(max_digits=_max_digits, decimal_places=_decimal_places)


class AdditionalInformation(CNABString):
    _max_str_length: ClassVar[int] = 40
    __root__: constr(max_length=_max_str_length)


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


class FEBRABAN205(CNABString):
    _max_str_length = 205
    __root__: constr(max_length=_max_str_length)


class RecordsNumber(CNABPositiveInt):
    _max_str_length = 6
    _min_int = 0
    _max_int = 999999
    __root__: conint(ge=_min_int, le=_max_int)
