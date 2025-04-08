def substituir(padrao:str, substituta:str, arq1, arq2):
    leitura = arq1.read()
    substituir = (leitura.replace(padrao, substituta)).replace(f'{padrao}\n', f'{substituta}\n')
    arq2.write(substituir)

original = open('original.txt', 'r', encoding='utf-8')
novo = open('novo.txt', 'w', encoding='utf-8')

substituir('frase motivacional', 'eu me sinto muito mal', original, novo)