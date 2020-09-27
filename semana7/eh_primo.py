def eh_primo(n):
    inicio = 1
    divisor = 0
    
    while inicio<= n:
        if n % inicio == 0:
            divisor +=1
        inicio +=1
    return divisor
        
def main():
    n =int(input("Digite um número: "))
    d = eh_primo(n)

    if d ==2:
        print(f'O número {n} é Primo')
    else:
        print(f'O número {n} não é primo')
        
if __name__ == '__main__':
    main()


    