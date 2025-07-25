import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import (
    BooleanType,
    DateType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_DATA_PATH", "S3_TARGET_DATA_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path = args["S3_INPUT_DATA_PATH"]
output_path = args["S3_TARGET_DATA_PATH"]

schema = StructType(
    [
        StructField("data", DateType(), True),
        StructField("ano", IntegerType(), True),
        StructField("mes", IntegerType(), True),
        StructField("dia", IntegerType(), True),
        StructField("semestre", IntegerType(), True),
        StructField("dia_semana", IntegerType(), True),
        StructField("dia_ano", IntegerType(), True),
        StructField("fim_semana", BooleanType(), True),
        StructField("decada", IntegerType(), True),
        StructField("periodo_historico", StringType(), True),
    ]
)

df = spark.read.option("recursiveFileLookup", "true").parquet(input_path)

df = (
    df.select("lancamento")
    .dropna()
    .distinct()
    .withColumn("data_col", F.to_date(F.col("lancamento"), "yyyy-MM-dd"))
    .withColumn("ano", F.year(F.col("data_col")))
    .withColumn("mes", F.month(F.col("data_col")))
    .withColumn("dia", F.dayofmonth(F.col("data_col")))
    .withColumn("semestre", F.when(F.month(F.col("data_col")) <= 6, 1).otherwise(2))
    .withColumn("dia_semana", F.dayofweek(F.col("data_col")))
    .withColumn("dia_ano", F.dayofyear(F.col("data_col")))
    .withColumn("fim_semana", F.col("dia_semana").isin([1, 7]))
    .withColumn("decada", (F.year(F.col("data_col")) / 10).cast(IntegerType()) * 10)
    .withColumn(
        "periodo_historico",
        F.when(F.year(F.col("data_col")) < 1993, "guerra fria")
        .when(F.year(F.col("data_col")) > 2013, "russia x ucrania")
        .otherwise("pos guerra fria")
    )
    .withColumn("data", F.col("data_col"))
    .drop("data_col", "lancamento")
    .select(
        "data",
        "ano",
        "mes",
        "dia",
        "semestre",
        "dia_semana",
        "dia_ano",
        "fim_semana",
        "decada",
        "periodo_historico"
    )
)

df = spark.createDataFrame(df.rdd, schema)

df.write.mode("overwrite").parquet(output_path)


job.commit()
