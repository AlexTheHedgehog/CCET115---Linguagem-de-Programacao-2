class ControleDeBonificacoes:
    def __init__(self, total=0):
        self._total = total
    
    def registra(self, funcionario):
        #if is_instance(funcionario, Funcionario):
        #if hasattr(funcionario, 'get_bonificacao'):
        try:
            self._total += funcionario.get_bonificacao()
        except AttributeError as ate:
            print('Referência não tem bonificação!')