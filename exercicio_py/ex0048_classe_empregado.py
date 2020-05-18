#criando classe
class Empregado:
    #variável da classe
    aumento = 1.05
    #variável de instância
    num_empregados = 0

    #construtor
    def __init__(self, nome, sobrenome, pagamento):
        #self.variável = parâmetro
        self.nome = nome
        self.sobrenome = sobrenome
        self.pagamento = pagamento
        #lower() toda string em minúsculo
        #replace() para retirar espaços em branco
        self.email = f'{nome}.{sobrenome}@email.com.br'.lower().replace(' ', '')
        #não usar self, pois o valor não é uma constante
        #   será incrementado a cada instância
        Empregado.num_empregados += 1

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def aumentar_salario(self):
        #aumento de 5% do salário
        #'self.aumento' ou 'Empregado.aumento'
        self.pagamento = int(self.pagamento * self.aumento)


print(f'Número de empregados: {Empregado.num_empregados}')
print()
#instanciado objeto
pessoa1 = Empregado('Enrico', 'Sandro', 8000)
#imprimindo na tela atributo 'nome'
print(f'Nome do funcionário: {pessoa1.nome}')
print(f'Sobrenome: {pessoa1.sobrenome}')
print(f'email: {pessoa1.email}')
print(f'Nome completo: {pessoa1.nome_completo()}')
print(f'Salário atual: R${pessoa1.pagamento}')
pessoa1.aumentar_salario()
print(f'Aumento: R${pessoa1.pagamento}')
#mapeando atributos do objeto para dicionário
print(pessoa1.__dict__)
print()
print(f'Número de empregados: {pessoa1.num_empregados}')
print()

nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
salario = float(input('Seu salário? R$'))

pessoa = Empregado(nome, sobrenome, salario)
print(f'Seu email será: {pessoa.email}')
print(f'Nome completo: {pessoa.nome_completo()}')
print(f'Salário atual: R${pessoa.pagamento}')
pessoa.aumentar_salario()
print(f'Aumento: R${pessoa.pagamento}')
print(pessoa.__dict__)
print()
print(f'Número de empregados: {pessoa.num_empregados}')
print()

#acessando a variável da classe
print(Empregado.aumento)
pessoa2 = Empregado('Fulano', 'Silva', 2000)
print(pessoa2.aumento)
print(pessoa2.__dict__)
Empregado.aumento = 2
print(pessoa2.aumento)
print()
print(f'Número de empregados: {pessoa2.num_empregados}')
