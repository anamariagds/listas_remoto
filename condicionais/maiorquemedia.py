def media(n1, n2, n3, n4, n5):
    media_notas = (n1+n2+n3+n4+n5)/5

    return media_notas
    
def main():
    n1 = int(input("Primeira nota: "))
    n2 = int(input("Segunda nota: "))
    n3 = int(input("Terceira nota: "))
    n4 = int(input("Quarta nota: "))
    n5 = int(input("Quinta nota: "))
    
    md = media(n1, n2,n3,n4,n5)   

    if n1>md:
        print(n1)
    if n2>md:
        print(n2)
    if n3 > md:
        print(n3)
    if n4 > md:
        print(n4)
    if n5 > md:
        print(n5)
    
    print(f'{md:.2f}')
   
    

if __name__=='__main__':
    main()