'''
Usuário digita uma palavra e programa retorna a mesma centralizada em 20 espaços.
'''

palavra = input('Digite uma palavra: ')

#^20 a string em um espaço de 20 caracteres
print(f'- {palavra:^20} -')
print(f'{palavra:-^20}')
print()
