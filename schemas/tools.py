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
