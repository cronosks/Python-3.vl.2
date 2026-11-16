#==================================================
#            Contagem regressiva
#==================================================
from time import sleep

fim = "🚀 Fim da contagem!"
Nome = int(input('Digite um numero para iniciar a contagem regressiva: '))

sleep(0.5)

print ("prepare-se...")

sleep(1.2)

for i in range(Nome, -1, -1):
    print (i)
    sleep (0.7)

print(fim)