hora= int(input("Quantas horas: "))
minuto = int(input("Minutos: "))
segundos = int(input("e os segundos: "))

desde_meia_noite = (hora*3600)+(minuto*60)+segundos

print("Desde a ultima meia noite se passaram ",desde_meia_noite," segundos")