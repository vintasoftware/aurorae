import itertools
from datetime import datetime

from cnab.cnab240.v10_7 import models
from connectors.legacy_spreadsheet.spreadsheet_handler import (
    generate_initial_data_with_connectors,
)
from connectors.utils import parse_args


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


def generate_cnab_files():
    args = parse_args()

    fields_initial_data = generate_initial_data_with_connectors(filename=args.filename)
    cnab = CNAB240File(fields_initial_data)
    cnab.generate_file()
    cnab.generate_html_file()
