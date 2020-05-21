'''
Usuário digita uma palavra ou frase e programa retorna o primeiro e o último caractere da string.
'''

msg = input('Digite uma palavra ou frase: ')

#posição inicial do primeiro caractere
print(f'Primeiro caractere: {msg[0]}')
#posição -1 indica que o caractere será contado detrás pra frente
#   assim pegando o último
print(f'Último caractere: {msg[-1]}')
print()
