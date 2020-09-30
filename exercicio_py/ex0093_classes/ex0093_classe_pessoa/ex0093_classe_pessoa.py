#importando módulo de data
from datetime import date

class Humano:
    '''
    Um humano que fala
    '''
    #método da classe
    def falar(self):
        print('Pessoa está falando...')


#criando classe
class Pessoa:
    '''
    Pessoa com nome e idade que tem ações
    '''
    #date.today().year pega o ano do sistema operacional
    #variável da classe pode ser usada por todos os métodos
    ano_atual = date.today().year

    #'self' é uma referência para o próprio objeto
    #construtor
    def __init__(self, nome, idade, comendo=False, falando=False):
        #self.variável = parâmetro
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        #variável válida apenas dentro do método init
        var = 'string qualquer'
        print(var)

    #método de instância
    def outro_metodo(self):
        '''
        Apenas testa um método qualquer
        '''
        print(f'Retornando a variável do construtor em outro método: {self.nome}')

    def comer(self, alimento):
        '''
        Executa ação de comer algo
        '''
        #verifica se está comendo
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            #ao chamar o return não é executado código abaixo
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        '''
        Executa ação de parar de comer
        '''
        #verifica se não está comendo
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        '''
        Executa a ação de falar sobre um determinado assunto
        '''
        if self.comendo:
            print(f'{self.nome} não pode falar de boca cheia.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        '''
        Executa a ação de parar de falar
        '''
        #verificando se a pessoa está calada
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def ano_nascimento(self):
        '''
        Ano em que a pessoa nasceu.
        '''
        return self.ano_atual - self.idade

    #método de classe
    #não precisa da instância, mas precisa da classe em si
    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        '''
        Cria pessoa por nome e ano de nascimento retornando nome e idade
        '''
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

