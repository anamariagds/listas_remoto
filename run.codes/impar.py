def par(n):
    return not (n % 2 == 0)

def main():
    num = int(input())

    eleeh = par(num)

    print(eleeh)

if __name__=='__main__':
    main()