FROM python:3.9-alpine3.14

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8081" ]