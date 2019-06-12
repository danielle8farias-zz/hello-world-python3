'''
Pede a idade do carro. Se menor ou igual a 3 anos, o carro é novo.
Senão o carro é velho.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('carro novo ou antigo?')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    tempo = int(input('Quantos anos tem seu carro? '))
    if tempo <= 3:
        print('Carro novo')
    else:
        print('Carro velho')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()

