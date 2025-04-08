#criar uma classe curso com os atributos encapsulados nome, codigo, carga horaria, utilizando um underscore (_)
#criar os métodos de acesso (getters) e modificação (setters) com decoradores (utilizando @) para os atributos nome, codigo e carga horaria
#criar um método para exibir as informações do curso

class Curso:
    def __init__(self, nome, codigo, carga_horaria):
        self._nome = nome
        self._codigo = codigo
        self._carga_horaria = carga_horaria
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self._codigo = novo_codigo
    
    @property
    def carga_horaria(self):
        return self._carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        self._carga_horaria = nova_carga_horaria
    
    def exibir_informacoes(self):
        print(f"Nome: {self._nome}")

#criar uma classe Disciplina com os atributos encapsulados nome, codigo, carga horaria e curso
#criar os métodos de acesso (getters) e modificação (setters) com decoradores (utilizando @) para os atributos nome, codigo, carga horaria e curso
#a Disciplina deve possuir uma referência para um objeto da classe Curso
#criar um método para exibir as informações da disciplina

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria, curso):
        self._nome = nome
        self._codigo = codigo
        self._carga_horaria = carga_horaria
        self._curso = curso
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self._codigo = novo_codigo
    
    @property
    def carga_horaria(self):
        return self._carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        self._carga_horaria = nova_carga_horaria
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, novo_curso):
        self._curso = novo_curso
    
    def exibir_informacoes(self):
        print(f"Nome: {self._nome}")


curso1 = Curso("Engenharia de Software", "ES123", 360)
curso1.exibir_informacoes()
print('--------------------')

curso1.nome = "Engenharia de Computação"
curso1.codigo = "EC456"
curso1.carga_horaria = 400
curso1.exibir_informacoes()
print('====================')

disciplina1 = Disciplina("Programação Orientada a Objetos", "POO123", 60, curso1)
disciplina1.exibir_informacoes()