#Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50
#elementos, cujos elementos sejam a intercalação dos elementos de A e B
def listaAB(n):
    A =[]
    B =[]
    c=[]
    

    for i in range(n):
        A.append(int(input()))
    for i in range(n):
        B.append(int(input()))
    
    for i in range(n):
            c.append(A[i])
            c.append(B[i])
    print(A)
    print(B)
    print(c)

def main():
    listaAB(25)
   
if __name__ == '__main__':
    main()