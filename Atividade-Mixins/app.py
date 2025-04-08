from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from manipulador import ManipuladorDeTributaveis
from seguro_de_vida import SeguroDeVida

conta1 = ContaCorrente(75, 'Daniel', 787.98)
conta2 = ContaPoupanca(88, 'Daniel', 200.98)

print(ManipuladorDeTributaveis.calcular_imposto(conta1, conta2))