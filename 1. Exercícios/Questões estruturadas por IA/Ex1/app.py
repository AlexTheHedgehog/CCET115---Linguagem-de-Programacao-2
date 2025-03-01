from livro import Livro
from membro import Membro
from biblioteca import Biblioteca

'''Crie um programa em Python que implemente um sistema de gerenciamento de biblioteca usando os
conceitos de orientação a objetos. O sistema deve ser capaz de gerenciar livros,membros e empréstimos.

Requisitos:

    Classe Livro:

        Atributos: título, autor, ano de publicação, ISBN, disponibilidade.

        Métodos: exibir informações do livro, verificar disponibilidade, alterar disponibilidade.

    Classe Membro:

        Atributos: nome, número de identificação, lista de livros emprestados.

        Métodos: exibir informações do membro, adicionar livro emprestado, remover livro emprestado, listar livros emprestados.

    Classe Biblioteca:

        Atributos: lista de livros, lista de membros.

        Métodos: adicionar livro, remover livro, procurar livro por título, adicionar membro, remover membro, registrar empréstimo, registrar devolução.'''

aia = Livro('O Conto da Aia', 'Jubiscreudison', 1986, 2315365462)
bosta = Livro('Uma Odisseia no Espaço', 'Cacetinho', 1990, 654685454982)
daniel = Membro('Daniel', 20230300001)
biblioteca = Biblioteca()
biblioteca.add_livro(aia)
biblioteca.add_livro(bosta)
biblioteca.add_membro(daniel)
biblioteca.emprestar(aia, daniel)
biblioteca.emprestar(bosta, daniel)
daniel.listar_livros()
