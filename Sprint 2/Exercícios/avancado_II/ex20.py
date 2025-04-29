with open('number.txt', 'r') as arquivo:
    linhas = arquivo.readlines()


pares = list(filter(lambda x: x % 2 == 0, map(int, linhas)))
top_pares = sorted(pares, reverse=True)[:5]
soma_top = sum(top_pares)

print(top_pares)
print(soma_top)