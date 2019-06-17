'''
Fazer uma contagem regressiva de 10 a 0.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from time import sleep

#programa principal
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    cabecalho('CONTAGEM REGRESSIVA')
    #2º laço que começa em 10 até 0 com passo -1
    for cont in range(10, -1, -1):
        print(cont)
        #pausa de 1 segundo
        sleep(1)
    print('BOM! BOOM!! POWW!!!')
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
