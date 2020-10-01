'''
Usuário lê nomes e duas notas de vários alunos. O programa retorna o boletim com, 
o nome, o número e a média de cada aluno. Ao final é permitido escolher 
o aluno pelo número para ver as notas individualmente. 
Os dados são armazenados em um dicionário.
'''

boletim = list()
estudante = dict()
notas = list()

while True:
    estudante['nome'] = input('Nome da(o) aluna(o): ')
    
    nota1 = float(input('1ª nota: '))
    notas.append(nota1)
    nota2 = float(input('2ª nota: '))
    notas.append(nota2)
    estudante['notas'] = notas[:]
    
    estudante['media'] = (nota1 + nota2)/2
    
    boletim.append(estudante.copy())
    estudante.clear()
    notas.clear()
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

print()
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for c, v in enumerate(boletim):
    print(f'{c:<4}{boletim[c]["nome"]:<10}{boletim[c]["media"]:>8.1f}')


while True:
    opcao = int(input('Mostrar nota de qual aluno? (99 interrompe): '))
    if opcao == 99:
        print(f'{"FINALIZANDO...":^30}')
        break
    if opcao <= len(boletim)-1:
        print(f'Notas de {boletim[opcao]["nome"]}: {boletim[opcao]["notas"]}')
print('>'*30)
