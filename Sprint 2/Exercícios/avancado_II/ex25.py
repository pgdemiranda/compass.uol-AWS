def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)

    acima_media = [
        (produto, preco) 
        for produto, preco in conteudo.items() 
        if preco > media
    ]

    produtos_ordenados = sorted(acima_media, key=lambda item: item[1])

    return produtos_ordenados
