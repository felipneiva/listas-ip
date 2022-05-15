qtdviews_1 = []
qtdviews_2 = []
qtdviews_3 = []
nomes = []
medias = []
primeiro = ''
segundo = ''
terceiro = ''

nome1 = input()
views1a = int(input())
views1b = int(input())

qtdviews_1.append(views1a)
qtdviews_1.append(views1b)
nomes.append(nome1)

nome2 = input()
views2a = int(input())
views2b = int(input())

qtdviews_2.append(views2a)
qtdviews_2.append(views2b)
nomes.append(nome2)

nome3 = input()
views3a = int(input())
views3b = int(input())
nomes.append(nome3)

qtdviews_3.append(views3a)
qtdviews_3.append(views3b)

media1 = (sum(qtdviews_1)) / 2
media2 = (sum(qtdviews_2)) / 2
media3 = (sum(qtdviews_3)) / 2
medias.append(media1)
medias.append(media2)
medias.append(media3)

for i in range(len(medias)):
    for j in range(i+1, len(medias)):
        if medias[i] < medias[j]:
            medias[i], medias[j] = medias[j], medias[i]
maior_media = medias[0]
meio_media = medias[1]
menor_media = medias[2]

if maior_media == media1:
    primeiro = nome1
elif maior_media == media2:
    primeiro = nome2
elif maior_media == media3:
    primeiro = nome3
if meio_media == media1:
    segundo = nome1
elif meio_media == media2:
    segundo = nome2
elif meio_media == media3:
    segundo = nome3
if menor_media == media1:
    terceiro = nome1
elif menor_media == media2:
    terceiro = nome2
elif menor_media == media3:
    terceiro = nome3


print(f'1º Lugar: {primeiro} com a media de views: {int(maior_media)}')
print(f'2º Lugar: {segundo} com a media de views: {int(meio_media)}')
print(f'3º Lugar: {terceiro} com a media de views: {int(menor_media)}')