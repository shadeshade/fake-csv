import csv
from pathlib import Path
from time import time

from faker import Faker

RECORD_COUNT = 10
fake = Faker('ru_RU')
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / 'media'


def create_csv_file():
    with open(UPLOAD_DIR / 'invoices.csv', 'w', newline='') as csvfile:
        fieldnames = ['full_name', 'job', 'email', 'domain_name', 'phone_number', 'company_name', 'text', 'integer',
                      'address', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'full_name': fake.name(),
                    'job': fake.job(),
                    'email': fake.email(),
                    'domain_name': fake.domain_name(),
                    'phone_number': fake.phone_number(),
                    'company_name': fake.company(),
                    'text': fake.paragraph(nb_sentences=5, variable_nb_sentences=False),  # Text (with specified range for a number of sentences)
                    'integer': fake.random_int(min=1, max=9),  # Integer (with specified range)
                    'address': fake.address(),
                    'date': fake.date(),
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))
