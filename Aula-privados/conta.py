class Conta:
    _total_contas = 0    #atributo de classe
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta._total_contas += 1
        
    #método de instância
    def get_total_contas(self):
        return Conta._total_contas
    
    #método estático
    @staticmethod
    def get_total_contas_estatico(cls):
        return cls._total_contas
    
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
    