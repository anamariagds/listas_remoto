def maior(a, b, c, d, e):
    return max(a, b, c, d, e)

def menor(a, b, c, d, e):
    return min(a, b, c, d, e)

def media_aritmetica(a, b, c, d, e):
    return (a+b+c+d+e)/5

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))
    n5 = int(input("Digite o quinto número: "))

    mx = maior(n1, n2, n3, n4, n5)
    mnr = menor(n1, n2, n3, n4, n5)
    media = media_aritmetica(n1, n2, n3, n4, n5)

    print(f'O maior número digitado é {mx} e o menor é {mnr}. A média aritmética dos número é {media}')

if __name__== '__main__':
    main()