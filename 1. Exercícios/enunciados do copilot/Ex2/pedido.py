from random import randint

class Pedido:
    def __init__(self, num=randint(0, 200)):
        self.num = num
        self.itens = []
        self.status = 'em preparo'
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    def remover_item(self, item):
        self.itens.remove(item)
    
    def total(self):
        soma = 0
        for i in self.itens:
            soma += i.preco
        
        return soma
    
    def alterar_status(self, status):
        self.status = status
    
    def __str__(self):
        return  f'Pedido nº {self.num}\nStatus: {self.status}\n'