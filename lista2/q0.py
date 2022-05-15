# variáveis

n = int(input(''))
competidor = ''
latas = 0
maiorl = latas
vencedor = competidor

# comando for
for i in range(1, n+1):
    competidor = input('')
    latas = int(input(''))
    if i == 1:
        maiorl = latas
        vencedor = competidor
    else:
        if latas > maiorl:
            maiorl = latas
            vencedor = competidor

#output

print(f'{vencedor} e o novo anjo!')
