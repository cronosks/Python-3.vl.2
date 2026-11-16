#==================================================
#            Detector de Palíndromo
#==================================================

frase = input("Digite uma palavra ou frase: ")

# Remove os espaços e transforma em letras minúsculas
frase = frase.replace(" ", "").lower()

# Inverte a frase
inverso = frase[::-1]

print()

if frase == inverso:
    print("A frase é um PALÍNDROMO! 💚")
else:
    print("A frase NÃO é um palíndromo.")
