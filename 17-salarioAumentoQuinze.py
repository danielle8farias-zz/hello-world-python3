'''
Leia o salário e o aumente em 15%.
'''
from mensagem import cabecalho
from mensagem import rodape

#função
def novo_salario(salario):
    novo_salario = salario + salario*0.15
    return novo_salario

#programa principal
cabecalho('SALÁRIO AUMENTO 15%')
while True:
    salario = float(input('Escreva o salário: R$'))
    valor_salario = novo_salario(salario)
    print(f'O novo salário com aumento de 15% é {valor_salario:.2f}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
rodape()
