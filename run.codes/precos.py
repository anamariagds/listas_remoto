def pagando_avista(preco):
    return f'{preco * 0.91:.2f}'

def atecincovx(preco):
    parcela = preco / 5
    return f'{parcela:.2f}'

def pagodezvx(preco):
    com_juros = preco*1.17
    prestacao = com_juros / 10
    return f'{prestacao:.2f}'

def main():
    valor_peca = float(input())
    
    pagoavista = pagando_avista(valor_peca)
    pagocincovx = atecincovx(valor_peca)
    pagardezvx = pagodezvx(valor_peca)

    print(pagoavista,pagocincovx, pagardezvx)

if __name__== '__main__':
    main()