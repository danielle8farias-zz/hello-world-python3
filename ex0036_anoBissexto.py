'''
Leia um ano qualquer e verifique se é bissexto.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula se o ano é bissexto
def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} NÃO é bissexto.')

#programa principal
cabecalho('ANO BISSEXTO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    ano = int(input('Informe o ano: '))
    ano_bissexto(ano)
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
