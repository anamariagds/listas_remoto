def menor(a, b, c, d, e):
    return min(a, b, c, d, e)

def maior(a, b, c, d, e):
    return max(a, b, c, d, e)

def media_aritmetica(a, b, c, d, e):
    return (a+b+c+d+e)

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    mnr = menor(n1, n2, n3, n4, n5)
    mx = maior(n1, n2, n3, n4, n5)
    media = media_aritmetica(n1, n2, n3, n4, n5)

    print(f'{mnr} {mx} {media}')

if __name__== '__main__':
    main()