'''
Leia nome, idade e sexo de 4 pessoas. Mostre a média de idade do grupo.
Qual é o homem mais velho. Quantas mulheres têm menos de 20 anos.
'''
somaidade = 0
velho = ''
maior = 0
menos_vinte = 0
for n in range(1,5):
    print('-'*10,' {}ª PESSOA '.format(n),'-'*10)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = input('Sexo(F/M): ').strip()
    if n == 1 and sexo in 'mM':
        velho = nome
    if sexo in 'mM' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        menos_vinte += 1

media = somaidade/4
print()
print('A média das idades é {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('{} mulheres têm menos de 20 anos.'.format(menos_vinte))
