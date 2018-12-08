'''
Leia um número e retorne seu fatorial.
'''
print('-'*50)
print('{: ^50}'.format('FATORIAL!'))
print('-'*50)
def fat(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

n = int(input("Digite um número: "))
print(f'O fatorial é {fat(n)}.')
