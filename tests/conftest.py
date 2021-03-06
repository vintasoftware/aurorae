import pytest


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


@pytest.fixture
def spreadsheet_data():
    return {
        "Empresa": {
            "* Nome da Empresa": "Random Company",
            "* Tipo de Inscrição da Empresa": "CGC/CNPJ",
            "* Número de Inscrição da Empresa": "11111111111111",
            "* Nome do Banco": "Banco",
            "* Código do Convênio no Banco": "77",
            "* Agência Mantenedora da Conta ": "1",
            "* Dígito Verificador da Agência": "0",
            "* Número da Conta Corrente": "888888",
            "* Dígito Verificador da Conta": "1",
            "* Dígito Verificador da Ag/Conta": "1",
            "Logradouro (Nome da Rua, Av, Pça, Etc)": "Endereco da Rua",
            "Número (Número do Local)": "0001",
            "Complemento (Casa, Apto, Sala, Etc)": "detalhes",
            "Nome da Cidade": "Recife",
            "CEP": "00000",
            "Complemento do CEP": "000",
            "Sigla do Estado": "PE",
        },
        "Funcionários": [
            {
                "Nome do Favorecido": "Maria Fulana da Silva",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "99999999999",
                "Código do Banco do Favorecido": "77",
                "* Ag. Mantenedora da Cta do Favor.": "0001",
                "* Dígito Verificador da Agência": "9",
                "* Número da Conta Corrente": "9999991",
                "* Dígito Verificador da Conta": "0",
                "* Dígito Verificador da AG/Conta": "0",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Rua das Amelias",
                "Número (Nº do Local)": "123",
                "Complemento (Casa, Apto, Etc)": "1 andar",
                "Bairro": "Centro",
                "Nome da Cidade": "Recife",
                "CEP": "50050",
                "Complemento do CEP": "000",
                "Sigla do Estado": "PE",
            },
            {
                "Nome do Favorecido": "Outro da Fulana da Silva",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "99999999992",
                "Código do Banco do Favorecido": "77",
                "* Ag. Mantenedora da Cta do Favor.": "0001",
                "* Dígito Verificador da Agência": "9",
                "* Número da Conta Corrente": "9999992",
                "* Dígito Verificador da Conta": "0",
                "* Dígito Verificador da AG/Conta": "0",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Rua das Amelias",
                "Número (Nº do Local)": "123",
                "Complemento (Casa, Apto, Etc)": "2 andar",
                "Bairro": "Centro",
                "Nome da Cidade": "Recife",
                "CEP": "50050",
                "Complemento do CEP": "000",
                "Sigla do Estado": "PE",
            },
            {
                "Nome do Favorecido": "Sicrano da Silva",
                "* Tipo de Inscrição do Favorecido": "CPF",
                "* Nº de Inscrição do Favorecido": "99999999993",
                "Código do Banco do Favorecido": "77",
                "* Ag. Mantenedora da Cta do Favor.": "0001",
                "* Dígito Verificador da Agência": "9",
                "* Número da Conta Corrente": "9999993",
                "* Dígito Verificador da Conta": "0",
                "* Dígito Verificador da AG/Conta": "0",
                "Logradouro (Nome da Rua, Av, Pça, Etc)": "Rua das Amelias",
                "Número (Nº do Local)": "123",
                "Complemento (Casa, Apto, Etc)": "3 andar",
                "Bairro": "Centro",
                "Nome da Cidade": "Recife",
                "CEP": "50050",
                "Complemento do CEP": "000",
                "Sigla do Estado": "PE",
            },
        ],
        "Pagamentos": [
            {
                "Funcionário": "Outro da Fulana da Silva",
                "Valor do Pagamento": "1000",
                "Data do Pagamento": "11062021",
            },
        ],
    }
