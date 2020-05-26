'''
Usuário digita um número e programa retorna a tabuada de multiplicação desse número, usando o laço for.
Antes de encerrar programa deve perguntar ao usuário se deseja continuar. Se a resposta for 'sim' o 
programa continua e pede outro número para efetuar a tabuada. Se a resposta for 'não' o programa é encerrado.
'''

print('Tabuada de multiplicação')
while True:
    num = float(input('Digite um número: '))
    i = 1
    for i in range(i, 10):
        print(f'{num:4} x {i} = {num*i}')
    print()
    #inicializando a variável 'resp' para entrar no laço
    resp = ' '
    #laço enquanto a resposta não for uma string que inicia com 's' ou 'n'
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()
print()
