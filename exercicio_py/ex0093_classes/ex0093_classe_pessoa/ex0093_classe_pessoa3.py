#importando a classe que será usada para montar o objeto
from ex0093_classe_pessoa import Pessoa

print()
#instanciando objeto pelo método de classe
p5 = Pessoa.por_ano_nasc('Victor', 2000)
print(f'{p5.nome} tem {p5.idade} anos.')
print()
