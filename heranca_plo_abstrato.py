#criar uma classe Aluno com os atributos encapsulados com um underscore (_): nome e matricula
#criar uma classe abstrata AlunoBolsista, filha de Aluno, e definir o método abstrato para o valor da bolsa


from abc import ABC, abstractmethod

class Aluno:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        self._matricula = nova_matricula

class AlunoBolsista(Aluno, ABC):
    @abstractmethod
    def valor_bolsa(self):
        pass

#criar uma classe AlunoMonitor, mais um atributo disciplina, que herda de AlunoBolsista e implementa o metodo abstrato

class AlunoMonitor(AlunoBolsista):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self._disciplina = disciplina
    
    @property
    def disciplina(self):
        return self._disciplina
    
    @disciplina.setter
    def disciplina(self, nova_disciplina):
        self._disciplina = nova_disciplina
    
    def valor_bolsa(self):
        return 700.00

#criar uma classe AlunoPIBIC, mais um atributo projeto, que herda de AlunoBolsista e implementa o metodo abstrato

class AlunoPIBIC(AlunoBolsista):
    def __init__(self, nome, matricula, projeto):
        super().__init__(nome, matricula)
        self._projeto = projeto
    
    @property
    def projeto(self):
        return self._projeto
    
    @projeto.setter
    def projeto(self, novo_projeto):
        self._projeto = novo_projeto
    
    def valor_bolsa(self):
        return 800.00

#criar instâncias das classes AlunoMonitor e AlunoPIBIC

aluno_monitor = AlunoMonitor("João", "123456", "Matemática")
aluno_pibic = AlunoPIBIC("Maria", "654321", "Inteligência Artificial")

#criar uma lista com os alunos e exibir as informações de cada um deles, incluindo o valor da bolsa
alunos = [aluno_monitor, aluno_pibic]
for i in alunos:
    print(f"Nome: {i.nome}, Matrícula: {i.matricula}, Disciplina/Projeto: {i.disciplina if isinstance(i, AlunoMonitor) else i.projeto}, Valor da Bolsa: R$ {i.valor_bolsa()}")