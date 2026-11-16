
#==================================================
#          Tratando Vários Valores v1.0
#==================================================

soma = 0
quantidade = 0
continuar = "S"

while continuar == "S":

    numero = int(input("Digite um número inteiro: "))

    soma += numero
    quantidade += 1

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()

media = soma / quantidade

print("\n========== RESULTADO ==========")
print("Quantidade de números:", quantidade)
print("Soma dos valores:", soma)
print("Média dos valores: {:.2f}".format(media))
