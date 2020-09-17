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

#adicionando nova chave e valor ao dicionário
#   verificando pelo valor
if 'Manaus' not in estado.values():
    estado['capital'] = 'Manaus'

if 'Rio Branco' not in estado1.values():
    estado1['capital'] = 'Rio Branco'

if 'São Luis' not in estado3.values():
    estado3['capital'] = 'São Luis'

#adicionado nova chave e valor ao dicionário estado
#   verificando pela chave
if 'capital' not in estado2:
    estado2['capital'] = 'Belém'

print()
print(brasil)
print()
