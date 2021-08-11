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
    address_cep: str
    address_cep_complement: str
    address_city: str
    address_state: str


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
    address_cep: str
    address_cep_complement: str
    address_city: str
    address_state: str


class SpreadsheetPayment(BaseModel):
    employee_name: str
    identification_number: str
    payment_amount: str
    payment_date: CNABDate


class Spreadsheet(BaseModel):
    company: SpreadsheetCompany
    employees: List[SpreadsheetEmployee]
    payments: List[SpreadsheetPayment]
