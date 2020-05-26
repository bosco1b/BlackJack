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


def resultadoJogador():
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

        elif ("A") in jogador:
            pos = jogador.index("A")
            jogador.pop(pos)

            onze = int(input("Escolha o valor do AS (1 ou 11)"))
            if onze == 1:
                jogador.insert(pos, 1)
            elif onze == 11:
                jogador.insert(pos, 11)


def resultadoDealer():
    Y = 0
    while Y < len(dealer):
        x = dealer[Y]
        Y += 1

    for x in dealer:
        if ("J") in dealer:
            pos = dealer.index("J")
            dealer.pop(pos)
            dealer.insert(pos, 10)
        elif ("Q") in dealer:
            pos = dealer.index("Q")
            dealer.pop(pos)
            dealer.insert(pos, 10)
        elif ("K") in dealer:
            pos = dealer.index("K")
            dealer.pop(pos)
            dealer.insert(pos, 10)

        if ("A") in dealer:
            pos = dealer.index("A")
            dealer.pop(pos)
            global onze

            if sum(dealer) < 11:
                jogador.insert(pos, 1)
            else:
                jogador.insert(pos, 11)


def nova_compra():
    while sum(jogador) < 21:

        compra = (input('Deseja comprar mais uma carta?(SIM/NÃO)'))
        if compra.upper() == 'SIM':

            jogador.append(baralho.pop())
            print("A carta foi {}".format(jogador[-1]))
            resultadoJogador()
            print("teste")
        else:
            print("Você parou com {} pontos!".format(sum(jogador)))
            break


def IADealer():
    while sum(dealer) < 16:
        dealer.append(baralho.pop())
        resultadoDealer()


inicio()
resultadoJogador()
nova_compra()
resultadoDealer()
IADealer()
print(jogador)
print(dealer)

if sum(jogador) > 21:
    print("OPS!SUA SOMA DEU {} E VOCÊ ESTOUROU!".format(sum(jogador)))
elif 21 > sum(jogador) > sum(dealer):
    print("Você venceu com {} pontos!".format(sum(jogador)))
elif sum(jogador) == sum(dealer):
    print("Empate! Você empatou com o dealer, ambos com {}".format(sum(dealer)))
elif 21 > sum(dealer) > sum(jogador):
    print("Vitoria do dealer com {} pontos! Você fez apenas {}".format(sum(dealer), sum(jogador)))
elif sum(dealer) > 21:
    print("O dealer estourou e você venceu!")

