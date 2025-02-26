class Sobrecarga:
    def __init__(self, *args):
        print('Um')
#    def __init__(self):
#        print('Dois')
#    def __init__(self):
#        print('Três')

Sobrecarga()

class Sobrecarga2:
    def __init__(self, *args):
        self._tam = len(args)
        if self._tam == 0:
            print('Zero')
        elif self._tam > 0:
            print(*args)
        
Sobrecarga2('Teste', 4)

class Calculadora:
    def soma(self, *args):
        return sum(args)
    def soma3(self, *args):
        return reduce(lambda x, y: x + y, args)

calc = Calculadora()
print(calc.soma(2, 2))
print(calc.soma(3.9, 6.1))
print(calc.soma3('Py', 'thon'))

from datetime import date
class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self._d = date.fromisoformat(data)
        if isinstance(data, date):
            self._d = data

    def __str__(self):
        return f'{self._d.day:02d}/{self._d.month}/{self._d.year}'
    
dia1 = Data('2025-02-21')
dia1 = Data(date.today())
print(dia1)

class Tempo:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
    
    def __str__(self):
        return f'{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}'

class Pessoa:
    def __init__(self, nome, idade=None):
        self._nome = nome
        self._idade = idade
    
    @classmethod
    def criar_pessoa(cls):
        return cls('Anônimo')

p1 = Pessoa('Maria', 30)
p2 = Pessoa('João')
p3 = Pessoa.criar_pessoa()
print(p1)
print(p2)
print(p3)
