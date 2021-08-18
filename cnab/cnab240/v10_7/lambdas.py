import datetime


def get_field_G016():
    """File creation date"""
    return datetime.datetime.now().strftime("%d%m%Y")


def get_field_G017():
    """File creation time"""
    return datetime.datetime.now().strftime("%H%M%S")


def get_field_G018():
    """File sequential number"""
    return "1"


def get_field_G002_for_bacth_payment():
    """
    Lote de Serviço
    Número seqüencial para identificar univocamente um lote de serviço. Criado e controlado
    pelo responsável pela geração magnética dos dados contidos no arquivo.

    Preencher com '0001' para o primeiro lote do arquivo. Para os demais: número do lote
    anterior acrescido de 1. O número não poderá ser repetido dentro do arquivo.
    """
    return "0001"


def get_field_G002_sequential():
    """
    Lote de Serviço
    Número seqüencial para identificar univocamente um lote de serviço. Criado e controlado
    pelo responsável pela geração magnética dos dados contidos no arquivo.

    Preencher com '0001' para o primeiro lote do arquivo. Para os demais: número do lote
    anterior acrescido de 1. O número não poderá ser repetido dentro do arquivo.
    """
    return 1


def get_field_G049():
    """
    The number of batches in a file. This number is
    defaulted as for now we only support one batch per file.
    """
    return "1"
