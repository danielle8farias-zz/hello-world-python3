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
rendimento = area/6
print(f'Será necessário {rendimento:.2f} litros de tinta.')

#cálculo para latas de 18 litros
# 0.9 para deixar a folga de 10% em cada lata
folga = 18 * 0.9 #16.2 litros
lata = ceil(rendimento//folga)
sobra_lata = (lata*18)-rendimento
if sobra_lata < 0:
    sobra_lata *= -1
preco_lata = lata * 80
linha()
print('Para latas de 18 litros cada:')
if rendimento < 18 or lata <= 1:
    print('Total de latas: 1')
    print('Valor: R$ 80,00')
    print('Não há sobras.')
elif sobra_lata < 18 or lata > 1:
    lata += 1
    preco_lata += 80
    print(f'Total de latas: {lata}')
    print(f'Valor: R$ {preco_lata:.2f}')
    print(f'Houve uma sobra de: {sobra_lata:.2f} litros')

#cálculo para galões de 4 litros
folga = 4 * 0.9 #16.2 litros
galao = ceil(rendimento//folga)
sobra_galao = (galao * 4)-rendimento
if sobra_galao < 0:
    sobra_galao *= -1
preco_galao = galao * 25
linha()
print('Para galões de 4 litros cada:')
if rendimento < 4 or galao <= 1:
    print('Total de galões: 1')
    print('Valor: R$ 25,00')
    print('Não há sobras.')
elif sobra_galao < 4 or galao > 1:
    galao += 1
    preco_galao += 25
    print(f'Total de galões: {galao}')
    print(f'Valor: R$ {preco_galao:.2f}')
    print(f'Houve uma sobra de: {sobra_galao:.2f} litros')

#incompleto
#misturando latas e galões de forma que o preço seja menor

rodape()