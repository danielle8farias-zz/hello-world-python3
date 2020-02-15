#!/usr/bin/env python3.7
'''
Leia a altura e largura da parede em metros e calcule a área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro pinta 2m².
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula a área
def area(largura,altura):
    area = largura*altura
    return area

#função que calcula a quantidade de tinta
def quant_tinta(valor_area):
    quant_tinta = valor_area/2
    return quant_tinta

#programa principal
cabecalho('CÁLCULO DA QUANTIDADE DE TINTA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    largura = float(input('Informe a largura da parede(m): '))
    altura = float(input('Informe a altura da parede(m): '))
    valor_area = area(largura,altura)
    #:.2f limita o número de duas casas decimais
    print(f'A área da parede é {valor_area:.2f}m².')
    tinta = quant_tinta(valor_area)
    #:.2f limita o número de duas casas decimais
    print(f'A quantidade de tinta necessária é {tinta:.2f} litros.')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
