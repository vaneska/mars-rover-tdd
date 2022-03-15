FROM python:3.10-slim

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get install -y -q \
      build-essential python3-dev libffi-dev git && \
    python3 -m pip install --no-cache-dir --quiet -U pip && \
    python3 -m pip install --no-cache-dir --quiet poetry

ADD . /app

WORKDIR /app

RUN poetry export --without-hashes --dev -o requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD FLASK_APP=apps.commands:app flask run --host 0.0.0.0 --port 8081
