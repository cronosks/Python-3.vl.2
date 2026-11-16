
#==================================================
#           Análise de Dados do Grupo
#==================================================

maiores = 0
homens = 0
mulheres_jovens = 0

while True:

    print("\n========== NOVO CADASTRO ==========")

    idade = int(input("Digite a idade: "))

    sexo = input("Digite o sexo [M/F]: ").strip().upper()

    while sexo not in ("M", "F"):
        sexo = input("Sexo inválido! Digite M ou F: ").strip().upper()

    if idade > 18:
        maiores += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade < 20:
        mulheres_jovens += 1

    continuar = input("\nDeseja cadastrar outra pessoa? [S/N]: ").strip().upper()

    while continuar not in ("S", "N"):
        continuar = input("Opção inválida! Digite S ou N: ").strip().upper()

    if continuar == "N":
        break

print("\n========== RESULTADO ==========")
print("Pessoas maiores de 18 anos:", maiores)
print("Homens cadastrados:", homens)
print("Mulheres com menos de 20 anos:", mulheres_jovens)
