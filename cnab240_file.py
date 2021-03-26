from pprint import pprint

from cnab240.v10_7 import models


class Lote:
    header = models.LoteHeader
    trailer = models.LoteTrailer
    segmento_a = models.LoteDetalheSegmentoA
    segmento_b = models.LoteDetalheSegmentoB
    segmento_c = models.LoteDetalheSegmentoC

    def __init__(self, initial_data):
        self.initial_data = initial_data

    def formatted_data(self):
        header = self.header(self.initial_data["lote_header"])
        segmento_a = self.segmento_a(self.initial_data["lote_detalhe_segmento_a"])
        segmento_b = self.segmento_a(self.initial_data["lote_detalhe_segmento_b"])
        segmento_c = self.segmento_a(self.initial_data["lote_detalhe_segmento_c"])
        trailer = self.header(self.initial_data["lote_trailer"])


class CNAB240_File():
    def __init__(self, initial_data):
        self.header = models.HeaderLine(initial_data["header"])
        self.trailer = models.TrailerLine(initial_data["trailer"])

    def generate_file(self):
        with open("testing_cnab240.txt", "w") as f:
            f.write(f"{self.header.formatted_data()}\n")
            f.write(f"{self.trailer.formatted_data()}\n")


if __name__ == "__main__":
    import data_handler
    spreadsheet_data = data_handler.get_spreadsheet_data()
    fields_initial_data = data_handler.get_initial_data(spreadsheet_data)

    # pprint(fields_initial_data)

    cnab = CNAB240_File(fields_initial_data)
    cnab.generate_file()
