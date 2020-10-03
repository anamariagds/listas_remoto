def comprimento(lista):
    c = 0    
    for i in lista:
        c +=1
    print(lista)    
    print(c)
def inverte(lista):
    c = 




def main():
    lista =[]
    while True:
        n = int(input("Digite números para a lista: "))
        lista.append(n)
        if n == 0:
            break
    
    comprimento(lista)

if __name__=='__main__':
    main()