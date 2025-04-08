from ordenar import Ordenar

original = open('original.txt', 'r', encoding='utf-8')
Ordenar.ordenar_arquivo(original)
original.close()