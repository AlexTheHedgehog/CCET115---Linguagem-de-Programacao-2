from tributavel import TributavelMixIn

class SeguroDeVida(TributavelMixIn):
    def __init__(self, num, val:float, cli):
        self._numero = num
        self._valor_seguro = val
        self._titular = cli
        self._imposto = 34 + (self._valor_seguro * (5/100))
    
    def valor_imposto(self):
        return self._imposto