class Igualador:
    @staticmethod
    def isfileequal(arq1, arq2):
        leitura1 = arq1.read()
        leitura2 = arq2.read()
        if leitura1 == leitura2:
            return True
        else:
            return False