'''
Leia o nome completo e retorne apenas o primeiro e o último nome.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('Retornando o primeiro e último nome')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip() remove os espaços no começo e no fim
    nome = input('Digite seu nome completo: ').strip()
    #split() transforma a string em lista
    n = nome.split()
    #[0] pegando o primeiro item da lista
    print(f'Seu primeiro nome é: {n[0]}')
    #[-1] pegando o último item da lista
    print(f'Seu último nome é: {n[-1]}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
