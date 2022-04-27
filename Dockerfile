# python3.9のイメージをダウンロード
FROM python:3.9-buster

COPY requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r ./requirements.txt && rm -rf ~/.cache/pip

COPY ./api /api

CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker api.main:app