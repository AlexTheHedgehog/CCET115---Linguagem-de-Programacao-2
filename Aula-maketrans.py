frase = 'Este é um texto transformado!'
tabela = frase.maketrans('abc', '130', 'x')
tabela2 = frase.maketrans({'E':'3', '!':None, 'a':'@', 'o':'0'})
print(tabela)
print(tabela2)
print(frase.translate(tabela))
print(frase.translate(tabela2))