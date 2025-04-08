from conta import Conta

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor