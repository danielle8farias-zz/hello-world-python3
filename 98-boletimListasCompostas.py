'''
Crie um programa que leia os nomes e duas notas de vaŕios alunos, guardando tudo em uma lista
composta. Ao final, mostre o boletim contendo a média de cada aluno e permita que se possa ver
as notas de um determinado aluno escolhido individualmente.
'''
lista = []
while True:
    nome = input('Nome da(o) aluna(o): ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) /2
    lista.append([nome,[nota1,nota2],media])
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-='*30)
while True:
    opc = int(input('Mostrar nota de qual aluno? (-1 interrompe): '))
    if opc < 0:
        print(f'{"FINALIZANDO":^30}')
        break
    if opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('>'*30)
