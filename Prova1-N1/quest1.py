#A entrada deveria ser por linha
#O total exibido está incorreto
#80%
produtos = dict()
i = 1

while i <= 3:
    try:
        print(f'\nPRODUTO {i}\n')
        nome = input('Nome do produto: ')
        quant = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        produtos[nome] = (quant, preco)
        i += 1
    except ValueError as vrr:
        print('Um dos valores inseridos não é compatível. Tente novamente.')

print('Produtos cadastrados!\n')
produto = input('Qual produto deseja verificar se está em estoque? ')

if produto in produtos:
    print(f'O produto {produto} está em estoque.\nValor total disponível: {sum(produtos[produto]):.2f}')
else:
    print('Este produto não está em estoque.')