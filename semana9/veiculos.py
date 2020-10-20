linhas = int(input("tamanho n: "))
colunas = int(input("Tamanho m: "))
matrix = []

for linn in range(linhas):
    linha = []
    nm = input("marca")
    linha.append(nm)
    for col in range(colunas):    
        x = int(input("valores: "))
        
        linha.append(x)
          
    matrix.append(linha)