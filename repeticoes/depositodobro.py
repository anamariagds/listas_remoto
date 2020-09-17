def montante(c, tx):
    m = c*(1+(tx/100))
    dobro_m = m*2
    tempo = 0

    while m < dobro_m:
        m = m*(1+(tx/100))
        tempo +=1
    return tempo



def main():
    deposito = float(input("Valor do depósito: "))
    taxa = float(input("Taxa de juros ao ano: "))

    anos = montante(deposito, taxa)
    print("Rendendo {}% ao ano seu dinheiro vai dobrar em {} anos".format(taxa, anos))

if __name__=='__main__':
    main()