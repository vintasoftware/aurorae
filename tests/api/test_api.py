import pytest
from fastapi.testclient import TestClient

from providers.api.main import app


client = TestClient(app)


@pytest.mark.usefixtures("spreadsheet_data")
class TestAPI:
    def test_api_response_with_valid_payload(self, spreadsheet_data):
        response = client.post("/parse_from_spreadsheet_data", json=spreadsheet_data)
        assert response.status_code == 200

    def test_api_response_for_missing_company(self, spreadsheet_data):
        del spreadsheet_data["Empresa"]

        response = client.post("/parse_from_spreadsheet_data", json=spreadsheet_data)
        assert response.status_code == 422

    def test_api_response_for_missing_employee(self, spreadsheet_data):
        del spreadsheet_data["Funcionários"]

        response = client.post("/parse_from_spreadsheet_data", json=spreadsheet_data)
        assert response.status_code == 422

    def test_api_response_for_missing_payment(self, spreadsheet_data):
        del spreadsheet_data["Pagamentos"]

        response = client.post("/parse_from_spreadsheet_data", json=spreadsheet_data)
        assert response.status_code == 422
