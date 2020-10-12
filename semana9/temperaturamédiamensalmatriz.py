def media_anual(temp):
    soma =0
    media = 0
    for t in temp:
        soma = soma + t
        media = soma/(len(temp))
    return round(media,2)
def tem_maior(temp, media):
    for t in range(len(temp)):
        if temp[t]> media:
            if t ==0 :
                print(f'Janeiro: {round(temp[t],2)}K')
            elif t ==1:
                print(f'Fevereiro: {round(temp[t],2)}K')
            elif t ==2:
                print(f'Março: {round(temp[t],2)}K')
            elif t ==3:
                print(f'Abril: {round(temp[t],2)}K')
            elif t ==4:
                print(f'Maio: {round(temp[t],2)}K')
            elif t ==5:
                print(f'Junho: {round(temp[t],2)}K')
            elif t ==6:
                print(f'Julho: {round(temp[t],2)}K')
            elif t ==7:
                print(f'Agosto: {round(temp[t],2)}K')
            elif t ==8:
                print(f'Setembro: {round(temp[t],2)}K')
            elif t ==9:
                print(f'Outubro: {round(temp[t],2)}K')
            elif t ==10:
                print(f'Novembro: {round(temp[t],2)}K')
            elif t ==11:
                print(f'Dezembro: {round(temp[t],2)}K')
                

def main():
    temp_med = []
    for linn in range(12):
        tk = float(input())
        esc = input().upper()[0]

        if esc == 'F':
            tk = round(((tk-32)*(5/9))+273.15, 2)
            temp_med.append(tk)
        elif esc == 'C':
            tk = round(tk + 273.15, 2)
            temp_med.append(tk)
        else:
            temp_med.append(round(tk,2))
    
    md = media_anual(temp_med)
    
    print("TEMPERATURA MÉDIA ANUAL")
    print(f'{md}K')
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    tem_maior(temp_med, md)

if __name__ =='__main__':
    main()
