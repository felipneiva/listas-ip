festas = int(input(''))
cerveja = 0
caipirinha = 0
vodca = 0

for i in range(0, festas):
    cerveja_festa = 0
    caipirinha_festa = 0
    vodca_festa = 0
    copos = int(input(''))
    for c in range(0, copos):
        bebida = input('')
        if bebida == 'cerveja':
            cerveja += 1
            cerveja_festa += 1
        elif bebida == 'caipirinha':
            caipirinha += 1
            caipirinha_festa += 1
        elif bebida == 'vodca':
            vodca_festa += 1
            vodca += 1
    if cerveja_festa > vodca_festa and cerveja_festa > caipirinha_festa:
        print('O que ele mais tomou nessa festa foi: cerveja')
    elif caipirinha_festa > vodca_festa and caipirinha_festa > cerveja_festa:
        print('O que ele mais tomou nessa festa foi: caipirinha')
    elif vodca_festa > caipirinha_festa and vodca_festa > cerveja_festa:
        print('O que ele mais tomou nessa festa foi: vodca')

print(f'cerveja - {cerveja}')
print(f'caipirinha - {caipirinha}')
print(f'vodca - {vodca}')