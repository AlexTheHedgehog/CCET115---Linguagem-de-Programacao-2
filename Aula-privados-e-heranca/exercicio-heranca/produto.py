class Produto:
    def __init__(self, nome, preco, quant):
        self._nome = nome
        self._preco_compra = preco
        self._quantidade_estoque = quant
        self._historico = {'Compras':[], 'Vendas':[]}
        self._preco_venda = 0.0
    
    def definir_preco_venda(self, porcentagem_lucro=16):
        self._preco_venda = self._preco_compra + (self._preco_compra * (porcentagem_lucro/100))
        return self._preco_venda
    
    @property
    def preco_venda(self):
        return self._preco_venda
    
    @preco_venda.setter
    def preco_venda(self, preco):
        self._preco_venda = preco
    
    def vender_produto(self):
        if self._quantidade_estoque > 0:
            self._historico['Vendas'].append(f'Produto {self._nome} vendido por {self._preco_venda}')
            self._quantidade_estoque -= 1
        else:
            print('Produto esgotado!')
    
    def comprar_produto(self):
        self._historico['Compras'].append(f'Produto {self._nome} comprado por {self._preco_compra}')
        self._quantidade_estoque += 1
    
    def __str__(self):
        return f'Nome: {self._nome}, Preço de compra: {self._preco_compra}, Preço de venda: {self._preco_venda}, Quantidade em estoque: {self._quantidade_estoque}'