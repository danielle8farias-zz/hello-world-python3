'''
Leia o nome e o preço de vários produtos. O programa deve perguntar se o
usuário deseja continuar a cada inserção. Ao final, mostre:
Total de gasto da compra;
Quantos produtos custam mais de R$ 1000.00;
O nome do produto mais barato.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

#programa principal
cabecalho('LOJA SUPER BARATÃO')
#inicializando variáveis
total = cont = quant = menor = 0
produto_barato = ' '
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #upper: joga a string para maiúsculo
    #strip: remove os espaços no começo e no fim
    nome = input('Nome do produto: ').upper().strip()
    preco = float(input('Preço: R$ '))
    quant += 1
    total += preco
    if preco > 1000:
        cont += 1
    if quant == 1 or preco < menor:
        menor = preco
        produto_barato = nome
    pergunta = ' '
    while pergunta not in 'SN':
        #[0] captura apenas o primeiro caractere
        pergunta = input('Quer continuar? [S/N] ').upper().strip()[0]
    if pergunta == 'N':
        #quebrando o 1º laço
        break
print()
linha()
print(f'Total da compra: R$ {total:.2f}')
print(f'Temos {cont} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato}; custando R$ {menor:.2f}')
rodape()
