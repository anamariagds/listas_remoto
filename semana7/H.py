def somatorio():
    n = int(input("Digite o valor de n: "))
    i = 1
    H = 1

    while i <n:
        i+=1
        H += (1/i)
        if i ==n:
            break
    print(f'O valor de H é {H:.4f}')
def main():
    somatorio()

if __name__=='__main__':
    main()
