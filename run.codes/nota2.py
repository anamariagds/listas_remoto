def media(n1,n2,n3):
    if n3 > 8:
        med = ((n1+n2+n3)/3) + 1
    else:
        med = (n1+n2+n3)/3
    
    if med > 10:
        return 10
    return med


def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    nota = media(n1, n2, n3)

    print(f'{nota:.2f}')

if __name__=='__main__':
    main()
