print('Entre com os grupos de convidados, separados por vírgula.\n')

a = set(input('Grupo A: ').split(','))
b = set(input('Grupo B: ').split(','))

convidados = {'união': a | b, 'comum': a & b, 'apenas a': a - b, 'exclusivos': a ^ b}

print(f'União dos grupos: {convidados["união"]}')
print(f'Interseção entre os grupos: {convidados["comum"]}')
print(f'Convidados apenas no grupo A: {convidados["apenas a"]}')
print(f'Convidados exclusivos: {convidados["exclusivos"]}')
