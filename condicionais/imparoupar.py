def par(n):
    return not (n % 2 == 0)

def main():
    num = int(input("Digite um número: "))

    eleeh = par(num)

    print(f'Esse número é {eleeh}')

if __name__=='__main__':
    main()