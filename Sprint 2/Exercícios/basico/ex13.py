import random 

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)

random_list_ord = sorted(random_list)

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

tamanho = len(random_list_ord)
if tamanho % 2 == 0:
    mediana = (random_list_ord[tamanho // 2 - 1] + random_list_ord[tamanho // 2]) / 2
else:
    mediana = random_list_ord[tamanho // 2]

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
