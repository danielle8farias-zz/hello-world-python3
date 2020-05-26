'''
Usuário informa o 1º termo de uma PA e a sua razão.
O programa calcula e retorna os 10 primeiros termos.
Em seguida, pergunta se o usuário quer mostrar mais termos.
Quando escolhido 0 termos o programa encerra.
'''

A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 1
An = A1
termo = 10
total_termos = 10
#laços aninhados
while termo != 0:
    while termo > 0:
        print(f'{An}', end=' -> ')
        An = A1 + i*r
        i += 1
        termo -= 1
    print('pausa')
    termo = int(input('Quantos termos deseja mostrar? '))
    total_termos += termo
print(f'Total de termos mostrados: {total_termos}')
print('FIM')
