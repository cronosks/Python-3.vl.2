
#==================================================
#                Calculadora de Fatorial
#==================================================

from time import sleep

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = numero

if numero < 0:

    print("Não existe fatorial de número negativo!")

else:

    print("\nCalculando...")
    sleep(1)

    while contador > 0:

        fatorial *= contador
        contador -= 1

    print("\nO fatorial de {} é: {}".format(numero, fatorial))

print("\n========== FIM DO PROGRAMA ==========")
