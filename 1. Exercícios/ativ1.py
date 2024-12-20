import sys
#Faça um programa para solicitar dois valores de entrada para um usuário,
#o primeiro valor deve obrigatoriamente ser armazenado em uma variável do
#tipo int e o outro do tipo float, caso contrário o programa deve solicitar
#ao usuário uma entrada aceitável (com tratamento de exceções). 

while True:
    try:
        a = int(input('Digite um inteiro: '))
        try:
            b = float(input('Digite um real: '))
            break
        except ValueError:
            print('Entre com um real válido.')
    except ValueError:
        print('Entre com um inteiro válido.')
    except:
        print(f'ERRO: {sys.exc_info()[0]}')
print(f'{a:.3f} {b:.3f}')