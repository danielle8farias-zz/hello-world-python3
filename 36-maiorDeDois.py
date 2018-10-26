'''
Faça um programa que compare dois números.
'''
print('-'*50)
print('{: ^50}'.format('MAIOR ENTRE DOIS NÚMEROS'))
print('-'*50)
while True:
    num1 = int (input("Digite o 1º número: "))
    num2 = int (input("Digite o 2º número: "))
    if num1 > num2:
        print("O maior número é",num1)
    elif num2 > num1:
        print("O maior número é:",num2)
    else:
        print('Os valores são iguais.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
