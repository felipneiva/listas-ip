#variáveis

categoria = input('')
genero = input('')
filme = 'nada'
serie = 'nada'

#opções de filme

if categoria == 'Filme':
    if genero =='Acao':
        filme = 'Kill Bill Vol. I'
    elif genero == 'Terror':
        filme = 'It - A Coisa'
    elif genero == 'Drama':
        filme = 'Sempre ao Seu Lado'
    elif genero == 'Romance':
        filme = 'Me Chame Pelo Seu Nome'
    elif genero == 'Aventura':
        filme = 'Homem - Aranha: Sem Volta para Casa'
    elif genero == 'Animacao':
        filme = 'Encanto'
    elif genero == 'Comedia':
        filme = 'Nao Olhe Para Cima'
    elif genero == 'Fantasia':
        filme = 'Harry Potter e a Pedra Filosofal'
    elif genero == 'Suspense':
        filme = 'Corra!'
    elif genero == 'Policial':
        filme = 'Cidade de Deus'
    elif genero == 'Ficcao':
        filme = 'Interestelar'
    print(f'{filme} e o filme mais popular do genero {genero} no momento.')

#opções de série

elif categoria == 'Serie':
    if genero =='Acao':
        serie = 'The Boys'
    elif genero == 'Terror':
        serie = 'A Maldicao da Residencia Hill'
    elif genero == 'Drama':
        serie = 'Euphoria'
    elif genero == 'Romance':
        serie = 'Bridgerton'
    elif genero == 'Aventura':
        serie = 'The Witcher'
    elif genero == 'Animacao':
        serie = 'Arcane'
    elif genero == 'Comedia':
        serie = 'FRIENDS'
    elif genero == 'Fantasia':
        serie = 'Game Of Thrones'
    elif genero == 'Suspense':
        serie = 'Prison Break'
    elif genero == 'Policial':
        serie = 'Peaky Blinders'
    elif genero == 'Ficcao':
        serie = 'Dark'
    print(f'{serie} e a serie mais popular do genero {genero} no momento.')
