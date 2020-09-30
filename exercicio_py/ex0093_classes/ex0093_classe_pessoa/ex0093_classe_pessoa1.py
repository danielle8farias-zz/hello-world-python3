#importando a classe que será usada para montar o objeto
from ex0093_classe_pessoa import Humano


print()
#instanciando objeto
pessoa1 = Humano()
#mostra na tela o endereço de memória do objeto
print(pessoa1)
pessoa1.nome = 'Danielle'
#retorna a string na tela
print(pessoa1.nome)
#chamando o método da classe
pessoa1.falar()
print()
