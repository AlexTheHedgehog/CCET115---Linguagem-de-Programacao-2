#ok
from motor import Motor
from veiculo import Veiculo
from concessionaria import Concessionaria

veiculo1 = Veiculo('GOL', Motor('Nome de motor', 325))
veiculo2 = Veiculo('Fusca', Motor('Nome de motor 2', 100))
veiculo1.exibir_informacoes()
veiculo2.exibir_informacoes()

concessionaria = Concessionaria()
concessionaria.adicionar_veiculos(veiculo1)
concessionaria.adicionar_veiculos(veiculo2)
concessionaria.listar_veiculos()
concessionaria.adicionar_veiculos(veiculo1)