#Todos os veículos deveriam ter obrigatoriamente um motor associado.
#Dessa forma ainda podemos passar qualquer argumento na variável motor.
#85%

class Veiculo:
    def __init__(self, nome, motor):
        self.nome = nome
        self.motor = motor

    def exibir_informacoes(self):
        print(f'Modelo do veículo: {self.nome}\nMotor: {self.motor.nome}\nPotência: {self.motor.potencia}\n')
