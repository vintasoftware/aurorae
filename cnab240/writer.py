import sys

sys.path.append("/home/sarai/Documents/vinta/vinta-pagamentos")


from v10_7 import models


class CNAB240File:
    def __init__(self, initial_data):
        assert len(initial_data["header"]) == 1
        assert len(initial_data["trailer"]) == 1
        assert len(initial_data["lote_detalhe_segmento_c"]) == len(
            initial_data["lote_detalhe_segmento_b"]) == len(initial_data["lote_detalhe_segmento_a"])

        self.header = models.HeaderLine(initial_data["header"][0])
        self.lote = Lote(initial_data)
        self.trailer = models.TrailerLine(initial_data["trailer"][0])

    def generate_file(self):
        with open("testing_cnab240_v3.txt", "w") as f:
            f.write(f"{self.header.formatted_data()}\n")
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
        lote_content = []
        header = self.header(self.initial_data["lote_header"][0])
        lote_content = f"{header.formatted_data()}\n"

        for i, _ in enumerate(self.initial_data["lote_detalhe_segmento_a"]):
            segmento_a = self.segmento_a(self.initial_data["lote_detalhe_segmento_a"][i])
            lote_content = f"{lote_content}{segmento_a.formatted_data()}\n"

            segmento_b = self.segmento_b(
                self.initial_data["lote_detalhe_segmento_b"][i])
            lote_content = f"{lote_content}{segmento_b.formatted_data()}\n"

            # segmento_c = self.segmento_c(
            #     self.initial_data["lote_detalhe_segmento_c"][i])
            # lote_content = f"{lote_content}{segmento_c.formatted_data()}\n"

        trailer = self.trailer(self.initial_data["lote_trailer"][0])
        lote_content = f"{lote_content}{trailer.formatted_data()}\n"

        return lote_content


if __name__ == "__main__":
    from spreadsheet_handler import generate_initial_data

    fields_initial_data = generate_initial_data()
    cnab = CNAB240File(fields_initial_data)
    cnab.generate_file()
