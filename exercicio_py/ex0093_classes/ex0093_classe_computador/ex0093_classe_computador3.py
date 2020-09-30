#importando a classe que será usada para montar o objeto
from ex0093_classe_computador import Computador

#passando atributos para a classe
pc3 = Computador('Acer', '16gb', 'ATM', '1tb')
#retorna string formatada na tela
print(f'\nMarca do computador: {pc3.marca}')
#print() vazia pula uma linha
print()
#chamando método da classe; mensagem
pc3.exibir_config()
print()
