def soma_e_maior(lista):
    conj = set(lista)
    soma = sum(conj)
    maior = max(conj)
    return soma, maior


print(soma_e_maior([1, 2, 3, 3, 4, 5, 4, 6]))

frase = 'Infelizmente ele morreu. Morreu e foi humilhado. Ele gostou que foi ao jogo.'

def freq_palavras(txt):
    palavras = txt.replace('.', '').lower().split()
    return {i:palavras.count(i) for i in set(palavras)}


print(freq_palavras(frase))