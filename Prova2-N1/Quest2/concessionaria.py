#ok

class Concessionaria:
    def __init__(self):
        self.veiculos = {}

    def adicionar_veiculos(self, veiculo):
        try:
            if veiculo.nome not in self.veiculos.keys():
                self.veiculos[veiculo.nome] = veiculo
            else:
                raise IndexError

        except IndexError as err:
            print(f'Não são permitidos modelos duplicados!')

    def listar_veiculos(self):
        print('Veículos presentes nessa concessionária:\n')
        for i in self.veiculos.keys():
            print(i)
