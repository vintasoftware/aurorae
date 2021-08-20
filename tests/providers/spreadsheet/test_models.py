import re

import pytest
from pydantic.error_wrappers import ValidationError

from aurorae.cnab240.v10_7.types import RegistrationType, RegistrationTypeEnum
from aurorae.providers.spreadsheet.models import (
    Spreadsheet,
    SpreadsheetCompany,
    SpreadsheetEmployee,
    SpreadsheetPayment,
)


@pytest.mark.usefixtures("spreadsheet_data")
class TestModels:
    def test_sending_dict_when_string_is_expected_raises_validation_error(
        self, spreadsheet_data
    ):
        company_data = spreadsheet_data["Empresa"]
        company_data["CEP"] = {
            "number": "88888",
        }

        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\nCEP\n  "
                + "str type expected (type=type_error.str)"
            ),
        ):
            SpreadsheetCompany(**company_data)

    def test_not_sending_required_field_raises_validation_error(self, spreadsheet_data):
        company_data = spreadsheet_data["Empresa"]
        del company_data["* Nome do Banco"]

        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\n* Nome do Banco\n  "
                + "field required (type=value_error.missing)"
            ),
        ):
            SpreadsheetCompany(**company_data)

    def test_sending_none_on_required_field_raises_validation_error(
        self, spreadsheet_data
    ):
        company_data = spreadsheet_data["Empresa"]
        company_data["* Nome do Banco"] = None

        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetCompany\n* Nome do Banco\n  "
                + "none is not an allowed value (type=type_error.none.not_allowed)"
            ),
        ):
            SpreadsheetCompany(**company_data)

    def test_sending_invalid_date_format_raises_validation_error(
        self, spreadsheet_data
    ):

        payment_data = spreadsheet_data["Pagamentos"][0]
        payment_data["Data do Pagamento"] = "20210727"

        with pytest.raises(
            ValidationError,
            match=re.escape(
                "1 validation error for SpreadsheetPayment\nData do Pagamento -> __root__\n  "
                + "{value} is not valid (type=value_error)"
            ),
        ):
            SpreadsheetPayment(**payment_data)

    def test_registration_type_default_value(self, spreadsheet_data):
        company_data = spreadsheet_data["Empresa"]

        company = SpreadsheetCompany(**company_data)

        assert company.registration_type == RegistrationType(
            __root__=RegistrationTypeEnum.cnpj
        )

    def test_multiple_payments_for_one_employee(self, spreadsheet_data):
        company_data = spreadsheet_data["Empresa"]
        company = SpreadsheetCompany(**company_data)

        employee_data = spreadsheet_data["Funcionários"][0]
        employee_data["Nome do Favorecido"] = "Employee Name"
        employee = SpreadsheetEmployee(**employee_data)

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

    def test_multiple_payments_for_multiple_employees(self, spreadsheet_data):
        company_data = spreadsheet_data["Empresa"]
        company = SpreadsheetCompany(**company_data)

        employees_data = spreadsheet_data["Funcionários"]

        employees_data[0]["Nome do Favorecido"] = "Employee 1"
        employee_1 = SpreadsheetEmployee(**employees_data[0])

        employees_data[1]["Nome do Favorecido"] = "Employee 2"
        employee_2 = SpreadsheetEmployee(**employees_data[1])

        employees_data[2]["Nome do Favorecido"] = "Employee 3"
        employee_3 = SpreadsheetEmployee(**employees_data[2])

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
