'''
Crie uma lista com marcas de carros e depois acesse o terceiro item.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('LISTA DE CARROS')
#lista
carros = ['FIAT', 'Ford','BMW', 'Jeep','Tesla']
#lista inicia em 0, logo o carros[2] é o terceiro elemento
print(f'O terceiro carro é: {carros[2]}')
rodape()
