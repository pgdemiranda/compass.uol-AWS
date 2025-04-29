x = 4 
y = 5

class Calculo:
    def adicao(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y


soma_resultado = Calculo().adicao(x, y)
subtracao_resultado = Calculo().subtracao(x, y)

print(f"Somando: {x} + {y} = {soma_resultado}")
print(f"Subtraindo: {x} - {y} = {subtracao_resultado}")
