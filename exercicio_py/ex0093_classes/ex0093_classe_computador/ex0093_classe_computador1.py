#importando a classe que será usada para montar o objeto
from ex0093_classe_computador import Computador

#instanciando a classe
pc1 = Computador('Asus', '8gb', 'Nvidia', '200gb')
#retorna string formatada na tela
print(f'\nMarca do computador: {pc1.marca}')
#função print vazia não retorna nada; pula uma linha
print()
#chamando método da classe; mensagem
pc1.ligar()
pc1.ligar()
pc1.desligar()
pc1.exibir_config()
print()
