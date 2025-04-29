primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, primeiroNome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[i]
    idade = idades[i]

    print(f'{i} - {primeiroNome} {sobreNome} está com {idade} anos')
