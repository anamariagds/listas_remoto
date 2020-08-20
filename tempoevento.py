def mostrahora(s):
    #aqui o resultado inteiro da divisão é a qtd de horas
    hr = s //3600
    #O resto da divisão anterior são os segundos que restam
    s = s % 3600
    #Os segundos que sobram dividido aqui a parte inteira são os minutos
    mnts = s // 60
    #agora o que sobrar dessa divisão são os segundos 
    sg = s % 60
    return f'{hr}:{mnts}:{sg}'

def main():
    seg = int(input("Informe o tempo de duração do evento em segundos:\n"))
    duracao = mostrahora(seg)

    print(f'O evento na fábrica durou cerca de {duracao}')

if __name__== '__main__':
    main()