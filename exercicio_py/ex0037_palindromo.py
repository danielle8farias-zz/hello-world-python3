'''
Usuário informa uma palavra ou frase e programa retorna se é palíndromo.
'''

msg = input('Digite uma frase: ').strip().lower()

#split() divide uma string em uma lista
lista_palavras = msg.split()
#join concatena strings separada pelo caractere ''(sem espaço)
#retirando os espaços entre as palavras
msg_junto = ''.join(lista_palavras)
inverso = ''
tamanho_junto = len(msg_junto)

#laço for 
#   início: tamanho-1; para começar em 0
#   fim: -1; até a última string
#   passo: -1; decrescendo
for letra in range(tamanho_junto-1, -1, -1):
    #concatenando cada caractere detrás pra frente
    inverso += msg_junto[letra]

if inverso == msg_junto:
    print('É um palíndromo!')
    print(inverso)
else:
    print('Não é palíndromo')
    print(inverso)
print()
