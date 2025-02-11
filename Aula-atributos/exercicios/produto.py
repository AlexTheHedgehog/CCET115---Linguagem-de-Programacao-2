class Produto:
    _desconto = 0
    def __init__(self, nome:str, preco:float):
        try:
            if Produto.is_preco_valido(preco):
                self._nome = nome
                self._preco = preco
        except ValueError as e:
            print(e)
        
    @property
    def preco(self):
        return self._preco
    
    @classmethod
    def atualizar_desconto(cls, porcentagem):
        cls._desconto = porcentagem
    
    @staticmethod
    def is_preco_valido(preco):
        if preco < 0:
            raise ValueError('Não pode ser negativo.')
        else:
            return True
    
    def preco_descontado(self):
        return self._preco - (self._preco * (Produto._desconto / 100))
    