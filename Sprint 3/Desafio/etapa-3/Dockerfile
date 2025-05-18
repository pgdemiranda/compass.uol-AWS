FROM python:3.13.3-alpine

WORKDIR /app

COPY ./etl.py /app/etl.py

COPY ./concert_tours_by_women.csv /app/concert_tours_by_women.csv

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /app/volume

CMD ["python3", "etl.py"]
