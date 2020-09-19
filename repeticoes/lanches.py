def lanche():
    conta = 0
    while True:
        codigo = input('Código: ').upper()[0]
        if codigo == 'H':
            conta += 5.50
        elif codigo == 'C':
            conta +=6.80
        elif codigo == 'M':
            conta+= 4.50
        elif codigo == 'A':
            conta +=7.00
        elif codigo == 'Q':
            conta += 4.00
        elif codigo != 'H' and codigo != 'C' and codigo != 'M' and codigo != 'A' and codigo != 'Q' and codigo != 'X':
            print("Opção inválida.")
        if codigo == 'X':
            print(f'{conta:.2f}')
            break


def main():
    print('''
CÓDIGO  PRODUTO          PREÇO (R$)
H       Hamburger        5.50
C       Cheeseburger     6.80
M       Misto Quente     4.50
A       Americano        7.00
Q       Queijo Prato     4.00
X       PARA TOTAL DA CONTA
''', end='')
    lanche()


if __name__=='__main__':
    main()
