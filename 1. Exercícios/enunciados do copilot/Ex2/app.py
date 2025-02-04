from cliente import Cliente
from lanchonete import Lanchonete

'''Crie um programa em Python que implemente um sistema de gerenciamento de transações de uma lanchonete usando os conceitos de orientação a objetos. O sistema deve ser capaz de gerenciar os itens do cardápio, os pedidos dos clientes e as transações financeiras.

Requisitos:

Classe ItemCardapio:

Atributos: nome, preço, disponibilidade.

Métodos: exibir informações do item, verificar disponibilidade, alterar disponibilidade.

Classe Pedido:

Atributos: número do pedido, lista de itens, status do pedido (ex: "em preparo", "pronto", "entregue").

Métodos: adicionar item ao pedido, remover item do pedido, calcular valor total, alterar status do pedido.

Classe Cliente:

Atributos: nome, número de identificação, lista de pedidos.

Métodos: exibir informações do cliente, adicionar pedido, listar pedidos.

Classe Lanchonete:

Atributos: lista de itens do cardápio, lista de clientes.

Métodos: adicionar item ao cardápio, remover item do cardápio, procurar item por nome, adicionar cliente, remover cliente, registrar pedido, atualizar status do pedido.'''