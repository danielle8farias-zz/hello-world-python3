'''
Crie um programa onde o usuário digite uma expressão matemática que faça uso de parenteses.
Seu programa deverá analisar se os números de parenteses abertos correspondem aos números de
parenteses fechados.
'''
print('-'*50)
print('{: ^50}'.format('VALIDADOR DE EXPRESSÕES MATEMÁTICAS'))
print('-'*50)
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
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
