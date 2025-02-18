from produto_promocional import ProdutoPromocional
from produto_parcelado import ProdutoParcelado

p1 = ProdutoPromocional('Arroz', 12.50, 34)
p1.definir_preco_venda(20)
p2 = ProdutoParcelado('Feijão', 15.99, 50)
p2.definir_preco_venda(20)

print(p1)
print(p2)