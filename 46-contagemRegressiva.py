'''
Fazer uma contagem regressiva de 10 a 0.
'''
from mensagem import cabecalho
from mensagem import rodape
from time import sleep

cabecalho('CONTAGEM REGRESSIVA')

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOM! BOOM!! POWW!!!')

rodape()
