cartas_luke = []
cartas_demonio = []


def duelo(a, b):
    vencedor = ''
    if int(a[1]) > int(b[1]):
        vencedor = 'Luke'
    elif int(b[1]) > int(a[1]):
        vencedor = 'Demonio'
    return vencedor


for i in range(5):
    cartas_luke.append(input().split('/'))
for i in range(5):
    cartas_demonio.append(input().split('/'))


vitorias_luke = 0
vitorias_demonio = 0
round = 1

continua = True

for i in range(5):
    if duelo(cartas_luke[i], cartas_demonio[i]) == 'Luke':
        vitorias_luke += 1
        print(f'Luke foi muito esperto, usou {cartas_luke[i][0]} e ganhou o {round}º round!')
        if vitorias_luke == 3:
            break
    elif duelo(cartas_luke[i], cartas_demonio[i]) == 'Demonio':
        vitorias_demonio += 1
        print(f'Inscryption nao aliviou, usou {cartas_demonio[i][0]} e venceu o {round}º round!')
        if vitorias_demonio == 3:
            break
    round += 1

if vitorias_luke == 3:
    print('Luke Carter ganhou na batalha de cartas e avançou de fase na sua luta para conseguir sair da cabana!')
elif vitorias_demonio == 3:
    print('Luke Carter foi derrotado na batalha de cartas e sua alma permanecera na cabana para todo o sempre!')