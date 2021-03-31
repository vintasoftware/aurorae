from cnab240.v10_7 import models


class CNAB240File:
    def __init__(self, initial_data):
        self.header = models.HeaderLine(initial_data["header"])
        self.lote = Lote(initial_data)
        self.trailer = models.TrailerLine(initial_data["trailer"])

    def generate_file(self):
        with open("testing_cnab240.txt", "w") as f:
            f.write(f"{self.header.formatted_data()}")
            f.write(f"{self.lote.formatted_data()}")
            f.write(f"{self.trailer.formatted_data()}")


class Lote:
    header = models.LoteHeader
    segmento_a = models.LoteDetalheSegmentoA
    segmento_b = models.LoteDetalheSegmentoB
    segmento_c = models.LoteDetalheSegmentoC
    trailer = models.LoteTrailer

    def __init__(self, initial_data):
        self.initial_data = initial_data

    def formatted_data(self):
        header = self.header(self.initial_data["lote_header"])
        lote_content = f"{header.formatted_data()}"

        segmento_a = self.segmento_a(self.initial_data["lote_detalhe_segmento_a"])
        lote_content = f"{lote_content}{segmento_a.formatted_data()}"

        segmento_b = self.segmento_b(self.initial_data["lote_detalhe_segmento_b"])
        lote_content = f"{lote_content}{segmento_b.formatted_data()}"

        segmento_c = self.segmento_c(self.initial_data["lote_detalhe_segmento_c"])
        lote_content = f"{lote_content}{segmento_c.formatted_data()}"

        trailer = self.header(self.initial_data["lote_trailer"])
        lote_content = f"{lote_content}{trailer.formatted_data()}"

        return lote_content


if __name__ == "__main__":
    import spreadsheet_handler
    spreadsheet_data = spreadsheet_handler.get_spreadsheet_data()
    fields_initial_data = spreadsheet_handler.get_initial_data(spreadsheet_data)

    cnab = CNAB240File(fields_initial_data)
    cnab.generate_file()
