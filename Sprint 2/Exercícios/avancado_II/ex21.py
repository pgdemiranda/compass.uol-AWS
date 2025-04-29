def conta_vogais(texto:str)-> int:
    lista_vogais = list(filter(lambda x: x.lower() in 'aeiouAEIOU', texto))
    return len(lista_vogais)
