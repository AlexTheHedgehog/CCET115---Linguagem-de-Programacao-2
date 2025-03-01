class Veiculo:
    def __init__(self, placa, modelo, ano):
        self._placa = placa
        self._modelo = modelo
        self._ano = ano
        self._disponivel = True
    
    def alocar(self):
        if self._disponivel:
            self._disponivel = False
        else:
            raise ValueError('Impossível alocar.')
        
    def liberar(self):
        if not self._disponivel:
            self._disponivel = True
        else:
            raise ValueError('Impossível liberar.')
    
    def verificar_disponibilidade(self):
        # return self._disponivel
        if self._disponivel:
            return 'Veículo disponível.'
        else:
            return 'Veículo indisponível.'
    
    def __str__(self):
        return f'Modelo: {self._modelo}\nPlaca: {self._placa}'
    
    @classmethod
    def iniciar_de_dict(cls, dicio):
        try:
            if ('placa' in dicio.keys()) and ('modelo' in dicio.keys()) and ('ano' in dicio.keys()):
                return cls(dicio['placa'], dicio['modelo'])
            else:
                raise ValueError('É necessário ter 3 chaves, denominadas: placa, modelo e ano')
        except ValueError as e:
            print(e)