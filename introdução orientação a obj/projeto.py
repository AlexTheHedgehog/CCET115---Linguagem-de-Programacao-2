from projeto_funcionario import projetoFuncionario

class Projeto:
    def __init__(self, id, nome, desc):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.funcionarios = []
    
    def lista_funcionarios(self):
        print('Funcionários do projeto:')
        for item in self.funcionarios:
            print(item.funcionario)
        print(f'Total de funcionários: {len(self.funcionarios)}')
    
    def adicionar_funcionario(self, func, cargo, data):
        associacao = projetoFuncionario(self, func, cargo, data)
        self.funcionarios.append(associacao)
        func.projetos.append(associacao)
    
    def remover_funcionario(self, func):
        for item in self.funcionarios:
            if item.funcionario.id == func.id:
                self.funcionarios.remove(item)
                func.projetos.remove(item)
    
    def __str__(self):
        return f'Projeto: {self.nome} ({self.id})'