#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de linha
from mensagem import linha

#criando a classe
class Computador:
    #construtor
    def __init__(self, marca, memoria_ram, placa_video, hd, estado=False):
        #self.variável = parâmetro
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
        self.hd = hd
        self.estado = estado

    #método da classe
    def ligar(self):
        #verificando se computador está desligado
        if not self.estado:
            print(f'{self.marca} ligando...')
            self.estado = True
            return
        
        print(f'{self.marca} já está ligado.')

    def desligar(self):
        if self.estado:
            print(f'{self.marca} desligando...')
            self.estado = False
            return
        
        print(f'{self.marca} já está desligado.')

    def exibir_config(self):
        if not self.estado:
            print(f'Não é possível acessar! {self.marca} está desligado.')
            return

        print(f'{self.marca} possui as seguintes configurações:')
        print(f'Memória ram: {self.memoria_ram}')
        print(f'Placa de vídeo: {self.placa_video}')
        print(f'HD: {self.hd}')


#instanciando a classe
pc1 = Computador('Asus', '8gb', 'Nvidia', '200gb')
#retorna string formatada na tela
print(f'Marca do computador: {pc1.marca}')
#função print vazia não retorna nada; pula uma linha
print()
#chamando método da classe
pc1.ligar()
pc1.ligar()
pc1.desligar()
pc1.exibir_config()

#chamando função linha
linha()

#passando atributos para a classe
pc2 = Computador('Dell', '10gb', 'GeForce', '150gb')
print(f'Marca do computador: {pc2.marca}')
print()
pc2.desligar()
pc2.ligar()
pc2.exibir_config()

linha()

pc3 = Computador('Acer', '16gb', 'ATM', '1tb')
print(f'Marca do computador: {pc3.marca}')
print()
pc3.exibir_config()

print()
