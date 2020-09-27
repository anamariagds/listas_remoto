# -*- coding: utf-8 -*-
def posso_pagar():
    pp = 10000
    t = 0
    pc = float(input("Preço do carro: "))
    while pp<=pc:
        pp *=1.007
        pc *=1.004
        t +=1
        if pp >= pc:
            print(t)
            break


def main():
    qnd = posso_pagar()


if __name__=='__main__':
    main()