def diz_codigo(a):
    a = ord(a)
    print(f'O código desse caracter é {a}')

def main():
    n = str(input("Digite apenas um caracter: "))
    diz_codigo(n)

if __name__=='__main__':
    main()
