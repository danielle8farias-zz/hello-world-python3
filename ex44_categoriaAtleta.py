'''
Leia o ano de nascimento de um atleta e defina sua categoria de acordo com
a idade.
até 9 anos = mirim
até 14 anos = infantil
até 19 anos = júnior
até 25 anos = sênior
acima de 25 = master
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

#função que faz a classificação do atleta
def classificacao(idade):
    if idade < 10:
        print('Classificação: Mirim')
    elif idade < 15:
        print('Classificação: Infantil')
    elif idade < 20:
        print('Classificação: Júnior')
    elif idade < 26:
        print('Classificação: Sênior')
    else:
        print('Classificação: Master')

#programa principal
cabecalho('CLASSIFICAÇÃO DE ATLETAS')
#date.today().year pega o ano do SO
atual = date.today().year
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    #fazendo a validação da idade
    if idade <= 0 or idade >= 100:
        print('Idade inválida! Digite novamente')
    else:
        print(f'Sua idade é {idade} anos.')
        classificacao(idade)
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
