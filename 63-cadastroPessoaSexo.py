'''
Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada deve-se
perguntar ao usuário se quer ou não continuar. Ao final mostre:
Quantas pessoas têm mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres têm menos de 20 anos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('CADASTRO DE PESSOAS')
#inicializando variáveis
maior_de_dezoito = quantidade_homem = mulheres_menores = 0
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maior_de_dezoito += 1
    genero = ' '
    #laço até que seja digitado um dos dois valores válidos
    while genero not in 'FM':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        genero = input('Digite o sexo: [F/M] ').upper().strip()[0]
    if genero in 'M':
        quantidade_homem += 1
    elif genero in 'F' and idade < 20:
        mulheres_menores += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha == 'N':
        #quebrando o 1º laço
        break
print(f'Total de pessoas com mais de 18 anos: {maior_de_dezoito}')
print(f'Ao todo temos {quantidade_homem} homens cadastrados.')
print(f'E temos {mulheres_menores} mulheres com menos de 20 anos.')
rodape()
