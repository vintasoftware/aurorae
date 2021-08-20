# pylint: disable=unsubscriptable-object
import itertools
from typing import List, Optional

from pydantic import BaseModel, root_validator, validator
from pydantic.fields import PrivateAttr

from aurorae.cnab240.v10_7 import models, types


class Company(BaseModel):
    bank_code: types.BankConventionCode
    registration_type: types.RegistrationType
    registration_number: types.RegistrationNumber
    bank_agency: types.BankAgencyNumber
    bank_agency_digit: Optional[types.BankDigitCheck] = None
    bank_account_number: types.BankAccountNumber
    bank_account_digit: Optional[types.BankDigitCheck] = None
    bank_account_agency_digit: Optional[types.BankDigitCheck] = None
    company_name: types.CompanyName
    bank_name: types.BankName
    address_location: types.AddressName
    address_number: types.AddressNumber
    address_complement: types.AddressDetails
    address_city: types.AddressCityName
    address_cep: types.AddressCEP
    address_cep_complement: types.AddressCEPComplement
    address_state: types.AddressState

    class Config:
        validate_all = True
        validate_assignment = True

    @validator("bank_agency_digit", "bank_account_digit", "bank_account_agency_digit")
    def prevent_none(cls, v):  # noqa
        if v is None:
            return ""

        return v


class Employee(BaseModel):
    bank_code: types.BankCode
    registration_type: types.RegistrationType
    registration_number: types.RegistrationNumber
    bank_agency: types.BankAgencyNumber
    bank_agency_digit: Optional[types.BankDigitCheck] = None
    bank_account_number: types.BankAccountNumber
    bank_account_digit: Optional[types.BankDigitCheck] = None
    bank_account_agency_digit: Optional[types.BankDigitCheck] = None
    name: types.RecipientName
    initiation_form: Optional[types.InitiationForm]

    # Information 10
    address_location: Optional[types.AddressName]
    # OR
    pix_tx_id: Optional[types.PIXTXID]

    # Information 11
    pix_key: Optional[types.PIXKey]
    # OR
    message: Optional[types.Message]
    # OR
    address_number: Optional[types.AddressNumber]
    address_complement: Optional[types.AddressDetails]
    address_district: Optional[types.AddressDistrict]
    address_city: Optional[types.SmallAddressCityName]
    address_cep: Optional[types.AddressCEP]
    address_cep_complement: Optional[types.AddressCEPComplement]
    address_state: Optional[types.AddressState]

    class Config:
        validate_all = True
        validate_assignment = True

    @validator("bank_agency_digit", "bank_account_digit", "bank_account_agency_digit")
    def prevent_none(cls, v):  # noqa
        if v is None:
            return ""

        return v

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
    rebate_amount: types.RebateAmount = 0
    discount_amount: types.DiscountAmount = 0
    arrears_amount: types.ArrearsAmount = 0
    fine_amount: types.FineAmount = 0
    notify_recipient: types.NotifyRecipient = types.NotifyRecipientEnum.no_notification
    registration_type: types.InformationRegistrationType = str(
        types.CNABRegistrationTypeEnum.cpf.value
    )

    class Config:
        validate_all = True
        validate_assignment = True

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
                or "registration_type" in values
            ), (
                "You must include all fields: payment_date, payment_amount, rebate_amount, "
                "discount_amount, arrears_amount, fine_amount, notify_recipient, "
                "registration_type"
            )

        return values


class Payroll(BaseModel):
    company: Company
    employees: List[Employee]
    payments: List[Payment]

    _line_counter: int = PrivateAttr()

    class Config:
        validate_all = True
        validate_assignment = True

    @root_validator
    def check_payments_employees_exist(cls, values):  # noqa
        employees_names = map(
            lambda employee: employee.name, values.get("employees", [])
        )

        for payment in values.get("payments", []):
            assert (
                payment.employee_name in employees_names
            ), f"Employee not found for name: {payment.employee_name.value}"

        return values

    def _get_employee_by_name(self, employee_name):
        for employee in self.employees:
            if employee.name != employee_name:
                continue
            return employee

    def _get_payment_amount_sum(self):
        return sum([payment.payment_amount.value for payment in self.payments])

    def _get_cnab_batch(self):
        batch_header = models.CNABBatchHeader(
            initial_data=self.company.dict(), line_number=next(self._line_counter)
        )

        batch_records = []
        record_counter = 0
        for payment in self.payments:
            payment.company = self.company
            payment.employee = self._get_employee_by_name(payment.employee_name)

            record_counter += 1
            segment_a = models.CNABBatchSegmentA(
                payment=payment,
                record_number=record_counter,
                line_number=next(self._line_counter),
            )

            record_counter += 1
            segment_b = models.CNABBatchSegmentB(
                payment=payment,
                record_number=record_counter,
                line_number=next(self._line_counter),
            )

            batch_records.append(
                models.CNABBatchRecord(segment_a=segment_a, segment_b=segment_b)
            )

        batch_trailer = models.CNABBatchTrailer(
            company=self.company,
            total_batch_lines=record_counter + 2,
            sum_payment_values=self._get_payment_amount_sum(),
            line_number=next(self._line_counter),
        )
        return models.CNABBatch(
            header=batch_header, records=batch_records, trailer=batch_trailer
        )

    def get_cnab_file(self):
        self._line_counter = itertools.count(1)
        batches = []

        file_header = models.CNABHeader(
            initial_data=self.company.dict(), line_number=next(self._line_counter)
        )

        batches.append(self._get_cnab_batch())

        last_line_number = next(self._line_counter)
        file_trailer = models.CNABTrailer(
            company=self.company,
            total_file_lines=last_line_number,
            line_number=last_line_number,
        )

        return models.CNABFile(
            header=file_header, batches=batches, trailer=file_trailer
        )
