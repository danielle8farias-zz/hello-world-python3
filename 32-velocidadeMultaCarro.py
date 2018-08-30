'''
Leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre
a mensagem informando que foi multado.
A multa deve custar R$7,00 por cada Km acima do limite.
'''
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
