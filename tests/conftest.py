from datetime import datetime

import pytest
from freezegun.api import freeze_time

from providers.legacy_spreadsheet.handler import LegacySpreadsheetHandler


@pytest.fixture
def spreadsheet_data():
    return {
        "Empresa": [
            {
                "* Nome da Empresa": " Random Company",
                "* Tipo de Inscrição da Empresa": "2",
                "* Número de Inscrição da Empresa": "00000000000000",
                "* Nome do Banco": "Banco",
                "* Código do Convênio no Banco": "77",
                "* Agência Mantenedora da Conta ": "1",
                "* Dígito Verificador da Agência": "0",
                "* Número da Conta Corrente": "888888",
                "* Dígito Verificador da Conta": "1",
                "* Dígito Verificador da Ag/Conta": "1",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Endereco da Rua",
                "Número (Número do Local)": "0000",
                "Complemento (Casa, Apto, Sala, Etc)": "detalhes",
                "Nome da Cidade": "Recife",
                "Complemento do CEP": "000",
                "Sigla do Estado": "PE",
                "CEP": "00000",
            }
        ],
        "Funcionários": [
            {
                "Nome do Favorecido": "Nome da Fulana Silva",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "99988877700",
                "* Forma de Iniciação": "05",
                "* Código da Câmara Centralizadora": "000",
                "Código do Banco do Favorecido": "00",
                "* Ag. Mantenedora da Cta do Favor.": "0000",
                "* Dígito Verificador da Agência": "0",
                "* Número da Conta Corrente": "0000000",
                "* Dígito Verificador da Conta": "0",
                "* Dígito Verificador da AG/Conta": "0",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Rua da Aleatoriedade ",
                "Número (Nº do Local)": "000",
                "Complemento (Casa, Apto, Etc)": "Casa",
                "Bairro": "Bairro",
                "Nome da Cidade": "Cidade",
                "Sigla do Estado": "PE",
                "CEP": "00000",
                "Complemento do CEP": "000",
            },
            {
                "Nome do Favorecido": "Outro da Fulana Silva",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "99988877700",
                "* Forma de Iniciação": "05",
                "* Código da Câmara Centralizadora": "000",
                "Código do Banco do Favorecido": "00",
                "* Ag. Mantenedora da Cta do Favor.": "0000",
                "* Dígito Verificador da Agência": "0",
                "* Número da Conta Corrente": "1111111",
                "* Dígito Verificador da Conta": "0",
                "* Dígito Verificador da AG/Conta": "0",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Rua da Aleatoriedade ",
                "Número (Nº do Local)": "000",
                "Complemento (Casa, Apto, Etc)": "Casa",
                "Bairro": "Bairro",
                "Nome da Cidade": "Cidade",
                "Sigla do Estado": "PE",
                "CEP": "00000",
                "Complemento do CEP": "000",
            },
        ],
        "Pagamentos": [
            {
                "Funcionário": "Nome da Fulana Silva",
                "Nº do Docum. Atribuído p/ Empresa": None,
                "* Nº do Docum. Atribuído pelo Banco": "1",
                "* Tipo da Moeda": "R$",
                "Quantidade da Moeda": "0",
                "Valor do Pagamento": "1000",
                "Data do Pagamento": "11062021",
                "Valor Real da Efetivação do Pagto": "1",
                "Data Real da Efetivação Pagto": "11062021",
                "Data do Vencimento (Nominal)": "11062021",
                "Valor do Documento (Nominal)": "1",
                "Valor do Abatimento": "0",
                "Valor do Desconto": "0",
                "Valor da Mora": "0",
                "Valor da Multa": "0",
                "Código/Documento do Favorecido": "1",
                "Valor do IR": "0",
                "Valor do ISS": "0",
                "Valor do IOF": "0",
                "Valor Outras Deduções": "0",
                "Valor Outros Acréscimos": "0",
                "Agência do Favorecido": "0000",
                "Dígito Verificador da Agência": "0",
                "Número Conta Corrente": "0000000",
                "Dígito Verificador da Conta": "0",
                "Dígito Verificador Agência/Conta": "0",
                "Valor do INSS": "0",
                "Código ISPB": "0",
                "Número Conta Pagamento Creditada": "0000000",
                "Aviso ao Favorecido": "0",
            },
            {
                "Funcionário": "Outro da Fulana Silva",
                "Nº do Docum. Atribuído p/ Empresa": None,
                "* Nº do Docum. Atribuído pelo Banco": "1",
                "* Tipo da Moeda": "R$",
                "Quantidade da Moeda": "0",
                "Valor do Pagamento": "1000",
                "Data do Pagamento": "11062021",
                "Valor Real da Efetivação do Pagto": "1",
                "Data Real da Efetivação Pagto": "11062021",
                "Data do Vencimento (Nominal)": "11062021",
                "Valor do Documento (Nominal)": "1",
                "Valor do Abatimento": "0",
                "Valor do Desconto": "0",
                "Valor da Mora": "0",
                "Valor da Multa": "0",
                "Código/Documento do Favorecido": "1",
                "Valor do IR": "0",
                "Valor do ISS": "0",
                "Valor do IOF": "0",
                "Valor Outras Deduções": "0",
                "Valor Outros Acréscimos": "0",
                "Agência do Favorecido": "0000",
                "Dígito Verificador da Agência": "0",
                "Número Conta Corrente": "0000000",
                "Dígito Verificador da Conta": "0",
                "Dígito Verificador Agência/Conta": "0",
                "Valor do INSS": "0",
                "Código ISPB": "0",
                "Número Conta Pagamento Creditada": "0000000",
                "Aviso ao Favorecido": "0",
            },
        ],
    }


@pytest.fixture()
@freeze_time(datetime(2021, 7, 8, 13, 30, 50))
def legacy_spreadsheet_handler():
    return LegacySpreadsheetHandler(
        input_filename="./tests/fixtures/test_legacy_spreadsheet.xlsx"
    )


@pytest.fixture
def payroll_data():
    return {
        "company": {
            "bank_code": "77",
            "registration_type": "CGC/CNPJ",
            "registration_number": "99999999000999",
            "bank_agency": "77",
            "bank_agency_digit": "1",
            "bank_account_number": "999999",
            "bank_account_digit": "1",
            "bank_account_agency_digit": "1",
            "company_name": "Vinta Servicos e Solucoes Tec",
            "bank_name": "Banco",
            "address_location": "Rua Test Rua",
            "address_number": "123",
            "address_complement": "Casa",
            "address_city": "Recife",
            "address_cep": 55999,
            "address_cep_complement": 000,
            "address_state": "PE",
        },
        "employees": [
            {
                "name": "Maria Fulana da Silva",
                "registration_number": "99999999999",
                "registration_type": "CPF",
                "bank_code": "77",
                "bank_agency": "0001",
                "bank_agency_digit": "9",
                "bank_account_number": "9999999",
                "bank_account_digit": "0",
                "bank_account_agency_digit": "0",
                "address_location": "Rua das Amelias",
                "address_number": "123",
                "address_complement": "1 andar",
                "address_district": "Centro",
                "address_city": "Recife",
                "address_state": "PE",
                "address_cep": "50050",
                "address_cep_complement": "000",
            }
        ],
        "payments": [
            {
                "employee_name": "Maria Fulana da Silva",
                "payment_amount": "1000",
                "payment_date": "11062021",
                "rebate_amount": "0",
                "discount_amount": "0",
                "arrears_amount": "0",
                "fine_amount": "0",
                "notify_recipient": "0",
                "registration_number": "1",
            }
        ],
    }
