'''
Leia vários números. Coloque-os em uma lista em ordem decresccente. Ao final informe quantos números
foram digitados; e se o valor 5 está na lista.
'''
lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse = True)
print('A lista em ordem decrescente é:')
print(lista)
if 5 in lista:
    print('O número 5 pertence a lista.')
else:
    print('O número 5 NÃO pertence a lista.')
