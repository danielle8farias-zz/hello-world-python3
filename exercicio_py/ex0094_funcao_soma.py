'''
Funções que somam dois inteiros.
'''

#função que soma duas variáveis
def soma(n1, n2):
    #retorna a soma dos parâmetros
    return n1 + n2

print(soma(4, 5))

#o retorno da função deve ser guardado numa variável para uso posterior
resultado = soma(3, 3)
print(resultado)

def outra_soma(n1, n2):
    print(f'1º valor: {n1}')
    print(f'2º valor: {n2}')
    return n1 + n2


resultado = outra_soma(5, 3)
print(resultado)

#para trocar a ordem dos parâmetros é preciso deixar explícito
resultado = outra_soma(n2=5, n1=3)
print(resultado)
