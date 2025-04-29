list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_map(list, f):
    resultado = []

    for x in list:
        resultado.append(f(x))

    return resultado


def pot(i):
    return i ** 2


lista_final = my_map(list, pot)
print(lista_final)
