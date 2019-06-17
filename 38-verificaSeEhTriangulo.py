'''
Leia o comprimento de 3 retas e verifique se é possível formar um
triângulo. Também deve indicar de que tipo é o triângulo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que verifica e identifica o triângulo
def verifica_triangulo(lado1, lado2, lado3):
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        if lado1 == lado2 and lado2 == lado3:
            print('Triângulo Equilátero: três lados iguais.')
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Triângulo Isósceles: quaisquer dois lados iguais.')
        else:
            print('Triângulo Escaleno: três lados diferentes.')
    else:
        print('Esses valores não formam um triângulo.')

#programa principal
cabecalho('VERIFICA SE É TRIÂNGULO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    lado1 = float(input("Digite o 1º lado do triângulo: "))
    lado2 = float(input("Digite o 2º lado do triângulo: "))
    lado3 = float(input("Digite o 3º lado do triângulo: "))
    verifica_triangulo(lado1, lado2, lado3)
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
