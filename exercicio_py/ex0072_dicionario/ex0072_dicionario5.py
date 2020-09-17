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

#checando as chave de um dicionário
if 'UF' in estado2:
    print(f'O estado {estado2["UF"]} já foi adicionado.')
else:
    print(False)
print()

if 'UF' in estado1.keys():
    print(f'O estado {estado1["UF"]} já foi adicionado.')
else:
    print(False)
print()

#checando o valor
if 'Amazonas' in estado.values():
    print(f'O estado {estado["UF"]} já foi adicionado.')
else:
    print(False)
print()

if 'AM' in estado:
    print(f'O estado {estado["sigla"]} já foi adicionado.')
else:
    print(False)
