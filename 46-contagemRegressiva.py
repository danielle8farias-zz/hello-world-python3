'''
Fazer uma contagem regressiva de 10 a 0.
'''
from time import sleep
print('-'*50)
print('{: ^50}'.format('CONTAGEM REGRESSIVA'))
print('-'*50)
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOM! BOOM!! POWW!!!')
