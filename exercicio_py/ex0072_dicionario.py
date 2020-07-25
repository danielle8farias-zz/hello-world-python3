'''
Dicionário com as unidades federativas do Brasil.
'''

#criando dicionário
estado = {}
brasil = []

for i in range(3):
    estado['UF'] = input('Digite o nome do estado: ').capitalize()
    estado['sigla'] = input('Digite a sigla do estado: ').upper()
    #fazendo a cópia do dicionário
    brasil.append(estado.copy())
print()

print(brasil)
print()

estado1 = {'UF': 'Amazonas', 'sigla': 'AM'}
brasil.append(estado1)

print('mostrando cada dicionário dentro da lista')
for i in brasil:
    print(i)
print()

estado2 = {'UF': 'Pará',
        'sigla': 'PA'}
brasil.append(estado2)

print('mostrando itens do dicionário; com chave e valor')
for i in brasil:
    #mostrando itens do dicionário; com chave e valor
    for c, v in i.items():
        print(f'{c}: {v}')
print()

print('mostrando apenas os valores dentro do dicionário (sem as chaves)')
for i in brasil:
    #mostrando apenas os valores dentro do dicionário (sem as chaves)
    for v in i.values():
        print(v, end=' ')
    print()
print()

#checando a chave
if 'UF' in estado2:
    print(f'O estado {estado2["UF"]} já foi adicionado.')

if 'UF' in estado1.keys():
    print(f'O estado {estado1["UF"]} já foi adicionado.')

#checando o valor
if 'Manaus' not in estado1.values():
    estado1['capital'] = 'Manaus'


#adicionado nova chave e valor ao dicionário estado2
if 'capital' not in estado2:
    estado2['capital'] = 'Belém'


print(brasil)
print('UF' in estado1)
print('UF' in estado2.keys())
print('Belém' in estado2.values())
