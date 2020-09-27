def fatorial():
    i = 0
    N = int(input("Digite um número: "))
    fat = N

    while True:
        if N ==0:
            fat = 1
            break
        else:
            i +=1
            fat *= i
            if i == (N-1):
                break
    print(fat)

def main():
    fatorial()

if __name__=='__main__':
    main()