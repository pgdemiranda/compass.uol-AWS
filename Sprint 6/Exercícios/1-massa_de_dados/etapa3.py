import os
import random
import time

import names

inicio_tarefa = time.perf_counter()

try:
    os.mkdir("data")
except FileExistsError:
    print("Não foi necessário criar o diretório 'data'.")

path = os.path.join("data", "nomes_aleatorios.txt")

random.seed(40)

qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

inicio_aleatorios = time.perf_counter()

dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open(path, "w") as file:
    for i in dados:
        file.write(i + "\n")

fim_tarefa = time.perf_counter()

print(
    f"Arquivo 'nomes_aleatorios.txt' criado com sucesso em {fim_tarefa - inicio_tarefa:.2f} segundos"
)
