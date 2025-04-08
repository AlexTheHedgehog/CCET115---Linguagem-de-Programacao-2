class Ordenar:
    @staticmethod
    def ordenar_arquivo(arquivo):
        leitura = arquivo.read()
        numeros = [int(i) for i in list(leitura.split('\n')) if i.isnumeric()]
        numeros.sort()
        numeros = [str(i) for i in numeros]
        novo = open('novo.txt', 'w', encoding='utf-8')
        novo.write('\n'.join(numeros))
        novo.close()
        
        