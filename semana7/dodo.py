def dodow():
    inicial = int(input())

    atual = inicial
    ano = 1600
    nasc = atual*0.01
    morte = atual *0.06


    while True:
    
        atual-= atual*0.05
        print(f'Em {round(ano)} nasceram {round(nasc)} aves e morreram {round(morte)} totalizando {round(atual)} dodôs.')
        nasc = atual*0.01
        morte = atual *0.06

        ano +=1    
    
        if atual <= (inicial*0.1):
            break



def main():
    dodow()

if __name__ == '__main__':
    main()