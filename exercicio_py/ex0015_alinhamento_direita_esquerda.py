'''
Usuário digita duas palavras e programa retorna uma delas alinhada a esquerda e outra à direita.
'''

frase1 = input('Digite uma palavra: ')
frase2 = input('Digite outra palavra: ')

#<20 alinhado à esquerda num espaço mínimo de 20 caracteres
#>20 alinhado à esquerda num espaço mínimo de 20 caracteres
print(f'{frase1:<20} e {frase2:>20}')
print()
