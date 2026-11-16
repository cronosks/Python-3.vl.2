#==================================================
#              Progressão Aritmética
#==================================================

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

print("\nOs 10 primeiros termos da PA:")

for i in range(10):
    termo = primeiro + (i * razao)
    print(termo, end=" → ")

print("FIM")