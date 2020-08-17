def meianoite(h, m, s):
    return (h*3600)+(m*60)+s

def main():
    hora= int(input("Quantas horas: "))
    minuto = int(input("Minutos: "))
    segundos = int(input("e os segundos: "))

    desde_meia_noite = meianoite(hora,minuto,segundos)

    print("Desde a ultima meia noite se passaram ",desde_meia_noite," segundos")

if __name__=='__main__':
    main()