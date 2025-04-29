class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print('Voando...')

    def emitir_som(self):
        print(f'{self.nome} emitindo som...')


class Pato(Passaro):
    def __init__(self):
        super().__init__('Pato')

    def emitir_som(self):
        super().emitir_som()
        print('Quack Quack')


class Pardal(Passaro):
    def __init__(self):
        super().__init__('Pardal')

    def emitir_som(self):
        super().emitir_som()
        print('Piu Piu')


pato = Pato()
print(pato.nome)
pato.voar()
pato.emitir_som()
pardal = Pardal()
print(pardal.nome)
pardal.voar()
pardal.emitir_som()
