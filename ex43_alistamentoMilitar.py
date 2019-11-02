'''
Informe o ano de nascimento e retorne se o usuário precisa se alistar e
quanto tempo falta.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from datetime import date

#função que confere a condição de alistamento de acordo com a idade
def alistamento(idade):
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos.')
        print(f'Faltam {saldo} anos para seu alistamento.')
    else:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos')
    
#programa principal
cabecalho('ALISTAMENTO MILITAR')
#date.today().year pega o ano do SO
atual = date.today().year
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    nasc = int(input('Seu ano de nascimento: '))
    idade = atual - nasc
    print(f'Sua idade é {idade} anos')
    alistamento(idade)
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
