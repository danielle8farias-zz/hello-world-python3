#importando módulo de data
from datetime import date
from time import sleep

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


print('Classe Humano')
#instanciando objeto
p1 = Humano()
#mostra na tela o endereço de memória do objeto
print('mostra na tela o endereço de memória do objeto')
print(p1)
p1.nome = 'Danielle'
#retorna a string na tela
print(p1.nome)
#chamando o método da classe
p1.falar()
#print() vazio pula uma linha
print()

sleep(1)
print('Classe pessoa')
#método construtor sempre é chamado ao instanciar a classe
# por isso aparece na tela o print de var
print('método construtor sempre é chamado ao instanciar a classe, por isso aparece na tela o print de var')
p2 = Pessoa('Luis', 30)
#retorna string formatada na tela
print(f'Nome: {p2.nome}')
#chamando método da classe; mensagem
p2.comer('maçã')
#verificando se pode comer 2x
print('verificando se pode comer 2x')
p2.comer('melancia')
p2.parar_comer()
p2.comer('melancia')
p2.falar('política')
p2.parar_comer()
p2.falar('política')
p2.comer('tomate')
print()

sleep(1)
#p3.nome = 'Sandra'
#p3.idade = 50
p3 = Pessoa('Sandra', 50)
p3.outro_metodo()
p3.parar_comer()
p3.falar('culinária')
p3.falar('cães')
p3.parar_falar()
p3.parar_falar()
print()

sleep(1)
#imprimindo a variável da classe através da instância
print('imprimindo a variável da classe através da instância')
print(p2.ano_atual)
print(p3.ano_atual)
#imprimindo a variável da classe através da própria classe
print('imprimindo a variável da classe através da própria classe')
print(Pessoa.ano_atual)
print()

print(f'{p2.nome} nasceu em {p2.ano_nascimento()}.')
print(f'{p3.nome} nasceu em {p3.ano_nascimento()}.')
print()

sleep(1)
#instanciando objeto pelo método de classe
print('instanciando objeto pelo método de classe')
p4 = Pessoa.por_ano_nasc('Victor', 2000)
print(f'{p4.nome} tem {p4.idade} anos.')
print()
