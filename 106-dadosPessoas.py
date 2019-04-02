'''
Crie um dicionário que leia o nome, sexo e idade de várias pessoas, guardando esses dados em
uma lista. Ao final, mostre: Quantas pessoas cadastradas, a média de idades, uma lista com
as mulheres, uma lista com as pessoas com a idade acima da média.
'''
dados = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [F/M] ').upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO. Digite F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO. Responda S ou N.')
    if resp == 'N':
        break
print('-'*50)
print(f'Pessoas cadastradas: {len(dados)}')
media = soma/len(dados)
print(f'Média das idades: {media:.2f}')
print('As mulheres são:')
for p in dados:
    if p['sexo'] == 'F':
        print(p['nome'])
print('Pessoas acima da média: ')
for p in dados:
    if p['idade'] > media:
        print(p['nome'])
