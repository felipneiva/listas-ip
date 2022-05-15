# variáveis

vida_lucas = 100
vida_severino = 100
acao_bug1 = ''
acao_bug2 = ''

# comando for

for i in range(0, 12):

    # ações realizadas

    acao_1 = input('')
    acao_2 = input('')

    # rodadas normais

    if not (i == 3 or i == 6 or i == 9):
        if acao_1 == 'Golpe Rapido' and acao_2 == 'Golpe Rapido':
            vida_lucas -= 12
            vida_severino -= 12
        elif acao_1 == 'Golpe Rapido' and acao_2 == 'Bloqueio':
            vida_severino -= 6
        elif acao_1 == 'Golpe Rapido' and acao_2 == 'Esquivar':
            vida_severino -= 12
        elif acao_1 == 'Golpe Rapido' and acao_2 == 'Golpe Forte':
            vida_lucas -= 25
            vida_severino -= 12
        elif acao_1 == 'Golpe Forte' and acao_2 == 'Bloqueio':
            vida_severino -= 20
        elif acao_1 == 'Golpe Forte' and acao_2 == 'Esquivar':
            vida_lucas -= 20
        elif acao_2 == 'Golpe Rapido' and acao_1 == 'Bloqueio':
            vida_lucas -= 6
        elif acao_2 == 'Golpe Rapido' and acao_1 == 'Esquivar':
            vida_lucas -= 12
        elif acao_2 == 'Golpe Rapido' and acao_1 == 'Golpe Forte':
            vida_severino -= 25
            vida_lucas -= 12
        elif acao_2 == 'Golpe Forte' and acao_1 == 'Bloqueio':
            vida_lucas -= 20
        elif acao_2 == 'Golpe Forte' and acao_1 == 'Esquivar':
            vida_severino -= 20

    # rodada 4

    if i == 3:
        vida_lucas, vida_severino = vida_severino, vida_lucas

    # armazenar usos da rodada 6

    if i == 5:
        acao_bug1 = acao_1
        acao_bug2 = acao_2

    # rodada 7

    if i == 6:
        if acao_bug1 == 'Golpe Rapido' and acao_bug2 == 'Golpe Rapido':
            vida_lucas -= 12
            vida_lucas -= 6
            vida_lucas -= 3
            vida_severino -= 12
            vida_severino -= 6
            vida_severino -= 3
        elif acao_bug1 == 'Golpe Rapido' and acao_bug2 == 'Bloqueio':
            vida_severino -= 6
            vida_severino -= 3
            vida_severino -= 1.5
        elif acao_bug1 == 'Golpe Rapido' and acao_bug2 == 'Esquivar':
            vida_severino -= 12
            vida_severino -= 6
            vida_severino -= 3
        elif acao_bug1 == 'Golpe Rapido' and acao_bug2 == 'Golpe Forte':
            vida_lucas -= 25
            vida_lucas -= 12.5
            vida_lucas -= 6.25
            vida_severino -= 12
            vida_severino -= 6
            vida_severino -= 3
        elif acao_bug1 == 'Golpe Forte' and acao_bug2 == 'Bloqueio':
            vida_severino -= 20
            vida_severino -= 10
            vida_severino -= 5
        elif acao_bug1 == 'Golpe Forte' and acao_bug2 == 'Esquivar':
            vida_lucas -= 20
            vida_lucas -= 10
            vida_lucas -= 5
        elif acao_bug2 == 'Golpe Rapido' and acao_bug1 == 'Bloqueio':
            vida_lucas -= 6
            vida_lucas -= 3
            vida_lucas -= 1.5
        elif acao_bug2 == 'Golpe Rapido' and acao_bug1 == 'Esquivar':
            vida_lucas -= 12
            vida_lucas -= 6
            vida_lucas -= 3
        elif acao_bug2 == 'Golpe Rapido' and acao_bug1 == 'Golpe Forte':
            vida_severino -= 25
            vida_severino -= 12.5
            vida_severino -= 6.25
            vida_lucas -= 12
            vida_lucas -= 6
            vida_lucas -= 3
        elif acao_bug2 == 'Golpe Forte' and acao_bug1 == 'Bloqueio':
            vida_lucas -= 20
            vida_lucas -= 10
            vida_lucas -= 5
        elif acao_bug2 == 'Golpe Forte' and acao_bug1 == 'Esquivar':
            vida_severino -= 20
            vida_severino -= 10
            vida_severino -= 5

    # rodada 10

    if i == 9:
        if vida_lucas > vida_severino:
            vida_severino = vida_lucas
        elif vida_severino > vida_lucas:
            vida_lucas = vida_severino

    # luta acaba antes das 12 rodadas

    if vida_severino <= 0 < vida_lucas:
        print('Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!')
        break
    elif vida_lucas <= 0 < vida_severino:
        print('Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!')
        break
    elif vida_severino <= 0 and vida_lucas <= 0:
        print('Pela primeira vez na historia, ha um empate e ambos irao levar para casa o grande premio do BBCIn do 2021.2!!')
        break

# luta acaba após 12 rodadas

if vida_lucas > 0 and vida_severino > 0:
    if vida_lucas > vida_severino:
        print('Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!')
    elif vida_severino > vida_lucas:
        print('Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!')
    elif vida_lucas == vida_severino:
        print('Pela primeira vez na historia, ha um empate e ambos irao levar para casa o grande premio do BBCIn do 2021.2!!')
