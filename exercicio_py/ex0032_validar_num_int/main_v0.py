#criando a função
def ler_num_int(n: int) -> int:
    '''
    função que faz a validação de uma entrada; verificando se é um número inteiro.
    '''
    try:
        #int() convertendo tipo inteiro
        #atribuindo valor à variável 'num'
        num = int(n)
    #criando exceção
    #   caso o valor digitado seja diferente de um número
    except ValueError:
        #print() retorna uma string na tela
        print('Digite um número inteiro!')
    #se o 'try' for válido        
    else:
        #retorna o próprio valor
        return num


if __name__ == '__main__':
    #chamadas da função
    #lendo string como entrada da função
    print(ler_num_int('danielle8farias'))
    #lendo string (que pode ser convertida num inteiro) como entrada da função
    print(ler_num_int('13'))
    print(ler_num_int(2008))
