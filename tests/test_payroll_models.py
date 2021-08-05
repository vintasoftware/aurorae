import pytest
from pydantic import ValidationError

from cnab.payroll import models


def test_creates_company_raises_validation_error_on_empty_dict():
    company_data = {}

    with pytest.raises(ValidationError):
        models.Company(**company_data)


def test_creates_company():
    company_data = {
        "bank_code": "77",
        "registration_type": 2,
        "registration_number": "99999999999999",
        "bank_agency": "0235",
        "bank_agency_digit": "0",
        "bank_account_number": "1356",
        "bank_account_digit": "1",
        "bank_account_agency_digit": "0",
        "company_name": "Just Another Company",
        "bank_name": "A Bank",
        "address_location": "Rua Test",
        "address_number": "123",
        "address_complement": "Av.",
        "address_city": "Recife",
        "address_cep": "55565",
        "address_cep_complement": "565",
        "address_state": "PE",
    }
    assert models.Company(**company_data)


def test_creates_employee_raises_validation_error_on_empty_dict():
    employee_data = {}
    with pytest.raises(ValidationError):
        models.Employee(**employee_data)


def test_creates_employee_raises_required_fields_validations():
    employee_data = {
        "bank_code": "77",
        "registration_type": 1,
        "registration_number": "66600066600",
        "bank_agency": "1",
        "bank_agency_digit": "9",
        "bank_account_number": "1234",
        "bank_account_digit": "8",
        "bank_account_agency_digit": "0",
        "name": "Name",
    }

    with pytest.raises(
        ValidationError, match=r"You must include the address_location or pix_tx_id"
    ):
        models.Employee(**employee_data)

    employee_data["pix_tx_id"] = "102"
    with pytest.raises(
        ValidationError,
        match=r"You must include the pix_key or message or all address information",
    ):
        models.Employee(**employee_data)

    del employee_data["pix_tx_id"]
    employee_data["address_location"] = "Rua"
    with pytest.raises(
        ValidationError,
        match=r"You must include the pix_key or message or all address information",
    ):
        models.Employee(**employee_data)


def test_creates_employee():
    employee_data = {
        "bank_code": "77",
        "registration_type": 1,
        "registration_number": "66600066600",
        "bank_agency": "1",
        "bank_agency_digit": "9",
        "bank_account_number": "1234",
        "bank_account_digit": "8",
        "bank_account_agency_digit": "0",
        "name": "Name",
    }
    employee_data["pix_tx_id"] = "102"
    employee_data["pix_key"] = "102"
    models.Employee(**employee_data)

    del employee_data["pix_tx_id"]
    del employee_data["pix_key"]
    employee_data["address_district"] = "Bairro"
    employee_data["address_location"] = "Rua"
    employee_data["address_number"] = "123"
    employee_data["address_complement"] = "Av."
    employee_data["address_city"] = "Recife"
    employee_data["address_cep"] = "55565"
    employee_data["address_cep_complement"] = "565"
    employee_data["address_state"] = "PE"
    models.Employee(**employee_data)


def test_creates_payment_raises_validation_error_on_empty_dict():
    payment_data = {}

    with pytest.raises(ValidationError):
        models.Payment(**payment_data)


def test_creates_payment():
    payment_data = {
        "employee_name": "Linux Swift",
        "payment_amount": "120.00",
        "payment_date": "03082021",
    }

    models.Payment(**payment_data)


def test_creates_payment_with_optional_fields():
    payment_data = {
        "employee_name": "Linux Swift",
        "payment_amount": "120.00",
        "payment_date": "03082021",
        "rebate_amount": "1",
        "discount_amount": "1",
        "arrears_amount": "1",
        "fine_amount": "1",
        "registration_number": "99900099900",
    }
    models.Payment(**payment_data)
