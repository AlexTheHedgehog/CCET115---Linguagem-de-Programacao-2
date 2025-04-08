from abc import ABC, abstractmethod

#crie uma classe Aluno com atributos encapsulados com underscore (_): nome e matricula
#faça os atributos serem acessíveis por meio de @property e @setter

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


#crie um MixIn chamado BolsaPesquisaMixIn, com o método solicitar_bolsa_pesquisa(), que retorna mensagem confirmando a solicitação

class BolsaPesquisaMixIn:
    def solicitar_bolsa_pesquisa(self):
        return f"Solicitação de bolsa de pesquisa para {self._nome} foi enviada com sucesso!"
    
#crie duas subclasses, AlunoGraduacao e AlunoPosGraduacao, que herdam de Aluno
#AlunoGraduacao possui um atributo chamado curso, e AlunoPosgraduacao possui um atributo chamado pesquisa. ambos com underscore e encapsulados (_)

class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self._curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, novo_curso):
        self._curso = novo_curso
    
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
    
class AlunoPosGraduacao(Aluno, BolsaPesquisaMixIn):
    def __init__(self, nome, matricula, pesquisa):
        super().__init__(nome, matricula)
        self._pesquisa = pesquisa
    
    @property
    def pesquisa(self):
        return self._pesquisa
    
    @pesquisa.setter
    def pesquisa(self, nova_pesquisa):
        self._pesquisa = nova_pesquisa
    
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

#crie uma interface EditalInterface, com abc, que exige implementação do método exibir_detalhes_edital() polimorficamente nas subclasses, retornando uma mensagem personalizada sobra a elegibilidade do aluno ao edital

class EditalInterface(ABC):
    @abstractmethod
    def exibir_detalhes_edital(self):
        pass

aluno1 = AlunoGraduacao("João", "12345", "Engenharia")
aluno2 = AlunoPosGraduacao("Maria", "67890", "Inteligência Artificial")
print(aluno2.solicitar_bolsa_pesquisa())
print(aluno1.nome, aluno1.matricula, aluno1.curso)
print(aluno2.nome, aluno2.pesquisa)