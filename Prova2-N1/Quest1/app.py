# 100%
from universidade import Universidade
from centro import Centro

ccet = Centro('Centro de Ciências Exatas e Tecnológicas', 'CCET')
ccsd = Centro('Centro de Ciências da Saúde e Desporto', 'CCSD')
ccet2 = Centro('Centro de Ciências Exatas e Tecnológicas', 'CCET2')
ufac = Universidade('UFAC')
ufac.adicionar_centro(ccet)
ufac.adicionar_centro(ccsd)
ufac.listar_centros()
ufac.adicionar_centro(ccet)
ufac.adicionar_centro(ccet2) #acrescentei
