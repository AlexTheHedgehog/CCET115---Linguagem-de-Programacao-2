cont = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    sequencia1 = []
    sequencia2 = []

    for i in range(n):
        sequencia2.append(int(input()))
        if len(sequencia2) == m:
            sequencia1.append(sequencia2.copy())
            sequencia2.clear()
    
    print(sequencia1)      
    media = [int(sum(x)/len(x)) for x in sequencia1]
    media.sort()
    menor = media[0]
    maior = media[-1]
    
    print(f'Teste {cont}')
    print(menor, maior)
    print()
    cont += 1