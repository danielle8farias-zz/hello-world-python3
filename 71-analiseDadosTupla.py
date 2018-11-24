'''
Leia quatro valores pelo teclado e armazene em uma tupla. Verifique:
- quantas vezes apareceu o valor 9;
- posição do primeiro valor 3;
- quais foram os números pares.
'''
print('-'*50)
print('{: ^50}'.format('ANÁLISE DE DADOS EM UMA TUPLA'))
print('-'*50)
num = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))
print('Os números digitados foram: {}'.format(num))
print('O valor 9 apareceu {} vezes.'.format(num.count(9)))
if 3 in num:
    print('O valor 3 apareceu na {}ª posição.'.format(num.index(3)))
else:
    print('Não há número 3.')
print('Os valores pares são: ',end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' - ')
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
