'''
Leia o salário de um funcionário. Se for superior a R$1.250,00 calcule
o aumento de 10%. Senão, o aumento é de 15%.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o aumento do salário
def f_salario(salario):
    if salario <= 1250:
        novo = salario + (salario * 0.15)
        print('Aumento de 15%')
    else:
        novo = salario + (salario * 0.10)
        print('Aumento de 10%')
    print(f'O salário novo é R${novo:.2f}')

#programa principal
cabecalho('AUMENTO SALARIAL 10 OU 15%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    salario = float(input('Salário atual do funcionário: R$'))
    f_salario(salario)
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

