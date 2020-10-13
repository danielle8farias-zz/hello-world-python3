#criando a classe
class Personagem:
    #para inicializar o objeto a cada instanciamento
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
