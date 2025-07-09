import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import (StringType, StructType, StructField, 
                              IntegerType, DoubleType)

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_FILMES_CSV_PATH", "S3_INPUT_FILMES_JSON_PATH", "S3_TARGET_FILMES_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path_csv = args["S3_INPUT_FILMES_CSV_PATH"]
input_path_json = args["S3_INPUT_FILMES_JSON_PATH"]
output_path = args["S3_TARGET_FILMES_PATH"]

schema = StructType([
    StructField("id_imdb", StringType(), False),
    StructField("titulo_principal", StringType(), True),
    StructField("titulo_original", StringType(), True),
    StructField("ano_lancamento", IntegerType(), True),
    StructField("duracao_minutos", IntegerType(), True),
    StructField("nota_media_imdb", DoubleType(), True),
    StructField("total_votos_imdb", IntegerType(), True),
    StructField("media_tmdb", DoubleType(), True),
    StructField("votos_tmdb", IntegerType(), True),
    StructField("orcamento", DoubleType(), True),
    StructField("receita", DoubleType(), True),
    StructField("lucro", DoubleType(), True)
])

df_csv = (spark.read.option("recursiveFileLookup", "true")
          .parquet(input_path_csv)
          .select(
              F.col("id").alias("id_imdb"),
              F.col("tituloPincipal").alias("titulo_principal"),
              F.col("tituloOriginal").alias("titulo_original"),
              F.col("anoLancamento").cast(IntegerType()).alias("ano_lancamento"),
              F.col("tempoMinutos").cast(IntegerType()).alias("duracao_minutos"),
              F.col("notaMedia").cast(DoubleType()).alias("nota_media_imdb"),
              F.col("numeroVotos").cast(IntegerType()).alias("total_votos_imdb")
          )
          .dropna(subset=["id_imdb", "titulo_principal"])
          .distinct())

df_json = (spark.read.option("recursiveFileLookup", "true")
           .parquet(input_path_json)
           .select(
               F.col("id_imdb"),
               F.col("media_tmdb").cast(DoubleType()),
               F.col("votos_tmdb").cast(IntegerType()),
               F.col("orcamento").cast(DoubleType()),
               F.col("recebimento").cast(DoubleType()).alias("receita"),
               (F.col("recebimento").cast(DoubleType()) - F.col("orcamento").cast(DoubleType())).alias("lucro")
           )
           .dropna(subset=["id_imdb"])
           .distinct())

df = df_csv.join(df_json, "id_imdb", "inner")
df = spark.createDataFrame(df.rdd, schema)

df.write.mode("overwrite").parquet(output_path)

job.commit()