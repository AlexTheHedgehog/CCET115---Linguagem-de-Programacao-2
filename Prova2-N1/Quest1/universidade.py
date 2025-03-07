# 100%
class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.centros = []

    def adicionar_centro(self, centro):
        if self.centros:
            nomes = [i.nome for i in self.centros]
            codigos = [i.cod for i in self.centros]

            if (centro.nome in nomes) or (centro.cod in codigos):
                print(f'O {centro.nome} já existe na universidade!')
            else:
                self.centros.append(centro)
        else:
            self.centros.append(centro)

    def listar_centros(self):
        print('Centros acadêmicos presentes na universidade:\n')
        for i in self.centros:
            print(f'- Nome do centro acadêmico: {i.nome}, Código: {i.cod}')