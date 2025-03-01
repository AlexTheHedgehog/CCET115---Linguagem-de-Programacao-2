from pedido import Pedido

class Lanchonete:
    def __init__(self):
        self.cardapio = []
        self.clientes = []
    
    def add_item_card(self, item):
        self.cardapio.append(item)
    
    def rem_item_card(self, item):
        self.cardapio.remove(item)
    
    def procurar_item(self, nome):
        nomes = [i.nome for i in self.cardapio]
        if nome in nomes:
            return f'Pedido encontrado!\n\n{self.cardapio[nomes.find(nome)]}'
        else:
            return 'Pedido não encontrado.'
    
    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def rem_cliente(self, cliente):
        self.cliente.remove(cliente)
    
    def reg_pedido(self, cliente, *itens):
        pedido = Pedido()
        for i in itens:
            pedido.adicionar_item(i)
        
        cliente.add_pedido(pedido)
    
    def atualizar_status(self, pedido):
        if pedido.status == 'em preparo':
            pedido.alterar_status('pronto')
        elif pedido.status == 'pronto':
            pedido.alterar_status('entregue')
        else:
            print('Esse pedido já está entregue.')
    