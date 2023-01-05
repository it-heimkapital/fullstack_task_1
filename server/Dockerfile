# pull official base image
FROM python:3.11

# set work directory
RUN mkdir -p /usr/server/app
WORKDIR /usr/server/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off

# install system level dependency
RUN apt update && apt install libpq-dev libcairo2 libpango-1.0-0 libpangocairo-1.0-0 poppler-utils gettext --yes

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock /usr/server/app/poetry.lock

COPY pyproject.toml /usr/server/app/pyproject.toml
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# copy project
COPY entrypoint.sh /usr/server/app/
RUN chmod u+x /usr/server/app/entrypoint.sh

COPY . /usr/server/app/

EXPOSE 8005

# run entrypoint.sh
CMD ["/bin/bash", "/usr/server/app/entrypoint.sh"]
