'''
Leia o ano de nascimento de 7 pessoas. Mostre quantas são maiores de 21
e quantas são menores.
'''
#importando parte do código
from datetime import date
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('maiores e menores de 21 anos')
#date.today().year pega o ano do sistema operacional
atual = date.today().year
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    maior = 0
    menor = 0
    #laço de 1 até 7
    for pessoas in range(1, 8):
        nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
        idade = atual - nasc
        print(f'Essa pessoa tem {idade} anos.')
        if idade >= 21:
            maior += 1
        else:
            menor += 1
    print(f'Existem {maior} pessoas maiores de idade.')
    print(f'Existem {menor} pessoas menores de idade.')
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
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
