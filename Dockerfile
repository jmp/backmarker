FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip && \
    apt-get update && \
    apt-get install -y curl netcat build-essential libpq-dev && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && \
    rm -rf /var/lib/apt/lists/*
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app
COPY . .
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

ENTRYPOINT ["/app/docker-entrypoint.sh"]
