'''
Dados dois números inteiros positivos, determinar o máximo divisor comum
entre eles usando o algoritmo de Euclides.
Exemplo: mdc(21, 15) = 3
'''
print('-'*50)
print('{: ^50}'.format('MDC DE DOIS NÚMEROS'))
print('-'*50)
while True:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    div = num1 % num2
    while div != 0:
        a = num2
        b = div
        div = a % b
    print('M.D.C.({},{}) = {}'.format(num1,num2,b))
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
