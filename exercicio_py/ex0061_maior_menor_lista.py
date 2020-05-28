'''
Usuário informa 5 números inteiros. O programa os guarda em uma lista 
e retorna o maior e o menor deles e a sua posição. 
Números repetidos são permitidos.
'''

lista_num = list()

for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    lista_num.append(num)
    if i == 0:
        #inicializando as variáveis menor e maior
        #   na 1ª rodada do laço
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

#não pode fazer 'posicao_maior = posicao_menor = []'
#   senão as listas serão clones uma da outra
posicao_maior = []
posicao_menor = []
#usando lista para guardar as posições
#   caso haja números maiores e menores repetidos
for p,i in enumerate(lista_num):
    if lista_num[p] == maior:
        posicao_maior.append(p)
    if lista_num[p] == menor:
        posicao_menor.append(p)

print(f'Os números escolhidos foram: {lista_num}')
print(f'Maior: {maior}; na posição {posicao_maior}')
print(f'Menor: {menor}; na posição {posicao_menor}\n')
