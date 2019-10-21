'''
Dados os catetos, calcule o valor da hipotenusa.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

#função que calcula a hipotenusa
def hipotenusa(b,c):
    a = sqrt(b**2 + c**2)
    return a

#programa principal
cabecalho('CÁLCULO DA HIPOTENUSA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    b = float(input('Digite o primeiro cateto: '))
    c = float(input('Digite o segundo cateto: '))
    h = hipotenusa(b,c)
    #:.2f limita o número de duas casas decimais
    print(f'O valor da hipotenusa é: {h:.2f}')
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

'''
Também pode ser feito assim:
from math import hypot
a = hypot(b, c)
'''