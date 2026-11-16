
#==================================================
#          Vários Números com Flag
#==================================================

soma = 0
quantidade = 0

print("Digite 999 para encerrar.")

while True:

    numero = int(input("Digite um número: "))

    if numero == 999:
        break

    soma += numero
    quantidade += 1

print("\n========== RESULTADO ==========")
print("Quantidade de números:", quantidade)
print("Soma dos valores:", soma)
print("Programa encerrado!")
