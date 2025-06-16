import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import os

import boto3
import pandas as pd
import requests

bucket_name = os.environ.get("BUCKET_NAME")
tmdb_api_key = os.environ.get("TMDB_API_KEY")

s3 = boto3.client("s3")


def lambda_handler(event, context):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix="RAW/Local/CSV/Movies/")
    objetos_ordenados = sorted(
        response["Contents"], key=lambda obj: obj["LastModified"], reverse=True
    )
    ultimo_objeto = objetos_ordenados[0]["Key"]

    obj = s3.get_object(Bucket=bucket_name, Key=ultimo_objeto)
    df = pd.read_csv(
        obj['Body'],
        sep="|",
        usecols=[
            "id",
            "tituloPincipal",
            "tituloOriginal",
            "anoLancamento",
            "tempoMinutos",
            "genero",
            "notaMedia",
            "numeroVotos",
        ],
        low_memory=False
    )

    df = df.drop_duplicates(subset="id")
    df = df[df["genero"].str.contains("War", na=False)]

    df["anoLancamento"] = pd.to_datetime(df["anoLancamento"], errors="coerce").dt.year
    df = df[
        ((df["anoLancamento"] >= 1945) & (df["anoLancamento"] <= 1992))
        | (df["anoLancamento"] >= 2015)
    ]

    lista_imdb_ids = df["id"].tolist()

    data_atual = datetime.now()
    prefix = f"RAW/TMDB/Json/{data_atual.year}/{data_atual.month:02d}/{data_atual.day:02d}/"

    def upload_chunk_to_s3(chunk):
        filename = f"{uuid.uuid4()}.json"
        key = prefix + filename
        json_bytes = json.dumps(chunk, ensure_ascii=False, indent=4).encode("utf-8")
        s3.put_object(
            Bucket=bucket_name, Key=key, Body=json_bytes, ContentType="application/json"
        )
        print(f"Upload para {key} com {len(chunk)} filmes.")

    def processar_filme(imdb_id):
        try:
            url_find = (
                f"https://api.themoviedb.org/3/find/{imdb_id}"
                f"?api_key={tmdb_api_key}&language=pt-BR&external_source=imdb_id"
            )
            response = requests.get(url_find)
            data_find = response.json()

            movie_results = data_find.get("movie_results", [])
            if not movie_results:
                return None

            movie = movie_results[0]
            movie_id = movie["id"]

            detalhes_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=pt-BR"
            detalhes_response = requests.get(detalhes_url)
            detalhes = detalhes_response.json()

            countries = detalhes.get("production_countries", [])
            codigos_pais = [p["iso_3166_1"] for p in countries]

            if not any(c in ["US", "RU", "SU", "UA"] for c in codigos_pais):
                return None

            nomes_pais = [p["name"] for p in countries]

            return {
                "id": movie_id,
                "id_imdb": detalhes.get("imdb_id"),
                "titulo": detalhes.get("title"),
                "titulo_original": detalhes.get("original_title"),
                "lancamento": detalhes.get("release_date"),
                "media_tmdb": detalhes.get("vote_average"),
                "votos_tmdb": detalhes.get("vote_count"),
                "orcamento": detalhes.get("budget"),
                "recebimento": detalhes.get("revenue"),
                "lucro": detalhes.get("revenue", 0) - detalhes.get("budget", 0),
                "paises_codigo": ", ".join(codigos_pais),
                "paises_nome": ", ".join(nomes_pais),
            }

        except Exception as e:
            print(f"Erro ao processar {imdb_id}: {e}")
            return None

    chunk = []
    chunk_size = 100

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(processar_filme, imdb_id) for imdb_id in lista_imdb_ids]
        for future in as_completed(futures):
            resultado = future.result()
            if resultado:
                chunk.append(resultado)
                if len(chunk) >= chunk_size:
                    upload_chunk_to_s3(chunk)
                    chunk = []

    if chunk:
        upload_chunk_to_s3(chunk)

    return {
        "statusCode": 200,
        "body": f"Processamento finalizado com {len(lista_imdb_ids)} filmes.",
    }
