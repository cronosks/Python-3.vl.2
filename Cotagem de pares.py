#==================================================
#            Contagem de Pares
#==================================================

from time import sleep

fim = "========🚀 Fim da contagem!========"

while True:

    numero = int(input("Digite um número par que deseja iniciar: "))

    print()
    sleep (1.5)

    if numero % 2 != 0:
        print("Erro, o seu numero não é par é impar.")
        continue

    for par in range(numero, numero + 41, 2):
        print ("{}.". format(par), end=" ")
        sleep (0.7)

    print()
    print()
    sleep (0.2)

    print (fim)

    print()