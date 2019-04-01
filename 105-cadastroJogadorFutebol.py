cadastro = {}
partidas = []
cadastro['nome'] = input('Nome do jogador: ')
n = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for i in range(n):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    partidas.append(gols)
cadastro['gols'] = partidas[:]
cadastro['total'] = sum(partidas)
print('-'*50)
print(cadastro)
print('-'*50)
for k,v in cadastro.items():
    print(f'{k} = {v}')
print('-'*50)
print(f'O jogador {cadastro["nome"]} jogou {n} partidas.')
for i in range(n):
    print(f'Na partida {i+1} fez {partidas[i]} gols.')
print('-'*50)
print(f'Total de gols = {cadastro["total"]}')
print('-'*50)
