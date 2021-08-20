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


def get_field_G002_sequential():
    """
    Sequential number to uniquely identify a service batch. Created and controlled
    by the person responsible for the magnetic generation of the data contained in the file.

    Fill in with '0001' for the first batch of the file. For others: batch number
    previous plus 1. The number cannot be repeated within the file.
    """
    return 1


def get_field_G049():
    """
    The number of batches in a file. This number is
    defaulted as for now we only support one batch per file.
    """
    return "1"
