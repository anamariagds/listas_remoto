def sua_sorte(num):
    n_sorte =0

    while num > 0:
        n_sorte +=(num%10)
        num = num//10
    
    print(n_sorte)

def main():
    num = int(input("Digite a data do seu nascimento no formato ddmmaaaa: "))

    sua_sorte(num)


if __name__=='__main__':
    main()
