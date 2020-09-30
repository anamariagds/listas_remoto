compras = []
while True:
    produto = input("Produto ('fim'para terninar): ")
    if produto.upper() == 'FIM':
        break
    compras.append(produto)

for p in compras:
    print(p)