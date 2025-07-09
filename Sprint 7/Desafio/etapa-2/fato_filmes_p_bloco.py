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
        "S3_INPUT_TRUSTED_PATH",
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

input_trusted_path = args["S3_INPUT_TRUSTED_PATH"]
dim_filmes_path = args["S3_DIM_FILMES_PATH"]
dim_paises_path = args["S3_DIM_PAISES_PATH"]
dim_datas_path = args["S3_DIM_DATAS_PATH"]
output_path = args["S3_TARGET_FATO_PATH"]

schema = StructType(
    [
        StructField("id_filme", IntegerType(), False),
        StructField("id_imdb", StringType(), True),
        StructField("data", DateType(), True),
        StructField("votos_tmdb", IntegerType(), True),
        StructField("media_tmdb", DoubleType(), True),
        StructField("total_votos_imdb", IntegerType(), True),
        StructField("nota_media_imdb", DoubleType(), True),
        StructField("orcamento", DoubleType(), True),
        StructField("recebimento", DoubleType(), True),
        StructField("lucro", DoubleType(), True),
        StructField("id_bloco", IntegerType(), True),
        StructField("bloco_historico", StringType(), True),
        StructField("ano", IntegerType(), True),
        StructField("mes", IntegerType(), True),
        StructField("decada", IntegerType(), True),
        StructField("periodo_historico", StringType(), True),
    ]
)

dim_filmes = spark.read.parquet(dim_filmes_path)
dim_paises = spark.read.parquet(dim_paises_path)
dim_datas = spark.read.parquet(dim_datas_path)

df = spark.read.option("recursiveFileLookup", "true").parquet(input_trusted_path)

fato_filmes = (
    df.withColumn("paises_codigo_array", F.sort_array(F.split(F.col("paises_codigo"), ",\s*")))
    .withColumn("data_col", F.to_date(F.col("lancamento"), "yyyy-MM-dd"))
    .withColumn("ano_lancamento", F.year(F.col("data_col")))
    .withColumn(
        "bloco_historico",
        F.when(
            (F.array_contains(F.col("paises_codigo_array"), "US")) & (F.col("ano_lancamento") < 1993),
            "ocidental"
        )
        .when(
            F.array_contains(F.col("paises_codigo_array"), "SU"),
            "sovietico"
        )
        .when(
            (F.array_contains(F.col("paises_codigo_array"), "RU")) & (F.col("ano_lancamento") > 2012),
            "russia"
        )
        .when(
            F.array_contains(F.col("paises_codigo_array"), "UA"),
            "ucrania"
        )
        .otherwise("outros")
    )
    .withColumn(
        "id_bloco",
        F.when(F.col("bloco_historico") == "ocidental", 1)
        .when(F.col("bloco_historico") == "sovietico", 2)
        .when(F.col("bloco_historico") == "russia", 3)
        .when(F.col("bloco_historico") == "ucrania", 4)
        .otherwise(5)
    )
    .alias("base")
    .join(
        dim_filmes.select("id_imdb", "votos_tmdb", "media_tmdb", "total_votos_imdb", "nota_media_imdb", "orcamento", "receita", "lucro").alias("df"),
        "id_imdb",
        "inner"
    )
    .join(
        dim_datas.select("data", "ano", "mes", "decada", "periodo_historico").alias("dd"),
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
        F.col("base.data_col"),
        F.col("base.bloco_historico"),
        F.col("base.id_bloco"),
        F.col("df.votos_tmdb"),
        F.col("df.media_tmdb"),
        F.col("df.total_votos_imdb"),
        F.col("df.nota_media_imdb"),
        F.col("df.orcamento"),
        F.col("df.receita"),
        F.col("df.lucro"),
        F.col("dd.ano"),
        F.col("dd.mes"),
        F.col("dd.decada"),
        F.col("dd.periodo_historico")
    )
    .agg(F.collect_set(F.col("dp.id_pais")).alias("id_pais_array"))
    .withColumn("id_filme", F.row_number().over(Window.orderBy("id_imdb")))
    .select(
        "id_filme",
        F.col("id_imdb"),
        F.col("data_col").alias("data"),
        F.col("votos_tmdb").cast(IntegerType()),
        F.col("media_tmdb").cast(DoubleType()),
        F.col("total_votos_imdb").cast(IntegerType()),
        F.col("nota_media_imdb").cast(DoubleType()),
        F.col("orcamento").cast(DoubleType()),
        F.col("receita").cast(DoubleType()).alias("recebimento"),
        F.col("lucro").cast(DoubleType()),
        F.col("id_bloco"),
        F.col("bloco_historico"),
        F.col("ano"),
        F.col("mes"),
        F.col("decada"),
        F.col("periodo_historico")
    )
    .filter((F.col("id_bloco") != 5) & ((F.col("ano") < 1993) | (F.col("ano") > 2013)))
    .distinct()
)

fato_filmes = spark.createDataFrame(fato_filmes.rdd, schema)

fato_filmes.write.mode("overwrite").partitionBy("bloco_historico").parquet(output_path)

job.commit()
