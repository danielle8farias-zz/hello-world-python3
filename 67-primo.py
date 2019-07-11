'''
Verificar se um número inteiro é primo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o número primo
def primo(n):
    i = c = 0
    #enquanto i for menor do que o número dado pelo usuário
    while i < n:
        #incrementa i
        i+= 1
        #verifica se n é dividido por i
        if (n % i == 0):
            #incrementa c que é o números de vezes que n foi dividido por i
            c += 1
    #se um número é dividido por apenas dois números (1 e ele mesmo), então é primo
    if c == 2:
        print('É PRIMO!')
    #se é dividido por mais de dois números não é primo
    else:
        print("não é primo")

#programa principal
cabecalho('É PRIMO?')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    n = int(input("Digite um número inteiro: "))
    primo(n)
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
