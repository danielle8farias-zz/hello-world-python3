'''
Tabela de preços de produtos de uma livraria guardada em uma tupla composta.
'''

produtos = (('lápis', 1.75), ('borracha', 0.99), ('caderno', 15.9), ('estojo', 18), 
('transferidor', 4.2), ('compasso', 9.99), ('mochila', 120.9), ('caneta', 1.99), 
('marca-texto', 7.99))


#texto centralizado em um mínimo de 40 caracteres
print(f'{"Tabela de preços:":^40}')

for i in range(len(produtos)):
    #:-<30 
    #   preeenche os caracteres restantes com -
    #   < alinhado a esquerda
    #   espaço mínimo de 30 caracteres
    print(f'{produtos[i][0]:-<30} R$ {produtos[i][1]:>6.2f}')
