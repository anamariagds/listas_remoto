def ler_nome(a):
    return len(a)

def main():
    x = str(input("Digite um nome: "))
    nome = ler_nome(x)
    
    print(f'O nome {x} tem {nome} caracteres')

if __name__=='__main__':
    main()

