from conta import Conta
from tributavel import TributavelMixIn

class ContaCorrente(Conta, TributavelMixIn):
    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)
        self._imposto = super()._saldo * (2/100)
    
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor
    
    def valor_imposto(self):
        return self._imposto