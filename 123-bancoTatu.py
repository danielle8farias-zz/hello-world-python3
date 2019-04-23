class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def resumo(self):
        print(f'CC Número: {self.numero} - Saldo: {self.saldo:.2f}')
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    
    def deposito(self, valor):
        self.saldo += valor

joao = Cliente('João da Silva','777-123')
maria = Cliente('Maria Benedita', '555-321')

conta1 = Conta([joao],1,2500)
print(f'Nome: {joao.nome} - Telefone: {joao.telefone}')
conta1.resumo()
print()
conta2 = Conta([maria],2,5999)
print(f'Nome: {maria.nome} - Telefone: {maria.telefone}')
conta2.resumo()
