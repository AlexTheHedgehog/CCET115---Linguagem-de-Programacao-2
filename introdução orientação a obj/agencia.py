from conta import Conta

class Agencia:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.status = True
        self.contas = []
    
    def adicionar_conta(self, n, c, s, l):
        if self.status:
            conta = Conta(n, c, s, l)
            self.contas.append(conta)
            conta.clientes.append(conta)
        else:
            print(f'Essa agência está fechada.')

    def fechar_agencia(self):
        self.contas.clear()
        self.status = False
        print(f'Essa agência {self} agora está encerrada.')
    
    def imprimir_contas(self):
        print(f'Contas da agência: {self}')
        for i in self.contas:
            print(f'Conta nº {i.numero} de {i.titular}')
    
    def __str__(self):
        return f'Nome: {self.nome}\nCNPJ: {self.cnpj}'