
#==================================================
#          Simulador de Caixa Eletrônico
#==================================================

from time import sleep

print("========== BANCO PYTHON ==========")

valor = int(input("Qual valor deseja sacar? R$ "))

while valor <= 0:
    print("Valor inválido! Digite um valor positivo.")
    valor = int(input("Qual valor deseja sacar? R$ "))

total = valor

cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

while total >= 50:
    total -= 50
    cedulas_50 += 1

while total >= 20:
    total -= 20
    cedulas_20 += 1

while total >= 10:
    total -= 10
    cedulas_10 += 1

while total >= 1:
    total -= 1
    cedulas_1 += 1

print("\nProcessando saque...")
sleep(1.5)

print("\n========== CÉDULAS ENTREGUES ==========")

if cedulas_50 > 0:
    print("{} cédula(s) de R$ 50,00".format(cedulas_50))

if cedulas_20 > 0:
    print("{} cédula(s) de R$ 20,00".format(cedulas_20))

if cedulas_10 > 0:
    print("{} cédula(s) de R$ 10,00".format(cedulas_10))

if cedulas_1 > 0:
    print("{} cédula(s) de R$ 1,00".format(cedulas_1))

print("\nValor total sacado: R$ {:.2f}".format(valor))
print("=======================================")
print("Obrigado por utilizar o Banco Python!")
