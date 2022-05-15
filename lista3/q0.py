passo = ''
passos = []

while passo != 'FIM':
    passo = input()
    passos.append(passo)

passos_faltantes = len(passos) - 4

print(f'Olá seguimores! O primeiro passo da dancinha é {passos[0]}')
print(f'Depois, a gente faz o {passos[1]} e {passos[2]}')
print(f'Temos ainda mais {passos_faltantes} passos pra aprender!')
print(f'Por último, vamos fazer o {passos[-2]}')
