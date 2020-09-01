def comparando(a,b,c,d,e):
    mx = a
    if b > mx:
        mx = b
        return mx
    elif c > mx:
        mx = c
        return mx
    elif d > mx:
        mx = d
        return d
    elif e > mx:
        mx = e
        return mx 
    else:
        return mx 

def comparando_mnr(a,b,c,d,e):
    mnr = a
    if b < mnr:
        mnr = b
        return b
    elif c < mnr:
        mnr = c
        return c
    elif d < mnr:
        mnr = d
        return d
    elif e < mnr:
        mnr = e
        return e
    else:
        return a

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input()) 

    maior = comparando(a,b,c,d,e)
    menor = comparando_mnr(a,b,c,d,e)

    print(maior)
    print(menor)

if __name__=='__main__':
    main()