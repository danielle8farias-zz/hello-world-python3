########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Funções para:
#           validar número float;
#           validar número inteiro;
#           validar o divisor da operação de divisão;
#           validar índice de raízes;
#           validar números naturais;
########

def ler_num_float(n):
    '''
    Validação todo o conjuntos dos números reais
    '''
    while True:
        try:
            num = float(input(n))
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            return num


def ler_num_int(n):
    '''
    Valida números inteiros positivos ou negativos.
    '''
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #int() convertendo a string recebida para tipo inteiro
            #atribuindo valor à variável 'num'
            num = int(input(n))
        #criando exceção
        #   caso o valor digitado seja diferente de um número
        except ValueError:
            #print() retorna uma string na tela
            print('Digite um número inteiro!')
            #volta para o início do laço
            continue
        #se o 'try' for válido        
        else:
            #retorna valor de mes
            return num


def ler_divisor(n):
    while True:
        '''
        Valida divisor. Não aceita zero.
        '''
        try:
            num = float(input(n))
            if num == 0:
                raise Exception('Não é possível dividir por 0.')
        except ValueError:
            print('Digite um número.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return num


def ler_indice(n):
    '''
    valida índice de uma raiz.
    Deve ser maior ou igual a 2
    '''
    while True:
        try:
            num = int(input(n))
            if num < 2:
                raise Exception('Índice deve ser maior ou igual a 2')
        except ValueError:
            print('Digite um número inteiro.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return num


def ler_num_nat(n):
    '''
    aceita somente números naturais
    '''
    while True:
        try:
            num = int(input(n))
            if num < 0:
                raise Exception('Digite um número maior ou igual a zero.')
        except ValueError:
            print('Apenas números naturais.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return num

