
#==================================================
#             Estatísticas em Produtos
#==================================================

total = 0
produtos_caros = 0
menor_preco = 0
produto_barato = ""
quantidade = 0

while True:

    print("\n========== CADASTRO DE PRODUTO ==========")

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))

    total += preco
    quantidade += 1

    if preco > 1000:
        produtos_caros += 1

    if quantidade == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    continuar = input("\nDeseja cadastrar outro produto? [S/N]: ").strip().upper()

    while continuar not in ("S", "N"):
        continuar = input("Opção inválida! Digite S ou N: ").strip().upper()

    if continuar == "N":
        break

print("\n========== ESTATÍSTICAS ==========")
print("Total gasto: R$ {:.2f}".format(total))
print("Produtos acima de R$ 1.000: {}".format(produtos_caros))
print("Produto mais barato: {}".format(produto_barato))
print("Preço do produto mais barato: R$ {:.2f}".format(menor_preco))
print("Quantidade de produtos: {}".format(quantidade))
