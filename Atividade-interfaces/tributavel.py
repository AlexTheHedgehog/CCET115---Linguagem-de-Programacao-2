import abc

class TributavelInterface(abc.ABC):
    """TributavelInterface
    
    É uma classe interface que implementa o método abstrato valor_imposto. Não
    funciona se for implementada diretamente e deve ser herdada de outra classe.
    """
    
    @abc.abstractmethod
    def valor_imposto():
        pass