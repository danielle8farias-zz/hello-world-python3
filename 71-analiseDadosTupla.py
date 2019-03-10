'''
Leia quatro valores pelo teclado e armazene em uma tupla. Verifique:
- quantas vezes apareceu o valor 9;
- posição do primeiro valor 3;
- quais foram os números pares.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('ANÁLISE DE DADOS EM UMA TUPLA')

num = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))
print(f'Os números digitados foram: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('Não há número 3.')
print('Os valores pares são: ',end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' - ')
print()

rodape()
