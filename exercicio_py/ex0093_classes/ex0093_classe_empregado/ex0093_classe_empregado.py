#criando classe
class Empregado:
    #variável da classe
    valor_aumento = 1.05
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

