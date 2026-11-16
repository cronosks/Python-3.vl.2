#==================================================
#             Grupo da Maioridade
#==================================================

from datetime import datetime

ano_atual = datetime.now().year

maiores = 0
menores = 0

for pessoa in range(1, 8):

    nascimento = int(input("Digite o ano de nascimento da pessoa {}: ".format(pessoa)))

    idade = ano_atual - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print("\n========== RESULTADO ==========")

print("Pessoas maiores de idade:", maiores)
print("Pessoas menores de idade:", menores)

print("===============================")
