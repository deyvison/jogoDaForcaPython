def Entrada ():
    print('Bem Vindo ao jogo da forca!!')
    print('Objetivo do jogo: descobrir uma palavra adivinhando as letras que ela possui.')
    print('O jogo acaba quando você acerta a palavra ou suas possibilidades se esgotam!\n')


def ValidaJogada(letra,jogadas):
    if letra in jogadas:
        return True
    else:
        False

def TestaJogada(letra,listapalavra):
    if letra in listapalavra:
        return True
    elif letra not in listapalavra:
        return False

def TestaEntrada(letra):
    if len(letra)==1:
        return True
    else:
        return False


