pokebolas = int(input())
pocoes = int(input())
revives = int(input())


def mdc(x, y):
    if x > y:
        r = x % y
        if r > 0:
            x = y
            y = r
            return mdc(x, y)
        else:
            return y
    elif x < y:
        x, y = y, x
        return mdc(x, y)
    elif x == y:
        return x


if mdc(mdc(pokebolas, pocoes), revives) > 1:
    print(f'Gracas a Companhia Pokemon, {mdc(mdc(pokebolas, pocoes), revives)} treinadores pokemon vao receber itens do Professor!')
elif mdc(mdc(pokebolas, pocoes), revives) == 1:
    print('Infelizmente apenas 1 treinador pokemon ira receber os itens hoje, e com certeza nao e o atrasado do Ash.')
