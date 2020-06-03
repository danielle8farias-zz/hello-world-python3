'''
Dicionário com as unidades federativas do Brasil.
'''

#criando dicionário
estado = dict()
brasil = list()

for i in range(3):
    estado['UF'] = input('Digite o nome do estado: ')
    estado['sigla'] = input('Digite a sigla do estado: ')
    #fazendo a cópia do dicionário
    brasil.append(estado.copy())
print()

print(brasil)
print()

estado1 = {'UF': 'Amazonas', 'sigla': 'AM'}
brasil.append(estado1)

for i in brasil:
    print(i)
print()

estado2 = {'UF': 'Pará',
        'sigla': 'PA'}
brasil.append(estado2)

for i in brasil:
    #mostrando itens do dicionário; com chave e valor
    for c, v in i.items():
        print(f'{c}: {v}')
print()

for i in brasil:
    #mostrando apenas os valores dentro do dicionário (sem as chaves)
    for v in i.values():
        print(v, end=' ')
    print()
print()