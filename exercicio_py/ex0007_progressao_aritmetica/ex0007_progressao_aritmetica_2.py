########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o 1º termo de uma PA e sua razão. O programa retorna os 10 primeiros termos dessa PA.
########

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
    print('Digite zero para encerrar')
    termo = int(input('Quantos termos deseja mostrar? '))
    total_termos += termo
print(f'Total de termos mostrados: {total_termos}')
print('FIM')
