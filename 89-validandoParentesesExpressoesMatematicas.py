'''
Crie um programa onde o usuário digite uma expressão matemática que faça uso de parenteses.
Seu programa deverá analisar se os números de parenteses abertos correspondem aos números de
parenteses fechados.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('VALIDADOR DE EXPRESSÕES MATEMÁTICAS')

expre = input('Digite a expressão matemática: ')
pilha = []
for simbolo in expre:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0: #verifica se a pilha não está vazia
            pilha.pop() #remove o parentese aberto ao encontrar um fechado
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão VÁLIDA!') #foi removido todos os pares
else:
    print('Expressão inválida.')

rodape()
