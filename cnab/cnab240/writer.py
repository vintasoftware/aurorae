from datetime import datetime

from cnab.cnab240.v10_7 import models


class CNAB240File:
    default_folder = "generated_files"
    default_name = "cnab240"

    def __init__(self, initial_data):
        assert len(initial_data["header"]) == 1
        assert len(initial_data["trailer"]) == 1
        assert (
            len(initial_data["lote_detalhe_segmento_c"])
            == len(initial_data["lote_detalhe_segmento_b"])
            == len(initial_data["lote_detalhe_segmento_a"])
        )

        self.header = models.HeaderLine(initial_data["header"][0])
        self.lote = Lote(initial_data)
        self.trailer = models.TrailerLine(initial_data["trailer"][0])

    def generate_file(self):
        created_at = datetime.now().isoformat()
        file_path = f"{self.default_folder}/{self.default_name}-{created_at}.txt"

        with open(file_path, "w") as f:
            f.write(f"{self.header.formatted_data()}\n")
            f.write(f"{self.lote.formatted_data()}")
            f.write(f"{self.trailer.formatted_data()}")

    def generate_html_file(self):
        created_at = datetime.now().isoformat()
        file_path = f"{self.default_folder}/{self.default_name}-{created_at}.html"
        with open(file_path, "w") as f:
            f.write("<html><head>")
            f.write("<link href='../staticfiles/styles.css' rel='stylesheet'>")
            f.write("</head><body>")
            f.write(f"{self.header.formatted_html()}\n")
            f.write(f"{self.lote.formatted_html()}")
            f.write(f"{self.trailer.formatted_html()}")
            f.write("</body></html>")


class Lote:
    header = models.LoteHeader
    segmento_a = models.LoteDetalheSegmentoA
    segmento_b = models.LoteDetalheSegmentoB
    segmento_c = models.LoteDetalheSegmentoC
    trailer = models.LoteTrailer

    def __init__(self, initial_data):
        self.initial_data = initial_data

    def formatted_data(self):
        header = self.header(self.initial_data["lote_header"][0])
        lote_content = f"{header.formatted_data()}\n"

        for i, _ in enumerate(self.initial_data["lote_detalhe_segmento_a"]):
            segmento_a = self.segmento_a(
                self.initial_data["lote_detalhe_segmento_a"][i]
            )
            lote_content = f"{lote_content}{segmento_a.formatted_data()}\n"

            segmento_b = self.segmento_b(
                self.initial_data["lote_detalhe_segmento_b"][i]
            )
            lote_content = f"{lote_content}{segmento_b.formatted_data()}\n"

        trailer = self.trailer(self.initial_data["lote_trailer"][0])
        lote_content = f"{lote_content}{trailer.formatted_data()}\n"

        return lote_content

    def formatted_html(self):
        header = self.header(self.initial_data["lote_header"][0])
        lote_content = f"{header.formatted_html()}\n"

        for i, _ in enumerate(self.initial_data["lote_detalhe_segmento_a"]):
            segmento_a = self.segmento_a(
                self.initial_data["lote_detalhe_segmento_a"][i]
            )
            lote_content = f"{lote_content}{segmento_a.formatted_html()}\n"

            segmento_b = self.segmento_b(
                self.initial_data["lote_detalhe_segmento_b"][i]
            )
            lote_content = f"{lote_content}{segmento_b.formatted_html()}\n"

        trailer = self.trailer(self.initial_data["lote_trailer"][0])
        lote_content = f"{lote_content}{trailer.formatted_html()}\n"
        return lote_content


if __name__ == "__main__":
    from spreadsheet_handler import generate_initial_data_with_connectors

    fields_initial_data = generate_initial_data_with_connectors()
    cnab = CNAB240File(fields_initial_data)
    cnab.generate_file()
    cnab.generate_html_file()
