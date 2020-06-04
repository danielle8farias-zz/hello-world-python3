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
