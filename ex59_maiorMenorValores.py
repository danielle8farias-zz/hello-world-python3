'''
Leia vários números inteiros. No final da execução mostre a média entre eles
e qual foi o maior e o menor valor lido.
O programa deve perguntar se o usuário quer continuar ou não a digitar mais
valores.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('soma, média, maior e menor')
resp = 'S'
#inicializando as variáveis com zero
soma = cont = media = maior = menor = 0
#1º laço fazendo o programa rodar até que o usuário decida parar
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    #[0] captura apenas o primeiro caractere
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
media = soma/cont
print()
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
rodape()
