def eh_par(n):
    return n%2 ==0

def pares(inicio, quantidade):
    if eh_par(inicio):
        proximo = inicio + 2
    else:
        proximo = inicio + 1
    
    numeros_pares =''
    for n in range(quantidade):
        numeros_pares += str(proximo)+ ' '
        proximo += 2
    return numeros_pares.strip()    

    
def main():
    inicio = int(input("Inicio do intervalo: "))
    qtd = int(input("Quantidade de números: "))

    print(f'{qtd} pares após {inicio}: ')
    print(pares(inicio, qtd))

if __name__=='__main__':
    main()
