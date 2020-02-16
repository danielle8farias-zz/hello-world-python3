#!/usr/bin/env python3.7
'''
Faça um programa para uma loja de tintas

O programa deve pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é 1 litro para cada 6 metros quadrados e
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
galões de 4 litros, que custam R$ 25.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
com apenas latas de 18 litros;
com apenas galões de 4 litros;
misturando latas e galões de forma que o preço seja menor

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha
from math import ceil

#programa principal
cabecalho('loja de tintas')
area = float(input('Tamanho da área (m²): '))
#redimento em litros
rendimento = area/6
#{:.2f} para duas casas decimais
print(f'Serão necessários {rendimento:.2f} litros de tinta.')
print()
linha()
print('-- Para latas de 18 litros cada:')
# 0.9 para deixar a folga de 10% em cada lata
# total de litros na lata real 16.2
folga = 18 * 0.9
print(f'Cada lata cabe = {folga} litros. Com folga de 10%.')
# divisão inteira pois não existe 1/2 lata
lata = ceil(rendimento//folga)
sobra_lata = rendimento%folga
preco_lata = lata * 80
print()
if rendimento <= folga:
    print('Total de latas: 1')
    print('Valor: R$ 80,00')
    print('Não há sobras.')
else:
    print(f'Total de latas: {lata}')
    print(f'Valor: R$ {preco_lata:.2f}')
    print(f'Houve uma sobra de: {sobra_lata:.2f} litros')
print()
print('-- Para galões de 4 litros cada:')
# 0.9 para deixar a folga de 10% em cada lata
# total de litros no galão real 3.6
folga = 4 * 0.9
print(f'Cada galão cabe = {folga} litros. Com folga de 10%.')
# divisão inteira pois não existe 1/2 galao
galao = ceil(rendimento//folga)
sobra_galao = rendimento%folga
preco_galao = galao * 25
print()
if rendimento <= folga:
    print('Total de galões: 1')
    print('Valor: R$ 25,00')
    print('Não há sobras.')
else:
    print(f'Total de galões: {galao}')
    print(f'Valor: R$ {preco_galao:.2f}')
    print(f'Houve uma sobra de: {sobra_galao:.2f} litros')
rodape()
