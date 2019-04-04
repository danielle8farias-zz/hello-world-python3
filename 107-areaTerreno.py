'''
Usando função, calcule a área de um terreno.
'''
from mensagem import cabecalho
from mensagem import rodape

def area(a, b):
    area = a * b
    print(f'Área: {area} m².')    


cabecalho('área de terreno')

while True:
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    area(largura, comprimento)
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
