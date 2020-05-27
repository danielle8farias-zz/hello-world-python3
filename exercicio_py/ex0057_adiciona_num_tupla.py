'''
Quatro números inteiros são guardados em uma tupla. Retorna quantos números 8 foram digitados. 
A posição do número 3, se houver e quais desses números na tupla são pares.
'''

tupla_num = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))

print(f'Você digitou os valores: {tupla_num}\n')

print('Procurando o número 8...')
print(f'O 8 apareceu {tupla_num.count(8)} vezes.\n')

print('Procurando o número 3...')
if 3 in tupla_num:
    print(f'O 3 está na {tupla_num.index(3) + 1} posição.\n')
else:
    print('Não há número 3.\n')

print('Os pares são: ', end='')
for i in tupla_num:
    if i % 2 == 0:
        print(i, end=' ')
print()
