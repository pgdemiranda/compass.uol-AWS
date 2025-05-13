import hashlib

while True:
    entrada = input("Digite a informação a ser convertida em Hash, ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    print("Informação convertida em SHA-1:", hashlib.sha1(entrada.encode()).hexdigest())