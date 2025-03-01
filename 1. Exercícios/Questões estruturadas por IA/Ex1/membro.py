class Membro:
    # criar classe
    def __init__(self, nome, num):
        self.nome = nome
        self.num = num
        self.livros_emp = []
    
    # exibir info
    def __str__(self):
        return f'Nome: {self.nome}\nNúmero de identificação: {self.num}\n'
    
    # adicionar livro emprestado
    def emp_livro(self, livro):
        self.livros_emp.append(livro)
    
    def rem_emp_livro(self, livro):
        self.livros_emp.remove(livro)

    # listar livros emprestados
    def listar_livros(self):
        print('Livros emprestados para esse membro:\n')
        for i in self.livros_emp:
            print(f'{i.__str__()}\n')
