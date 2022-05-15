import math

x_tantan = int(input(''))
z_tantan = int(input(''))

distancia_hogsmeade = math.sqrt(((34-x_tantan)**2) + ((220 - z_tantan)**2))
distancia_kakariko = math.sqrt(((0-x_tantan)**2) + ((0 - z_tantan)**2))
distancia_solitude = math.sqrt(((140-x_tantan)**2) + ((456 - z_tantan)**2))

print(f'Distancia para Hogsmeade: {distancia_hogsmeade:.2f}')
print(f'Distancia para Kakariko: {distancia_kakariko:.2f}')
print(f'Distancia para Solitude: {distancia_solitude:.2f}')
