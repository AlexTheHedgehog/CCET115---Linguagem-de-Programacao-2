class Pessoa:
    def __init__(self, nome:str, cpf:str, idade:int):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
    
    def __str__(self):
        cpf_censurado = self._cpf[:8] + '***'
        return f'Nome: {self._nome}\nCPF: {cpf_censurado}\nIdade: {self._idade}'

class Motorista(Pessoa):
    def __init__(self, nome:str, cpf:str, idade:int, cnh:str):
        super().__init__(nome, cpf, idade)
        self._cnh = cnh
    
    def __str__(self):
        return f'{super().__str__()}\nCNH: {self._cnh}'

class Gestor(Pessoa):
    def __init__(self, nome:str, cpf:str, idade:int, setor:str):
        super().__init__(nome, cpf, idade)
        self._setor = setor
    
    def __str__(self):
        return f'{super().__str__()}\nSetor: {self._setor}'