from os import environ as env

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = env.get("API_KEY")

url_generos = (
    f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
)
res_generos = requests.get(url_generos).json()
genre_id_para_nome = {g["id"]: g["name"] for g in res_generos["genres"]}

url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"

response = requests.get(url)
data = response.json()

filmes = []
for movie in data["results"]:
    generos_nomes = [
        genre_id_para_nome.get(i, "Desconhecido") for i in movie.get("genre_ids", [])
    ]

    df = {
        "Título": movie["title"],
        "Título Original": movie["original_title"],
        "Gêneros": ", ".join(generos_nomes),
        "Data de Lançamento": movie["release_date"],
        "Média de votos": movie["vote_average"]
    }
    filmes.append(df)

df = pd.DataFrame(filmes)

print(df)