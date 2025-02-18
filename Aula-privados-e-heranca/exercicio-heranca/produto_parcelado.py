from produto import Produto

class ProdutoParcelado(Produto):
    def __init__(self, nome, preco, quant):
        super().__init__(nome, preco, quant)
    
    def definir_preco_venda(self, lucro):
        margem = self._preco_compra * lucro
        self._preco_venda = (self._preco_compra + margem) * 1.05
    
    def __str__(self):
        return super().__str__()
        