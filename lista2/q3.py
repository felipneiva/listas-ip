# variáveis

chegada = int(input(''))
progresso = int(input(''))
local_final = 0

# comandos for e while

for i in range(1, progresso + 1):
    local_final += i
while progresso > 0:
    progresso = int(input(''))
    for i in range(1, progresso + 1):
        local_final += i

# outputs

if local_final < chegada:
    print('Ainda nos falta um pouco...')
elif local_final == chegada:
    print('Pode beijar a noiva, afinal, vocês conseguiram!')
elif chegada < local_final < (20 * chegada):
    print('Parece que os pombinhos passaram um pouco do local...')
elif (20 * chegada) <= local_final <= (100 * chegada):
    print('Acho que nos perdemos um pouco no caminho, onde estamos?')
elif local_final > (100 * chegada):
    print('Hum... acho que o casal deve rever seus votos de matrimônio...')
