from datetime import date

def pergunta_nome():
    global nome
    print()
    print('Digite N para parar!')
    print()
    nome = input('Qual é seu nome? ')
    return nome

def pergunta_idade(atual):
    nasc = int(input(f'{nome} em que ano você nasceu? '))
    idade = atual - nasc
    print(f'Você tem {idade} anos.')
    return (nasc, idade)


atual = date.today().year
pode_parar = False
lista_nomes = []
lista_idades = []

while pode_parar == False:
    nome_informado = pergunta_nome()
    if nome_informado == 'N':
        pode_parar = True
    else:
        lista_nomes.append(nome_informado)
        lista_idades.append(pergunta_idade(atual))

lista_final = list(zip(lista_nomes, lista_idades))
print(lista_final)
