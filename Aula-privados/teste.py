from conta import Conta
c1 = Conta(101, 'Fulano', 1000, 200)
c2 = Conta(200, 'Good', 56121.20, 8000)
#print(c1._saldo)
print(vars(c1))
print(c1.saldo)
c1.saldo = 2000
print(c1.saldo)
print(c1._total_contas)