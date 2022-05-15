dias_reais = int(input(''))
casas = int(input(''))
horas_reais = dias_reais * 3
minutos_reais = horas_reais * 60

#Dividindo 24000 por 20 descobrimos que cada minuto tem 1200 ticks

ticks = minutos_reais * 1200
ticks_construindo = ticks / 2
ticks_casa = ticks_construindo / casas
print(int(ticks_casa))