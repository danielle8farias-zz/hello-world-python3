'''
Usuário digita palavra ou frase, escolhe uma letra que deseja procurar e 
programa retorna a quantidade delas.
'''

msg = input('Digite uma palavra ou frase: ')
escolha = input('Que letra deseja contar? ')
#count() conta quantas vezes aparece o caractere
num = msg.count(escolha)
print(f'Tem a letra {escolha}: {num} vezes.')
print()

msg1 = 'Um livro é a prova de que os seres humanos são capazes de fazer magia'
print(len(msg1))
#contando a letra 'e'
num1 = msg1.count('e')
print(f'Quantas letras "e"? {num1}')
#da posição 7 a 60; contando a letra escolhida
num2 = msg1.count(escolha, 7, 60)
print(f'Tem a letra {escolha}: {num2} vezes.')
print()
