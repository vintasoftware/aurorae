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


class Company(BaseModel):
    name: str
    registration_type = RegistrationType.cnpj
    registration_number: str
    bank_name: str
    bank_convention_code: str
    bank_agency_number: str
    bank_agency_check_digit: str
    bank_account_number: str
    bank_account_check_digit: str
    bank_agency_account_check_digit: str
    address_location: str
    address_number: str
    address_complement: str
    city: str
    zip_code_complement: str
    state: str
    zip_code: str


class Employee(BaseModel):
    name: str
    registration_type = RegistrationType.cpf
    registration_number: str
    bank_code: str
    bank_agency: str
    bank_agency_check_digit: str
    bank_account_number: str
    bank_account_check_digit: str
    bank_agency_account_check_digit: str
    address_location: str
    address_number: str
    address_complement: str
    neighbourhood: str
    city: str
    state: str
    zip_code_complement: str
    zip_code: str


class Payment(BaseModel):
    employee_name: str
    identification_number: str
    value: str
    date: CNABDate


class SpreadSheet(BaseModel):
    company: Company
    employees: List[Employee]
    payments: List[Payment]
