
#==================================================
#             Maior e Menor Valores
#==================================================

quantidade = 0
maior = 0
menor = 0
continuar = "S"

while continuar == "S":

    numero = int(input("Digite um número: "))

    if quantidade == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    quantidade += 1

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()

print("\n========== RESULTADO ==========")
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade de números:", quantidade)
