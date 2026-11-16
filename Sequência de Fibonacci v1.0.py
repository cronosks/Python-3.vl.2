
#==================================================
#          Sequência de Fibonacci v1.0
#==================================================

print("========== FIBONACCI ==========")

quantidade = int(input("Quantos termos deseja mostrar? "))

primeiro = 0
segundo = 1
contador = 0

while contador < quantidade:

    print(primeiro, end=" → ")

    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo

    contador += 1

print("FIM")
