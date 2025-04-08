from especificador import Especificador

original = open('original.txt', 'r', encoding='utf-8')
resposta = Especificador.especificar(original)
original.close()
print(resposta)