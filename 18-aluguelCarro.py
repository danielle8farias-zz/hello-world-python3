'''
Calcule o preço de um aluguel de um carro, sabendo que custa R$60,00
por dia e R$0,15 por quilômetro rodado.
'''
dias = int(input('Dias alugados: '))
km = float(input('Quilometros rodados: '))
preco = dias*60 + km*0.15
print('O total a pagar foi R${:.2f}'.format(preco))
