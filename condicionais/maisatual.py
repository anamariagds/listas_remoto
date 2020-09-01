def recente(ano1, ano2, mes1, mes2, dia1, dia2):
    if (ano1 > ano2) or (ano1 == ano2 and mes1>mes2) or (ano1 == ano2 and mes1==mes2 and dia1>dia2):
        return f'{dia1}/{mes1}/{ano1}'
    elif (ano2 > ano1) or (ano1 == ano2 and mes2 > mes1) or  (ano1 == ano2 and mes2==mes1 and dia2>dia1):
        return f'{dia2}/{mes2}/{ano2}'
    elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
        return f'{dia2}/{mes2}/{ano2}
def main():
    dia1= int(input("Diga o dia: "))
    mes1 = int(input("Diga o mês: "))
    ano1 = int(input("Diga o ano: "))

    dia2= int(input("Diga o dia: "))
    mes2 = int(input("Diga o mês: "))
    ano2 = int(input("Diga o ano: "))

    atual = recente(ano1, ano2, mes1, mes2, dia1, dia2)

    print(atual)

if __name__ == '__main__':
    main()

