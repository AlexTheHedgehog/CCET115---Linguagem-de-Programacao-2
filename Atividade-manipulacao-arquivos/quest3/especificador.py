class Especificador:
    @staticmethod
    def especificar(arquivo):
        leitura = arquivo.read()
        caracteres = len(leitura)
        palavras = len(list((leitura.replace('\n', ' ')).split()))
        linhas = len(list(leitura.split('\n')))
        
        
        return f'Nome do arquivo: {arquivo.name}\nQuantidade de linhas: {linhas}\nNº de caracteres: {caracteres}\nNº de palavras: {palavras}'
        