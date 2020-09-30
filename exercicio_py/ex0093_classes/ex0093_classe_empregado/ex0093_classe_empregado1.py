#importando a classe que será usada para montar o objeto
from ex0093_classe_empregado import Empregado

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
