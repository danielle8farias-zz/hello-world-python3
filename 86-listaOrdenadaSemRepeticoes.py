'''
Crie um programa onde o usuário pode digitar 5 valores inteiros e coloque-os numa lista.
A cada nova inserção faça a ordenação e mostre em qual posição o novo número ocupa.
Ao final mostre toda a lista ordenada.
'''
lista = []
for c in range(0,5):
    num = int(input('Insira um número: '))
    if c == 0: #se no número for o primeiro
        lista.append(num)
        print('Adicionado ao final da lista')
    elif num > lista[-1]: #se o número for maior do que o último
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): #vai da posição 0 até a última
            if num <= lista[pos]: #verifica se o número a ser inserido é menor do que em cada posição
                lista.insert(pos, num)
                print(f'Adicionado na posiçao {pos} da lista.')
                break
            pos += 1
print('-'*50)
print(f'Os valores digitados em ordem foram: {lista}')
