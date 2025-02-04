class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    #forma pytonica
    @property
    def saldo(self):
        return self._saldo
    
    #Não é necessário por já ter sacar e depositar
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    #Covenção padrão para getters e setters
    def get_saldo(self):
        return self._saldo
    