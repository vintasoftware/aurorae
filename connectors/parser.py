import copy


def get_fields_from_lote():
    from cnab.cnab240.v10_7 import models

    return (
        dir(models.LoteHeader)
        + dir(models.LoteDetalheSegmentoA)
        + dir(models.LoteDetalheSegmentoB)
        + dir(models.LoteDetalheSegmentoC)
        + dir(models.LoteTrailer)
    )


def format_field_info(field_name: str, field_value: str, amount_of_payments: int):
    has_multiple_entries = field_name in get_fields_from_lote()

    if has_multiple_entries:
        if len(field_value) == 1:
            # This happens when the field has one correspondence on the origin file AND repeats for all lines
            # a good example is the field field_01_3A
            data_cp = [{field_name: field_value} for _ in range(amount_of_payments)]
        else:
            data_cp = [{field_name: value} for value in field_value]
    else:
        data_cp = [{field_name: field_value}]

    return data_cp


def fill_segment_data(
    data: dict, segment_name: str, segment_value: dict, amount_of_payments: int
):
    data_cp = copy.deepcopy(data)
    if not data_cp.get(segment_name):
        data_cp[segment_name] = [{} for _ in range(amount_of_payments)]

    for item_to_add, line_detail in zip(segment_value, data_cp[segment_name]):
        field_key = list(item_to_add.keys())[0]
        field_value = list(item_to_add.values())[0]

        if not line_detail.get(field_key):
            line_detail[field_key] = (
                field_value[0] if isinstance(field_value, list) else field_value
            )
        else:
            if isinstance(field_value, list):
                line_detail[field_key].update({field_key: field_value[0]})
            else:
                line_detail[field_key].update({field_key: field_value})
    return data_cp


def get_field_values_based_on(
    field_name: str,
    origin_spreadsheet_name: str,
    sheet_rows: dict,
    amount_of_payments: int,
):
    invalid_field_maps = []
    is_composed_field = isinstance(origin_spreadsheet_name, list)

    lines = []
    for row in sheet_rows:
        try:
            if is_composed_field:
                # Multiple fields mapped as one column
                composed_fields = {}
                composed_fields_definition = origin_spreadsheet_name
                for composed_field_def in composed_fields_definition:
                    composed_column_name = composed_field_def["name"]
                    try:
                        composed_fields[composed_column_name] = row[
                            composed_column_name
                        ]
                    except KeyError:
                        error_msg = (
                            f"The column '{composed_column_name}' doesn't "
                            f"exists on the '{origin_spreadsheet_name}' sheet."
                        )
                        invalid_field_maps.append({field_name: error_msg})
                lines.append(composed_fields)
            else:
                data = row[origin_spreadsheet_name]
                lines.append(data)
        except KeyError:
            error_msg = (
                f"The column '{origin_spreadsheet_name}' doesn't "
                f"exists on the '{origin_spreadsheet_name}' sheet."
            )
            invalid_field_maps.append({field_name: error_msg})

    initial_data = format_field_info(
        field_name=field_name, field_value=lines, amount_of_payments=amount_of_payments
    )
    return initial_data, invalid_field_maps
