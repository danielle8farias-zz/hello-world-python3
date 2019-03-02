'''
Leia o comprimento de 3 retas e veriique se é possível formar um
triângulo. Também deve indicar de que tipo é o triângulo.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('VERIFICA SE É TRIÂNGULO')

while True:
    lado1 = float(input("Digite o 1º lado do triângulo: "))
    lado2 = float(input("Digite o 2º lado do triângulo: "))
    lado3 = float(input("Digite o 3º lado do triângulo: "))
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        if lado1 == lado2 and lado2 == lado3:
            print("Triângulo Equilátero: três lados iguais.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triângulo Isósceles: quaisquer dois lados iguais.")
        else:
            print("Triângulo Escaleno: três lados diferentes.")
    else:
        print("Esses valores não formam um triângulo.")
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
