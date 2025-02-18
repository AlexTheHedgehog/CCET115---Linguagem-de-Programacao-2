class Liquidacao:
    _historico = []
    def registrar(self, produto):
        produto.definir_preco_venda()
        liquidacao = produto.self._preco_venda *  0.5
        preco = produto.preco_venda - liquidacao
        Liquidacao._historico.append(f'Produto {produto._nome} vendido em liquidação.')