from datetime import date

class Entrevista():

    nome = ''
    nasc = 0
    idade = 0

    def pergunta_nome(self):
        print()
        print('Digite N para parar!')
        print()
        self.nome = input('Qual é seu nome? ')
        return self.nome

    def pergunta_idade(self,atual):
        self.nasc = int(input(f'{self.nome} em que ano você nasceu? '))
        self.idade = atual - self.nasc
        print(f'Você tem {self.idade} anos.')
    
    def __repr__(self):
        return f'Entrevista({self.nome}, {self.idade})'


atual = date.today().year
pode_parar = False
lista_entrevistados = []

while pode_parar == False:
    entrevistado = Entrevista()
    if entrevistado.pergunta_nome() == 'N':
        pode_parar = True
    else:
        entrevistado.pergunta_idade(atual)
        lista_entrevistados.append(entrevistado)

print(lista_entrevistados)
