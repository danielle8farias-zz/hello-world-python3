'''
Verifique se o número é ímpar ou par.
'''
print('-'*50)
print('{: ^50}'.format('VERIFICA SE É PAR OU ÍMPAR'))
print('-'*50)
while True:
    num = int(input("Digite um número: "))
    if num % 2 == 1:
        print("O número",num,"é ímpar.")
    else:
        print("O número",num,"é par.")
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
