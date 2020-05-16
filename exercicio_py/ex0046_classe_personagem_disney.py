#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de linha
from mensagem import linha

#criando a classe
class Personagem:
    #construtor
    def __init__(self, nome, cor):
        #self.variável = parâmetro        
        self.nome = nome
        self.cor = cor

    #criando uma representação do meu objeto que foi construído
    def __repr__(self):
        return f'Personagem: ("{self.nome}", "{self.cor}")'


#instanciando os objetos
rato = Personagem('Mickey', 'preto')
cachorro = Personagem('Pluto', 'amarelo')
pato = Personagem('Donald', 'branco')

#por causa de __repr__ é possível ver os atributos do personagem
print(rato)
print(cachorro)
print(pato)
