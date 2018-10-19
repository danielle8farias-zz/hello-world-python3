'''
Faça a soma de dois números.
'''
print('-'*50)
print('{: ^50}'.format('SOMA DOIS NÚMEROS'))
print('-'*50)
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    def soma(x,y):
        z = x+y
        print(x,"+",y,"=",z)
    soma(num1,num2)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
