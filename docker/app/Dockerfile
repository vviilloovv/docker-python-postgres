FROM python:3.11.1-bullseye

WORKDIR /app

COPY ./app /app

RUN apt update && apt install -y jq vim
RUN pip config set global.trusted-host "pypi.org pypi.python.org files.pythonhosted.org"

RUN pip install --upgrade pip
RUN pip install -e .[dev]
