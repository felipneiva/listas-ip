# variáveis

n = int(input(''))
pessoa = ''
paredao = ''
ganhador = ''
restantes = 19 - n

for i in range(0, n):
    pessoa = input('')
    if pessoa == 'Prior':
        print('IIIHHH! El mago esta eliminado!')
    if pessoa == 'Manu':
        print('Manu saiu! Bruna Marquezine deve estar muito triste :(')
    if pessoa == 'Pyong':
        print('Agora o Pyong que dormiu, esta eliminado')
    if pessoa == 'Gizelly':
        print('PPPPPYYYYYOOOONNNGGG LEEEEEE, Gizelly volta pra casa!')
    if i == 0:
        paredao = pessoa
    ganhador = pessoa

print(f'- O indicado(a) ao paredao nessa semana e: {paredao}')
if restantes > 1:
    print(f'- Ainda restam {19-n} pessoas na disputa pela lideranca!')
else:
    print(f'- O novo lider da semana e: {ganhador}!')
