import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import (StringType, StructType, StructField, 
                              IntegerType, DoubleType)

args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_FILMES_CSV_PATH", "S3_TARGET_FILMES_PATH"]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path_csv = args["S3_INPUT_FILMES_CSV_PATH"]
output_path = args["S3_TARGET_FILMES_PATH"]

schema = StructType([
    StructField("id_imdb", StringType(), False),
    StructField("titulo_principal", StringType(), True),
    StructField("titulo_original", StringType(), True),
])

df = (spark.read.option("recursiveFileLookup", "true")
          .parquet(input_path_csv)
          .select(
              F.col("id").alias("id_imdb"),
              F.col("tituloPincipal").alias("titulo_principal"),
              F.col("tituloOriginal").alias("titulo_original")
          )
          .distinct()
     )
          
df.write.mode("overwrite").parquet(output_path)

job.commit()