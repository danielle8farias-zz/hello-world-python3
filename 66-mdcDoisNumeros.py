'''
Dados dois números inteiros positivos, determinar o máximo divisor comum
entre eles usando o algoritmo de Euclides.
Exemplo: mdc(21, 15) = 3
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o máximo divisor comum
def mdc(num1, num2):
    #usando o algoritmo de Euclides
    div = num1 % num2
    while div != 0:
        troca = div
        num1 = num2
        num2 = troca
        div = num1 % num2
    return num2
    
#programa principal
cabecalho('MDC DE DOIS NÚMEROS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    #comparando os números
    if num1 > num2:
        print(f'M.D.C.({num1},{num2}) = {mdc(num1, num2)}')
    else:
        print(f'M.D.C.({num1},{num2}) = {mdc(num2, num1)}')
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
