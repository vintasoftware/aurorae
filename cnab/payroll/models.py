from typing import List, Optional

from pydantic import BaseModel, root_validator

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
    address_number: Optional[types.AddressNumber]
    address_complement: Optional[types.AddressDetails]
    address_district: Optional[types.AddressDistrict]
    address_city: Optional[types.SmallAddressCityName]
    address_cep: Optional[types.AddressCEP]
    address_cep_complement: Optional[types.AddressCEPComplement]
    address_state: Optional[types.AddressState]

    @classmethod
    def has_all_address_fields(cls, values):  # noqa
        return (
            "address_number" in values
            and "address_complement" in values
            and "address_district" in values
            and "address_city" in values
            and "address_cep" in values
            and "address_cep_complement" in values
            and "address_state" in values
        )

    @classmethod
    def has_all_bank_info(cls, values):  # noqa
        return (
            "bank_code" in values
            and "bank_agency" in values
            and "bank_agency_digit" in values
            and "bank_account_number" in values
            and "bank_account_digit" in values
            and "bank_account_agency_digit" in values
        )

    @root_validator(pre=True)
    def check_information_10(cls, values):  # noqa
        """
        Field defined in CNAB document that requires information from multiple fields <field_09_3B>
        """
        assert (
            "address_location" in values or "pix_tx_id" in values
        ), "You must include the address_location or pix_tx_id"
        return values

    @root_validator(pre=True)
    def check_information_11(cls, values):  # noqa
        """
        Field defined in CNAB document that requires information from multiple fields <field_10_3B>
        """
        assert (
            "pix_key" in values
            or "message" in values
            or cls.has_all_address_fields(values)
        ), "You must include the pix_key or message or all address information"
        return values

    @root_validator(pre=True)
    def check_pix_info(cls, values):  # noqa
        if "pix_tx_id" in values:
            assert (
                "pix_tx_id" in values and "pix_key" in values
            ), "You must include all pix info, please add pix_key and pix_tx_id"

        return values

    @root_validator(pre=True)
    def check_address_fields(cls, values):  # noqa
        if "pix_tx_id" not in values and "pix_key" not in values:
            assert "address_location" in values and (
                cls.has_all_address_fields(values)
            ), "You must include all address information"

        return values

    @root_validator(pre=True)
    def check_initiation_form(cls, values):  # noqa
        if "initiation_form" not in values:
            values["initiation_form"] = types.InitiationFormEnum.bank_info

        init_form = values["initiation_form"]
        is_pix = types.InitiationFormEnum.bank_info != init_form
        if is_pix:
            has_pix_info = "pix_tx_id" in values and "pix_key" in values
            assert (
                is_pix and has_pix_info
            ), "Initiation form set to pix, please fill the pix information: pix_tx_id and pix_key"
            return values

        has_bank_info = cls.has_all_bank_info(values)
        assert has_bank_info, (
            "Initiation form set to bank, please fill the information: bank_code, bank_agency, "
            "bank_agency_digit, bank_account_number, bank_account_digit, bank_account_agency_digit"
        )
        return values


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

    @root_validator(pre=True)
    def check_information_12(cls, values):  # noqa
        """
        Field defined in CNAB document that requires information from multiple fields <field_11_3B>
        """
        if "rebate_amount" in values:
            assert (
                "payment_date" in values
                or "payment_amount" in values
                or "rebate_amount" in values
                or "discount_amount" in values
                or "arrears_amount" in values
                or "fine_amount" in values
                or "notify_recipient" in values
                or "registration_number" in values
            ), (
                "You must include all fields: payment_date, payment_amount, rebate_amount, "
                "discount_amount, arrears_amount, fine_amount, notify_recipient, "
                "registration_number"
            )

        return values


class Payroll(BaseModel):
    company: Company
    employees: List[Employee]
    payments: List[Payment]
