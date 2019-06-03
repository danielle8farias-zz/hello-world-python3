'''
Digite algo e mostre a tipagem da mesma.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TIPO DE DADO')
while True:
    a = input('Digite algo: ')
    print('O tipo primitivo desse valor é', type(a))
    print('Só tem espaços?', a.isspace())
    print('É um número?', a.isnumeric())
    print('É composto de letras?', a.isalpha())
    print('Ele é alfanumérico?', a.isalnum())
    print('Está em maiúsculas?', a.isupper())
    print('Está em minúsculas?', a.islower())
    print('Está capitalizada?', a.istitle())
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
