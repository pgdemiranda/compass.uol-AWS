FROM python:3.13.3-alpine

WORKDIR /app

COPY ./data /app/data

COPY .env etapa1.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD python3 etapa1.py