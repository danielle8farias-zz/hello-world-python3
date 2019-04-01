'''
Faça um programa que leia o nome, ano de nascimento e carteira de trabalho; registrando tudo
em um dicionário. Se o CTPS for diferente de zero, o dicionário reeberá também o ano de
contratação e o salário. Calcule e registre com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('salário: R$ '))
    dados['aposentadoria'] = ((dados['contratacao'] + 35) - datetime.now().year) + dados['idade']
print('-'*50)
for k,v in dados.items():
    print(f'{k} = {v}')
