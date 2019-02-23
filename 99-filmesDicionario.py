filme = {'título': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
        }

filme1 = {'título': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
        }

filme2 = {'título': 'Man of Steel',
        'ano': 2013,
        'diretor': 'Zack Snyder'
        }

print(filme.values())
print()
print(filme.keys())
print()
print(filme.items())
print()
print(filme)
print()
for k,v in filme.items():
    print(f'O {k} é {v}')
print()

locadora = [filme, filme1, filme2]
print(locadora[0]['ano'])
print(locadora[2]['título'])
