import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat


def primo():
    ler_cabecalho('número primo')
    n = ler_num_nat("Digite um número inteiro: ")
    i = 0
    c = 0
    while i < n:
        i+= 1
        if (n % i == 0):
            c += 1
    if c == 2:
        print('É PRIMO!')
    else:
        print("não é primo")
    print()

