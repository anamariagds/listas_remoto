def eh_primo(n):
    inicio = 1
    divisor = 0    
    while inicio<= n:
        if n % inicio == 0:
            divisor +=1
        inicio +=1
    if divisor ==2:
        return True
        
def no_intervalo():
    first = int(input("Digite o inicio: "))
    end =int(input("O último número: "))

    while first <= end:
        first +=1
        if eh_primo(first):
            print(first)

def main():
    no_intervalo()

if __name__ == '__main__':
    main()