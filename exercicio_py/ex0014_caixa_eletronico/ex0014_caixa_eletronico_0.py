########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Simulador de um caixa eletrônico. Usuário informa o valor que deseja sacar e programa retorna a quantidade de cédulas que serão entregues.
########

print('Caixa eletrônico\n')
saque = int(input('Quanto deseja sacar? R$'))

#separando as cédulas de R$200
if saque >= 200:
    cedulas = saque // 200
    print(f'{cedulas} cédulas de R$200')
    #atualizando valor que sobrou do saque
    saque = saque % 200
#separando as cédulas de R$100
if saque >= 100:
    cedulas = saque // 100
    print(f'{cedulas} cédulas de R$100')
    #atualizando valor que sobrou do saque
    saque = saque % 100
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
#separando as cédulas de R$5
if saque >= 5:
    cedulas = saque // 5
    print(f'{cedulas} cédulas de R$5')
#separando as cédulas de R$2
if saque >= 2:
    cedulas = saque // 2
    print(f'{cedulas} cédulas de R$2')
