from banco import Banco

class ManipuladorDeTributaveis(Banco):
    def calcular_imposto(self):
        tributaveis = super()._contas
        return sum([i.valor_imposto() for i in tributaveis])