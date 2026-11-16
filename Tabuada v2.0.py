#==================================================
#                  Tabuada v2.0
#==================================================

from time import sleep

fim = "========🚀 Fim! ========"

while True:

    numero = int(input("Seu numero para a criação da Tabuada: "))

    sleep(1)

    print ()

    print("A sua TABUADA:")

    print()

    sleep(1)

    for n in range(1, 11):
        print("{} x {} = {}".format(numero, n, n*numero))

    sleep (1.2)

    print ()
    print (fim)
    print ()

    sleep(1.2)