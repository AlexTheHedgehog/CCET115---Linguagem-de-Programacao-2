class itemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.disp = True
    
    def __str__(self):
        return f'Nome: {self.nome}\nPreço: R${self.preco:.2f}'
    
    def ver_disp(self):
        if self.disp:
            return f'Disponível'
        else:
            return f'Indisponível'

    def alterar_disp(self):
        if self.disp:
            self.disp = False
        else:
            self.disp = True
