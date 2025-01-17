class Pessoa:
    #init
    def __init__(self, n:str, i:int):
        self.nome = n
        self.idade = i
    
    #Método
    def exibirDados(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}')