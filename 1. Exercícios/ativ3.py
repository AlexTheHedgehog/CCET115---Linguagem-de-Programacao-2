frase = 'Python é Divertido!'

def maius(s:str):
    m = ''
    for i in range(len(s)):
        if s[i].isupper():
            m += s[i]
    return m


def emb(s:str, ind:list):
    return ''.join([s[i] for i in ind])
    
print(maius(frase))
print(emb(frase, [5, 0, 4, 3, 2, 1]))