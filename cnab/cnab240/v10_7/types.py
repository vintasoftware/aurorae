# pylint: disable=unsubscriptable-object
from datetime import datetime
from enum import Enum, IntEnum
from typing import ClassVar

from pydantic import BaseModel, conint, constr
from pydantic.class_validators import validator


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


class BankAgencyDigitCheck(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class BankAccountNumber(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 12
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 999999999999

    __root__: conint(ge=_min_int, le=_max_int)


class BankAccountDigitCheck(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 1
    _max_int: ClassVar[int] = 9

    __root__: conint(ge=_min_int, le=_max_int)


class BankAgencyAccountDigitCheck(CNABPositiveInt):
    _max_str_length: ClassVar[int] = 1
    _min_int: ClassVar[int] = 1
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


class FEBRABAN9(CNABString):
    _max_str_length: ClassVar[int] = 9
    __root__: constr(max_length=_max_str_length)


class FEBRABAN10(CNABString):
    _max_str_length: ClassVar[int] = 10
    __root__: constr(max_length=_max_str_length)


class FEBRABAN29(CNABString):
    _max_str_length: ClassVar[int] = 29
    __root__: constr(max_length=_max_str_length)
