FROM python:3.10-bullseye AS development

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    cmake

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH $PATH:/root/.local/bin/

WORKDIR /app/src

CMD poetry install && poetry run python crawl-tweet.py
