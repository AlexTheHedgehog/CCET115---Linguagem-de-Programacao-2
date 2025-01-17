class Hotel:
    def __init__(self, n, end):
        self.nome = n
        self.endereco = end
        self.quartos = []
    
    def incluir_quartos(self, quarto):
        self.quartos.append(quarto)
    
    def reservar_quarto(self, num, cli):
        for q in self.quartos:
            if q.numero == num:
                if q.reservar():
                    print(f'Quarto {q.numero} reservado com sucesso pelo {cli.nome}!')
                else:
                    print(f'Quarto {q.numero} está ocupado!')
    
    def liberar_quarto(self, num):
        for q in self.quartos:
            if q.numero == num:
                if q.liberar():
                    print(f'Quarto {q.numero} liberado!')
    
    def verificar_disponibilidade(self):
        
        for quarto in self.quartos:
            if quarto.disponivel:
                print(f'Quarto: {quarto.capacidade}')
        

class Quarto:
    def __init__(self, n, c):
        self.numero = n
        self.capacidade = c
        self.disponivel = True
    
    def reservar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False
    
    def liberar(self):
        self.disponivel = True
    
    def __str__(self):
        return f'{self.numero}|{self.capacidade}|{self.disponivel}'

class Cliente:
    def __init__(self, n, c):
        self.nome = n
        self.cpf = c