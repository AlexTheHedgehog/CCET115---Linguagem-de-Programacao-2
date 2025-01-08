from conta import Conta


c1 = Conta(2, 'Daniel', 1017.98, 400) #Cria uma instância da classe Conta
print(c1)
print(f'Conta de {c1.titular}')
print(c1.ver_saldo())
c2 = Conta(3, 'Juan', 0, 0)
c1.trasferir(30.55, c2)
print(f'Conta de {c2.titular}')
print(c2.ver_saldo())
