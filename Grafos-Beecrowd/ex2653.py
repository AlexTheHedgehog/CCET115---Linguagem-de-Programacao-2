cont = 0
joias = []

while cont < 10**6:
    try:
        joia = input()
        joias.append(joia)
        cont += len(joia)
    except EOFError:
        break

joias_dif = set(joias)
print(len(joias_dif))