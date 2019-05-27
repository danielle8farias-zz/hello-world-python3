def main():
    carro1 = Carro('brasília',1968,'amarela',80)
    carro2 = Carro('fuscão',1981,'preto',95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)


class Carro():
    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_inicial = 0
        self.velocidade_maxima = velocidade_maxima

    def imprima(self):
        if self.velocidade_inicial == 0:
            print(f'{self.modelo}, {self.cor}, {self.ano}')
        elif self.velocidade_inicial <  self.velocidade_maxima:
            print(f'{self.modelo},{self.cor} indo a {self.velocidade_inicial} Km/h')
        else:
            print(f'{self.modelo}, {self.cor} indo muito rápido! Velocidade máxima!')

    def acelere(self, velocidade):
        self.velocidade_inicial = velocidade
        if self.velocidade_inicial > self.velocidade_maxima:
            self.velocidade_inicial = self.velocidade_maxima #para não ultrapassar a velocida máxima
        self.imprima()

    def pare(self):
        self.velocidade_inicial = 0
        self.imprima()

main()
