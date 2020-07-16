import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_nat


def verificar_primo(n):
    raiz = int(n ** (0.5))
    for divisor in range(2, raiz+1):
        if n % divisor == 0:
            return False
    return True


def primo():
    ler_cabecalho('número primo')
    n = ler_num_nat("Digite um número inteiro: ")
    resultado = verificar_primo(n)
    if resultado:
        print('É PRIMO!')
    else:
        print("não é primo")
    print()

