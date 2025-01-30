from agencia import Agencia
from conta import Conta

# Desenvolva uma classe Agencia que possui
# uma lista de contas bancárias, mas as contas 
# só existem enquanto a agência existir. Adicione
# a capacidade de fechar uma agência, excluindo todas
# as suas contas associadas.

inter = Agencia('Banco Inter')

inter.adicionar_conta(20, 'Daniel', 1000, 800)
inter.imprimir_contas()