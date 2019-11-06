'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
Pergunta se o usuário quer mostrar mais termos.
Quando escolhido 0 termos o programa encerra.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula a P.A.
def prog_aritm():
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    #inicializando contador
    cont = 1
    An = A1
    total = 0
    mais = 10
    #inicialmente é mostrado 10 termos
    #2º laço: 'mais' é o número de termos a serem mostrados
    while mais != 0:
        #calculando total de termos
        total += mais
        #3º laço: contador não pode superar o total de termos
        while cont <= total:
            print(f'{An} - ', end='')
            An += r
            cont += 1
        print('PAUSA')
        #atualizando o número de termos
        mais = int(input('Quantos termos você quer mostrar a mais? '))
    print(f'Foram mostrados {total} termos.')

#programa principal
cabecalho('TERMOS DE UMA P.A.')
print('Para encerrar digite zero')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    prog_aritm()
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
