# pylint: disable=unsubscriptable-object
from datetime import datetime
from enum import Enum, IntEnum
from typing import ClassVar

from pydantic import BaseModel, conint, constr
from pydantic.class_validators import validator


class CNABString(BaseModel):
    def as_fixed_width(self):
        return self.__root__.ljust(self._max_str_length, " ").upper()


class CNABEnum(BaseModel):
    def as_fixed_width(self):
        return str(self.__root__.value)


class CNABPositiveInt(BaseModel):
    __root__: conint(ge=0)

    def as_fixed_width(self):
        return str(self.__root__).rjust(self._max_str_length, "0")


class CNABAlphaPositiveInt(BaseModel):
    __root__: conint(ge=0)

    def as_fixed_width(self):
        return str(self.__root__).ljust(self._max_str_length, " ")


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


class ServiceBatchEnum(str, Enum):
    file_header = "0000"
    file_trailer = "9999"


class ServiceBatch(CNABEnum):
    __root__: ServiceBatchEnum


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
    _max_str_length = 14


class BankConventionCode(CNABAlphaPositiveInt):
    _max_str_length = 20


class BankAgencyNumber(CNABPositiveInt):
    _max_str_length = 5


class BankAgencyDigitCheck(CNABPositiveInt):
    _max_str_length = 1


class BankAccountNumber(CNABPositiveInt):
    _max_str_length = 12


class BankAccountDigitCheck(CNABPositiveInt):
    _max_str_length = 1


class BankAgencyAccountDigitCheck(CNABPositiveInt):
    _max_str_length = 1


class CompanyName(CNABString):
    _max_str_length = 30
    __root__: constr(max_length=_max_str_length)


class BankName(CNABString):
    _max_str_length = 30
    __root__: constr(max_length=_max_str_length)


class RemmitanceReturnCode(CNABPositiveInt):
    _max_str_length = 1


class FileSequentialNumber(CNABPositiveInt):
    _max_str_length = 6


class FileLayoutVersionNumber(CNABPositiveInt):
    _max_str_length = 3


class FileRecordDensity(CNABPositiveInt):
    _max_str_length = 5


class BankReservedField(CNABString):
    _max_str_length = 20
    __root__: constr(max_length=_max_str_length)


class CompanyReservedField(CNABString):
    _max_str_length = 20
    __root__: constr(max_length=_max_str_length)


class FEBRABAN9(CNABString):
    _max_str_length = 9
    __root__: constr(max_length=_max_str_length)


class FEBRABAN10(CNABString):
    _max_str_length = 10
    __root__: constr(max_length=_max_str_length)


class FEBRABAN29(CNABString):
    _max_str_length = 29
    __root__: constr(max_length=_max_str_length)
