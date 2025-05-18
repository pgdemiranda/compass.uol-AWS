FROM python:3.13.3-alpine

WORKDIR /app

COPY ./job.py /app/job.py

COPY ./csv_limpo.csv /app/csv_limpo.csv

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /app/volume

CMD ["python3", "job.py"]
