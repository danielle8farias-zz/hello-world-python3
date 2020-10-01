'''
Usando o método get em um dicionário.
'''

estado = {'UF': 'Amazonas', 'sigla': 'AM'}

#usando o método get
print(estado.get('sigla'))
print()

print(estado.get('Area'))
print()

#usando o get com o argumento padrão, caso não seja encontrado no dicionário
print(estado.get('Area', 'não informada'))
print()

print(estado.get('UF', 'não informado'))
print()
