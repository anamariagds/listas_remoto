def eh_par(n):
    return n%2 ==0

def pares(inicio, quantidade):
    if eh_par(inicio):
        inicio += 2
    else:
        inicio += 1
    
    numeros_pares =''
    for n in range(inicio, inicio+(quantidade*2), 2):
        numeros_pares += str (n) + ' '
    return numeros_pares.strip()    

    
def main():
    inicio = int(input("Inicio do intervalo: "))
    qtd = int(input("Quantidade de números: "))

    print(f'{qtd} pares após {inicio}: ')
    print(pares(inicio, qtd))

if __name__=='__main__':
    main()
