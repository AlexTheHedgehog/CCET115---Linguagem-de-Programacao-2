from produto import Produto

class ProdutoParcelado(Produto):
    def __init__(self, nome, preco, quant):
        super().__init__(nome, preco, quant)
    
    def definir_preco_venda(self):
        super().definir_preco_venda
        super().preco_venda = super().preco_venda + (super().preco_venda * (5/100))
    
    def __str__(self):
        return super().__str__()
        