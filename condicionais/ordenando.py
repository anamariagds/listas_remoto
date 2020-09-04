def ordenar(a,b,c):
    if a<b<c:
        return f'{a}\n{b}\n{c}'
    elif b<c<a:
        return f'{b}\n{c}\n{a}'
    elif a<c<b:
        return f'{a}\n{c}\n{b}'
    elif b<a<c:
        return f'{b}\n{a}\n{c}'
    elif c<a<b:
        return f'{c}\n{a}\n{b}'
    elif c<b<a:
        return f'{c}\n{b}\n{a}'   


def main():
    a = int(input("Primeiro númeor: "))
    b = int(input("Segundo númeor: "))
    c = int(input("Terceiro númeor: "))

    crescente = ordenar(a,b,c)

    print(crescente)


if __name__=='__main__':
    main()