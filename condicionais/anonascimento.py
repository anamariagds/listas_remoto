def sua_idade(atual, nasc, mes_today, mes_born, today, born):
    bth = atual - nasc
    #se o mes atual é maior do seu aniversario
    if  mes_today < mes_born:
        bth = bth -1
    elif mes_today == mes_born:
        if today < born:
            bth = bth -1
    return bth


def main():
    dia1 = int(input("Dia atual: ")) 
    mes1 = int(input("Mês atual: "))
    ano1 = int(input("Ano atual: "))

    dia2 = int(input("Dia do seu nascimento: "))
    mes2 = int(input("Mês de seu nascimento: "))
    ano2 = int(input("Ano em que nasceu: "))

    idade = sua_idade(ano1, ano2, mes1, mes2, dia1, dia2)
    
    if dia1 == dia2:
        print(f'Hoje {dia1}/{mes1}/{ano1} é seu {idade} aniversario, parabéns!')
    elif dia1 < dia2:
        print(f'Ainda não é seu aniversario')
    elif dia1 > dia2:
        print(f'Seu aniversário já passou!')


if __name__=='__main__':
    main()