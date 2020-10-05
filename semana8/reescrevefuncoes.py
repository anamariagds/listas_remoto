#informa comprimento da lista
def comprimento(lista):
    print(lista)
    c = 0    
    for i in lista:
        c +=1
    return c

#inverte função 
def inverte(lista):
    print("O inverso da lista: ")    
    print(lista[::-1])

#imprime o menor da lista
def menor(l2):
    p =0
    mnr =l2[p]

    for val in l2:
        if mnr > val:
            mnr = int(val)
    print(f'O menor número da lista é {mnr}')    
#imprime o maior da lista
def maior(l2):
    p =0
    mx =l2[p]

    for val in l2:
        if mx < val:
            mx = int(val)
    print(f'O maior número da lista é {mx}') 
#soma os elementos da lista   
def soma(l2):
    sm = 0
    for num in l2:
        sm+= num
    print(f'A soma dos elementos da lista é {sm}')

def main():
    lista =[]
    while True:
        n = int(input("Números da lista: "))
        lista.append(n)
        if n == 0:
            lista.pop()
            break
    
    c = comprimento(lista)
    print(f'O comprimento da lista é {c}')
    inverte(lista)
    menor(lista)
    maior(lista)
    soma(lista)

if __name__=='__main__':
    main()
