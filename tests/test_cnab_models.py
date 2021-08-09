from datetime import datetime

import pytest
from freezegun.api import freeze_time
from pydantic import ValidationError

from cnab.cnab240.v10_7 import lambdas, types
from cnab.cnab240.v10_7.models import (
    CNABBatchHeader,
    CNABBatchSegmentA,
    CNABBatchSegmentB,
    CNABBatchTrailer,
    CNABHeader,
    CNABTrailer,
)
from cnab.payroll.models import Company, Employee, Payment


@freeze_time(datetime(2021, 7, 8, 13, 30, 50))
class TestCNABModels:
    def setup_method(self, __):
        lambdas.COUNT = 0

    def test_header_fixed_width(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }
        header = CNABHeader(header_data, line_number=1)

        expected_header = (
            "07700000         99999999900099977                  00001900000099999999 VINTA "
            "SERVICOS E SOLUCOES TECBANCO INTERMEDIUM                       1080720211330500"
            "0000110301600                                                                     "
        )
        assert header.as_fixed_width() == expected_header

    def test_payroll_to_cnab_header(self):
        company_data = {
            "bank_code": "77",
            "registration_type": "9",
            "registration_number": "99999999000999",
            "bank_agency": "1",
            "bank_agency_digit": "9",
            "bank_account_number": "999999",
            "bank_account_digit": "9",
            "bank_account_agency_digit": "9",
            "company_name": " Vinta Servicos e Solucoes Tec",
            "bank_name": "Banco Intermedium",
            "address_location": "",
            "address_number": 1,
            "address_complement": "",
            "address_city": "",
            "address_cep": 1,
            "address_cep_complement": 1,
            "address_state": "",
        }

        company = Company.parse_obj(company_data)

        expected_header = (
            "07700000         99999999900099977                  00001900000099999999 VINTA "
            "SERVICOS E SOLUCOES TECBANCO INTERMEDIUM                       1080720211330500"
            "0000110301600                                                                     "
        )

        cnab_header = CNABHeader(company.dict(), line_number=1)
        assert cnab_header.as_fixed_width() == expected_header

    def test_header_error_on_field_01_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "7777",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_header_error_on_field_12_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "999999",
            "field_11_0": "9",
            "field_12_0": "999",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_header_error_on_field_10_0_with_size_bigger_than_expected(self):
        header_data = {
            "field_01_0": "77",
            "field_05_0": "9",
            "field_06_0": "99999999000999",
            "field_07_0": "77",
            "field_08_0": "1",
            "field_09_0": "9",
            "field_10_0": "9999998888888",
            "field_11_0": "9",
            "field_12_0": "9",
            "field_13_0": " Vinta Servicos e Solucoes Tec",
            "field_14_0": "Banco Intermedium",
        }

        with pytest.raises(ValidationError):
            CNABHeader(header_data, line_number=1)

    def test_batch_header_fixed_width(self):
        batch_header_data = {
            "field_01_1": "77",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        batch_header = CNABBatchHeader(batch_header_data, line_number=1)
        expected_header = (
            "07700011C3001046 19999999900099977                  00001100000099999911VINTA "
            "SERVICOS E SOLUCOES TEC                                         RUA TEST RUA"
            "                  00123CASA           RECIFE              55999000PE01                "
        )
        assert batch_header.as_fixed_width() == expected_header

    def test_batch_header_fixed_width_with_custom_field_01_1(self):
        batch_header_data = {
            "field_01_1": "1",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        batch_header = CNABBatchHeader(batch_header_data, line_number=1)
        expected_header = (
            "00100011C3001046 19999999900099977                  00001100000099999911VINTA "
            "SERVICOS E SOLUCOES TEC                                         RUA TEST RUA"
            "                  00123CASA           RECIFE              55999000PE01                "
        )
        assert batch_header.as_fixed_width() == expected_header

    def test_batch_header_with_wrong_field_01_1(self):
        batch_header_data = {
            "field_01_1": "1111",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        with pytest.raises(ValidationError):
            CNABBatchHeader(batch_header_data, line_number=1)

    def test_batch_header_with_wrong_field_05_1_enum_value(self):
        batch_header_data = {
            "field_01_1": "1111",
            "field_05_1": "91",
            "field_09_1": "1",
            "field_10_1": "99999999000999",
            "field_11_1": "77",
            "field_12_1": "1",
            "field_13_1": "1",
            "field_14_1": "999999",
            "field_15_1": "1",
            "field_16_1": "1",
            "field_17_1": "Vinta Servicos e Solucoes Tec",
            "field_19_1": "Rua Test Rua",
            "field_20_1": "123",
            "field_21_1": "Casa",
            "field_22_1": "Recife",
            "field_23_1": 55999,
            "field_24_1": 000,
            "field_25_1": "PE",
        }

        with pytest.raises(ValidationError):
            CNABBatchHeader(batch_header_data, line_number=1)

    @pytest.mark.usefixtures("payroll_data")
    def test_segment_a_fixed_width(self, payroll_data):
        company = Company.parse_obj(payroll_data["Company"])
        employee = Employee.parse_obj(payroll_data["Employee"])
        payment = Payment.parse_obj(payroll_data["Payment"])

        payment.employee = employee
        payment.company = company

        segment_a = CNABBatchSegmentA(payment=payment, line_number=1)

        expected_segment_a = (
            "0770001300001A00001807700001900000999999900MARIA FULANA DA SILVA                "
            "             11062021BRL000000000000000000000000001000                    110620"
            "21000000000000000                                        01          0          "
        )
        assert segment_a.as_fixed_width() == expected_segment_a

    @pytest.mark.usefixtures("payroll_data")
    def test_trailer_fixed_width(self, payroll_data):
        company = Company.parse_obj(payroll_data["Company"])
        trailer = CNABTrailer(company=company, line_number=6)

        expected_trailer = expected_trailer = (
            "07799999         000001000006000000                                             "
            "                                                                                "
            "                                                                                "
        )
        assert trailer.as_fixed_width() == expected_trailer

    @pytest.mark.usefixtures("payroll_data")
    def test_trailer_error_on_field_01_9_with_size_bigger_than_expected(
        self, payroll_data
    ):
        company_data = payroll_data["Company"]
        company_data["bank_code"] = "9999"
        company = Company.parse_obj(payroll_data["Company"])

        with pytest.raises(
            ValidationError,
            match=r"(?s).*bank_code.*ensure this value is less than or equal to 999.*",
        ):
            CNABTrailer(company=company, line_number=6)

    @pytest.mark.usefixtures("payroll_data")
    def test_trailer_error_on_field_01_9_with_invalid_number(self, payroll_data):
        company_data = payroll_data["Company"]
        company_data["bank_code"] = "invalid_bank_code"

        with pytest.raises(
            ValidationError, match=r"(?s).*bank_code.*value is not a valid integer.*"
        ):
            Company.parse_obj(payroll_data["Company"])

    @pytest.mark.usefixtures("payroll_data")
    def test_batch_detail_segment_b_as_fixed_width(self, payroll_data):
        employee = Employee.parse_obj(payroll_data["Employee"])
        payment = Payment.parse_obj(payroll_data["Payment"])

        payment.employee = employee

        batch_detail_segment_b_model = CNABBatchSegmentB(
            payment=payment, record_number=2, line_number=4
        )
        expected_line = (
            "0770001300002B05 100099999999999RUA DAS AMELIAS                    001231 ANDAR "
            "       CENTRO         RECIFE         50050000PE110620210000000000010000000000000"
            "000000000000000000000000000000000000000000000000001              000000000000000"
        )

        assert batch_detail_segment_b_model.as_fixed_width() == expected_line
        assert batch_detail_segment_b_model.field_02_3B == types.SequentialServiceBatch(
            __root__=1
        )  # noqa
        assert batch_detail_segment_b_model.field_03_3B == types.EntryType(
            __root__=3
        )  # noqa
        assert (
            batch_detail_segment_b_model.field_05_3B
            == types.DetailRecordSegmentType(__root__="B")
        )  # noqa

    @pytest.mark.usefixtures("payroll_data")
    def test_batch_detail_segment_b_as_fixed_width_with_custom_field_01_3B(
        self, payroll_data
    ):
        employee_data = payroll_data["Employee"]
        employee_data["bank_code"] = "1"
        employee_data["registration_number"] = "99966699900"

        employee = Employee.parse_obj(payroll_data["Employee"])
        payment = Payment.parse_obj(payroll_data["Payment"])

        payment.employee = employee

        batch_detail_segment_b_model = CNABBatchSegmentB(
            payment=payment, record_number=1, line_number=4
        )

        assert batch_detail_segment_b_model.field_01_3B.as_fixed_width() == "001"

    @pytest.mark.usefixtures("payroll_data")
    def test_batch_detail_segment_b_with_wrong_field_01_3B(self, payroll_data):
        employee = Employee.parse_obj(payroll_data["Employee"])
        payment = Payment.parse_obj(payroll_data["Payment"])

        payment.employee = employee

        payment.employee.bank_code = "111111"

        with pytest.raises(ValidationError):
            CNABBatchSegmentB(payment=payment, record_number=1, line_number=4)

    @pytest.mark.usefixtures("payroll_data")
    def test_batch_trailer_fixed_width(self, payroll_data):
        company = Company.parse_obj(payroll_data["Company"])

        batch_trailer = CNABBatchTrailer(
            company=company, sum_payment_values="1000", line_number=5
        )

        expected_batch_trailer = (
            "07700015         000004000000000000001000000000000000000000000000               "
            "                                                                                "
            "                                                                                "
        )
        assert batch_trailer.as_fixed_width() == expected_batch_trailer

    @pytest.mark.usefixtures("payroll_data")
    def test_batch_segment_b_record_number(self, payroll_data):
        employee = Employee.parse_obj(payroll_data["Employee"])
        payment = Payment.parse_obj(payroll_data["Payment"])
        payment.employee = employee

        record_number = 6

        segment = CNABBatchSegmentB(
            payment=payment, record_number=record_number, line_number=4
        )

        assert segment.field_04_3B == types.RecordSequentialNumber.parse_obj(
            record_number
        )
