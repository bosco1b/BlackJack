import random


def inicio():
    print("BEM VINDO AO JOGO!")
    input("PRESS ANY KEY TO START")

    global jogador, dealer, baralho
    jogador = []
    dealer = []
    baralho = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"] * 4
    random.shuffle(baralho)
    primeiraDistribuição()
    print("Sua primeira carta foi {}, e a do dealer foi {}".format(jogador[0], dealer[0]))
    print("Sua segunda carta foi {}!".format(jogador[1]))


def primeiraDistribuição():
    for _ in range(2):
        jogador.append(baralho.pop())
        dealer.append(baralho.pop())



def resultado():
    Y = 0
    while Y < len(jogador):
        x = jogador[Y]
        Y += 1

    for x in jogador:
        if ("J") in jogador:
            pos = jogador.index("J")
            jogador.pop(pos)
            jogador.insert(pos, 10)
        elif ("Q") in jogador:
            pos = jogador.index("Q")
            jogador.pop(pos)
            jogador.insert(pos, 10)
        elif ("K") in jogador:
            pos = jogador.index("K")
            jogador.pop(pos)
            jogador.insert(pos, 10)

        if ("A") in jogador:
            pos = jogador.index("A")
            jogador.pop(pos)
            global onze
            onze = int(input("Escolha o valor do AS (1 ou 11)"))
            if onze == 1:
                jogador.insert(pos, 1)
            else:
                jogador.insert(pos, 11)

def nova_compra():
    while sum(jogador) < 21:

        compra = (input('Deseja comprar mais uma carta?(SIM/NÃO)'))
        if compra.upper() == 'SIM' :

            jogador.append(baralho.pop())
            print("A carta foi {}".format(jogador[-1]))
            resultado()
        else:
            print("Você parou com {} pontos!".format(sum(jogador)))
            break





      





inicio()
resultado()
nova_compra()
print(jogador)


if sum(jogador) > 21:
    print("OPS!SUA SOMA DEU {} E VOCÊ ESTOUROU!".format(sum(jogador)))



