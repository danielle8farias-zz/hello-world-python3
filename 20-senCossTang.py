'''
Informe um ângulo e calcule o valor do seno, cosseno e tangente.
'''
print('-'*50)
print('{: ^50}'.format('SENO COSSENO TANGENTE'))
print('-'*50)
import math
while True:
    angulo = float(input('Digite um ângulo: '))
    seno = math.sin(math.radians(angulo))
    print('O seno é {:.2f}'.format(seno))
    cosseno = math.cos(math.radians(angulo))
    print('O cosseno é {:.2f}'.format(cosseno))
    tangente = math.tan(math.radians(angulo))
    print('A tangente é {:.2f}'.format(tangente))
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
