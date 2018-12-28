galera = []
dado = []
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

maior = menor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Total de maiores: {maior}')
print(f'Total de menores: {menor}')
