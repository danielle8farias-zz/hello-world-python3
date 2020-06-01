'''
Outra maneira de fazer o ex0070.

Usuário lê nomes e duas notas de vários alunos. O programa guarda os dados numa lista composta. 
Retorna o boletim com, o nome, o número e a média de cada aluno. Ao final é permitido escolher 
o aluno pelo número para ver as notas individualmente.
'''

boletim = []

while True:
    nome = input('Nome da(o) aluna(o): ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))

    media = (nota1 + nota2)/2
    #adicionando lista composta dentro da lista 'boletim'
    boletim.append([nome,[nota1,nota2],media])
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

print()
print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for c, v in enumerate(boletim):
    print(f'{c:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-='*15)
print()

while True:
    opcao = int(input('Mostrar nota de qual aluno? (99 interrompe): '))
    if opcao == 99:
        print(f'{"FINALIZANDO...":^30}')
        break
    if opcao <= len(boletim)-1:
        print(f'Notas de {boletim[opcao][0]}: {boletim[opcao][1]}')
print('>'*30)
