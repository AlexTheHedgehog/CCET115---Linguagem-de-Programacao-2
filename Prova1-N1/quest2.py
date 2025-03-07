#Faltou implementar 'b' e 'f'
#75%
print('TABELA DA CRIPTOGRAFIA\n')

frase = input('Entre com um texto para criptografar: ')

while True:
    try:
        originais = input('Entre com os caracteres que serão substituídos: ')
        novos = input('Entre com os novos caracteres: ')
        sub = frase.maketrans(originais, novos)
        break
    except ValueError as err:
        print('As entradas devem ter a mesma quantidade de caracteres. Tente novamente.')

crip = frase.translate(sub)
print(f'Texto criptografado: {crip}')
print(f'Texto criptografado ao contrário: {crip[::-1]}')

vogais = [i for i in crip.split() if set('aeiou') & set(i)]

if vogais:
    palavras = ' '.join(vogais)#(eba)#
else:
    palavras = 'Sem palavras com vogais no texto.'
print(f'Texto apenas com palavras com vogais: {palavras}')
