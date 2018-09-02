'''
Fazer uma contagem regressiva de 10 a 0.
'''
from time import sleep
print('{:=^10}'.format(' Contagem regressiva '))
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOM! BOOM!! POWW!!!')
