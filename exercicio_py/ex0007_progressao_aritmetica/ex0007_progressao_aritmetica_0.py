########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o 1º termo de uma PA e sua razão. O programa retorna os 10 primeiros termos dessa PA.
########

A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))

#fórmula da Progressão aritmética
#   calculando o último termo
An = A1 + (10-1)*r
#laço for:
#   início: A1
#   fim: An+r. O intervalo do range é aberto, ou seja, não inclui o último termo, por isso esse recurso de An+r.
#   passo: r em r
for n in range(A1, An + r, r):
    print(f'{n}', end = ' -> ')
print('FIM')
