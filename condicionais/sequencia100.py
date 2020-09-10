def par_ou_impar(n):
    pares = 0
    impares = 0
    for i in range(n):
        alg = int(input("Digite um número: "))
        if alg%2 ==0:
            pares += 1
        else:
            impares +=1
    return pares, impares
            

    

def main():
    pares, impares = par_ou_impar(100)
    print(f'Você digitou {pares} números pares')
    print(f'e {impares} impares')

if __name__=='__main__':
    main()