import abc
from banco import Banco

class Conta(Banco, abc.ABC):
    @abc.abstractmethod
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        #self._extrato = Historico()
        super()._contas.append(self)
    
    @abc.abstractmethod
    def atualiza(self, taxa):
        pass