import collections

from .tasks import create_csv_file

from .models import Job, Schema


def get_column_dict(schema: Schema):  # return an ordered dict with columns' info
    columns_dict = {}

    columns = schema.columns.all()
    for column in columns:
        columns_dict[column.order] = {
            'name': column.name,
            'type': column.type,
            'args': {
                'range_from': column.range_from,
                'range_to': column.range_to,
                'quantity': column.quantity
            }
        }

    ordered_columns_dict = collections.OrderedDict(sorted(columns_dict.items()))

    return ordered_columns_dict


def start_job(schema_id: int, rows_count: str):
    schema = Schema.objects.get(id=schema_id)
    payload = dict(
        record_count=int(rows_count),
        column_dict=get_column_dict(schema),
        schema_id=schema_id,
        column_separator=schema.column_separator,
        string_character=schema.string_character
    )
    job = Job.objects.create(payload=payload)
    create_csv_file.delay(job_id=job.id)


def parse_column_form_data(data):
    """fix forms' numeration, num of total and initial forms to pass validation"""
    parsed_data = {}

    name_num = 0
    type_num = 0
    range_from_num = 0
    range_to_num = 0
    quantity_num = 0
    order_num = 0
    id_num = 0

    for key in data.keys():
        if key.endswith('-name'):
            parsed_data[f'form-{name_num}-name'] = data[key]
            name_num += 1
        elif key.endswith('-type'):
            parsed_data[f'form-{type_num}-type'] = data[key]
            type_num += 1
        elif key.endswith('-range_from'):
            parsed_data[f'form-{range_from_num}-range_from'] = data[key]
            range_from_num += 1
        elif key.endswith('-range_to'):
            parsed_data[f'form-{range_to_num}-range_to'] = data[key]
            range_to_num += 1
        elif key.endswith('-quantity'):
            parsed_data[f'form-{quantity_num}-quantity'] = data[key]
            quantity_num += 1
        elif key.endswith('-order'):
            parsed_data[f'form-{order_num}-order'] = data[key]
            order_num += 1
        elif key.endswith('-id'):
            parsed_data[f'form-{id_num}-id'] = data[key]
            id_num += 1
        else:
            parsed_data[key] = data[key]

        parsed_data['form-TOTAL_FORMS'] = id_num
        parsed_data['form-INITIAL_FORMS'] = 0

    return parsed_data
