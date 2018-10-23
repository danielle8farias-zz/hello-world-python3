'''
Leia a altura e largura da parede em metros e calcule a área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro pinta 2m².
'''
print('-'*50)
print('{: ^50}'.format('CÁLCULO DA QUANTIDADE DE TINTA'))
print('-'*50)
while True:
    largura = float(input('Informe a largura da parede: '))
    altura = float(input('Informe a altura da parede: '))
    area = largura*altura
    print('A área da parede é {}m².'.format(area))
    tinta = area/2
    print('A quantidade de tinta necessária é {:.2f} litros.'.format(tinta))
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
