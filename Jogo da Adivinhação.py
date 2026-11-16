#==================================================
#              Jogo da Adivinhação
#==================================================

from random import randint
from time import sleep

computador = randint(0, 10)
tentativas = 0

print("========== JOGO DA ADIVINHAÇÃO ==========")
print("Estou pensando em um número entre 0 e 10...")

sleep(1.5)

jogador = -1

while jogador != computador:

    jogador = int(input("\nQual é o seu palpite? "))

    tentativas += 1

    if jogador < computador:
        print("Mais alto! Tente novamente.")

    elif jogador > computador:
        print("Mais baixo! Tente novamente.")

    else:
        print("\n🎉 PARABÉNS! Você acertou!")

print("\n========== RESULTADO ==========")
print("Número escolhido pelo computador:", computador)
print("Quantidade de tentativas:", tentativas)
print("================================")
