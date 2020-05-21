'''
Usuário digita duas palavras e programa retorna uma delas alinhada a esquerda e outra à direita.
'''

msg1 = input('Digite uma palavra: ')
msg2 = input('Digite outra palavra: ')

#<20 alinhado à esquerda num espaço mínimo de 20 caracteres
#>20 alinhado à esquerda num espaço mínimo de 20 caracteres
print(f'{msg1:<20} e {msg2:>20}')
print()
