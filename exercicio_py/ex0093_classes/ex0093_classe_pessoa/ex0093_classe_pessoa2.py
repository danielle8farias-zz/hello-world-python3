#importando a classe que será usada para montar o objeto
from ex0093_classe_pessoa import Pessoa

print()
#método construtor sempre é chamado ao instanciar a classe
# por isso aparece na tela o print de var
p3 = Pessoa('Luis', 30)
#retorna string formatada na tela
print(f'Nome: {p3.nome}')
#chamando método da classe; mensagem
p3.comer('maçã')
#verificando se pode comer 2x
p3.comer('melancia')
p3.parar_comer()
p3.comer('melancia')
p3.falar('política')
p3.parar_comer()
p3.falar('política')
p3.comer('tomate')
print()

#p4.nome = 'Sandra'
#p4.idade = 50
p4 = Pessoa('Sandra', 50)
p4.outro_metodo()
p4.parar_comer()
p4.falar('culinária')
p4.falar('cães')
p4.parar_falar()
p4.parar_falar()
print()

#imprimindo a variável da classe através da instância
print(p3.ano_atual)
print(p4.ano_atual)
#imprimindo a variável da classe através da própria classe
print(Pessoa.ano_atual)
print()

print(f'{p3.nome} nasceu em {p3.ano_nascimento()}.')
print(f'{p4.nome} nasceu em {p4.ano_nascimento()}.')
print()
