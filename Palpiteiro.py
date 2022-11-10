#Este é um palpiteiro para jogos da Mega Sena
#Diga quantos jogos você deseja e o programa sorteará 6 números para cada jogo
import random
palpites = list()
jogo = list()
while True:
    try:
        usuario = int(input('Quantos palpites você quer obter?'))
        break
    except ValueError:
        print("ERRO.\nDigite um número válido!")
for c in range(0,usuario):
    while len(jogo) < 6:
        sorteio = random.randint(1,60)
        if sorteio not in jogo:
            jogo.append(sorteio)
            jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
for d in palpites:
    print(d)
