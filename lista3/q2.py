usuarios = []
likes = []
max_likes = 0
posicao = 0

n = int(input())

for i in range(0, n):
    usuario = input()
    n_likes = int(input())
    usuarios.append(usuario)
    likes.append(n_likes)

for valor in likes:
    if valor > max_likes:
        max_likes = valor
        posicao = likes.index(valor)

likes.sort(reverse=True)

print('O numero de curtidas dos videos que vao aparecer na For You segue a ordem:')
for numero in likes[0:n-1]:
    print(f'{numero}, ', end='')
print(likes[-1])
print(f'O primeiro usuario que vai aparecer na For You e {usuarios[posicao]}!')