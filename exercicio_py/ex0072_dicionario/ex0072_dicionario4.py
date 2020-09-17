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

for i in brasil:
    #mostrando apenas os valores dentro do dicionário (sem as chaves)
    for v in i.values():
        print(v, end=' ')
    print()
