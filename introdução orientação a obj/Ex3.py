from hotel import Hotel, Quarto, Cliente

# 3)Crie um pequeno sistema de Reserva de Hotel com as
# classes Hotel, Quarto e Cliente. Garanta que os quartos
# só possam ser reservados se estiverem disponíveis.
# Implemente métodos para checar reservas e liberar
# quartos.

hotel = Hotel('Uirapuru', 'Rua Uirapuru')

q1 = Quarto('Suite Master', 2)
q2 = Quarto('Suite Plus', 3)
q3 = Quarto('Suite Single', 1)

hotel.incluir_quartos(q1)
hotel.incluir_quartos(q2)
hotel.incluir_quartos(q3)

cliente1 = Cliente('Daniel', '02280763230')

print(f'Capacidade do Hotel: {len(hotel.quartos)}')

hotel.reservar_quarto('Suite Master', cliente1)