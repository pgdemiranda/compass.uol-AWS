import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import (
    ArrayType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)
from pyspark.sql.window import Window

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_PAIS_PATH", "S3_TARGET_PAIS_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path = args["S3_INPUT_PAIS_PATH"]
output_path = args["S3_TARGET_PAIS_PATH"]

schema = StructType(
    [
        StructField("id_pais", IntegerType(), True),
        StructField("paises_codigo_array", ArrayType(StringType()), True),
        StructField("paises_nome_array", ArrayType(StringType()), True),
    ]
)


df = spark.read.option("recursiveFileLookup", "true").parquet(input_path)

df = (
    df.withColumn(
        "paises_codigo_array", F.sort_array(F.split(F.col("paises_codigo"), ",\s*"))
    )
    .withColumn(
        "paises_nome_array", F.sort_array(F.split(F.col("paises_nome"), ",\s*"))
    )
    .select("paises_codigo_array", "paises_nome_array")
    .distinct()
    .withColumn("id_pais", F.row_number().over(Window.orderBy("paises_codigo_array")))
    .select("id_pais", "paises_codigo_array", "paises_nome_array")
)

df = spark.createDataFrame(df.rdd, schema)

df.write.mode("overwrite").parquet(output_path)

job.commit()
