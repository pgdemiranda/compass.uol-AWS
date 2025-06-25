# Etapa 1
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql import functions as F

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("../1-massa_de_dados/data/nomes_aleatorios.txt")
print("Etapa 1: importação e exemplos de linhas no dataframe \n")
df_nomes.show(10)
print("\n")

# Etapa 2
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
print("Etapa2: schema com coluna renomeada e 10 linhas do dataframe \n")
df_nomes.printSchema()
df_nomes.show(10)
print("\n")

# Etapa 3
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    F.when(F.rand() < 1/3, "Fundamental")
     .when(F.rand() < 2/3, "Médio")
     .otherwise("Superior")
)

print("Etapa 3:dataframe com coluna Escolaridade")
df_nomes.show(10)
print("\n")

# Etapa 4
paises = [
    'Brasil', 
    'Chile', 
    'Colômbia', 
    'Paraguai', 
    'Suriname', 
    'Venezuela', 
    'Paraguai', 
    'Peru', 
    'Equador', 
    'Bolívia', 
    'Uruguai', 
    'Guiana', 
    'Argentina'
    ]

paises_sql = "'" + "','".join(paises) + "'"

df_nomes = df_nomes.withColumn(
    "Pais",
    F.expr(f"element_at(array({paises_sql}), cast(rand() * {len(paises)} + 1 as int))")
)

print("Etapa 4: dataframe com coluna Pais")
df_nomes.show(10)
print("\n")

# Etapa 5
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    F.floor(F.rand() * (2010 - 1945) + 1945)
) 

print("Etapa 5: dataframe com coluna AnoNascimento")
df_nomes.show(10)
print("\n")

# Etapa 6
df_select = df_nomes[df_nomes['AnoNascimento'] >= 2001].select(['Nomes'])
print("Etapa 6: dataframe com pessoas nascidas neste século")
df_select.show(10)
print("\n")

# Etapa 7
df_nomes.createOrReplaceTempView("tabela")

df_select = spark.sql("""
    SELECT Nomes
    FROM tabela
    WHERE AnoNascimento >= 2001
""")

print("Etapa 7: dataframe com pessoas nascidas neste século")
df_select.show(10)
print("\n")

# Etapa 8
print("Etapa 8: número de pessoas da geração Millenials (nascidos entre 1980 e 1994)")
print(df_nomes.filter((df_nomes['AnoNascimento'] >= 1980) & (df_nomes['AnoNascimento'] <= 1994)).select(['Nomes']).count())
print("\n")

# Etapa 9
df_nomes.createOrReplaceTempView("tabela")

millennials = spark.sql("""
    SELECT COUNT(*) AS total
    FROM tabela
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

print("Etapa 9: número de pessoas da geração Millenials (nascidos entre 1980 e 1994)")
millennials.show()
print("\n")

# Etapa 10
df_nomes.createOrReplaceTempView("tabela")

geracoes = spark.sql("""
    SELECT 
        Pais,
        CASE 
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials (Geração Y)'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM tabela
    WHERE AnoNascimento BETWEEN 1944 AND 2015
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

print("Etapa 10: quantidade de pessoas por geração e pais")
geracoes.show(n=geracoes.count(), truncate=False)
print("\n")

# fechando o Spark
spark.sparkContext.stop()
spark.stop()