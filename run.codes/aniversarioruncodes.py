def sua_idade(atual, nasc):
    return  atual - nasc
    


def main():
    dia1 = int(input()) 
    mes1 = str(input())
    ano1 = int(input())

    dia2 = int(input())
    mes2 = str(input())
    ano2 = int(input())

    idade = sua_idade(ano1, ano2)

    print(idade)

if __name__=='__main__':
    main()