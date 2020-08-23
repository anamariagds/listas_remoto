def pagando_avista(preco):
    return preco * 0.91

def atecincovx(preco):
    parcela = preco / 5
    return parcela

def pagodezvx(preco):
    com_juros = preco*1.17
    prestacao = com_juros / 10
    return prestacao

def main():
    valor_peca = float(input())
    
    pagoavista = pagando_avista(valor_peca)
    pagocincovx = atecincovx(valor_peca)
    pagardezvx = pagodezvx(valor_peca)

    print(f'{pagoavista:.2f}')
    print(f'{pagocincovx:.2f}')
    print(f'{pagardezvx:.2f}')

if __name__== '__main__':
    main()