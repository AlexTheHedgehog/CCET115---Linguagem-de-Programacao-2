class SalarioError(Exception):
    print('Salário não pode ser negativo.')

class Funcionario:
    def __init__(self, nome, salario, cargo):
        try:
            if salario < 0:
                raise SalarioError()
            self._salario = salario
            self._nome = nome
            self._cargo = cargo
        except SalarioError as se:
            print(se)
    
    def aumentar_salario(self, percentual):
        self._salario += self._salario * percentual / 100
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        try:
            if valor < 0:
                raise SalarioError
            self._salario = valor
        except SalarioError as se:
            print(se)
    
    def trocar_cargo(self, novo_cargo):
        self._cargo = novo_cargo
    
    def mostrar_funcionario(self):
        return f'Nome: {self._nome}\nSalário: {self._salario},\nCargo: {self._cargo}'