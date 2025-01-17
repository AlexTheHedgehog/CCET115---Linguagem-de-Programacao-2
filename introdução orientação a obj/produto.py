class Produto:
    #init
    def __init__(self, n:str, p:float, q:int):
        self.nome = n
        self.preco = p
        self.quantidade = q
    
    #Métodos
    def valorTotal(self):
        return f'R$ {self.preco * self.quantidade:.2f}'.replace('.', ',')
    
    def incluirItens(self, q:int):
        self.quantidade += q
    
    def removerItens(self, q:int):
        self.quantidade -= q