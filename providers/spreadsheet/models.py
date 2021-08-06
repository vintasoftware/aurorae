from enum import Enum
from typing import List

from pydantic import BaseModel

from cnab.cnab240.v10_7.types import CNABDate


class RegistrationType(Enum):
    exempt = "Exempt/Not Informed"
    cpf = "CPF"
    cnpj = "CGC/CNPJ"
    pis = "PIS/PASEP"
    others = "Others"


class BaseConfig:
    allow_population_by_field_name = True

    @classmethod
    def alias_generator(cls, field: str) -> str:
        if field not in cls._mapping:
            print(field)
            raise Exception()
        return cls._mapping[field]


class SpreadsheetCompany(BaseModel):
    company_name: str
    registration_type = RegistrationType.cnpj
    registration_number: str
    bank_name: str
    bank_code: str
    bank_agency: str
    bank_agency_digit: str
    bank_account_number: str
    bank_account_digit: str
    bank_account_agency_digit: str
    address_location: str
    address_number: str
    address_complement: str
    address_city: str
    address_cep_complement: str
    address_state: str
    address_cep: str

    class Config(BaseConfig):
        _mapping = {
            "bank_code": "* Código do Convênio no Banco",
            "registration_type": "* Tipo de Inscrição da Empresa",
            "registration_number": "* Número de Inscrição da Empresa",
            "bank_agency": "* Agência Mantenedora da Conta ",
            "bank_agency_digit": "* Dígito Verificador da Agência",
            "bank_account_number": "* Número da Conta Corrente",
            "bank_account_digit": "* Dígito Verificador da Conta",
            "bank_account_agency_digit": "* Dígito Verificador da Ag/Conta",
            "company_name": "* Nome da Empresa",
            "bank_name": "* Nome do Banco",
            "address_location": "Logradouro (Nome da Rua, Av, Pça, Etc)",
            "address_number": "Número (Número do Local)",
            "address_complement": "Complemento (Casa, Apto, Sala, Etc)",
            "address_city": "Nome da Cidade",
            "address_cep": "CEP",
            "address_cep_complement": "Complemento do CEP",
            "address_state": "Sigla do Estado",
        }


class SpreadsheetEmployee(BaseModel):
    name: str
    registration_type = RegistrationType.cpf
    registration_number: str
    bank_code: str
    bank_agency: str
    bank_agency_digit: str
    bank_account_number: str
    bank_account_digit: str
    bank_account_agency_digit: str
    address_location: str
    address_number: str
    address_complement: str
    address_district: str
    address_city: str
    address_state: str
    address_cep_complement: str
    address_cep: str

    class Config(BaseConfig):
        _mapping = {
            "bank_code": "Código do Banco do Favorecido",
            "registration_type": "* Tipo de Inscrição do Favorecido",
            "registration_number": "* Nº de Inscrição do Favorecido",
            "bank_agency": "* Ag. Mantenedora da Cta do Favor.",
            "bank_agency_digit": "* Dígito Verificador da Agência",
            "bank_account_number": "* Número da Conta Corrente",
            "bank_account_digit": "* Dígito Verificador da Conta",
            "bank_account_agency_digit": "* Dígito Verificador da AG/Conta",
            "name": "Nome do Favorecido",
            "address_location": "Logradouro (Nome da Rua, Av, Pça, Etc)",
            "address_number": "Número (Nº do Local)",
            "address_complement": "Complemento (Casa, Apto, Etc)",
            "address_district": "Bairro",
            "address_city": "Nome da Cidade",
            "address_cep": "CEP",
            "address_cep_complement": "Complemento do CEP",
            "address_state": "Sigla do Estado",
        }


class SpreadsheetPayment(BaseModel):
    employee_name: str
    identification_number: str
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
