'''
Usuário digita vários números e o programa retorna quantos foram digitados. 
A condição de parada é quando for informado o número 999 (desconsiderar este da contagem).
'''

i = 0
while True:
    num = float(input('Digite um número: '))
    if num == 999:
        break
    i += 1
print(f'Foram digitados {i} números.')
