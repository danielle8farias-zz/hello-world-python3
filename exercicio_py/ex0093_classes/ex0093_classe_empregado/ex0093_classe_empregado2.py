#importando a classe que será usada para montar o objeto
from ex0093_classe_empregado import Empregado

#criando objetos separados por hífen
pessoa_str4 = 'Victor-José-6000'
pessoa_str5 = 'Elana-Tanan-4000'
pessoa_str6 = 'Henrique-Costa-1200'

#instanciado objeto de moto indireto; através de uma variável
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

