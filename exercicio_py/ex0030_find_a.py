'''
Usuário digita uma string e programa retorna 
quantas letras 'a' possui; a posição da primeira e da última letra 'a'.
'''

#strip() retira espaços em branco no começo e no fim da string
#lower() converte string para minúscula
msg = input('Digite uma palavra ou frase: ').lower().strip()
#count() retorna a quantidade de caractere entre parênteses
quant_a = msg.count('a')
print(f'A letra A aparece {quant_a} vezes.')
#find() retorna o posição do primeiro caractere entre parênteses
#   somando 1 porque a string começa em 0.
primeiro_a = msg.find('a') + 1
print(f'A primeira letra A está na posição: {primeiro_a}')
#rfind() busca o primeiro caractere de trás pra frente na string
ultimo_a = msg.rfind('a') + 1
print(f'A última letra A está na posição: {ultimo_a}')
print()
