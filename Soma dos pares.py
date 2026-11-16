#==================================================
#        Soma dos pares
#==================================================

from time import sleep

fim = "========🚀 Fim da contagem!========"

while True:

    conta = int(input("digite um numero para a soma dos pares: "))
    soma = 0

    sleep(1)

    print ()

    if conta < 1:
        print ("Digite um número valido, sem ser negativo.")
        sleep(1.2)
        print ()
        continue

    for numero in range(conta, conta + 51):
        if numero % 2 == 0 and numero % 3 != 0:
            soma += numero

    sleep (1.2)

    print("Soma dos pares {}, do numero {}, de 50 casas a frente.". format(soma, conta))

    sleep (1.2)

    print ()
    print (fim)
    print ()

    sleep(1.2)