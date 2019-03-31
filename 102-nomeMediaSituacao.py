'''
Faça um programa que leia o nome e a média de um aluno, e retorne a situação. Esses dados devem
ser guardados em um dicionário. Ao final mostre o conteúdo da estrutura na tela.
'''
aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Recuperação'
print('-'*50)
for k,v in aluno.items():
    print(f'{k} = {v}')
print('-'*50)
