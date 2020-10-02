from datetime import date

#criando a classe
class Usuario:
    '''
    Usuário com nome e data de nascimento
    '''
    #construtor
    def __init__(self, nome_completo, aniversario):
        #self.variável = parâmetro
        self.nome_completo = nome_completo
        self.aniversario = aniversario
        #split() separa strings de acordo com o que está entre parenteses
        #   no nosso caso, espaço e coloca em uma lista
        #separando o nome
        #criando variável no escopo do construtor
        #não é preciso usar self na variável 'nome_completo,
        #   pois já foi utilizado antes
        pedaco_nome = nome_completo.split(' ')
        #criando variável que não possui parâmetro declarado acima
        #pegando o primeiro elemento da lista
        self.primeiro_nome = pedaco_nome[0]
        #pegando o último elemento da lista
        self.ultimo_nome = pedaco_nome[-1]

    def idade(self):
        '''
        Informa a idade do usuário em dias e anos
        '''
        hoje = date.today()
        #split() separa strings de acordo com o que está entre parenteses
        #   no nosso caso, / e coloca em uma lista
        #separando a data de nascimento em dia, mês e ano
        pedaco_nasc = self.aniversario.split('/')
        dia = int(pedaco_nasc[0])
        mes = int(pedaco_nasc[1])
        ano = int(pedaco_nasc[2])
        #'hoje' foi informado no formado date.
        #   a data_nasc deve seguir o mesmo padrão de formato
        #   para que seja possível executar operações entre elas
        data_nasc = date(ano, mes, dia)
        #.days para retornar apenas o valor de dias
        #formato datetime.timedelta(days=idade_dias)
        idade_dias = (hoje - data_nasc).days
        idade_anos = idade_dias/365
        #idade de anos deve ser um número inteiro
        return idade_dias, int(idade_anos)

print()
user1 = Usuario('Nicolau Farias', '11/09/1937')
print(user1.nome_completo)
print(user1.primeiro_nome)
print(user1.ultimo_nome)
print(user1.aniversario)
print('idade em dias, idade em anos')
print(user1.idade())
print()
