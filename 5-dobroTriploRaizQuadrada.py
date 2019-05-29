'''
Digite um número e mostro o dobro, o triplo e a raiz quadrada.
'''
from mensagem import cabecalho
from mensagem import rodape

#funções
def dobro(num):
    dobro = num*2
    return dobro


def triplo(num):
    triplo = num*3
    return triplo

def raiz(num):
    raiz = num**(1/2)
    return raiz

#programa principal
cabecalho('DOBRO, TRIPLO E RAÍZ QUADRADA')
while True:
    num = float(input('Digite um número: '))
    dobro_info = dobro(num)
    print(f'O dobro é: {dobro_info}')
    triplo_info = triplo(num)
    print(f'O triplo é: {triplo_info}')
    raiz_info = raiz(num)
    print(f'A raiz quadrada é: {raiz_info}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
rodape()
