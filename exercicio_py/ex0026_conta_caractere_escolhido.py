'''
Usuário digita palavra ou frase, escolhe uma letra que deseja procurar e 
programa retorna a quantidade delas.
'''

msg = input('Digite uma palavra ou frase: ')
escolhido = input('Que letra deseja contar? ')
#count() conta quantas vezes aparece o caractere
num = msg.count(escolhido)
print(f'Essa palavra tem a letra {escolhido}: {num} vezes.')
print()
