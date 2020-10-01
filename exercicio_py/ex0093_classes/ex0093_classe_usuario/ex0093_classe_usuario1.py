#importando a classe que será usada para montar o objeto
from ex0093_classe_usuario import Usuario

print()
user1 = Usuario('Nicolau Farias', '11/09/1937')
print(user1.nome_completo)
print(user1.primeiro_nome)
print(user1.ultimo_nome)
print(user1.aniversario)
print(user1.idade())
print()
