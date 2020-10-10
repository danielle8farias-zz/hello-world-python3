import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho


#criando classe
class Empregado:
    #variável da classe
    valor_aumento = 1.05
    #variável de instância
    num_empregados = 0

    #construtor (serve para inicializar o objeto a cada instanciamento)
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
        self.pagamento = int(self.pagamento * self.valor_aumento)

    #não precisa da instância, mas precisa da classe em si
    @classmethod
    def definir_aumento(cls, novo_aumento):
        #usa-se 'cls' ao invés de 'self', pois é um método de classe
        cls.valor_aumento = novo_aumento

    @classmethod
    def criar_pessoa(cls,pessoa_str):
        #slit() retira o que estiver entre parênteses e
        #   retorna os valor separados em uma lista
        #atribuindo para cada variável, cada item da lista de acordo com a posição
        nome, sobrenome, pagamento = pessoa_str.split('-')
        #criando e retornando novo empregado
        return cls(nome, sobrenome, pagamento)

    #método estático
    @staticmethod
    #usa-se 'day' do módulo 'datetime'
    def dia_util(day):
        #verificando se o dia da semana é sábado(5) ou domingo(6)
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



#retorna string formatada na tela
print(f'\nNúmero de empregados inicial: {Empregado.num_empregados}')
#print() vazia pula uma linha
print()

#instanciado objeto
pessoa1 = Empregado('Enrico', 'Sandro', 8000)
#imprimindo na tela atributo 'nome'
print(f'Nome do funcionário: {pessoa1.nome}')
print(f'Sobrenome: {pessoa1.sobrenome}')
print(f'email: {pessoa1.email}')
print(f'Nome completo: {pessoa1.nome_completo()}')
print(f'Salário atual: R${pessoa1.pagamento}')
print()

#chamando método da classe; mensagem
pessoa1.aumentar_salario()
print(f'Aumento: R${pessoa1.pagamento}')
print()

print('Mapeando atributos do objeto para dicionário:')
print(pessoa1.__dict__)
print()

print(f'Número de empregados: {pessoa1.num_empregados}')
print()

ler_cabecalho('novo cadastro de empregado')

print('Inserindo novo usuário')
#input() recebe o que for digitado no teclado
#strip() retira espaços no começo e no final da string
nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
#float() converte a string para número real
salario = float(input('Seu salário? R$'))
print()
print('Exibindo dados do novo usuário')
#criando objeto com o que foi capturado pelo teclado
pessoa2 = Empregado(nome, sobrenome, salario)
print(f'Seu email será: {pessoa2.email}')
print(f'Nome completo: {pessoa2.nome_completo()}')
print(f'Salário atual: R${pessoa2.pagamento}')
print()

pessoa2.aumentar_salario()
print(f'Aumento: R${pessoa2.pagamento}')
print()

#mapeando atributos do objeto para dicionário
print('Mapeando atributos do objeto para dicionário:')
print(pessoa2.__dict__)
print()

print(f'Número de empregados: {pessoa2.num_empregados}')
print()

ler_cabecalho('empregado 3')

pessoa3 = Empregado('Fulano', 'Silva', 2000)

print('acessando a variável da classe')
print(Empregado.valor_aumento)
print(pessoa3.valor_aumento)
print()

print('Atribuindo aumento de 30%')
Empregado.valor_aumento = 1.3
print(pessoa3.valor_aumento)
print()

print(f'Atribuindo novo aumento de 50% através do método de classe')
Empregado.definir_aumento(1.50)
print(pessoa3.valor_aumento)
print()

print('Mapeando atributos do objeto para dicionário:')
print(pessoa3.__dict__)
print()

print(f'Número de empregados: {pessoa2.num_empregados}')
print()

ler_cabecalho('dia de trabalho')
#importanto módulo de data
from datetime import date
#hoje = date(2020, 9, 27)
#date.today() retorna a data atual (ano, mês, dia)
hoje = date.today()
dia_trabalho = Empregado.dia_util(hoje)

if dia_trabalho:
    print('Dia de trabalho.')
else:
    print('Final de semana!')
print()

ler_cabecalho('cadastrando novos empregados')

print('criando objetos separados por hífen')
pessoa_str4 = 'Victor-José-6000'
pessoa_str5 = 'Elana-Tanan-4000'
pessoa_str6 = 'Henrique-Costa-1200'

#instanciado objeto de modo indireto; através de uma variável
pessoa4 = Empregado.criar_pessoa(pessoa_str4)
pessoa5 = Empregado.criar_pessoa(pessoa_str5)
pessoa6 = Empregado.criar_pessoa(pessoa_str6)

#retorna string formatada na tela
print(f'\nNome do funcionário: {pessoa4.nome}')
print(f'Sobrenome: {pessoa4.sobrenome}')
print(f'email: {pessoa4.email}')
print(f'Nome completo: {pessoa4.nome_completo()}')
print(f'Salário atual: R${pessoa4.pagamento}')
#print() vazia pula uma linha
print()

print(f'Nome do funcionário: {pessoa5.nome}')
print(f'Sobrenome: {pessoa5.sobrenome}')
print(f'email: {pessoa5.email}')
print(f'Nome completo: {pessoa5.nome_completo()}')
print(f'Salário atual: R${pessoa5.pagamento}')
print()

print(f'Nome do funcionário: {pessoa6.nome}')
print(f'Sobrenome: {pessoa6.sobrenome}')
print(f'email: {pessoa6.email}')
print(f'Nome completo: {pessoa6.nome_completo()}')
print(f'Salário atual: R${pessoa6.pagamento}')
print()

print(f'Número de empregados: {pessoa6.num_empregados}')
print()
