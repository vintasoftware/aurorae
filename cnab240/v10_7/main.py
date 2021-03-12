import models

for seg in segments
    for key in keys:
        
        if MODELS_SPREADSHEET_MAP.get(seq)
            get_from_spreadsheet

header_data = {
    "field_01_0": "123"
    "field_02_0": "1111"
    "field_03_0": "1"
    "field_05_0": "1"
    "field_06_0": "12332112332112"
    "field_07_0": "3211233211233123123"
    "field_08_0": "12313"
    "field_09_0": "2"
    "field_10_0": "12312313123"
    "field_11_0": "2"
    "field_12_0": "3"
    "field_13_0": "Vinta"
    "field_14_0": "Itaú"
    "field_16_0": "1"
    "field_17_0": "10012021"
    "field_18_0": "102030"
    "field_19_0": "1"
    "field_20_0": "323"
    "field_21_0": "12331"
}

with open("generated_files/test_1.txt", 'w') as f:
    header = models.HeaderLine(initial_data=header_data)
    f.write(header.to_cnab240_representation())
    f.write('\n')

    for i in person:
        lote_header = models.LoteHeader(initial_data=lote_data)
        f.write(lote_header.to_cnab240_representation())
        f.write('\n')

        lote_seg_a = models.LoteDetalheSegmentoA(initial_data=segmento_a_data)
        f.write(lote_seg_a.to_cnab240_representation())
        f.write('\n')

        lote_seg_b = models.LoteDetalheSegmentoB(initial_data=segmento_b_data)
        f.write(lote_seg_b.to_cnab240_representation())
        f.write('\n')

        lote_seg_c = models.LoteDetalheSegmentoC(initial_data=segmento_c_data)
        f.write(lote_seg_c.to_cnab240_representation())
        f.write('\n')

        lote_trailer = models.LoteTrailer(initial_data=lote_trailer_data)
        f.write(lote_trailer.to_cnab240_representation())
        f.write('\n')

    trailer = models.TrailerLine(initial_data=trailer_data)
    f.write(trailer.to_cnab240_representation())
    f.write('\n')
