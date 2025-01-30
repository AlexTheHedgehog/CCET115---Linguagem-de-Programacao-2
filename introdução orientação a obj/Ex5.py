from emprestimo import Emprestimo
from conta import Conta

# Implemente uma classe Emprestimo que está diretamente associada a uma conta. a conta
# pode ter empréstimos vinculados. Adicione a funcionalidade de pagar parcelas, diminuindo
# o saldo da conta e reduzindo a dívida.

c1 = Conta(120, 787.98, 800)
crediario = Emprestimo(c1, 2750.50)
print(f'{crediario.divida:.2f}')

crediario.pagar_parcela(200)
print(f'{c1.saldo:.2f} {crediario.divida:.2f}')
