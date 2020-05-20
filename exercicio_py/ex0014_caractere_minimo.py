'''
Usuário informa uma frase e programa retorna a mesma com pelo menos 20 caracteres.
'''

frase = input('Digite uma frase: ')
#len() retorna o tamanho da string
print(f'{len(frase)}')
#caso seja menor do que 20, será preenchido com espaços
print(f'{frase:20}!')
print()
