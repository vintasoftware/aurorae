import copy


def get_fields_from_lote():
    from cnab240.v10_7 import models

    return (
        dir(models.LoteHeader)
        + dir(models.LoteDetalheSegmentoA)
        + dir(models.LoteDetalheSegmentoB)
        + dir(models.LoteDetalheSegmentoC)
        + dir(models.LoteTrailer)
    )


def fill_data(data: dict, field_name: str, field_value: str):
    data_cp = copy.deepcopy(data)
    has_multiple_entries = field_name in get_fields_from_lote()

    if not data_cp.get(field_name) and has_multiple_entries:
        data_cp[field_name] = []
    elif not data_cp.get(field_name) and not has_multiple_entries:
        data_cp[field_name] = None

    if has_multiple_entries:
        last_item = data_cp[field_name][-1] if len(data_cp[field_name]) > 0 else {}
        if last_item and field_name in last_item.keys():
            data_cp.append({field_name: field_value})
        else:
            last_item.update({field_name: field_value})
    else:
        data_cp.update({field_name: field_value})

    return data_cp

