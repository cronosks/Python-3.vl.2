
#==================================================
#                Menu de Opções
#==================================================

from time import sleep

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior número")
    print("[4] Novos números")
    print("[5] Sair do programa")
    print("====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        resultado = numero1 + numero2
        print("\nA soma é:", resultado)

    elif opcao == "2":

        resultado = numero1 * numero2
        print("\nA multiplicação é:", resultado)

    elif opcao == "3":

        if numero1 > numero2:
            print("\nO maior número é:", numero1)

        elif numero2 > numero1:
            print("\nO maior número é:", numero2)

        else:
            print("\nOs dois números são iguais!")

    elif opcao == "4":

        numero1 = int(input("\nDigite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

    elif opcao == "5":

        print("\nEncerrando o programa...")
        sleep(1)
        break

    else:
        print("\nOpção inválida! Tente novamente.")

    sleep(1)

print("\n========== PROGRAMA ENCERRADO ==========")
