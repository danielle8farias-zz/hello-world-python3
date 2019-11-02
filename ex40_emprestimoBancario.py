'''
Escreva um programa para aprovação de empréstimo bancário para compra de uma
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
vai pagar. A prestação será negada se exceder 30% do salário do comprador.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula a prestação mensal e se o empréstimo foi aprovado
def prestacao(valor_casa, anos, salario):
    prestacao_mensal = valor_casa / (anos * 12)
    #:.2f limita o número de duas casas decimais
    print(f'O valor da prestação mensal será de R${prestacao_mensal:.2f}')
    if prestacao_mensal < (salario * 0.3):
        print('Empréstimo aprovado!')
    else:
        print('Empréstimo negado.')

#programa principal
cabecalho('APROVAÇÃO DE EMPRÉSTIMO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    valor_casa = float(input('Valor da casa que deseja comprar: R$ '))
    salario = float(input('Salário do comprador: R$ '))
    anos = int(input('Em quantos anos pretende pagar? '))
    prestacao(valor_casa, anos, salario)
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
