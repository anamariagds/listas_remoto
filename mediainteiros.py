def media(a, b, c):
    return (a+b+c)/3

def main():
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite um número inteiro: "))
    c = int(input("Digite um número inteiro: "))

    med = media(a,b,c)
    print(f'A média entre{a}, {b}e{c} é {med:.2f}')
    
if __name__== '__main__':
    main()