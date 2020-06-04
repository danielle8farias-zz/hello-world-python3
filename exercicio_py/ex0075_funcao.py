'''
Funções que criam linhas e formatos de títulos.
'''

#criando função sem parâmetro
def mostra_linha():
    print('-'*50)


print('sistema de alunos')
#chamada da função
mostra_linha()

print('cadastro de funcionários')
mostra_linha()

print('erro no sistema')
mostra_linha()

#criando função com parâmetro
def titulo(msg):
    print(f'{msg.upper():^50}')

#chamada da função com passagem de parâmetro
titulo('sistema de alunos')


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

#empacotamento
def contador(*num):
    print(num)


contador(1, 2, 3)
contador(4,5)
contador(9, 8, 7, 6)

#o empacotamento cria tupla
def cont(*num):
    tamanho = len(num)
    print(f'Contém {tamanho} valores.')
    for v in num:
        print(f'{v}', end=' ')
    print()


cont(1, 2, 3)
cont(4,5)
cont(9, 8, 7, 6)
