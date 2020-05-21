'''
Fatiando string
'''

msg = 'A ciência nos convida a aceitar os fatos, mesmo quando eles não estão de acordo com nossos preconceitos'

#pegando da posição 2 até 8
print(msg[2:9])
#pegando da posição 11 até o final da string
print(msg[11:])
#pegando da posição inicial até a 20
print(msg[:21])
#do início até o fim da string
#   mostra a primeira posição e então pula duas posições
print(msg[::2])
#separa a string em uma lista; o separador são os espaços por padrão
#   split() = split(' ')
nova_msg = msg.split()
print(nova_msg)
#imprime o segundo item da lista
print(nova_msg[1])
print()
