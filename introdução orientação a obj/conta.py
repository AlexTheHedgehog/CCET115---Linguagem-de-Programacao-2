class Conta:
    #init
    def __init__(self, n:int, t:str, s:float, l:float): #Método de inicialização
        self.numero = n
        self.titular = t
        self.saldo = s
        self.limite = l
        
    #Métodos da conta
    def sacar(self, valor:float):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def depositar(self, valor:float):
        self.saldo += valor
    
    def ver_saldo(self):
        return f'Saldo: R${self.saldo:.2f}'
    
    def trasferir(self, valor:float, destino:object):
        self.saldo -= valor
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False
    
    def __str__(self):
        return f'Número: {self.n}\n'