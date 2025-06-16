import os
import sys
from datetime import datetime
from pathlib import Path

import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from dotenv import load_dotenv


class GerenciadorS3:
    def __init__(
        self, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token
    ):
        self.bucket_name = bucket_name
        self.cliente_s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            region_name="us-east-1",
        )

    def enviar_arquivo(self, caminho_local, caminho_s3):
        if not caminho_local.exists():
            return False

        try:
            self.cliente_s3.upload_file(
                str(caminho_local), self.bucket_name, caminho_s3
            )
            return True
        except (ClientError, NoCredentialsError):
            return False

    def gerar_caminho_s3(self, nome_arquivo):
        data_atual = datetime.now()
        ano = data_atual.strftime("%Y")
        mes = data_atual.strftime("%m")
        dia = data_atual.strftime("%d")

        if "movies" in nome_arquivo.lower():
            categoria = "Movies"
        elif "series" in nome_arquivo.lower():
            categoria = "Series"
        else:
            categoria = "Outros"

        return f"RAW/Local/CSV/{categoria}/{ano}/{mes}/{dia}/{nome_arquivo}"

    def enviar_lote_arquivos(self, lista_arquivos, pasta_local):
        resultados = {"sucesso": [], "falha": [], "nao_encontrado": []}

        for arquivo in lista_arquivos:
            caminho_completo = pasta_local / arquivo

            if not caminho_completo.exists():
                resultados["nao_encontrado"].append(arquivo)
                continue

            destino_s3 = self.gerar_caminho_s3(arquivo)
            if self.enviar_arquivo(caminho_completo, destino_s3):
                resultados["sucesso"].append(arquivo)
            else:
                resultados["falha"].append(arquivo)

        return resultados


def carregar_variaveis_ambiente():
    load_dotenv()

    variaveis_necessarias = {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "bucket_name": os.getenv("BUCKET_NAME"),
        "aws_session_token": os.getenv("AWS_SESSION_TOKEN"),
    }

    variaveis_faltantes = [
        nome for nome, valor in variaveis_necessarias.items() if not valor
    ]
    if variaveis_faltantes:
        raise ValueError(
            f"Variáveis de ambiente faltando: {', '.join(variaveis_faltantes)}"
        )

    return variaveis_necessarias


def executar_processo():
    ARQUIVOS_CSV = ["movies.csv", "series.csv"]
    DADOS = Path("./data")

    try:
        credenciais = carregar_variaveis_ambiente()
        gerenciador = GerenciadorS3(
            aws_access_key_id=credenciais["aws_access_key_id"],
            aws_secret_access_key=credenciais["aws_secret_access_key"],
            bucket_name=credenciais["bucket_name"],
            aws_session_token=credenciais["aws_session_token"],
        )

        if not DADOS.exists():
            print(f"Pasta de dados não encontrada: {DADOS}")
            sys.exit(1)

        relatorio = gerenciador.enviar_lote_arquivos(ARQUIVOS_CSV, DADOS)

        print(f"Arquivos enviados com sucesso: {', '.join(relatorio['sucesso'])}")
        if relatorio["falha"]:
            print(f"Falha no envio: {', '.join(relatorio['falha'])}")
        if relatorio["nao_encontrado"]:
            print(f"Arquivos não encontrados: {', '.join(relatorio['nao_encontrado'])}")

        if relatorio["falha"] or relatorio["nao_encontrado"]:
            sys.exit(1)

    except ValueError as erro:
        print(f"Erro de configuração: {erro}")
        sys.exit(1)
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    executar_processo()
