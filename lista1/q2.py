
nome = input('')
valor_semestre1 = int(input(''))
valor_semestre2 = int(input(''))
valor_total = valor_semestre1 + valor_semestre2
media_mensal = int(valor_total / 12)

if nome != 'Jim Halpert' and nome != 'Dwight Schrute' and nome != 'Phyllis Vance' and nome != 'Stanley Hudson':
    print('Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.')
elif media_mensal  <= 50:
    print(f'{nome}, voce so vendeu {(media_mensal)} por mes? Voce ta demitido... Brincadeira!')
elif 100 > media_mensal > 50:
    print(f'{nome}, voce mandou mal... Vai ter que pagar meu almoco.')
elif media_mensal >100:
    print(f'Parabens, {nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!')
