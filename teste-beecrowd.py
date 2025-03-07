cont = 1

while True:
    temperaturas = []
    n, m = map(int, input().split())
    if n == m == 0:
        break
    
    for i in range(n):
        temperaturas.append(int((int(input()))/m))
    
    print(f'Teste {cont}\n{min(temperaturas)} {max(temperaturas)}\n')
    cont += 1