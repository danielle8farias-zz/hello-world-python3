#importando a classe que será usada para montar o objeto
from ex0093_classe_computador import Computador

#passando atributos para a classe
pc2 = Computador('Dell', '10gb', 'GeForce', '150gb')
#retorna string formatada na tela
print(f'\nMarca do computador: {pc2.marca}')
#print() vazia pula uma linha
print()
#chamando método da classe; mensagem
pc2.desligar()
pc2.ligar()
pc2.exibir_config()
print()
