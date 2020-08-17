def data(dia, mes, ano):
    print(f'{dia}/{mes}/{ano}')

def main():
    dia = int(input("Digite um dia: "))
    mes = int(input("O mês: "))
    ano = int(input("e o ano: "))
     
    dt = data(dia, mes, ano)

if __name__=='__main__':
    main()