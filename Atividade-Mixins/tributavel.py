import abc

class TributavelMixIn(abc.ABC):
    @abc.abstractmethod
    def valor_imposto():
        pass