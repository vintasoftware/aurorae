header = [2, 3, 4, 15,16,17,18,19,20,21,22,23,24]
lote_header = [2,3,4,5,6,7,8,26,27,28]
lote_detalhe_segmento_a = [2,3,4,5,6,7,18,22,23,24,25,26,27,28,29,30]
lote_detalhe_segmento_b = [2,3,4,5,12]
lote_detalhe_segmento_c = [2,3,4,5,6,19]
lote_trailer = [2,3,4,5,6,7,8,9,10]
trailer = [2,3,4,5,6,7,8]

segments = [header, lote_header, lote_detalhe_segmento_a, lote_detalhe_segmento_b, lote_detalhe_segmento_c, lote_trailer, trailer]
names = ["header", "lote_header", "lote_detalhe_segmento_a", "lote_detalhe_segmento_b", "lote_detalhe_segmento_c", "lote_trailer", "trailer"]
suffix = ['_0', '_1', '_3A', '_3B', '_3C', '_5', '_9']

output_dict = {}
missing_fields = []
for i, seg in enumerate(segments):
    output_dict[names[i]] = {}
    for j in seg:
        leading_zero = str(j).zfill(2)
        name = f"field_{leading_zero}{suffix[i]}"
        output_dict[names[i]][name] = {}