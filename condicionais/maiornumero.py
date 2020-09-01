def comparando(a,b,c,d,e):
    if(a!=b and a!=c and a!=d and a!=e) and (b!=c and b!=d and b!=e) and (c!=d and c!=e) and (d!=e):
        if (a!= 0 and b!=0 and c!=0 and d!=0 and e!=0):
            if (a/b)>1 and (a/c)>1 and (a/d)>1 and (a/e)>1:
                return a
            elif (b/a)>1 and (b/c)>1 and (b/d)>1 and (b/e)>1:
                return b
            elif (c/a)>1 and (c/b)>1 and (c/d)>1 and (c/e)>1:
                return c
            elif (d/a)>1 and (d/b)>1 and (d/c)>1 and (c/e)>1:
                return d
            else:
                return e

def comparando_mnr(a,b,c,d,e):
    if(a!=b and a!=c and a!=d and a!=e) and (b!=c and b!=d and b!=e) and (c!=d and c!=e) and (d!=e):
        if (a!= 0 and b!=0 and c!=0 and d!=0 and e!=0):
            if not ((a/b)>1 and (a/c)>1 and (a/d)>1 and (a/e)>1):
                return a
            elif not ((b/a)>1 and (b/c)>1 and (b/d)>1 and (b/e)>1):
                return b
            elif not ((c/a)>1 and (c/b)>1 and (c/d)>1 and (c/e)>1):
                return c
            elif not ((d/a)>1 and (d/b)>1 and (d/c)>1 and (c/e)>1):
                return d
            else:
                return e
def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    d = int(input("Digite o quarto número: "))
    e = int(input("Digite o quinto número: ")) 

    maior = comparando(a,b,c,d,e)

    print(f'O maior número digitado foi: {maior}')

if __name__=='__main__':
    main()