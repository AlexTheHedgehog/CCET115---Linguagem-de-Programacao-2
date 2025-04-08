arquivo = open('teste.txt', 'a', encoding='utf-8')
arquivo.write('\ncom mais uma linha de verdade!')
for i in range(5):
    arquivo.write(f'\nLinha {i}: -> Mais uma linha.')
arquivo.close()
leitura = open('teste.txt')
#conteudo = leitura.read()
#print(conteudo)
#Segunda forma de ler um arquivo
linha = leitura.readline()
while linha != '':
    print(linha, end='')
    linha = leitura.readline()
print('\nFim da leitura')
leitura.close()