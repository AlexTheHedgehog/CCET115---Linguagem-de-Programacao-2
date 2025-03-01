import sistema_viagem, pessoa, veiculos

p1 = pessoa.Motorista('Daniel', '02280763230', 20, 'XXXXXX')
v1 = veiculos.Veiculo('A4FGX-320', 'Fiat UNO', 2013)

sistema = sistema_viagem.Viagem(p1, v1, 'Rio Branco')
sistema.iniciar()
sistema.finalizar('05/03/2025')

print(sistema)
print(sistema.calcular_tempo_estimado(325, 80))