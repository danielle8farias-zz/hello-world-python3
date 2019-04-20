class Televisao:
    def __init__ (self):
        self.ligada = False
        self.canal = 2
    def muda_canal_cima(self):
        self.canal += 1
    def muda_canal_baixo(self):
        self.canal -= 1

tv = Televisao()
tv.muda_canal_cima()
tv.muda_canal_cima()
tv.muda_canal_cima()
print(f'Estamos no canal {tv.canal}')

tv.muda_canal_baixo()
print(f'Agora estamos no canal {tv.canal}')
