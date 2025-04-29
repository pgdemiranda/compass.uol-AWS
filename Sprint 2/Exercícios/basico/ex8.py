def imprimir_parametros(*args, **kwargs):
    print("Parâmetros não nomeados (args):")

    for i, arg in enumerate(args, 1):
        print(f"  Argumento {i}: {arg}")

    print("\nParâmetros nomeados (kwargs):")
    for chave, valor in kwargs.items():
        print(f"  {chave}: {valor}")
