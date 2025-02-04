class Cliente:
    def __init__(self, nome, num):
        self.nome = nome
        self.num = num
        self.pedidos = []
    
    def __str__(self):
        return f'Nome: {self.nome}\nNúmero de identificação: {self.num}'
    
    def add_pedido(self, pedido):
        self.pedidos.append(pedido)
    
    def listar_pedidos(self):
        for i in self.pedidos:
            print(i.__str__())
        