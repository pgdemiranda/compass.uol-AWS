lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def limpa_lista(lista):
    return list(set(lista))


print(limpa_lista(lista))
