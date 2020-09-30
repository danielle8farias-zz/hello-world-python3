#criando a classe
class Computador:
    '''
    Computador com seus componentes
    '''
    #construtor
    def __init__(self, marca, memoria_ram, placa_video, hd, estado=False):
        #self.variável = parâmetro
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
        self.hd = hd
        self.estado = estado

    #método de instância
    def ligar(self):
        '''
        Liga o computador
        '''
        #verificando se computador está desligado
        if not self.estado:
            print(f'{self.marca} ligando...')
            self.estado = True
            return
        
        print(f'{self.marca} já está ligado.')

    def desligar(self):
        '''
        Desliga o computador
        '''
        if self.estado:
            print(f'{self.marca} desligando...')
            self.estado = False
            return
        
        print(f'{self.marca} já está desligado.')

    def exibir_config(self):
        '''
        Exibe as especificações técnicas do computador
        '''
        if not self.estado:
            print(f'Não é possível acessar! {self.marca} está desligado.')
            return

        print(f'{self.marca} possui as seguintes configurações:')
        print(f'Memória ram: {self.memoria_ram}')
        print(f'Placa de vídeo: {self.placa_video}')
        print(f'HD: {self.hd}')

