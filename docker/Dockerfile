FROM python:3.12-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip --no-cache-dir install poetry==1.8.3 \
    && poetry install --no-interaction

COPY . .

CMD [ "python3", "src/main.py"]
