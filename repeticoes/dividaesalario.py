def divida(sal, dvd):
    mes = 10
    ano = 2016

    while sal > dvd:
        mes +=1
        dvd = dvd * 1.15

        if mes ==12:
            mes = 1
            ano +=1
            dvd *=1.15
        if mes == 3:
            sal = sal*1.05
    print(f'{mes}/{ano}')


def main():
    sal = float(input("Informe o salário de Pedro: "))
    dvd = float(input("Informe a divida no cartão: "))

    divida(sal, dvd)

if __name__=='__main__':
    main()

    
