'''
Crie uma lista com marcas de carros e depois acesse o terceiro item.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('LISTA DE CARROS')

carros = ['FIAT', 'Ford','BMW', 'Jeep','Tesla']
print('O terceiro carro é: {}'.format(carros[2]))

rodape()
