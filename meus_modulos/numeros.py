'''
Funções para:
validar número float;
validar número inteiro;
validar o divisor da operação de divisão;
'''

#função que captura um número informado pelo usuário para validação
def ler_num_float(n):
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #float() convertendo a string recebida para tipo flutuante
            #atribuindo valor à variável 'num'
            num = float(input(n))
        #criando exceção
        #   caso o valor digitado seja diferente de um número
        except ValueError:
            #print() retorna uma string na tela
            print('Digite um valor válido!')
            #volta para o início do laço
            continue
        #se o 'try' for válido        
        else:
            #retorna valor de mes
            return num


def ler_num_int(n):
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #float() convertendo a string recebida para tipo flutuante
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
    valida índice de uma raiz
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

