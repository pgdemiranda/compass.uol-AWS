from os import environ as env

import boto3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

access_key = env.get('AWS_ACCESS_KEY_ID')
secret_key = env.get('AWS_SECRET_ACCESS_KEY')
bucket_name = env.get('BUCKET_NAME')

if not all([access_key, secret_key, bucket_name]):
    missing = [name for name, value in [
        ('AWS_ACCESS_KEY_ID', access_key),
        ('AWS_SECRET_ACCESS_KEY', secret_key),
        ('BUCKET_NAME', bucket_name)
    ] if not value]
    raise ValueError(f"Variáveis de ambiente faltando: {', '.join(missing)}")

df_raw = pd.read_csv('../data/anuario-2024-dados_abertos-tabela2-19.csv', sep=';')

s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1',
)

try:
    s3.head_bucket(Bucket=bucket_name)
    print(f'Bucket encontrado')

    df_raw.to_csv(
        f's3://{bucket_name}/anuario-2024-dados_abertos-tabela2-19.csv',
        storage_options={
            'key': access_key,
            'secret': secret_key
        },
        index=False
    )
    print('Upload realizado')

except Exception as e:
    print('Erro:', e)
