'''
Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada deve-se
perguntar ao usuário se quer ou não continuar. Ao final mostre:
Quantas pessoas têm mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres têm menos de 20 anos.
'''
print('-'*40)
print('CADASTRO DE PESSOA')
print('-'*40)
maior_de_dezoito = quantidade_homem = mulheres_menores = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maior_de_dezoito += 1
    genero = input('Digite o sexo: [F/M] ').upper().strip()[0]
    if genero in 'M':
        quantidade_homem += 1
    elif genero in 'F' and idade < 20:
        mulheres_menores += 1
    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha != 'S':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(maior_de_dezoito))
print('Ao todo temos {} homens cadastrados.'.format(quantidade_homem))
print('E temos {} mulheres com menos de 20 anos.'.format(mulheres_menores))
