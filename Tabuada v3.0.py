
#==================================================
#                 Tabuada v3.0
#==================================================

while True:

    numero = int(input("\nDigite um número para ver sua tabuada (negativo para sair): "))

    if numero < 0:
        break

    print("\n========== TABUADA ==========")

    for i in range(1, 11):
        print("{} x {:2} = {}".format(numero, i, numero * i))

    print("=============================")

print("\nPrograma encerrado!")
