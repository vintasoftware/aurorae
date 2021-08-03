from typing import List, Optional

from pydantic import BaseModel

from cnab.cnab240.v10_7 import types


class Company(BaseModel):
    bank_code: types.BankConventionCode
    registration_type: types.RegistrationType
    registration_number: types.RegistrationNumber
    bank_agency: types.BankAgencyNumber
    bank_agency_digit: types.BankAgencyDigitCheck
    bank_account_number: types.BankAccountNumber
    bank_account_digit: types.BankAccountDigitCheck
    bank_account_agency_digit: types.BankAgencyAccountDigitCheck
    company_name: types.CompanyName
    bank_name: types.BankName
    address_location: types.NameAddress
    address_number: types.AddressNumber
    address_complement: types.AddressDetails
    address_city: types.AddressCityName
    address_cep: types.AddressCEP
    address_cep_complement: types.AddressCEPComplement
    address_state: types.AddressState


class Employee(BaseModel):
    bank_code: types.BankCode
    registration_type: types.RegistrationType
    registration_number: types.RegistrationNumber
    bank_agency: types.BankAgencyNumber
    bank_agency_digit: types.BankAgencyDigitCheck
    bank_account_number: types.BankAccountNumber
    bank_account_digit: types.BankAccountDigitCheck
    bank_account_agency_digit: types.BankAgencyAccountDigitCheck
    name: types.RecipientName
    initiation_form: Optional[types.InitiationForm]

    # Information 10
    address_location: Optional[types.Information35]
    # OR
    pix_tx_id: Optional[types.Information35]

    # Information 11
    pix_key: Optional[types.Information99]
    # OR
    message: Optional[types.Information99]
    # OR
    address_number: types.AddressNumber
    address_complement: types.AddressDetails
    address_district: types.AddressDistrict
    address_city: types.SmallAddressCityName
    address_cep: types.AddressCEP
    address_cep_complement: types.AddressCEPComplement
    address_state: types.AddressState


class Payment(BaseModel):
    employee: Optional[Employee]
    company: Optional[Company]
    employee_name: types.PersonName
    payment_amount: types.PaymentAmount
    payment_date: types.CNABDate
    release_method: Optional[types.ReleaseMethod]
    payment_method: Optional[types.PaymentMethod]
    ted_finality_code: Optional[types.TEDFinalityCode]
    doc_service_type: Optional[types.ServiceTypeComplement]

    # Information 12 Employee.pix_key OR
    # payment_date
    # payment_amount
    # and the following fields
    rebate_amount: Optional[types.RebateAmount]
    discount_amount: Optional[types.DiscountAmount]
    arrears_amount: Optional[types.ArrearsAmount]
    fine_amount: Optional[types.FineAmount]
    notify_recipient: Optional[types.NotifyRecipient]
    registration_number: Optional[types.RecipientRegistrationNumberInformation12]


class Payroll(BaseModel):
    company: Company
    employees: List[Employee]
    payments: List[Payment]
