estado = {}
brasil = []
for c in range(3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
