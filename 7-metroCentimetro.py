'''
Transforma metros em centímetros e milímetros.
'''
print('-'*50)
print('{: ^50}'.format('CONVERSOR PARA CM E MM'))
print('-'*50)
metros = float(input('Dê um valor em metros: '))
cent = metros*100
mil = metros*1000
print('{}m corresponde a {}cm'.format(metros, cent))
print()
print('{}m corresponde a {}mm'.format(metros, mil))
