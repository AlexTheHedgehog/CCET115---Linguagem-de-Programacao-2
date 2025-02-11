from produto import Produto

p1 = Produto('Arroz', 23.55)

if p1.is_preco_valido(p1.preco):
    print('Preço válido')