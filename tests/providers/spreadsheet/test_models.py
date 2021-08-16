import re

import pytest
from pydantic.error_wrappers import ValidationError

from cnab.cnab240.v10_7.types import RegistrationTypeEnum
from providers.spreadsheet.models import (
    Spreadsheet,
    SpreadsheetCompany,
    SpreadsheetEmployee,
    SpreadsheetPayment,
)


class TestModels:
    def test_sending_dict_when_string_is_expected_raises_validation_error(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\nCEP\n  "
                + "str type expected (type=type_error.str)"
            ),
        ):
            SpreadsheetCompany(
                company_name="Company Level",
                registration_type=RegistrationTypeEnum.cnpj,
                registration_number="111",
                bank_name="Company Bank",
                bank_code="222",
                bank_agency="333",
                bank_agency_digit="4",
                bank_account_number="555",
                bank_account_digit="6",
                bank_account_agency_digit="46",
                address_location="Company Address",
                address_number="77",
                address_complement="",
                address_cep={
                    "number": "88888",
                },
                address_cep_complement="888",
                address_city="Company City",
                address_state="PE",
            )

    def test_not_sending_required_field_raises_validation_error(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\n* Nome do Banco\n  "
                + "field required (type=value_error.missing)"
            ),
        ):
            SpreadsheetCompany(
                company_name="Company Level",
                registration_type=RegistrationTypeEnum.cnpj,
                registration_number="111",
                bank_code="222",
                bank_agency="333",
                bank_agency_digit="4",
                bank_account_number="555",
                bank_account_digit="6",
                bank_account_agency_digit="46",
                address_location="Company Address",
                address_number="77",
                address_complement="",
                address_cep_complement="888",
                address_cep="88888",
                address_city="Company City",
                address_state="PE",
            )

    def test_sending_none_on_required_field_raises_validation_error(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\n* Nome do Banco\n  "
                + "none is not an allowed value (type=type_error.none.not_allowed)"
            ),
        ):
            SpreadsheetCompany(
                company_name="Company Level",
                registration_type=RegistrationTypeEnum.cnpj,
                registration_number="111",
                bank_name=None,
                bank_code="222",
                bank_agency="333",
                bank_agency_digit="4",
                bank_account_number="555",
                bank_account_digit="6",
                bank_account_agency_digit="46",
                address_location="Company Address",
                address_number="77",
                address_complement="",
                address_cep_complement="888",
                address_cep="88888",
                address_city="Company City",
                address_state="PE",
            )

    def test_sending_invalid_date_format_raises_validation_error(self):
        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetPayment\nData do Pagamento -> __root__\n  "
                + "{value} is not valid (type=value_error)"
            ),
        ):
            SpreadsheetPayment(
                employee_name="Employee Name",
                identification_number="1",
                payment_amount="100000",
                payment_date="20210727",
            )

    def test_registration_type_default_value(self):
        company = SpreadsheetCompany(
            company_name="Company Level",
            registration_number="111",
            bank_name="Company Bank",
            bank_code="222",
            bank_agency="333",
            bank_agency_digit="4",
            bank_account_number="555",
            bank_account_digit="6",
            bank_account_agency_digit="46",
            address_location="Company Address",
            address_number="77",
            address_complement="",
            address_cep="88888",
            address_cep_complement="888",
            address_city="Company City",
            address_state="PE",
        )

        assert company.registration_type == RegistrationTypeEnum.cnpj

    def test_multiple_payments_for_one_employee(self):
        company = SpreadsheetCompany(
            company_name="Company Level",
            registration_type=RegistrationTypeEnum.cnpj,
            registration_number="111",
            bank_name="Company Bank",
            bank_code="222",
            bank_agency="333",
            bank_agency_digit="4",
            bank_account_number="555",
            bank_account_digit="6",
            bank_account_agency_digit="46",
            address_location="Company Address",
            address_number="77",
            address_complement="",
            address_cep="88888",
            address_cep_complement="888",
            address_city="Company City",
            address_state="PE",
        )

        employee = SpreadsheetEmployee(
            name="Employee Name",
            registration_type=RegistrationTypeEnum.cpf,
            registration_number="000",
            bank_code="111",
            bank_agency="222",
            bank_agency_digit="3",
            bank_account_number="444",
            bank_account_digit="5",
            bank_account_agency_digit="35",
            address_location="Employee Address",
            address_number="66",
            address_complement="",
            address_district="Employee Neighbourhood",
            address_cep="77777",
            address_cep_complement="777",
            address_city="Employee City",
            address_state="PE",
        )

        payment_1 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="1",
            payment_amount="100000",
            payment_date="27072021",
        )
        payment_2 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="2",
            payment_amount="100000",
            payment_date="27072021",
        )
        payment_3 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="3",
            payment_amount="100000",
            payment_date="27072021",
        )

        spreadsheet = Spreadsheet(
            company=company,
            employees=[employee],
            payments=[payment_1, payment_2, payment_3],
        )

        assert spreadsheet.payments[0].employee_name == spreadsheet.employees[0].name
        assert spreadsheet.payments[1].employee_name == spreadsheet.employees[0].name
        assert spreadsheet.payments[2].employee_name == spreadsheet.employees[0].name

    def test_multiple_payments_for_multiple_employees(self):
        company = SpreadsheetCompany(
            company_name="Company Level",
            registration_type=RegistrationTypeEnum.cnpj,
            registration_number="111",
            bank_name="Company Bank",
            bank_code="222",
            bank_agency="333",
            bank_agency_digit="4",
            bank_account_number="555",
            bank_account_digit="6",
            bank_account_agency_digit="46",
            address_location="Company Address",
            address_number="77",
            address_complement="",
            address_cep="88888",
            address_cep_complement="888",
            address_city="Company City",
            address_state="PE",
        )

        employee_1 = SpreadsheetEmployee(
            name="Employee 1",
            registration_type=RegistrationTypeEnum.cpf,
            registration_number="000",
            bank_code="111",
            bank_agency="222",
            bank_agency_digit="3",
            bank_account_number="444",
            bank_account_digit="5",
            bank_account_agency_digit="35",
            address_location="Employee 1 Address",
            address_number="66",
            address_complement="",
            address_district="Employee 1 Neighbourhood",
            address_cep="77777",
            address_cep_complement="777",
            address_city="Employee 1 City",
            address_state="PE",
        )
        employee_2 = SpreadsheetEmployee(
            name="Employee 2",
            registration_type=RegistrationTypeEnum.cpf,
            registration_number="777",
            bank_code="666",
            bank_agency="555",
            bank_agency_digit="4",
            bank_account_number="333",
            bank_account_digit="2",
            bank_account_agency_digit="24",
            address_location="Employee 2 Address",
            address_number="11",
            address_complement="",
            address_district="Employee 2 Neighbourhood",
            address_cep="00000",
            address_cep_complement="000",
            address_city="Employee 2 City",
            address_state="PE",
        )
        employee_3 = SpreadsheetEmployee(
            name="Employee 3",
            registration_type=RegistrationTypeEnum.cpf,
            registration_number="888",
            bank_code="999",
            bank_agency="101",
            bank_agency_digit="1",
            bank_account_number="121",
            bank_account_digit="1",
            bank_account_agency_digit="14",
            address_location="Employee 3 Address",
            address_number="15",
            address_complement="",
            address_district="Employee 3 Neighbourhood",
            address_cep="16161",
            address_cep_complement="161",
            address_city="Employee 3 City",
            address_state="PE",
        )

        payment_1 = SpreadsheetPayment(
            employee_name="Employee 1",
            identification_number="1",
            payment_amount="100000",
            payment_date="27072021",
        )
        payment_2 = SpreadsheetPayment(
            employee_name="Employee 2",
            identification_number="2",
            payment_amount="100000",
            payment_date="27072021",
        )
        payment_3 = SpreadsheetPayment(
            employee_name="Employee 3",
            identification_number="3",
            payment_amount="100000",
            payment_date="27072021",
        )

        spreadsheet = Spreadsheet(
            company=company,
            employees=[employee_1, employee_2, employee_3],
            payments=[payment_1, payment_2, payment_3],
        )

        assert spreadsheet.payments[0].employee_name == spreadsheet.employees[0].name
        assert spreadsheet.payments[1].employee_name == spreadsheet.employees[1].name
        assert spreadsheet.payments[2].employee_name == spreadsheet.employees[2].name
