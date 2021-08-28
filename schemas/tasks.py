import csv
import os

import requests
from django.conf import settings
from faker import Faker

from config.celery import app
from schemas.models import Job
from . import choices

from filestack import Client

client = Client(os.getenv('FILESTACK_API_KEY'))
fake = Faker()

# generate fake data
FAKE_ROWS = {
    'full_name': fake.name,
    'job': fake.job,
    'email': fake.email,
    'domain_name': fake.domain_name,
    'phone_number': fake.phone_number,
    'company_name': fake.company,
    'text': fake.paragraph,  # provide args to set range for a number of
    # sentences: ( nb_sentences: int, variable_nb_sentences: bool)
    'integer': fake.random_int,  # provide args to set specified range: (min: int, max: int)
    'address': fake.address,
    'date': fake.date
}


def get_fake_data_dict(column_dict: dict):  # return dict with a fake row
    fake_dict = {}

    for value in column_dict.values():
        column_type = value['type']
        column_name = value['name']
        if column_type == 'text':
            fake_dict[column_name] = FAKE_ROWS[column_type](
                nb_sentences=value['args']['quantity'],
                variable_nb_sentences=False
            )
        elif column_type == 'integer':
            fake_dict[column_name] = FAKE_ROWS[column_type](
                min=value['args']['range_from'],
                max=value['args']['range_to']
            )
        else:
            fake_dict[column_name] = FAKE_ROWS[column_type]()

    return fake_dict


def get_csv_file_name(job_id: int):
    return f'fake-schema-{job_id}.csv'


def get_csv_url(file):
    headers = {'Content-Type': 'text/csv'}
    data = open(file, 'rb')
    response = requests.post(
        "https://www.filestackapi.com/api/store/S3?key=AF461if9MSSm6DxNwihfZz",
        headers=headers,
        data=data
    )
    response = response.content.decode().split('"')[3]
    return response


@app.task
def create_csv_file(job_id: int):
    job = Job.objects.get(id=job_id)
    file_name = get_csv_file_name(job_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    column_dict = job.payload["column_dict"]
    record_count = job.payload["record_count"]
    column_separator = job.payload["column_separator"]
    string_character = job.payload["string_character"]

    try:
        with open(file_path, 'w', newline='') as csvfile:
            column_names = [value['name'] for value in column_dict.values()]
            writer = csv.DictWriter(
                csvfile,
                fieldnames=column_names,
                delimiter=column_separator,
                quotechar=string_character,
                quoting=csv.QUOTE_ALL
            )
            writer.writeheader()
            for i in range(record_count):
                fake_row_dict = get_fake_data_dict(column_dict)
                writer.writerow(
                    fake_row_dict
                )

            new_filelink = get_csv_url(csvfile)

    except Exception as error:
        job.status = choices.ERROR
        job.error = str(error)
        raise
    else:
        job.url = new_filelink
        job.status = choices.READY
    finally:
        job.save()



