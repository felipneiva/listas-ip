# variaveis

n_chefes = int(input(''))
pior_media = 100
pior_nome = ''
erro = False

# comando for

for i in range(1, n_chefes+1):
    nome = input('')
    nota1 = float(input(''))
    nota2 = float(input(''))
    nota3 = float(input(''))
    media = (nota1 + nota2 + nota3) / 3
    if media < pior_media:
        pior_media = media
        pior_nome = nome
    if media <= 0:
        erro = True

# outputs

if not erro:
    print(f'O chef eliminado da vez é: {pior_nome} - {pior_media:.2f}')
elif erro:
    print('Ocorreu um erro no sistema de notas, por favor insira notas validas')

