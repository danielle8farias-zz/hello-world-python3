'''
Simulador de caixa eletrônico. Usuário informa o valor que deseja sacar. 
O programa retorna quantas cédulas de cada valor serão entregues. 
O caixa possui cédulas de 50, 20, 10 e 1.
'''

print('Caixa eletrônico')
print()

saque = int(input('Quanto deseja sacar? R$'))

#separando as cédulas de R$50
if saque >= 50:
    cedulas = saque // 50
    print(f'{cedulas} cédulas de R$50')
    #atualizando valor que sobrou do saque
    saque = saque % 50
#separando as cédulas de R$20
if saque >= 20:
    cedulas = saque // 20
    print(f'{cedulas} cédulas de R$20')
    #atualizando valor que sobrou do saque
    saque = saque % 20
#separando as cédulas de R$10
if saque >= 10:
    cedulas = saque // 10
    print(f'{cedulas} cédulas de R$10')
    #atualizando valor que sobrou do saque
    saque = saque % 10
#separando as cédulas de R$1
if saque >= 1:
    cedulas = saque // 1
    print(f'{cedulas} cédulas de R$1')
