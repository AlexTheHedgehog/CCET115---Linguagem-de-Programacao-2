class Emprestimo:
    def __init__(self, conta, divida, parcelas):
        self.conta = conta
        self.conta.depositar(divida)
        self.divida = divida
        self.parcelas = parcelas
        self.valor_parcela = divida / parcelas
        self.parcelas_restantes = self.parcelas
        self.conta.adicionar_emprestimo(self)
    
    def pagar_parcela(self):
        if self.parcelas > 0:
            if self.conta.saldo >= self.valor_parcela:
                self.conta.sacar(self.valor_parcela)
                self.parcelas_restantes -= 1
                print(f'Pagou a parcela: {self.parcelas-self.parcelas_restantes}')
                print(f'Faltam {self.parcelas_restantes}')
            else:
                print(f'Saldo insuficiente para pagar a parcela')
        else:
            print('Emprestimo pago.')
    
