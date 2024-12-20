originais = 'aeiou14579'
novos = '@3!0#IESTN'
resp = -1

def edit_frase():
    return input('Entre com uma frase (você pode utilizar letras e números): ')


def crip(x):
    sub = x.maketrans(originais, novos)
    return x.translate(sub)


def decrip(x):
    sub = x.maketrans(novos, originais)
    return x.translate(sub)


def edit():
    a = input('Entre com os valores a serem substituídos: ')
    b = input('Entre com os novos valores: ')
    return [a, b]
    

frase = edit_frase()

while resp != 0:
    print(f'Sua frase: {frase}\n')
    print(f"{'-'*10}MENU{'-'*10}\nEntre com o valor respectivo à ação que será realizada.")
    print(f'[1] - Editar frase\n[2] - Editar mapeamento\n[3] - Criptografar\n[4] - Descriptografar\n[0] - Sair do programa')
    resp = int(input('Resposta: '))
    if resp == 1:
        frase = edit_frase()
    elif resp == 2:
        originais, novos = edit()
    elif resp == 3:
        frase = crip(frase)
    elif resp == 4:
        frase = decrip(frase)




"""
originais = 'aeiou14579'; novos = '@3!0#IESTN'
frase = input('Entre com uma frase (você pode utilizar letras e números): ')
resp = input('Você quer configurar seu próprio mapeamento? [S/N]: ')[0].upper()
if resp == 'S':
    originais = input('Entre com os valores a serem substituídos: ')
    novos = input('Entre com os novos valores: ')
    
sub = frase.maketrans(originais, novos)
print(f'Sua mensagem criptografada é: {frase.translate(sub)}')
resp = input('Deseja descriptografá-la? [S/N]: ')[0].upper()
if resp == 'S':
    sub2 = frase.maketrans(novos, originais)
    print(frase.translate(sub2))
"""