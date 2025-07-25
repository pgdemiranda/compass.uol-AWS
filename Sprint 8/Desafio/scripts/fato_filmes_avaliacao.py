import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import (
    ArrayType,
    DateType,
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)
from pyspark.sql.window import Window

args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "S3_INPUT_TRUSTED_PATH_CSV",
        "S3_INPUT_TRUSTED_PATH_JSON",
        "S3_DIM_FILMES_PATH",
        "S3_DIM_PAISES_PATH",
        "S3_DIM_DATAS_PATH",
        "S3_TARGET_FATO_PATH",
    ],
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path_CSV = args["S3_INPUT_TRUSTED_PATH_CSV"]
input_path_JSON = args["S3_INPUT_TRUSTED_PATH_JSON"]
dim_filmes_path = args["S3_DIM_FILMES_PATH"]
dim_paises_path = args["S3_DIM_PAISES_PATH"]
dim_datas_path = args["S3_DIM_DATAS_PATH"]
output_path = args["S3_TARGET_FATO_PATH"]

schema = StructType(
    [
        StructField("id", IntegerType(), False),  # PK
        StructField("id_imdb", StringType(), True),     # SK
        StructField("id_pais", ArrayType(IntegerType()), True),  # SK
        StructField("data", DateType(), True),          # SK
        StructField("votos_tmdb", IntegerType(), True),
        StructField("media_tmdb", DoubleType(), True),
        StructField("votos_imdb", IntegerType(), True),
        StructField("media_imdb", DoubleType(), True),
        StructField("orcamento", DoubleType(), True),
        StructField("recebimento", DoubleType(), True),
    ]
)

dim_filmes = spark.read.parquet(dim_filmes_path)
dim_paises = spark.read.parquet(dim_paises_path)
dim_datas = spark.read.parquet(dim_datas_path)

df_csv = spark.read.option("recursiveFileLookup", "true").parquet(input_path_CSV)
df_csv = df_csv.select(
    F.col("id").alias("id_imdb"),
    F.col("notamedia").alias("media_imdb"),
    F.col("numerovotos").alias("votos_imdb")
)

df_json = spark.read.option("recursiveFileLookup", "true").parquet(input_path_JSON)
df_json = df_json.select(
    "id_imdb",
    "media_tmdb",
    "votos_tmdb",
    "orcamento",
    "paises_codigo",
    "recebimento",
    "lancamento"
)

df_joined = df_json.join(df_csv, "id_imdb", "inner")

fato_avaliacao_filmes = (
    df_joined.withColumn("paises_codigo_array", F.split(F.col("paises_codigo"), ",\\s*"))
    .withColumn("data_col", F.to_date(F.col("lancamento"), "yyyy-MM-dd"))
    .alias("base")
    .join(
        dim_filmes.select("id_imdb").alias("df"),
        F.col("base.id_imdb") == F.col("df.id_imdb"),
        "inner"
    )
    .join(
        dim_datas.select("data").alias("dd"),
        F.col("base.data_col") == F.col("dd.data"),
        "inner"
    )
    .withColumn("codigo_pais_exploded", F.explode(F.col("base.paises_codigo_array")))
    .join(
        dim_paises.select("id_pais", "codigo_pais").alias("dp"),
        F.col("codigo_pais_exploded") == F.col("dp.codigo_pais"),
        "inner"
    )
    .groupBy(
        F.col("base.id_imdb"),
        F.col("dd.data"),
        F.col("base.votos_tmdb"),
        F.col("base.media_tmdb"),
        F.col("base.votos_imdb"),
        F.col("base.media_imdb"),
        F.col("base.orcamento"),
        F.col("base.recebimento"),
        F.col("base.data_col")
    )
    .agg(F.collect_set(F.col("dp.id_pais")).alias("id_pais_array"))
    .withColumn("id", F.row_number().over(Window.orderBy("id_imdb")))
    .select(
        "id",
        F.col("id_imdb"),
        F.col("id_pais_array").alias("id_pais"),
        F.col("data"),
        F.col("votos_tmdb").cast(IntegerType()),
        F.col("media_tmdb").cast(DoubleType()),
        F.col("votos_imdb").cast(IntegerType()),
        F.col("media_imdb").cast(DoubleType()),
        F.col("orcamento").cast(DoubleType()),
        F.col("recebimento").cast(DoubleType())
    )
    .distinct()
)

fato_avaliacao_filmes = spark.createDataFrame(fato_avaliacao_filmes.rdd, schema)

fato_avaliacao_filmes.write.mode("overwrite").parquet(output_path)

job.commit()