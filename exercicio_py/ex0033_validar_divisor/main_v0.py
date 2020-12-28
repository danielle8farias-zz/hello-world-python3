########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Fazendo a validação de um divisor.
########

def ler_divisor(n: int) -> int:
    '''
    Função que valida a entrada de um divisor
    '''
    try:
        #float() converte número para Real
        #variável 'num' recebe o valor convertido
        num = float(n)
        #verificando se o número é igual a zero
        if num == 0:
            #criando exceção, caso expressão acima seja verdadeira
            raise Exception('Não é possível dividir por 0.')
    #dispara exceção, caso a entrada não seja um número
    except ValueError:
        #print() imprime uma mensagem na tela
        print('Digite um número.')
    #dispara exceção criada
    except Exception as erro:
        print(f'Valor inválido: {erro}')
    #se o 'try' for válido retorna o próprio valor, convertido
    else:
        return num


if __name__ == '__main__':
    #chamadas da função
    #lendo número zero como entrada da função
    print(ler_divisor(0))
    print(ler_divisor('0'))
    print(ler_divisor(2))
