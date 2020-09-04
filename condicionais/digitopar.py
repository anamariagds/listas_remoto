def alg_par(n):
    unid = n%10
    n = n//10
    dzn = n%10
    n = n//10
    ctn = n%10
    
    par = 0
    
    if unid%2 == 0:
        par +=1
    if dzn%2 ==0:
        par +=1
    if ctn%2 == 0:
        par +=1 
    return par
def main():
    n = int(input("Digite um número inteiro entre 100 e 999: "))
    
    if n>= 100 and n<=999:
        quant_pares = alg_par(n)
        print(f'O número {n} tem {quant_pares} algarismos pares.')  
    else:
        print(f'Informe um número válido!')

if __name__=='__main__':
    main()