class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = 'Azul'


aviao_1 = Aviao('BOIENG456', '1500 km/h', 400)
aviao_2 = Aviao('Embraer Praetor 600', '863 km/h', 14)
aviao_3 = Aviao('Antonov An-2', '258 km/h', 12)

hangar = [aviao_1, aviao_2, aviao_3]

for aviao in hangar:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.')
