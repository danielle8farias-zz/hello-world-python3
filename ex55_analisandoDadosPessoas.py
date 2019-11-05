'''
Leia nome, idade e sexo de 4 pessoas. Mostre a média de idade do grupo.
Qual é o homem mais velho. Quantas mulheres têm menos de 20 anos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('Analisando dados de pessoas')
soma_idade = 0
velho = ''
maior = 0
menos_vinte = 0
#laço que vai de 1 a 4
for n in range(1,5):
    print('-'*10,f' {n}ª PESSOA ','-'*10)
    #strip: remove os espaços no começo e no fim
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    #somando as idades
    soma_idade += idade
    sexo = input('Sexo(F/M): ').strip()
    if n == 1 and sexo in 'mM':
        velho = nome
    if sexo in 'mM' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        menos_vinte += 1
media = soma_idade/4
print()
print(f'A média das idades é {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {velho}.')
print(f'{menos_vinte} mulheres têm menos de 20 anos.')
rodape()
