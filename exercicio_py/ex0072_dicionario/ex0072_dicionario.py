
if 'Manaus' not in estado1.values():
    estado1['capital'] = 'Manaus'


#adicionado nova chave e valor ao dicionário estado2
if 'capital' not in estado2:
    estado2['capital'] = 'Belém'


print(brasil)
print('UF' in estado1)
print('UF' in estado2.keys())
print('Belém' in estado2.values())
print()

#usando o método get
print('usando método get')
print(estado1.get('sigla'))
