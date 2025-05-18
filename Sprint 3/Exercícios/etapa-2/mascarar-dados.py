import hashlib

while True:
    entrada = input("Digite a informação a ser convertida em SHA-1, ou digite 'finalizar' para encerrar o script: ")
    if entrada.lower() == 'finalizar':
        break
    print("Informação convertida em SHA-1:", hashlib.sha1(entrada.encode()).hexdigest())
