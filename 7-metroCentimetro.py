'''
Transforma metros em centímetros e milímetros.
'''
print('-'*50)
print('{: ^50}'.format('CONVERSOR DE METROS PARA CM E MM'))
print('-'*50)
while True:
    metros = float(input('Dê um valor em metros: '))
    cent = metros*100
    mil = metros*1000
    print()
    print('{}m corresponde a {}cm'.format(metros, cent))
    print('{}m corresponde a {}mm'.format(metros, mil))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
