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
    valor_peca = float(input("Qual o preço da peça: "))
    
    pagoavista = pagando_avista(valor_peca)
    pago5vx = atecincovx(valor_peca)
    pago10vx = pagodezvx(valor_peca)

    print(f'A peça paga a vista sai {pagoavista:.2f} reais, dividindo em 5x fica {pago5vx:.2f} reais e em 10x {pago10vx:.2f} reais')

if __name__== '__main__':
    main()