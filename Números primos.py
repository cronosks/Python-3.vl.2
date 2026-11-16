#==================================================
#            Números primos
#==================================================

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("Esse número não é primo.")
else:
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print("Esse número é primo!")
    else:
        print("Esse número não é primo.")
