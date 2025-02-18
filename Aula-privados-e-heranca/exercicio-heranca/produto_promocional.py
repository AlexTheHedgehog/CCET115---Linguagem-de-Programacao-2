from produto import Produto

class ProdutoPromocional(Produto):
    def __init__(self, nome, preco, quant):
        super().__init__(nome, preco, quant)
    
    def definir_preco_venda(self, lucro):
        margem = self._preco_compra * lucro
        self._preco_venda = (self._preco_compra + margem) * 0.2
    
    def __str__(self):
        return super().__str__()