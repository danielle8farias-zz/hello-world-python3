'''
Transforma metros em centímetros e milímetros.
'''
from mensagem import cabecalho
from mensagem import rodape

#função
def transforme(metros):
    cent = metros*100
    mil = metros*1000
    return cent, mil

#programa principal
cabecalho('CONVERSOR DE METROS PARA CM E MM')
while True:
    metros = float(input('Dê um valor em metros: '))
    centimetro, milimetro = transforme(metros)
    print()
    print(f'{metros}m corresponde a {centimetro}cm')
    print(f'{metros}m corresponde a {milimetro}mm')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
rodape()
