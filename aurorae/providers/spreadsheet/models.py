# pylint: disable=unsubscriptable-object
from typing import List, Optional

from pydantic import BaseModel

from aurorae.cnab240.v10_7.types import CNABDate, RegistrationType, RegistrationTypeEnum


class BaseConfig:
    allow_population_by_field_name = True

    @classmethod
    def alias_generator(cls, field: str) -> str:
        if field not in cls._mapping:
            raise Exception()
        return cls._mapping[field]


class SpreadsheetCompany(BaseModel):
    company_name: str
    registration_type: RegistrationType = RegistrationTypeEnum.cnpj
    registration_number: str
    bank_name: str
    bank_code: str
    bank_agency: str
    bank_agency_digit: Optional[str]
    bank_account_number: str
    bank_account_digit: Optional[str]
    bank_account_agency_digit: Optional[str]
    address_location: str
    address_number: str
    address_complement: str
    address_cep: str
    address_cep_complement: str
    address_city: str
    address_state: str

    class Config(BaseConfig):
        _mapping = {
            "company_name": "* Nome da Empresa",
            "registration_type": "* Tipo de Inscrição da Empresa",
            "registration_number": "* Número de Inscrição da Empresa",
            "bank_name": "* Nome do Banco",
            "bank_code": "* Código do Convênio no Banco",
            "bank_agency": "* Agência Mantenedora da Conta ",
            "bank_agency_digit": "* Dígito Verificador da Agência",
            "bank_account_number": "* Número da Conta Corrente",
            "bank_account_digit": "* Dígito Verificador da Conta",
            "bank_account_agency_digit": "* Dígito Verificador da Ag/Conta",
            "address_location": "Logradouro (Nome da Rua, Av, Pça, Etc)",
            "address_number": "Número (Número do Local)",
            "address_complement": "Complemento (Casa, Apto, Sala, Etc)",
            "address_cep": "CEP",
            "address_cep_complement": "Complemento do CEP",
            "address_city": "Nome da Cidade",
            "address_state": "Sigla do Estado",
        }


class SpreadsheetEmployee(BaseModel):
    name: str
    registration_type: RegistrationType = RegistrationTypeEnum.cpf
    registration_number: str
    bank_code: str
    bank_agency: str
    bank_agency_digit: Optional[str]
    bank_account_number: str
    bank_account_digit: Optional[str]
    bank_account_agency_digit: Optional[str]
    address_location: str
    address_number: str
    address_complement: str
    address_district: str
    address_cep: str
    address_cep_complement: str
    address_city: str
    address_state: str

    class Config(BaseConfig):
        _mapping = {
            "name": "Nome do Favorecido",
            "registration_type": "* Tipo de Inscrição do Favorecido",
            "registration_number": "* Nº de Inscrição do Favorecido",
            "bank_code": "Código do Banco do Favorecido",
            "bank_agency": "* Ag. Mantenedora da Cta do Favor.",
            "bank_agency_digit": "* Dígito Verificador da Agência",
            "bank_account_number": "* Número da Conta Corrente",
            "bank_account_digit": "* Dígito Verificador da Conta",
            "bank_account_agency_digit": "* Dígito Verificador da AG/Conta",
            "address_location": "Logradouro (Nome da Rua, Av, Pça, Etc)",
            "address_number": "Número (Nº do Local)",
            "address_complement": "Complemento (Casa, Apto, Etc)",
            "address_district": "Bairro",
            "address_cep": "CEP",
            "address_cep_complement": "Complemento do CEP",
            "address_city": "Nome da Cidade",
            "address_state": "Sigla do Estado",
        }


class SpreadsheetPayment(BaseModel):
    employee_name: str
    identification_number: Optional[str]
    payment_amount: str
    payment_date: CNABDate

    class Config(BaseConfig):
        _mapping = {
            "employee_name": "Funcionário",
            "identification_number": "Nº do Docum. Atribuído p/ Empresa",
            "payment_amount": "Valor do Pagamento",
            "payment_date": "Data do Pagamento",
        }


class Spreadsheet(BaseModel):
    company: SpreadsheetCompany
    employees: List[SpreadsheetEmployee]
    payments: List[SpreadsheetPayment]

    class Config(BaseConfig):
        _mapping = {
            "company": "Empresa",
            "employees": "Funcionários",
            "payments": "Pagamentos",
        }
