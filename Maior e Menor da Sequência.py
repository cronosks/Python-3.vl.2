#==================================================
#           Maior e Menor da Sequência
#==================================================

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input("Digite o peso da pessoa {} (kg): ".format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print("\n========== RESULTADO ==========")
print("Maior peso: {} kg".format(maior))
print("Menor peso: {} kg".format(menor))
print("===============================")
