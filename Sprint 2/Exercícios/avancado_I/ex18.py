class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada.copy())

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada.copy(), reverse=True)


crescente = Ordenadora(listaBaguncada = [3, 4, 2, 1, 5])
decrescente = Ordenadora(listaBaguncada = [9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
