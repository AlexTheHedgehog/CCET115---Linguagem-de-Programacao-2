from igualador import Igualador

arq1 = open('arq1.txt', 'r', encoding='utf-8')
arq2 = open('arq2.txt', 'r', encoding='utf-8')
arq3 = open('arq3.txt', 'r', encoding='utf-8')

print(Igualador.isfileequal(arq1, arq2))
print(Igualador.isfileequal(arq2, arq3))

arq1.close()
arq2.close()
arq3.close()