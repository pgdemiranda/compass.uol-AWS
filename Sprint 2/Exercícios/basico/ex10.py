def soma(lista_string):
    return sum(map(int, lista_string.split(',')))


print(soma('1,3,4,6,10,76'))
