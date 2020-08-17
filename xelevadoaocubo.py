def cubo(x):
    return x**3

def main():
    x = int(input("Digite um número: "))
    
    cb = cubo(x)
    print(x,"ao cubo é: ",cb)

if __name__=='__main__':
    main()
