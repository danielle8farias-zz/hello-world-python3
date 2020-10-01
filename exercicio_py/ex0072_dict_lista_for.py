'''
Criando dicionário, com as unidades federativas do Brasil, dentro de uma lista com o laço for.
'''

#criando dicionário
estado = {}
#criando lista
brasil = []

for i in range(3):
    estado['UF'] = input('Digite o nome do estado: ').capitalize()
    estado['sigla'] = input('Digite a sigla do estado: ').upper()
    #fazendo a cópia do dicionário
    brasil.append(estado.copy())
print()

print(brasil)
print()
