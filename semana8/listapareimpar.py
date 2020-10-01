def par_impar(n):
    numero = []
    par = []
    impar = []
    for i in range(n):
        numero.append(int(input("Digite um número: ")))
    for v in numero:
        if v %2 ==0:
            par.append(v)
        else:
            impar.append(v)
    print(numero)
    print(par)
    print(impar)


def main():
    par_impar(20)

if __name__=='__main__':
    main()