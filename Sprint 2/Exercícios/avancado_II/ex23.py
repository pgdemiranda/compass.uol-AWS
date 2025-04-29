def calcular_valor_maximo(operadores,operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
    }

    valores = map(lambda x: operacoes[x[0]](*x[1]), zip(operadores, operandos))
    return max(valores)
