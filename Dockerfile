FROM python:3.8-buster

WORKDIR /usr/src/app

RUN pip install -U pip

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry install --no-interaction --no-ansi
RUN python manage.py collectstatic --noinput

#COPY ./entrypoint.sh .
#RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

COPY . .