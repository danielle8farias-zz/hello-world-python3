#importando a classe que será usada para montar o objeto
from ex0093_classe_pessoa import Humano

print()
#instanciando objeto
p1 = Humano()
#mostra na tela o endereço de memória do objeto
print(p1)
p1.nome = 'Danielle'
#retorna a string na tela
print(p1.nome)
#chamando o método da classe
p1.falar()
#print() vazio pula uma linha
print()

p2 = Humano()
print(p2)
p2.nome = 'Enrico'
print(p2.nome)
p2.falar()
print()
