'''
Transforma metros em centímetros e milímetros.
'''
metros = float(input('Dê um valor em metros: '))

cent = metros*100
mil = metros*1000

print('{}m corresponde a {}cm'.format(metros, cent))
print()
print('{}m corresponde a {}mm'.format(metros, mil))
