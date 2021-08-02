# pylint: disable=global-statement
import datetime


def get_field_P001():
    """
    '018' = TED (STR,CIP)
    '700' = DOC (COMPE)
    “988”- TED (STR/CIP) – Used when it's necessary to send TED using the ISPB code
    of the Recipient Financial Institution. In this case, it's mandatory to fill
    the field "ISPB Code" - field 26.3B, of the Payment Segment, as described in Note P015.
    “009” – PIX (SPI)
    """
    return "018"


def get_field_G016():
    """File creation date"""
    return datetime.datetime.now().strftime("%d%m%Y")


def get_field_G017():
    """File creation time"""
    return datetime.datetime.now().strftime("%H%M%S")


def get_field_G018():
    """File sequential number"""
    return "1"


def get_field_G019():
    """
    Code adopted by FEBRABAN to identify which is the received file
    layout version. The first 2 digits refer to the version, and the last
    digit for the release.
    """
    return "103"


def get_field_G015():
    return "1"


def get_field_G020():
    return "01600"


def get_field_G025():
    return "30"  # Salary Payment


def get_field_G100():
    """
    “01” – Pix Key – Phone type
    “02” – Pix Key – Email type
    “03” – Pix Key – CPF/CNPJ type
    “04” – Random Key
    “05” – Bank Data
    """
    return "05"


def get_field_P005():
    """
    '01' = Account Credit
    '02' = Payment of Rent/Condominium
    '03' = Payment of Duplicate/Securities
    '04' = Payment of Dividends
    '05' = Payment of School Tuition
    '06' = Salary Payment
    '07' = Payment to Suppliers
    '08' = Transactions of Foreign Exchange/Funds/Stock Exchange
    '09' = Transfer of Collection/Payment of Taxes
    '10' = International Transfer in Real
    '11' = DOC for Savings
    '12' = DOC for Judicial Deposit
    '13' = Others
    ‘16’ = Stipend Payment
    ‘17’ = Remuneration to the Member
    ‘18’ = Pagamento of Fees
    ‘19’ = Payment of Prebends (Remuneração to priests)
    """
    return "01"  # Salary Payment


def get_field_G029():
    return "01"  # Credit to Current Account/Salary


def get_field_P014():
    return "01"  # Debit at Current Account


def get_field_G060():
    return "0"  # Indicates INCLUSION


def get_field_G061():
    return "00"  # Inclusion of Released Detail Record


def get_field_P011():
    return ""


def get_field_G040():
    """
    "BTN" = National Treasury Bonus + TR
    "BRL" = Real
    "USD" = US Dollar
    "PTE" = Portuguese Shield
    "FRF" = French Franc
    "CHF" = Swiss Franc
    "JPY" = Japanese Yen
    "IGP" = General Price Index
    "IGM" = General Market Price Index
    "GBP" = Pound Sterling
    "ITL" = Italian Lira
    "DEM" = German Mark
    "TRD" = Daily Referential Rate
    "UPC" = Standard Capital Unit
    "UPF" = Standard Financing Unit
    "UFR" = Tax Reference Unit
    "XEU" = European Currency
    """
    return "BRL"


def get_field_G002():
    return "0001"


def get_field_G002_v2():
    return 1


COUNT = 0


def get_field_G038():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def get_field_G056():
    """
    Sum of record types.
    In our case, number of batch records + batch header + batch trailer + header + trailer
    Number of lines in the file
    """
    return str(COUNT + 2 + 2)


def get_field_G049():
    """
    The number of batches in a file. This number is
    defaulted as for now we only support one batch per file.
    """
    return "1"


def get_field_G057():
    """
    Sum of record types.
    In our case, number of batch records + batch header + batch trailer
    """
    return str(COUNT + 2)


def get_field_P007(spreadsheet_data):
    somatorio = 0
    for data_pagamento in spreadsheet_data["lote_detalhe_segmento_a"]:
        str_pagamento = str(data_pagamento["field_20_3A"])
        somatorio += int(str_pagamento)
    return str(somatorio)


def get_codigo_finalidade_complementar():
    pass


def get_field_G005():
    """
    '0' = Exempt / Not Informed
    '1' = CPF
    '2' = CGC / CNPJ
    '3' = PIS / PASEP
    '9' = Others
    """
    return "1"
