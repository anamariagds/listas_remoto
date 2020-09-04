def seu_signo(dia, mes):
    if (mes == 3 and dia>=21) or (mes == 4 and dia <= 19):
        return f'Áries'
    elif (mes == 4 and dia>=20) or (mes == 5 and dia <= 20):
        return f'Touro'
    elif (mes == 5 and dia>=21) or (mes == 6 and dia <= 21):
        return f'Gêmios'
    elif (mes == 6 and dia>=22) or (mes == 7 and dia <= 22):
        return f'Câncer'
    elif (mes == 7 and dia>=23) or (mes == 8 and dia <= 22):
        return f'Leão'
    elif (mes == 8 and dia>=23) or (mes == 9 and dia <= 22):
        return f'Virgem'
    elif (mes == 9 and dia>=23) or (mes == 10 and dia <= 22):
        return f'Libra'
    elif (mes == 10 and dia>=23) or (mes == 11 and dia <= 21):
        return f'Escorpião'
    elif (mes == 11 and dia>=22) or (mes == 12 and dia <= 21):
        return f'Sargitário'
    elif (mes == 12 and dia>=22) or (mes == 1 and dia <= 19):
        return f'Capricornio'
    elif (mes == 1 and dia>=20) or (mes == 2 and dia <= 18):
        return f'Aquário'
    elif (mes == 2 and dia>=19) or (mes == 3 and dia <= 20):
        return f'Peixes'
def main():
    dia = int(input("Dia do seu nascimento: "))
    mes = int(input("Mês do seu nascimento: "))
    ano = int(input("Ano em que nasceu: "))

    signo = seu_signo(dia, mes)
    
    print(f'Você nasceu em {dia}/{mes}/{ano} seu signo é {signo}')


if __name__=='__main__':
    main()