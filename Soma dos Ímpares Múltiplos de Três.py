#==================================================
#        Soma dos Ímpares Múltiplos de Três
#==================================================

from time import sleep

fim = "========🚀 Fim da contagem!========"

while True:

    multiplo = int(input("digite um numero para a soma dos multiplos de tres: "))
    soma = 0
    cont = 0

    sleep(1)

    print ()

    if multiplo < 1:
        print ("Digite um número valido, sem ser negativo.")
        sleep(1.2)
        print ()
        continue

    for numero in range(multiplo, multiplo + 51):
        if numero % 3 == 0 and numero % 2 != 0:
            soma += numero
            cont += 1

    sleep (1.2)

    print("A soma dos múltiplos de 3 entre seu numero({}) com mais 50 casas a frente é: {} , numero de casas divisiveis por 3 é {} .". format(multiplo, soma, cont))

    sleep (1.2)

    print ()
    print (fim)
    print ()

    sleep(1.2)