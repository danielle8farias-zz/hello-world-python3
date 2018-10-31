'''
Verificar se um número inteiro é primo.
'''
print('-'*50)
print('{: ^50}'.format('É PRIMO?'))
print('-'*50)
while True:
    n = int(input("Digite um número inteiro: "))
    i = 0
    c = 0
    while i < n:
        i+= 1
        if (n % i == 0):
            c += 1
    if c == 2:
        print('É PRIMO!')
    else:
        print("não é primo")
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
