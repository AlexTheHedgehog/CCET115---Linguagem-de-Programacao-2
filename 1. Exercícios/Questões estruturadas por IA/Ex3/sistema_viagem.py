from datetime import date

class Viagem:
    def __init__(self, motorista, veiculo, destino):
        self._motorista = motorista
        self._veiculo = veiculo
        self._destino = destino
        self._data_s = self._data_r = 'indefinida'
    
    def iniciar(self):
        try:
            self._veiculo.alocar()
            data = list(str(date.today()).split('-'))
            data.reverse()
            self._data_s = '/'.join(data)
        except ValueError as e:
            print(e)
    
    def finalizar(self, data):
        try:
            self._veiculo.liberar()
            self._data_r = data
        except ValueError as e:
            print(e)
    
    def __str__(self):
        return f'Motorista: {self._motorista._nome}\nVeículo: {self._veiculo._modelo}\nDestino: {self._destino}\nData de saída: {self._data_s}, Data de retorno: {self._data_r}'
    
    @staticmethod
    def calcular_tempo_estimado(dist:float, v_media:float):
        return dist / v_media
    
    @property
    def data_r(self):
        return self._data_r
    
    @data_r.setter
    def data_r(self, data):
        self._data_r = data