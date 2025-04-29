def parametros(*args, **kwargs):
    for i, arg in enumerate(args, 1):
        print(f'{arg}')

    for chave, valor in kwargs.items():
        print(f'{valor}')


parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
