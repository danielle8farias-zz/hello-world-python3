'''
Usuário informa a altura e largura de uma parede que será pintada. 
Programa retorna a área e a quantidade de tinta necessária para pintar essa área, 
sabendo que o rendimento da tinta é de 2m² por litro.
'''

alt = float(input('Digite a altura(m): '))
larg = float(input('Digite a largura(m): '))

#calculando área
area = alt * larg
print(f'Área: {area}m²')

quant = area / 2
#.2f mostra apenas duas casas de ponto flutuante
print(f'Quantidade de tinta necessária: {quant:.2f} litros.')
print()
