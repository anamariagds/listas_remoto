def conta_digitos(n):
    quantidade =0
    #a quantidade de vezes que repetir vai ser a qntdd de digitos
    while n> 0:
        quantidade +=1
        n //=10
    return quantidade

def main():
    n = int(input("Número inteiro positivo: "))
    q = conta_digitos(n)

    print(f"{n} tem {q} dígitos")

if __name__=='__main__':
    main()