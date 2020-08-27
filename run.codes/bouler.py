def pertence(n):
    if n in "0 1 2 3 4 5 6 7 8 9":
        return True
    else:
        return False

def main():
    numero = str(input())

    vf = pertence(numero)

    print(vf)

if __name__=='__main__':
    main()