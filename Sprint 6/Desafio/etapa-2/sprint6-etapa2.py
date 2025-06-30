import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_JSON_PATH", "S3_TARGET_JSON_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path = args["S3_INPUT_JSON_PATH"]
output_path = args["S3_TARGET_JSON_PATH"]

df = (
    spark.read.option("multiline", True)
    .option("recursiveFileLookup", "true")
    .json(input_path)
)

df = df.withColumn("input_path", F.input_file_name())

df = (
    df.withColumn("ano", F.regexp_extract("input_path", r"Json/(\d{4})", 1))
    .withColumn("mes", F.regexp_extract("input_path", r"Json/\d{4}/(\d{2})", 1))
    .withColumn("dia", F.regexp_extract("input_path", r"Json/\d{4}/\d{2}/(\d{2})", 1))
)

df = df.drop("input_path")

df.write.mode("overwrite").partitionBy("ano", "mes", "dia").parquet(output_path)


job.commit()
