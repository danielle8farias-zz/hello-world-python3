#!/usr/bin/env python3.8

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


#programa principal
#instanciando objeto
p1 = Humano()
#mostra na tela o endereço de memória do objeto
print(p1)
p1.nome = 'Danielle'
#retorna a string na tela
print(p1.nome)
#chamando o método da classe
p1.falar()
#função print vazia não retorna nada; pula uma linha
print()

p2 = Humano()
print(p2)
p2.nome = 'Rico'
print(p2.nome)
p2.falar()
print()

#método construtor sempre é chamado ao instanciar a classe
# por isso aparece na tela o print de var
p3 = Pessoa('Luis', 30)
#retorna string formatada na tela
print(f'Nome: {p3.nome}')
#chamando método da classe
p3.comer('maçã')
#verificando se pode comer 2x
p3.comer('melancia')
p3.parar_comer()
p3.comer('melancia')
p3.falar('política')
p3.parar_comer()
p3.falar('política')
p3.comer('tomate')
print()

#p4.nome = 'Sandra'
#p4.idade = 50
p4 = Pessoa('Sandra', 50)
p4.outro_metodo()
p4.parar_comer()
p4.falar('culinária')
p4.falar('cães')
p4.parar_falar()
p4.parar_falar()
print()

#imprimindo a variável da classe através da instância
print(p3.ano_atual)
print(p4.ano_atual)
#imprimindo a variável da classe através da própria classe
print(Pessoa.ano_atual)
print()

print(f'{p3.nome} nasceu em {p3.ano_nascimento()}.')
print(f'{p4.nome} nasceu em {p4.ano_nascimento()}.')
print()

#instanciando objeto pelo método de classe
p5 = Pessoa.por_ano_nasc('Enrico', 2000)
print(f'{p5.nome} tem {p5.idade} anos.')
