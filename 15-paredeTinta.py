'''
Leia a altura e largura da parede em metros e calcule a área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro pinta 2m².
'''
from mensagem import cabecalho
from mensagem import rodape

#funções
def area(largura,altura):
    area = largura*altura
    return area


def quant_tinta(valor_area):
    quant_tinta = valor_area/2
    return quant_tinta

#programa principal
cabecalho('CÁLCULO DA QUANTIDADE DE TINTA')
while True:
    largura = float(input('Informe a largura da parede: '))
    altura = float(input('Informe a altura da parede: '))
    valor_area = area(largura,altura)
    print(f'A área da parede é {valor_area}m².')
    tinta = quant_tinta(valor_area)    
    print(f'A quantidade de tinta necessária é {tinta:.2f} litros.')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
