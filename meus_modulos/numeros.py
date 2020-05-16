'''
Funções para:
validar número float;
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
        except ValueError as erro:
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
        except ValueError as erro:
            #print() retorna uma string na tela
            print('Digite um número inteiro!')
            #volta para o início do laço
            continue
        #se o 'try' for válido        
        else:
            #retorna valor de mes
            return num
