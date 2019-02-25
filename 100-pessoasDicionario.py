pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)

print()
print(pessoas['nome'])

print()
print(pessoas['idade'])

print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print()
print(pessoas.keys())

print()
print(pessoas.values())

print()
print(pessoas.items())

print()
for k in pessoas.keys():
    print(k)

print()
for v in pessoas.values():
    print(v)

print()
for k,v in pessoas.items():
    print(f'{k} = {v}')

print()
del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['nome'] = 'Leandro'
for k,v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} = {v}')
