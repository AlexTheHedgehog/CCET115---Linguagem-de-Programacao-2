class Produto:
    _historico = {'Compras':[], 'Vendas':[]}
    
    def __init__(self, nome='', preco=0, quant=0):
        self._nome = nome
        self._preco_compra = preco
        self._quantidade_estoque = quant
        Produto.definir_preco_venda(self, 20)
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
        
    @property
    def preco_compra(self):
        return self._preco_compra
    
    @preco_compra.setter
    def preco_compra(self, valor):
        self._preco_compra = valor
        
    @property
    def preco_venda(self):
        return self._preco_venda
    
    @preco_venda.setter
    def preco_venda(self, preco):
        self._preco_venda = preco
    
    def definir_preco_venda(self, porcentagem_lucro=16):
        self._preco_venda = self._preco_compra + (self._preco_compra * (porcentagem_lucro/100))
    
    def vender_produto(self, qtde=1):
        try:
            if self._quantidade_estoque >= qtde:
                self._quantidade_estoque -= qtde
                Produto._historico['Vendas'].append(f'{qtde} unidades do produto {self._nome}\nvendidas por R${self._preco_venda:.2f}\nValor total: R${self._preco_venda * qtde:.2f}')
            else:
                raise ValueError('Quantidade não disponível.')
        except ValueError as e:
            pass
    
    def comprar_produto(self, qtde, preco):
        self._quantidade_estoque += qtde
        self._preco_compra = preco
        self._historico['Compras'].append(f'{qtde} unidades do produto {self._nome}\ncompradas por R${self._preco_compra:.2f}\nValor total: R${self._preco_compra * qtde:.2f}')
        self.definir_preco_venda(30)
    
    def __str__(self):
        return f'Nome: {self._nome}, Preço de compra: {self._preco_compra}, Preço de venda: {self._preco_venda}, Quantidade em estoque: {self._quantidade_estoque}'