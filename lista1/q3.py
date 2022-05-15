coordA = int(input(''))
coordB = int(input(''))
r = int(input(''))
coordX = int(input(''))
coordY = int(input(''))
somaraios = r + 2
distancia = (((coordA - coordX) ** 2) + ((coordB - coordY) ** 2)) ** (1/2)
if r <= 0:
    print('Sua amplitude esta baixa, nao conseguimos te localizar no radar')
else:
    if distancia < somaraios:
        print('Esferas do dragao detectadas')
    elif distancia > somaraios:
        print('Esferas fora do radar')
