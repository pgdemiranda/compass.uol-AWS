import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_CSV_PATH", "S3_TARGET_CSV_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = args["S3_INPUT_CSV_PATH"]
target_path = args["S3_TARGET_CSV_PATH"]

df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .option("recursiveFileLookup", "true")
    .csv(source_file)
)

df.write.mode("overwrite").parquet(target_path)

job.commit()
