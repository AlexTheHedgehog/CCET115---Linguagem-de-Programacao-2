from produto import Produto

# 2)Desenvolva uma classe Produto com atributos nome,
# preço e quantidade. Implemente métodos para calcular
# o valor total do estoque e permitir inclusão ou remoção
# de itens.

p1 = Produto('Arroz', 23.50, 190)
print(p1.valorTotal())
p1.incluirItens(70)
print(p1.valorTotal())
p1.removerItens(40)
print(p1.valorTotal())