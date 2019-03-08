'''
Leia o nome e o preço de vários produtos. O programa deve perguntar se o
usuário desea continuar a cada inserção. Ao final, mostre:
Total de gasto da compra;
Quantos produtos custam mais de R$ 1000.00;
O nome do produto mais barato.
'''
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

cabecalho('LOJA SUPER BARATÃO')

total = cont = quant = menor = 0
produto_barato = ' '
while True:
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
        pergunta = input('Quer continuar? [S/N] ').upper().strip()[0]
    if pergunta == 'N':
        break
print()
linha()
print('Total da compra: R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(cont))
print('O produto mais barato foi {}; custando R$ {:.2f}'.format(produto_barato, menor))

rodape()
