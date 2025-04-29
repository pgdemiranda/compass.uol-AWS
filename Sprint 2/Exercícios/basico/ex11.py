def divide_listas(lista):
    tamanho = len(lista)
    terco = tamanho // 3

    lista1 = lista[:terco]
    lista2 = lista[terco:2 * terco]
    lista3 = lista[2 * terco:]

    return lista1, lista2, lista3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = divide_listas(lista)

print(lista1, lista2, lista3)
