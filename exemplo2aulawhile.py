#repetição com teste no início
def divisoes_por_2(n):
    quantidade = 0
    while n>0:
        n //=2
        quantidade +=1
    return quantidade

def main():
    n = int(input("Digite um número: "))
    qtd = divisoes_por_2(n)

    print("É possivel dividir {} por 2, {}vezes".format(n, qtd))

if __name__=='__main__':
    main()