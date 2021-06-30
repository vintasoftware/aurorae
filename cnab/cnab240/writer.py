import itertools
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
        lote_children = []
        line_count = itertools.count(1)

        self.header = models.HeaderLine(
            initial_data["header"][0], line_number=next(line_count)
        )

        lote_header = models.LoteHeader(
            initial_data["lote_header"][0], line_number=next(line_count)
        )
        for data_segmento_a, data_segmento_b in zip(
            initial_data["lote_detalhe_segmento_a"],
            initial_data["lote_detalhe_segmento_b"],
        ):
            segmento_a = models.LoteDetalheSegmentoA(
                data_segmento_a, line_number=next(line_count)
            )
            segmento_b = models.LoteDetalheSegmentoB(
                data_segmento_b, line_number=next(line_count)
            )
            lote_children.append(models.LoteChildren(segmento_a, segmento_b))

        lote_trailer = models.LoteTrailer(
            initial_data["lote_trailer"][0], line_number=next(line_count)
        )
        self.lote = models.Lote(
            header=lote_header, children=lote_children, trailer=lote_trailer
        )

        self.trailer = models.TrailerLine(
            initial_data["trailer"][0], line_number=next(line_count)
        )

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


class LoteChildren:
    def __init__(self, segmento_a, segmento_b, segmento_c=None):
        self.segmento_a = segmento_a
        self.segmento_b = segmento_b
        self.segmento_c = segmento_c

    def lines_count(self):
        return 3 if self.segmento_c else 2


class Lote:
    def __init__(self, header, trailer, children):
        self.header = header
        self.trailer = trailer
        self.children = children or []

    def formatted_data(self):
        lote_content = []
        lote_content = f"{self.header.formatted_data()}\n"

        for child in self.children:
            lote_content = f"{lote_content}{child.segmento_a.formatted_data()}\n"
            lote_content = f"{lote_content}{child.segmento_b.formatted_data()}\n"

        lote_content = f"{lote_content}{self.trailer.formatted_data()}\n"
        return lote_content

    def formatted_html(self):
        lote_content = []
        lote_content = f"{self.header.formatted_html()}\n"

        for child in self.children:
            lote_content = f"{lote_content}{child.segmento_a.formatted_html()}\n"
            lote_content = f"{lote_content}{child.segmento_b.formatted_html()}\n"

        lote_content = f"{lote_content}{self.trailer.formatted_html()}\n"
        return lote_content

    def lines_count(self):
        counter = 0
        for child in self.children:
            counter += child.lines_count
        return counter


if __name__ == "__main__":
    from spreadsheet_handler import generate_initial_data_with_connectors

    fields_initial_data = generate_initial_data_with_connectors()
    cnab = CNAB240File(fields_initial_data)
    cnab.generate_file()
    cnab.generate_html_file()
