def sua_idade(atual, nasc):
    return atual - nasc


def main():
    dia1 = int(input("Dia atual: ")) 
    mes1 = int(input("Mês atual: "))
    ano1 = int(input("Ano atual: "))

    dia2 = int(input("Dia do seu nascimento: "))
    mes2 = int(input("Mês de seu nascimento: "))
    ano2 = int(input("Ano em que nasceu: "))

    idade = sua_idade(ano1, ano2)

    print(f'Hoje {dia1}/{mes1}/{ano1} é seu {idade} aniversario, parabéns!')

if __name__=='__main__':
    main()