
#==================================================
#       Super Progressão Aritmética v3.0
#==================================================

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro
contador = 1
total = 0

while True:
    quantidade = int(input("\nQuantos termos deseja mostrar? (0 para parar): "))

    if quantidade == 0:
        break

    total += quantidade

    while contador <= total:
        print(termo, end=" → ")
        termo += razao
        contador += 1

    print()

print("\nTotal de termos apresentados:", total)
print("Fim da progressão!")
