import pytest
from pydantic.error_wrappers import ValidationError

from providers.spreadsheet.models import (
    SpreadsheetCompany,
    SpreadsheetEmployee,
    SpreadsheetPayment,
    RegistrationType,
    Spreadsheet,
)


class TestModels:
    def test_sending_dict_when_string_is_expected_raises_validation_error(self):
        with pytest.raises(ValidationError):
            # Zip code is defined as string in the model
            SpreadsheetCompany(
                name="Company Level",
                registration_type=RegistrationType.cnpj,
                registration_number="111",
                bank_name="Company Bank",
                bank_convention_code="222",
                bank_agency_number="333",
                bank_agency_check_digit="4",
                bank_account_number="555",
                bank_account_check_digit="6",
                bank_agency_account_check_digit="46",
                address="Company Address",
                address_number="77",
                address_complement="",
                city="Company City",
                zip_code_complement="888",
                state="PE",
                zip_code={
                    "number": "88888",
                },
            )

    def test_not_sending_required_field_raises_validation_error(self):
        with pytest.raises(ValidationError):
            # Not sending bank related fields
            SpreadsheetCompany(
                name="Company Level",
                registration_type=RegistrationType.cnpj,
                registration_number="111",
                address="Company Address",
                address_number="77",
                address_complement="",
                city="Company City",
                zip_code_complement="888",
                state="PE",
                zip_code="88888",
            )

    def test_sending_invalid_date_format_raises_validation_error(self):
        with pytest.raises(ValidationError):
            SpreadsheetPayment(
                employee_name="Employee Name",
                identification_number="1",
                value="100000",
                date="20210727",
            )

    def test_default_value_to_field(self):
        company = SpreadsheetCompany(
            name="Company Level",
            registration_number="111",
            bank_name="Company Bank",
            bank_convention_code="222",
            bank_agency_number="333",
            bank_agency_check_digit="4",
            bank_account_number="555",
            bank_account_check_digit="6",
            bank_agency_account_check_digit="46",
            address="Company Address",
            address_number="77",
            address_complement="",
            city="Company City",
            zip_code_complement="888",
            state="PE",
            zip_code="88888",
        )

        assert company.registration_type == RegistrationType.cnpj

    def test_multiple_payments_for_one_employee(self):
        company = SpreadsheetCompany(
            name="Company Level",
            registration_type=RegistrationType.cnpj,
            registration_number="111",
            bank_name="Company Bank",
            bank_convention_code="222",
            bank_agency_number="333",
            bank_agency_check_digit="4",
            bank_account_number="555",
            bank_account_check_digit="6",
            bank_agency_account_check_digit="46",
            address="Company Address",
            address_number="77",
            address_complement="",
            city="Company City",
            zip_code_complement="888",
            state="PE",
            zip_code="88888",
        )

        employee = SpreadsheetEmployee(
            name="Employee Name",
            registration_type=RegistrationType.cpf,
            registration_number="000",
            bank_code="111",
            bank_agency="222",
            bank_agency_check_digit="3",
            bank_account_number="444",
            bank_account_check_digit="5",
            bank_agency_account_check_digit="35",
            address="Employee Address",
            address_number="66",
            address_complement="",
            neighbourhood="Employee Neighbourhood",
            city="Employee City",
            state="PE",
            zip_code_complement="777",
            zip_code="77777",
        )

        payment_1 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="1",
            value="100000",
            date="27072021",
        )
        payment_2 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="2",
            value="100000",
            date="27072021",
        )
        payment_3 = SpreadsheetPayment(
            employee_name="Employee Name",
            identification_number="3",
            value="100000",
            date="27072021",
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
            name="Company Level",
            registration_type=RegistrationType.cnpj,
            registration_number="111",
            bank_name="Company Bank",
            bank_convention_code="222",
            bank_agency_number="333",
            bank_agency_check_digit="4",
            bank_account_number="555",
            bank_account_check_digit="6",
            bank_agency_account_check_digit="46",
            address="Company Address",
            address_number="77",
            address_complement="",
            city="Company City",
            zip_code_complement="888",
            state="PE",
            zip_code="88888",
        )

        employee_1 = SpreadsheetEmployee(
            name="Employee 1",
            registration_type=RegistrationType.cpf,
            registration_number="000",
            bank_code="111",
            bank_agency="222",
            bank_agency_check_digit="3",
            bank_account_number="444",
            bank_account_check_digit="5",
            bank_agency_account_check_digit="35",
            address="Employee 1 Address",
            address_number="66",
            address_complement="",
            neighbourhood="Employee 1 Neighbourhood",
            city="Employee 1 City",
            state="PE",
            zip_code_complement="777",
            zip_code="77777",
        )
        employee_2 = SpreadsheetEmployee(
            name="Employee 2",
            registration_type=RegistrationType.cpf,
            registration_number="777",
            bank_code="666",
            bank_agency="555",
            bank_agency_check_digit="4",
            bank_account_number="333",
            bank_account_check_digit="2",
            bank_agency_account_check_digit="24",
            address="Employee 2 Address",
            address_number="11",
            address_complement="",
            neighbourhood="Employee 2 Neighbourhood",
            city="Employee 2 City",
            state="PE",
            zip_code_complement="000",
            zip_code="00000",
        )
        employee_3 = SpreadsheetEmployee(
            name="Employee 3",
            registration_type=RegistrationType.cpf,
            registration_number="888",
            bank_code="999",
            bank_agency="101",
            bank_agency_check_digit="1",
            bank_account_number="121",
            bank_account_check_digit="1",
            bank_agency_account_check_digit="14",
            address="Employee 3 Address",
            address_number="15",
            address_complement="",
            neighbourhood="Employee 3 Neighbourhood",
            city="Employee 3 City",
            state="PE",
            zip_code_complement="161",
            zip_code="16161",
        )

        payment_1 = SpreadsheetPayment(
            employee_name="Employee 1",
            identification_number="1",
            value="100000",
            date="27072021",
        )
        payment_2 = SpreadsheetPayment(
            employee_name="Employee 2",
            identification_number="2",
            value="100000",
            date="27072021",
        )
        payment_3 = SpreadsheetPayment(
            employee_name="Employee 3",
            identification_number="3",
            value="100000",
            date="27072021",
        )

        spreadsheet = Spreadsheet(
            company=company,
            employees=[employee_1, employee_2, employee_3],
            payments=[payment_1, payment_2, payment_3],
        )

        assert spreadsheet.payments[0].employee_name == spreadsheet.employees[0].name
        assert spreadsheet.payments[1].employee_name == spreadsheet.employees[1].name
        assert spreadsheet.payments[2].employee_name == spreadsheet.employees[2].name
