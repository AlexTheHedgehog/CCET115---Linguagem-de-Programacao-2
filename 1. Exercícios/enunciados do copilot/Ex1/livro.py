class Livro:
    # iniciar classe
    def __init__(self, titulo, autor, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        self.disp = False
    
    # informações do livro
    def __str__(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nISBN: {self.isbn}\n'
    
    # verificar disponibilidade
    def ver_disp(self):
        if self.disp:
            return 'O livro está disponível.'
        else:
            return 'O livro não está disponível.'
    
    def alterar_disp(self):
        if self.disp:
            self.disp = False
        else:
            self.disp = True