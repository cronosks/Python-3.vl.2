#==================================================
#              Analisador Completo
#==================================================

soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
mulheres_menores = 0

for pessoa in range(1, 5):

    print("\n========== PESSOA {} ==========".format(pessoa))

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [M/F]: ").strip().upper()

    soma_idades += idade

    # Identifica o homem mais velho
    if sexo == "M":
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    # Conta mulheres com menos de 20 anos
    elif sexo == "F":
        if idade < 20:
            mulheres_menores += 1

    else:
        print("Sexo inválido!")

media = soma_idades / 4

print("\n========== RESULTADO ==========")

print("Média de idade do grupo: {:.1f} anos".format(media))

if nome_homem_mais_velho != "":
    print("Homem mais velho: {}".format(nome_homem_mais_velho))
    print("Idade: {} anos".format(maior_idade_homem))
else:
    print("Nenhum homem foi cadastrado.")

print("Mulheres com menos de 20 anos: {}".format(mulheres_menores))

print("================================")
