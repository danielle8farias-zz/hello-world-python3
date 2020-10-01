'''
Tabela de preços de produtos de uma livraria guardada em um dicionário.
'''

produtos = [{'lápis': 1.75}, 
{'borracha': 0.99}, 
{'caderno': 15.9}, 
{'estojo': 18}, 
{'transferidor': 4.2}, 
{'compasso': 9.99}, 
{'mochila': 120.9}, 
{'caneta': 1.99}, 
{'marca-texto': 7.99}]

#texto centralizado em um mínimo de 40 caracteres
print(f'{"Tabela de preços:":^40}')

for i in produtos:
    for p, v in i.items():
        print(f'{p:-<30} R${v:>6.2f}')

