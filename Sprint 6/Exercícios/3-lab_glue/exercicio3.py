import sys

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_INPUT_PATH", "S3_TARGET_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = args["S3_INPUT_PATH"]
target_path = args["S3_TARGET_PATH"]

dyf = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator": ","},
)

df = dyf.toDF()

print("Schema do dataframe:")
df.printSchema()

df = df.withColumn("nome", F.upper(F.col("nome")))

print(f"O dataframe possui {df.count()} linhas.")

contagem_nomes = (
    df.groupBy("ano", "sexo")
    .agg(F.count("nome").alias("contagem"))
    .orderBy(F.desc("ano"))
)

print("Contagem de nomes pelo ano mais recente:")
contagem_nomes.show()

contagem_nomes_fem = (
    df.select("nome", "total", "ano")
    .filter(F.col("sexo") == "F")
    .orderBy(F.desc("total"))
    .limit(1)
)

resultado = contagem_nomes_fem.collect()[0]

print(
    f"O nome feminino mais popular foi: {resultado['nome']} em {resultado['ano']} com {resultado['total']} registros."
)

contagem_nomes_masc = (
    df.select("nome", "total", "ano")
    .filter(F.col("sexo") == "M")
    .orderBy(F.desc("total"))
    .limit(1)
)

resultado = contagem_nomes_masc.collect()[0]

print(
    f"O nome masculino mais popular foi: {resultado['nome']} em {resultado['ano']} com {resultado['total']} registros."
)

total_registros = (
    df.groupBy("ano", "sexo")
    .agg(F.sum("total").alias("total"))
    .orderBy(F.asc("ano"))
    .limit(10)
)

print(
    "Total dos 10 primeiros registros de nomes masculinos e femininos por ano crescente:"
)
total_registros.show()

result_dyf = DynamicFrame.fromDF(df, glueContext, "result_dyf")

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(df, glueContext, "partitioned_df"),
    connection_type="s3",
    connection_options={
        "path": target_path,
        "partitionKeys": ["sexo", "ano"]
    },
    format="json"
)

job.commit()