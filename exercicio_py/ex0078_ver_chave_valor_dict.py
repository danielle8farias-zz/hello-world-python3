'''
Verificando a existência de uma chave ou valor, com retorno booleano, em um dicionário.
'''

estado = {}
brasil = []

estado = {'UF': 'Amazonas', 'sigla': 'AM'}
estado1 = {'UF': 'Acre', 'sigla': 'AC'}
estado2 = {'UF': 'Pará', 'sigla': 'PA'}
estado3 = {'UF': 'Maranhão', 'sigla': 'MA'}

brasil.append(estado)
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

#verifcando se existe a chave 'UF' em estado1
#   retorna um booleano
print('UF' in estado1)

print('UF' in estado2.keys())

#verificando a existência do valor 'Belém" em estado2
print('Belém' in estado2.values())
print()
