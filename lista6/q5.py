cartas = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei')
cartas_valores = (('As', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
          ('Valete', 11), ('Dama', 11), ('Rei', 11))
naipes = ('ouros', 'paus', 'espadas', 'copas')
cartas_jogadas = {'As': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '2': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '3': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '4': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '5': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '6': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '7': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '8': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '9': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  '10': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  'Valete': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  'Dama': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False},
                  'Rei': {'ouros': False, 'paus': False, 'espadas': False, 'copas': False}}

pont = 0
pont_dealer = 0

while pont < 17:
    carta_naipe = input().split(' ')
    carta = carta_naipe[0]
    naipe = carta_naipe[-1]
    if carta not in cartas or naipe not in naipes:
        print(f'A carta {carta} {carta_naipe[1]} {naipe} não existe, não me enganarão!')
    elif cartas_jogadas[carta][naipe]:
        print('EIEIEI, QUE ROUBO É ESSE!!!')
    else:
        cartas_jogadas[carta][naipe] = True
        for tupla in cartas_valores:
            if carta == tupla[0]:
                pont += tupla[1]
print(f'Minha rodada acaba por aqui com {pont} pontos.')
while pont_dealer < 17 and pont <= 21:
    carta_naipe = input().split(' ')
    carta = carta_naipe[0]
    naipe = carta_naipe[-1]
    if carta not in cartas or naipe not in naipes:
        print(f'A carta {carta} {carta_naipe[1]} {naipe} não existe, não me enganarão!')
    elif cartas_jogadas[carta][naipe]:
        print('EIEIEI, QUE ROUBO É ESSE!!!')
    else:
        cartas_jogadas[carta][naipe] = True
        for tupla in cartas_valores:
            if carta == tupla[0]:
                pont_dealer += tupla[1]
if pont_dealer > 0:
    print(f'A rodada da casa acaba por aqui com {pont_dealer} pontos.')

if pont == 21 or pont_dealer == 21:
    print('Blackjack!')
if pont > 21:
    print('Ah não, passei do ponto!')
elif pont_dealer > 21:
    print('AEEEEEEE, ele passou de 21, poder ir pagando chefa!!')
elif pont == pont_dealer:
    print('A próxima eu levo.')
elif pont > pont_dealer:
    print('O dinheiro é meu!')
elif pont < pont_dealer:
    print('Perdi tudo, F.')
