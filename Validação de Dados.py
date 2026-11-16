# ==================================================
#              Validação de Dados
# ==================================================

sexo = ""

while sexo != "M" and sexo != "F":

    sexo = input("Digite seu sexo [M/F]: ").strip().upper()

    if sexo != "M" and sexo != "F":
        print("Opção inválida! Digite apenas M ou F.")

print("\nCadastro realizado com sucesso!")
print("Sexo informado: {}".format(sexo))

print("========== FIM DO PROGRAMA ==========")
