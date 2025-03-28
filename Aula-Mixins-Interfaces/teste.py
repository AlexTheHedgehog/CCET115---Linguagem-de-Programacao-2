from diretor import Diretor
from cliente import Cliente
from login import Login
from presidente import Presidente
from autenticavel import AutenticavelInterface

d1 = Diretor()
c1 = Cliente()
p1 = Presidente()

login = Login()

login.logar(d1)
login.logar(c1)
login.logar(p1)

AutenticavelInterface.register(Presidente)
login.logar(p1)