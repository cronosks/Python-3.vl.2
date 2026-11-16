
#==================================================
#          Progressão Aritmética v2.0
#==================================================

from time import sleep

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro
contador = 1
total = 10

while contador <= total:
    print(termo, end=" → ")
    termo += razao
    contador += 1

    if contador > total:
        print("\n")
        continuar = int(input("Deseja mostrar mais termos? (0 para parar): "))

        if continuar == 0:
            break

        total += continuar

print("\nFim da progressão!")
