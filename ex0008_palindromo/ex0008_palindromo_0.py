########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa uma palavra ou frase e programa retorna se ela é um palíndromo.
########

msg = input('Digite uma frase: ').strip().lower()
lista_palavras = msg.split()
msg_junto = ''.join(lista_palavras)
inverso = ''
tamanho_junto = len(msg_junto)
#laço for:
#   início: tamanho-1; para ir do último caractere a 0
#   fim: -1; para ir até a última string
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
