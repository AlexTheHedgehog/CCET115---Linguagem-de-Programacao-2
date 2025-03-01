class Biblioteca:
    # iniciar classe
    def __init__(self):
        self.livros = []
        self.membros = []
        self.livros_emp = []
    
    # adicionar livro
    def add_livro(self, livro):
        if livro in self.livros:
            print('O livro já está na biblioteca.')
        else:
            self.livros.append(livro)
            livro.alterar_disp()
    
    # remover livro
    def rem_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            livro.alterar_disp()
        else:
            print('O livro não está na biblioteca.')
    
    # adicionar membro
    def add_membro(self, membro):
        if membro in self.membros:
            print('O membro já está na biblioteca.')
        else:
            self.membros.append(membro)
    
    # remover membro
    def rem_membro(self, membro):
        if membro in self.membros:
            self.membros.remove(membro)
        else:
            print('O membro não está na biblioteca.')
    
    # registrar emprestimo
    def emprestar(self, livro, membro):
        if (livro in self.livros) and (membro in self.membros):
            self.livros_emp.append(livro)
            membro.emp_livro(livro)
            self.rem_livro(livro)
        else:
            print(f'Algo deu errado 1.')
    
    # registrar devolução
    def devolver(self, livro, membro):
        if (livro in self.livros_emp) and (membro in self.membros) and (livro in membro.livros_emp):
            self.livros_emp.remove(livro)
            membro.rem_emp_livro(livro)
            self.add_livro(livro)
        else:
            print(f'Algo deu errado 2.')
