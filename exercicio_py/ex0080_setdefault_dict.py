'''
verificando a chave e criando um valor com o método setdefault, em um dicionário.
'''

estado = {'UF': 'Amazonas', 'sigla': 'AM'}

#usando o método setdefault
#   retorna o valor da chave se houver
print(estado.setdefault('sigla'))
print()

#cria a chave se não houver, com o valor None se não for passado nada
print(estado.setdefault('area'))
print()

print(estado.setdefault('capital', 'Manaus'))
print(estado)
print()
