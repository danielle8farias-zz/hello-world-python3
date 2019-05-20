from datetime import date
from statistics import median
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha
import json

cabecalho('dados dos entrevistados')

class Entrevista():

    def __init__(self, nome='', idade=0, nasc=0):
        super(Entrevista, self).__init__()
        self.nome = nome
        self.idade = idade
        self.nasc = nasc

    def pergunta_nome(self):
        nome_ok = False
        while nome_ok == False:
            print()
            print('Digite N para parar!')
            print()
            self.nome = input('Qual é seu nome? ')
            if self.nome:
                nome_ok = True
        self.nome = self.nome.title()
        return self.nome


    def pergunta_idade(self,atual):
        ano_ok = False
        while ano_ok == False:
            try:
                self.nasc = int(input(f'{self.nome} em que ano você nasceu? '))
                self.idade = atual - self.nasc
                ano_ok = True
            except:
                continue
            else:
                if self.idade >= 130:
                    ano_ok = False
        print(f'Você tem {self.idade} anos.')
    

    def __repr__(self):
        return f'Entrevista({self.nome}, {self.idade})'


atual = date.today().year
pode_parar = False
lista_entrevistados = []

def pega_dados(obj):
    instancia = Entrevista(
        nome = obj['nome'],
        idade = obj['idade'],
        nasc = obj['nasc']
    )
    return instancia

#lendo arquivo json
try:
    arquivo_json = open('dados.json','r')
    dados_json = json.load(arquivo_json)
    entrevistas = dados_json['Entrevista']

    lista_entrevistados = [pega_dados(entrevista) for entrevista in entrevistas]
except Exception as erro:
    print('Ocorreu um erro ao carregar o arquivo')
    print(f'O erro é: {erro}')


while pode_parar == False:
    entrevistado = Entrevista()
    if entrevistado.pergunta_nome().upper() == 'N':
        pode_parar = True
    else:
        try:
            entrevistado.pergunta_idade(atual)
            # x = 1000/0 exemplo de erro grosseiro que não deve impedir o código de rodar
        except ZeroDivisionError:
            print('Ocorreu um erro de divisão! Mas a lista foi salva.')
            lista_entrevistados.append(entrevistado)
        except Exception as erro:
            print('Ocorreu um erro! A lista NÃO foi salva.')
            print(f'O tipo de erro foi: {type(erro)}')
            print(f'Mensagem: {erro}')
        else:
            lista_entrevistados.append(entrevistado)

#Gravando arquivo json
lista_salvar = [
    dict(nome=obj.nome, nasc=obj.nasc, idade=obj.idade)
    for obj in lista_entrevistados
]

dict_salvar = {"Entrevista": lista_salvar}
#convertendo para o formato json
dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

try:
    arquivo_json = open('dados.json', 'w')
    arquivo_json.write(dict_salvar)
    arquivo_json.close()
except Exception as erro:
    print('Ocorreu um erro ao carregar o arquivo')
    print(f'O erro é: {erro}')
   

print(lista_entrevistados)
linha()

#lista por compreensão

#menor idade
menor_idade = min([objeto.idade for objeto in lista_entrevistados])
'''
lista_idade = []
for objeto in lista_entrevistados:
    lista_idade.append(objeto.idade)
menor = min(lista_idade)
'''
print(f'Menor idade: {menor_idade}')

#maior idade
maior_idade = max([objeto.idade for objeto in lista_entrevistados])
print(f'Maior idade: {maior_idade}')

#média de idade dos adultos
# lista = [<expressão para o valor> <loop> <expressão para o loop>]
media_adulto = median([objeto.idade for objeto in lista_entrevistados if objeto.idade >= 18])
print(f'A média de idades dos adultos: {media_adulto}')

#mostrar a quantidade de nascimento por décadas
lista_decada = [ (objeto.nasc//10*10) for objeto in lista_entrevistados ]
print(f'Décadas: {lista_decada}')

#set: coleção de objetos distintos sem ordenação
set_decadas = set(lista_decada)
print(f'Décadas sem repetição: {set_decadas}')

#dicionário por compreensão
#dicionário = { <expressão da chave>:<expressão para o valor> <loop> <expressão para o loop> }
qtd_nasc = { decada:lista_decada.count(decada) for decada in set_decadas }
print(f'Quantidade de nascimento por década: {qtd_nasc}')

rodape()
