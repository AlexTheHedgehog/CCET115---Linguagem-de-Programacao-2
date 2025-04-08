#criar classe Aluno com os atributos encapsulados com um underscore (_): nome, matricula e curso, e um método participar_evento
#criar a interface CertificadoInterface com um método verificar_certificado
#criar a classe Evento com atributos nome e valor_inscricao, um método para adicionar alunos e outro para emitir certificados, que verifica os alunos que participaram do evento

class Aluno:
    def __init__(self, nome, matricula, curso):
        self._nome = nome
        self._matricula = matricula
        self._curso = curso
        self._participou_evento = False

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

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        self._curso = novo_curso

    def participar_evento(self):
        self._participou_evento = True

class CertificadoInterface:
    def verificar_certificado(self):
        raise NotImplementedError("Método deve ser implementado na subclasse")

class Evento:
    def __init__(self, nome, valor_inscricao):
        self._nome = nome
        self._valor_inscricao = valor_inscricao
        self._alunos = []

    @property
    def nome(self):
        return self._nome

    @property
    def valor_inscricao(self):
        return self._valor_inscricao

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self._alunos.append(aluno)

    def emitir_certificados(self):
        for aluno in self._alunos:
            if aluno._participou_evento:
                print(f"Certificado emitido para {aluno.nome}")

#criar a classe AlunoCertificado, que herda de Aluno e implementa a interface CertificadoInterface
#a verificação do método verificar_certificado deve retornar True se o aluno participou do evento com 75% de aprovação e False caso contrário

class AlunoCertificado(Aluno, CertificadoInterface):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)

    def verificar_certificado(self):
        return self._participou_evento and self._curso.aprovacao >= 75

#criar uma instância da classe Evento
#criar instancias dos alunos certificados

evento = Evento("Evento de Programação", 50.00)
aluno1 = AlunoCertificado("João", "12345", "Engenharia da Computação")
aluno2 = AlunoCertificado("Maria", "67890", "Engenharia de Software")
aluno3 = AlunoCertificado("Pedro", "54321", "Sistemas de Informação")
aluno4 = AlunoCertificado("Ana", "98765", "Ciência da Computação")