def impar(n):
    n1 = n%10
    n = n//10
    n2 = n%10
    
    impar = 0
    if n1%2 != 0:
        impar +=1
    if n2%2 !=0:
        impar +=1
    
    impar 

    if impar == 0:
        return f'Nenhum dígito é ímpar'
    elif impar == 1:
        return f'Apenas um dígito é ímpar'
    else:
        return f'Os dois dígitos são ímpares'
        
def main():
    num = int(input("Digite um número inteiro entre 10 e 99: "))

    if num >=10 and num<=99:
        qnts_impar = impar(num)
        print(qnts_impar)


if __name__=='__main__':
    main()