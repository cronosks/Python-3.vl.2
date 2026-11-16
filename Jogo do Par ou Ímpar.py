
#==================================================
#              Jogo do Par ou Ímpar
#==================================================

from random import randint

vitorias = 0

print("========== PAR OU ÍMPAR ==========")

while True:

    jogador = int(input("\nDigite um número: "))

    computador = randint(0, 10)

    escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()

    while escolha not in ("P", "I"):
        escolha = input("Escolha inválida! Digite P ou I: ").strip().upper()

    resultado = jogador + computador

    print("\nVocê jogou:", jogador)
    print("Computador jogou:", computador)
    print("Total:", resultado)

    if resultado % 2 == 0:
        vencedor = "P"
        print("Resultado: PAR!")
    else:
        vencedor = "I"
        print("Resultado: ÍMPAR!")

    if escolha == vencedor:
        vitorias += 1
        print("Você venceu! 🎉")
        print("Vitórias consecutivas:", vitorias)
    else:
        print("Você perdeu! 😢")
        break

print("\n========== FIM DE JOGO ==========")
print("Total de vitórias consecutivas:", vitorias)
