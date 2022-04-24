# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.create false
RUN poetry install

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]